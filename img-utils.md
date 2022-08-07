# Image utils

## Image to text
- `yay tesseract tesseract-data-eng tesseract-data-rus` - installs
- `tesseract path/to/img output/path/and/name [-l lang]` - converts
- `gimagereader` - nice front for tesseract

## Image cropping, resizing etc
- `yay imagemagick`
- `display image.png`

## Images to pdf
- `convert image.png image.jpg out.pdf` - needs imagemagick to be installed
- `convert image.png image.jpg -quality 80 out.pdf` - same, but also compresses size
- 
