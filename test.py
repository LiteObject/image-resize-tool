import os
import unittest

from PIL import Image, ImageDraw
from image_tools import describe_image, resize_image


class TestDescribeImage(unittest.TestCase):

    def setUp(self):
        # Create a test image
        self.input_image_path = 'test_image.png'
        img = Image.new('RGB', (200, 200), color = 'red')
        draw = ImageDraw.Draw(img)
        # Draw some text
        draw.text((60, 80), "Hello World!", fill='black')

        img.save(self.input_image_path)

    def tearDown(self):
        # Clean up
        if os.path.exists(self.input_image_path):
            os.remove(self.input_image_path)

    def test_image_description(self):
        description = describe_image(self.input_image_path)
        print(description)
        
        # Check if the description is a non-empty string
        self.assertIsInstance(description, str)
        self.assertTrue(len(description) > 0)


class TestResizeImage(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_image_path = None

    def test_resize_image(self):
        # Create a test image
        input_image_path = 'images/test_image.png'
        self.output_image_path = 'images/test_image_resized.png'
        width = 100
        height = 100

        # Create a test image with a specific size
        img = Image.new('RGB', (200, 200))
        img.save(input_image_path)

        # Call the resize_image function
        resize_image(input_image_path, self.output_image_path, width, height)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Check if the output image has the correct size
        with Image.open(self.output_image_path) as output_img:
            self.assertEqual(output_img.size, (width, height))

        # Clean up
        os.remove(input_image_path)
        os.remove(self.output_image_path)

    def test_resize_image_aspect_ratio(self):
        # Create a test image
        input_image_path = 'images/test_image.png'
        self.output_image_path = 'images/test_image_resized.png'
        width = 100
        height = 200

        # Create a test image with a specific size
        img = Image.new('RGB', (200, 200))
        img.save(input_image_path)

        # Call the resize_image function
        resize_image(input_image_path, self.output_image_path, width, height)

        # Check if the output image exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Check if the output image has the correct aspect ratio
        with Image.open(self.output_image_path) as output_img:
            self.assertAlmostEqual(output_img.size[0] / output_img.size[1], width / height, places=2)

        # Clean up
        os.remove(input_image_path)
        os.remove(self.output_image_path)

    def tearDown(self):
        # Clean up
        if hasattr(self, 'output_image_path') and os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)


if __name__ == '__main__':
    unittest.main()
