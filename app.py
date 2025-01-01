import os
import argparse
from image_tools import resize_image

def main():
    parser = argparse.ArgumentParser(description='Resize an image to specific dimensions.')
    parser.add_argument('--input_image', type=str, required=True, help='Path to the input image')
    parser.add_argument('--output_image', type=str, required=True, help='Path to the output image')
    parser.add_argument('--width', type=int, required=True, help='Target width in pixels')
    parser.add_argument('--height', type=int, required=True, help='Target height in pixels')
    parser.add_argument('--dpi', type=int, default=300, help='DPI for the output image (default: 300)')

    args = parser.parse_args()

    resize_image(args.input_image, args.output_image, args.width, args.height, args.dpi)
    print('Done!')

if __name__ == '__main__':
    main()

    ## Define the input
    # full_input_image_path: str = 'images/cat.png'
    # filename_with_extension: str = os.path.basename(full_input_image_path)
    # filename, file_extension = os.path.splitext(filename_with_extension)

    ## Define the output image paths
    # full_output_image_path_11x14: str = f"images/output/{filename}_11x14{file_extension}"
    # full_output_image_path_8x10: str = f"images/output/{filename}_8x10{file_extension}"
    # full_output_image_path_5x7: str = f"images/output/{filename}_5x7{file_extension}"

    # new_dpi: int = 300

    ## Resize to 11x14 inches (3300x4200 pixels)
    # resize_image(full_input_image_path, full_output_image_path_11x14, 3300, 4200, new_dpi)
    ## Resize to 8x10 inches (2400x3000 pixels)
    # resize_image(full_input_image_path, full_output_image_path_8x10, 2400, 3000, new_dpi)
    ## Resize to 5x7 inches (1500x2100 pixels)
    # resize_image(full_input_image_path, full_output_image_path_5x7, 1500, 2100, new_dpi)
