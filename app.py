import os
from image_tools import resize_image

# Define the input
full_input_image_path: str = 'images/cat.png'
filename_with_extension: str = os.path.basename(full_input_image_path)
filename, file_extension = os.path.splitext(filename_with_extension)

# Define the output image paths
full_output_image_path_11x14: str = f"images/output/{filename}_11x14{file_extension}"
full_output_image_path_8x10: str = f"images/output/{filename}_8x10{file_extension}"
full_output_image_path_5x7: str = f"images/output/{filename}_5x7{file_extension}"

new_dpi: int = 300

## Resize to 11x14 inches (3300x4200 pixels)
resize_image(full_input_image_path, full_output_image_path_11x14, 3300, 4200, new_dpi)
## Resize to 8x10 inches (2400x3000 pixels)
resize_image(full_input_image_path, full_output_image_path_8x10, 2400, 3000, new_dpi)
## Resize to 5x7 inches (1500x2100 pixels)
resize_image(full_input_image_path, full_output_image_path_5x7, 1500, 2100, new_dpi)

print('Done!')
