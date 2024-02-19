from PIL import Image

def resize_image(input_path, output_path, target_width):
    # Open the image
    with Image.open(input_path) as img:
        # Calculate the aspect ratio
        aspect_ratio = img.width / img.height
        
        # Calculate the target height based on the target width and aspect ratio
        target_height = int(target_width / aspect_ratio)
        
        # Resize the image
        resized_img = img.resize((target_width, target_height))
        
        # Save the resized image
        resized_img.save(output_path)

resize_image(r'./outputs/figures/figure-1.png', r'./outputs/figures/figure-1_resized.png', 327)