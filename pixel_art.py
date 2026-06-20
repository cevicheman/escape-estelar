#codigo hecho con ayuda de IA
from PIL import Image
from colorama import init
import sys

# Initialize colorama
init(autoreset=True)

def rgb_to_ansi(r, g, b, bg=False):
    """
    Converts an RGB color to an ANSI escape code for 24-bit color.
    """
    return f"\033[48;2;{r};{g};{b}m" if bg else f"\033[38;2;{r};{g};{b}m"

def print_image(image_path, pixel_width=80):
    """
    Prints an image in the terminal using high-quality pixel art.

    :param image_path: Path to the image file.
    :param pixel_width: Width of the image in terminal characters.
    """
    try:
        # Open the image
        img = Image.open(image_path)
        # Resize image maintaining the aspect ratio
        aspect_ratio = img.height / img.width
        new_height = int(pixel_width * aspect_ratio * 0.55)  # Adjusted for aspect ratio difference in characters
        img = img.resize((pixel_width, new_height * 2), Image.LANCZOS)

        # Convert image to RGB
        img = img.convert('RGB')

        # Print each pixel
        for y in range(0, new_height * 2, 2):
            for x in range(pixel_width):
                try:
                    r1, g1, b1 = img.getpixel((x, y))
                    r2, g2, b2 = img.getpixel((x, y + 1))
                except IndexError:
                    # Handle edge case where y+1 might be out of bounds
                    r2, g2, b2 = 0, 0, 0

                # Use the most appropriate character based on luminance and color similarity
                char = '█' if (r1, g1, b1) == (r2, g2, b2) else '▀'
                sys.stdout.write(rgb_to_ansi(r1, g1, b1) + rgb_to_ansi(r2, g2, b2, bg=True) + char)
            sys.stdout.write('\n')
    except Exception as e:
        print(f"Error: {e}")

# This code block will only run if this script is executed directly
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Print an image as pixel art in the terminal.')
    parser.add_argument('image_path', help='Path to the image file.')
    parser.add_argument('--width', type=int, default=80, help='Width of the image in terminal characters.')

    args = parser.parse_args()

    print_image(args.image_path, args.width)

