

from random import randint
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


'''Alignment Utility
Alignment involves finding an optimum offset between images such that the intersecting pixels are well matched'''

def pixelDifference(p1, p2):
    difference = 0
    for i in range(3):
        difference += abs(p1[i] - p2[i])
    return difference

def compareCrop(im1, im2, verticalOffset, pixels1, pixels2):
    '''Compare images for similarity
    
    A 0 is given for no similar pixels. '''
    sumDifference = 0
    for x in range(0,im1.size[0], 10):
        for y in range(im2.size[1] - verticalOffset):
            sumDifference+= pixelDifference(pixels1[x,y], pixels2[x,y + verticalOffset])
    return 100 - sumDifference / (im1.size[0] * (im2.size[1] - verticalOffset))


ANALYZE = False


def alignOffset(im1, im2):
    '''Determine the optimal vertical offset for two images, with im2 being "above" im1.

    Assumes im1 and im2 are the same size.
    
    "Optimal" is handled by the compare Crop function.'''
    hiscore = None
    hiscorer = None
    pixels1 = im1.load()
    pixels2 = im2.load()
    for y in range(im2.size[1]):
        score = compareCrop(im1, im2, y, pixels1, pixels2)
        if ANALYZE:
            print(f'{y}, {score}, {hiscore}')
        if hiscore == None or score > hiscore:
            hiscore = score
            hiscorer = y
    return hiscorer


GMRO_SAMPLES = 5

def getMedianRandomOffset(images):
    samples = []
    for i in range(GMRO_SAMPLES):
        print(f'Acquiring MRO Sample {i+1}')
        image_index = randint(0, len(images) - 2)
        samples.append(alignOffset(images[image_index], images[image_index + 1]))
        print(f'Found offset {samples[-1]}')
    samples.sort()
    return samples[len(samples) // 2]


def stitch(im1, im2, offset=None):
    '''Stitches im2 on top of im1'''
    if offset == None:
        offset = alignOffset(im1, im2)
    out = Image.new(mode="RGB", size=(im1.size[0], im1.size[1] + offset))
    out.paste(im2)
    out.paste(im1, (0, offset))
    return out

def polystitch(images, printStatus=False):
    assert(images != None)
    assert(len(images) > 0)
    offset = getMedianRandomOffset(images)
    print(f'Median offset: {offset}')
    count = 0
    out = Image.new(mode="RGB", size=(images[0].size[0], images[0].size[1] + offset * (len(images)-1)))
    print(out.size)
    for image in images[::-1]:
        out.paste(image, (0, offset * count))
        count+=1
        if printStatus:
            print(f'Stitching image {count}')
    return out
