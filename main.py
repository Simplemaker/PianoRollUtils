from PIL import Image
from pianorollutils import alignOffset, polystitch
from pathlib import Path
import re

from videoextract import getImages

STANDARD_CROP = (0,0,1920, 512)

## Standard Pipeline:

## 1. Extract video frames (video -> frames)

## 2. Crop video frames (frames -> frames)

## 3. Stitch frames

def pathSort(p1):
    result = re.search('(\d+)', p1.name)
    print(result)
    return int(result.group(1))

# paths = [p for p in Path('frames').iterdir()]
# paths.sort(key=pathSort)

# images = [Image.open(p).crop(STANDARD_CROP) for p in paths]

videoFile = next(Path('video').iterdir())

images = getImages(videoFile, True, crop=STANDARD_CROP)
polystitch(images, printStatus=True).save('combined.png')