from PIL import Image
import ollama

def resize_image(
        input_image_path: str,
        output_image_path: str,
        target_width: int,
        target_height: int,
        dpi: int = 300):
    with Image.open(input_image_path) as img:
        # Calculate the aspect ratio
        original_width, original_height = img.size
        aspect_ratio = original_width / original_height

        # Determine the new dimensions while maintaining the aspect ratio
        if (target_width / target_height) > aspect_ratio:
            new_width = target_width
            new_height = int(target_width / aspect_ratio)
        else:
            new_height = target_height
            new_width = int(target_height * aspect_ratio)

        # Resize the image
        resized_img = img.resize(
            (new_width, new_height), Image.Resampling.LANCZOS)

        # Calculate the crop box
        left = (new_width - target_width) / 2
        top = (new_height - target_height) / 2
        right = (new_width + target_width) / 2
        bottom = (new_height + target_height) / 2

        # Crop the image
        cropped_img = resized_img.crop((left, top, right, bottom))

        # Set the DPI
        cropped_img.info['dpi'] = (dpi, dpi)

        # Save the resized and cropped image
        cropped_img.save(output_image_path, dpi=(dpi, dpi))

OLLAMA_MODEL: str = 'llama3.2-vision'

def describe_image(input_image_path: str):

    try:
        response: ollama.ChatResponse = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': ('You are an image analysis expert.' 
                                'Provide a detailed description based on the image provided by the user.'),
                    'temperature': 0.7  # specify the temperature here
                },
                {
                    'role': 'user',
                    'content': 'What is in this image?',
                    'images': [input_image_path]
                }
            ]
        )

        # print(response)
        return response['message']['content']

    except ollama.ResponseError as e:
        print('Error:', e.error)
        if e.status_code == 404:
            ollama.pull(OLLAMA_MODEL)
