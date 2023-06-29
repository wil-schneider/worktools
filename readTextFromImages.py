#C:\Program Files\Tesseract-OCR

import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_images(target_dir, text_filename):
    # Go through every image file in the target directory
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".png"):
                # Open the image file
                with Image.open(os.path.join(root, file)) as img:
                    # Use Tesseract to do OCR on the image
                    text = pytesseract.image_to_string(img)

                    # Open the text file and append the text
                    with open(text_filename, "a") as f:
                        f.write(f"Text from {file}:\n{text}\n")

# Use function on the target directory
extract_text_from_images("pptOutputDir", "extracted_text.txt")
