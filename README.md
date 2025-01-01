# Image Resize Tool
A Python application that resizes images to specific dimensions while maintaining their aspect ratio.

## Overview
This project consists of three main components:
- [`app.py`](app.py): The main application file that uses the `image_tools` module to resize images.
- [`image_tools.py`](image_tools.py): A module that provides functions for resizing images and describing their content using a machine learning model.
- [`test.py`](test.py): A test file that contains unit tests for the `image_tools` module.

## Functionality
The application can resize images to specific dimensions (e.g., 11x14, 8x10, 5x7) while maintaining their aspect ratio. It uses the `image_tools` module to perform the resizing and also provides a function to describe the content of an image using a machine learning model.

## Usage
To use the application, simply run the app.py file and provide the input image path, output image path, and desired dimensions as arguments.

```bash
python app.py --input_image images/cat.png --output_image images/output/cat_11x14.png --width 3300 --height 4200
```

This will resize the `cat.png` image to 11x14 inches (3300x4200 pixels) and save the output image as `cat_11x14.png` in the `images/output` directory.

## Testing
The `test.py` file contains unit tests for the `image_tools` module. To run the tests, simply execute:

```bash
python -m unittest test.py
```

## Dependencies
- Python 3.x
- Pillow library (pip install pillow)
- ollama library (pip install ollama) - This is optional and only required for describing image content.