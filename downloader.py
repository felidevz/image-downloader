from bs4 import BeautifulSoup
from bs4.element import ResultSet
from threading import Thread
import requests
import os


class ImageDownloader:
    def __init__(self, html_content: str, parser: str) -> None:
        """Creates a new instance of the ImageDownloader."""
        self._soup = BeautifulSoup(html_content, features=parser)
        self._threads = []
        self._images_length = 0
        self._current = 0

    def find_images(self, img_class: str) -> ResultSet:
        """
        Finds all `img` elements on HTML page with given class
        and returns `ResultSet` object.
        """
        return self._soup.find_all('img', attrs={'class': img_class})

    def _download_image(self, img_link: str) -> None:
        """
        Downloads a single image from given link to current working directory.
        Created for usage with `download_images` method.
        """
        filename = ''
        for extension in ('.jpg', '.jpeg', '.png'):
            extension_index = img_link.find(extension)
            if extension_index != -1:
                filename = img_link[:extension_index + len(extension)]
                break

        filename = filename.split('/')[-1]

        img_response = requests.get(img_link)

        with open(filename, 'wb') as file:
            file.write(img_response.content)

        self._current += 1
        print(f'Downloading image {self._current} of {self._images_length}...')

    def download_images(self, images: ResultSet) -> None:
        """
        Creates a directory with domain name if not exists
        and changes current working directory to save images there.
        Uses multiple threads to fast download all images found on page.
        """
        self._images_length = len(images)
        self._current = 0

        dir_name = images[0]['src'].split('/')[2].replace('.', '_')
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        os.chdir(dir_name)

        for image in images:
            thread = Thread(target=self._download_image, args=[image['src']])
            thread.start()
            self._threads.append(thread)

        for thread in self._threads:
            thread.join()
