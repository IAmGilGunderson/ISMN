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


def read_file_to_string(file_path):
    """
    Reads the contents of a file into a string.

    Args:
    file_path (str): The path to the file to be read.

    Returns:
    str: The contents of the file as a string.
    """
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except IOError:
        return f"Error: An IOError occurred while reading the file at {file_path}."

# Example usage:
# file_contents = read_file_to_string('path/to/your/file.txt')
# print(file_contents)

def write_string_to_file(file_path, content):
    """
    Writes the given content to a file.

    Args:
    file_path (str): The path to the file to be written.
    content (str): The content to write to the file.

    Returns:
    str: A message indicating whether the write was successful or if an error occurred.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f"Successfully wrote to the file at {file_path}."
    except IOError:
        return f"Error: An IOError occurred while writing to the file at {file_path}."

# Example usage:
# content = "The quick brown fox jumps over the lazy dog."
# file_path = "path/to/your/file.txt"
# result = write_string_to_file(file_path, content)
# print(result)  # Output: "Successfully wrote to the file at path/to/your/file.txt."

def search_and_replace(haystack, needle, pitchfork):
    """
    Searches for a string called needle in another string called haystack
    and replaces it with a string called pitchfork.

    Args:
    haystack (str): The string to be searched.
    needle (str): The string to search for.
    pitchfork (str): The string to replace the needle with.

    Returns:
    str: The modified string with needle replaced by pitchfork.
    """
    return haystack.replace(needle, pitchfork)

# Example usage:
# haystack = "The quick brown fox jumps over the lazy dog."
# needle = "fox"
# pitchfork = "cat"
# result = search_and_replace(haystack, needle, pitchfork)
# print(result)  # Output: "The quick brown cat jumps over the lazy dog."

def apply_mask(image_path, mask_path, output_path):
    print(f'image_path: {image_path}')
    print(f'mask_path: {mask_path}')
    print(f'output_path: {output_path}')
    inputSVG = read_file_to_string(mask_path)
    #print("=============",inputSVG,"============")
    newSVG = search_and_replace(inputSVG,"@@@@",image_path)
    write_string_to_file(output_path,newSVG)

# Example usage
image_path = sys.argv[1]


#image_path = "Chapter21-001.jpg"
mask_path = "oddmask.png"
suffix = "odd"

if is_numeric_part_even(image_path) == 0:
    mask_path = "oddpage.svg"
    suffix = "odd"
else:
    mask_path = "evenpage.svg"
    suffix = "even"

print("using mask", mask_path)
#ISMN-Chapter0x-Page00x-odd.svg
output_path = f'{image_path}-{suffix}.svg'


apply_mask(image_path, mask_path, output_path)
