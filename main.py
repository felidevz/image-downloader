# Enjoy fast downloading images from websites:
# pixabay.com & pexels.com

from driver import ChromeDriver
from downloader import ImageDownloader
import sys

USER_URL: str = ''
USER_IMG_CLASS: str = ''
USER_PAGE_SCROLLS: int = 1


def pre_configure() -> None:
    """Get config info from user inserted with CLI arguments."""
    global USER_URL, USER_IMG_CLASS, USER_PAGE_SCROLLS

    if len(sys.argv) == 4:
        USER_URL = sys.argv[1]
        USER_IMG_CLASS = sys.argv[2]
        USER_PAGE_SCROLLS = int(sys.argv[3])
    elif len(sys.argv) == 3:
        USER_URL = sys.argv[1]
        USER_IMG_CLASS = sys.argv[2]
    elif len(sys.argv) > 4:
        raise ValueError('Too much CLI arguments given.')
    else:
        raise ValueError('Not all required CLI arguments given. Try again.')


def main():
    pre_configure()

    driver = ChromeDriver('chromedriver.exe')
    html_content = driver.load_content(USER_URL, scrolls=USER_PAGE_SCROLLS)

    downloader = ImageDownloader(html_content, 'lxml')
    images = downloader.find_images(USER_IMG_CLASS)
    downloader.download_images(images)


if __name__ == '__main__':
    main()
