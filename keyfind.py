
'''Key Location Library

Example key template is available in demo.json'''

import argparse
import json
from PIL import Image, ImageDraw


def getConfig(filename):
    result = None
    with open(filename, 'r') as f:
        result = json.loads(f.read())
    return result


keyOffsets = [0, 0.4, 1, 1.6, 2, 3, 3.3, 4, 4.5, 5, 5.7, 6]


def getKeyPosition(midiIndex, config):
    octavePosition = (midiIndex - 60) // 12 * \
        config['octaveWidth'] + config['middleC']
    keyColor = midiIndex % 12
    keyWidth = config['octaveWidth'] / 7
    keyPosition = keyOffsets[keyColor] * keyWidth
    return octavePosition + keyPosition


def genKeyDict(config):
    '''Dictionary maps midi key values to x positions'''
    out = dict()
    for i in range(21, 109):
        out[str(i)] = getKeyPosition(i, config)
    return out


def renderKeyDict(keyDict):
    w = 1920
    h = 1080
    out = Image.new("RGBA", (w, h), (0,0,0,0))
    draw = ImageDraw.Draw(out)
    for k, v in keyDict.items():
        v = int(v)
        color = (64, 64, 64) if int(k) % 12 in [1, 3, 6, 8, 10] else "white"
        draw.line([(v, 0), (v, h)], fill=color, width=0)
    return out

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True)
    parser.add_argument('-j', '--json', type=str, required=True)
    parser.add_argument('-o','--output', type=str)
    args = parser.parse_args()

    config = getConfig(args.json)
    kd = genKeyDict(config)
    img = renderKeyDict(kd)

    orig = Image.open(args.input)
    img = Image.alpha_composite(orig, img)
    if args.output:
        img.save(args.output)
    else:
        img.show()
