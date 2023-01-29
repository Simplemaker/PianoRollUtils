
from PIL import Image

'''Denoise Utility

Using a median function, removes sparkles and other extraneous effects.'''

def medianOfPixels(pixelList):
    pixelList.sort(key = sum)
    return pixelList[len(pixelList)//2]


RANGE = 4

def denoise(im):
    oldpixels = im.load()
    im2 = Image.new("RGB", im.size)
    newpixels = im2.load()
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            ## Immediate neighborhood
            neighborhood = []
            for dx in range(-RANGE, RANGE+1):
                for dy in range(-RANGE, RANGE+1):
                    if(x + dx > 0 and y + dy > 0 and x + dx < im.size[0] and y + dy < im.size[1]):
                        neighborhood.append(oldpixels[x+dx, y+dy])
            newpixels[x, y] = medianOfPixels(neighborhood)
    return im2
