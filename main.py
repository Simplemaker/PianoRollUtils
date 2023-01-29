from PIL import Image
from pianorollutils import alignOffset, polystitch
from pathlib import Path
import re
import argparse


from videoextract import getImages



def pathSort(p1):
    result = re.search('(\d+)', p1.name)
    return int(result.group(1))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True)
    parser.add_argument('-o','--output', type=str)
    parser.add_argument('-f','--frameskip', type=int)
    args = parser.parse_args()
    videoFile = Path(args.input)
    
    outFile = args.output if args.output else "combined.png"
    frameskip = args.frameskip if args.frameskip else 30

    if(not videoFile.exists()):
        print("File does not exist: "+str(videoFile.as_posix()))
        exit(1)

    images = getImages(videoFile, True, crop=True, frameskip=frameskip)
    polystitch(images, printStatus=True).save(outFile)

