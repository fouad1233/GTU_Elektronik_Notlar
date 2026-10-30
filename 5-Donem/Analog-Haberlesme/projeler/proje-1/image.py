from PIL import Image

def convert_to_binary_image(input_image_path, output_image_path):
    # Open the input image
    img = Image.open(input_image_path)

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Threshold the grayscale image to create a binary image
    threshold = 128  # You can adjust this threshold value if needed
    img_binary = img_gray.point(lambda p: p > threshold and 255)

    # Save the binary image
    img_binary.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "image.jpg"  # Replace with the path to your input image
    output_image_path = "output.jpg"  # Replace with the desired output path and file format (e.g., .bmp)

    convert_to_binary_image(input_image_path, output_image_path)
