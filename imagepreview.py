from PIL import Image

PREVIEW_HEIGHT = 1080
PREVIEW_WIDTH = 1080

def imagePreview(imageList):
    '''Display the first 16 images in a grid, for exclusion'''
    images = imageList[:16]
    preview = Image.new(mode="RGB", size=(PREVIEW_WIDTH, PREVIEW_HEIGHT))
    for x in range(4):
        for y in range(4):
            i = x + 4*y
            tile = images[i].resize((PREVIEW_WIDTH//4, PREVIEW_HEIGHT//4))
            preview.paste(tile, (x*PREVIEW_WIDTH//4, y*PREVIEW_HEIGHT//4))
    preview.show()