from pathlib import Path
from PIL import Image
import numpy as np

# CONFIG -------------------------------------------------------------------------
INPUT_PATH = Path("images/input.jpg")
OUTPUT_PATH = Path("images/output.png")
BLOCK_SIZE = 8                                  # Multiple of 4 / min 4
METHOD = "median"
# --------------------------------------------------------------------------------

def load_image(path):
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with Image.open(path) as img:
        return np.array(img.convert("RGB"))

def save_image(array, path):
    path.parent.mkdir(parents = True, exist_ok = True)
    Image.fromarray(array.astype(np.uint8)).save(path)

def main():
    img = load_image(INPUT_PATH)

    #    block_size = validate_block_size(BLOCK_SIZE)
    #    image = load_image(INPUT_PATH)
    #    cropped = center_crop(image, block_size)
    #    result = pixelate(cropped, block_size, method=METHOD)
    #    save_image(result, OUTPUT_PATH)
    #    print(f"Saved pixel art ({block_size}px blocks, {METHOD}) -> {OUTPUT_PATH}")