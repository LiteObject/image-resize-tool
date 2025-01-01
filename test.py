import unittest
from image_tools import describe_image

# python -m unittest test.py

class TestDescribeImage(unittest.TestCase):
    def test_image_description(self):
        input_image_path = 'images/cat.png'
        response = describe_image(input_image_path)
        print(response)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        # self.assertIn('message', response)
        # self.assertIn('content', response.message)
        self.assertGreater(len(response), 0)

if __name__ == '__main__':
    unittest.main()
