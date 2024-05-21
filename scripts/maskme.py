from PIL import Image
import sys
import re

def is_numeric_part_even(filename):
    # Use regular expression to find the numeric portion of the filename
    #match = re.search(r'(\d+)', filename)
    match = re.search(r'-(\d+)\.jpg$', filename)

    if match:
        number = int(match.group(1))
        return number % 2 == 0
    else:
        raise ValueError("No numeric portion found in the filename")

def apply_mask(image_path, mask_path, output_path):
    # Load the images
    image = Image.open(image_path).convert("RGBA")
    mask = Image.open(mask_path).convert("L")  # Load mask as grayscale

    # Ensure mask is the same size as the image
    mask = mask.resize(image.size)

    white_background = Image.new('RGB', image.size, (255, 255, 255, 255))


    # Apply the mask to the image
    #result = Image.composite(image, Image.new('RGB', image.size), mask)
    result = Image.composite(image, white_background, mask)

    # Save the result
    result.save(output_path)

# Example usage
image_path = sys.argv[1]


#image_path = "Chapter21-001.jpg"
mask_path = "oddmask.png"

if is_numeric_part_even(image_path) == 0:
    mask_path = "oddmask.png"
else:
    mask_path = "evenmask.png"

print("using mask", mask_path)
output_path = image_path+"-textonly.jpg"# "Chapter21-001-textonly.jpg"


apply_mask(image_path, mask_path, output_path)
