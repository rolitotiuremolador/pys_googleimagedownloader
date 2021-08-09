# Source: https://towardsdatascience.com/automate-renaming-and-organizing-files-with-python-89da6560fe42
from pathlib import Path
from datetime import datetime
import os

image_folder = Path(r'/home/rolito/Desktop/ML/BuildOwnDataset/images')
# print(image_folder)
for file in image_folder.iterdir():
    # Setup key varialbles for the parent path and the file extenstions
    directory = file.parent
    extension = file.suffix

    # Use unpacking by splitting the old name on the '-' character