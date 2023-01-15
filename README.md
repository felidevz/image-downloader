# image-downloader

### A program used to scrap and download images in low quality from websites: pixabay.com, pexels.com.
#### You need Google Chrome web browser installed in your system and chromedriver.exe file extension in current project directory.

#### How to use:
Execute script from command line interface as:
- for pixabay.com - python main.py link_to_your_images image_class_name_from_html_source, ex. python main.py https://pixabay.com/pl/photos/search/sky/ photo-result-image
- for pexels.com - python main.py link_to_your_images image_class_name_from_html_source page_number_to_load, ex. python main.py https://www.pexels.com/pl-pl/szukaj/natura/ MediaCard_image__ljFAl 5

Program will open automated web browser controlled by selenium package, load page with images, scroll to the bottom of page to load everything and start downloading content to directories.

This project is licensed under the terms of the MIT license.
