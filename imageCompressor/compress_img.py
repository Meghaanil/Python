from PIL import Image
from tkinter import filedialog
import os

# Ask user to select an image file
file_path = filedialog.askopenfilename()

# Check if a file was selected
if file_path:
    # Ask user to choose the save location for the compressed image
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")

    # Check if a save location was chosen
    if save_path:
        # Get the file extension from the save path
        file_extension = os.path.splitext(save_path)[1].lower()

        # Check if the file extension is valid
        if file_extension not in ['.jpg', '.jpeg', '.png']:
            print("Invalid file extension. Please save the image as JPG or PNG.")
        else:
            # Compress the image
            img = Image.open(file_path)
            img.save(save_path, optimize=True, quality=50)
            print("Image compressed successfully!")
    else:
        print("No save location chosen.")
else:
    print("No image file selected.")

