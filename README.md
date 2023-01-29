# PianoRollUtils

A utility for converting piano roll video to a single image piano roll.

Usage: 
```python main.py -i <input video>
python main.py 
-i <input video> 
-o <output image>
-f <frameskip>
-s <enables the skip-early-frame dialog>
```

Frameskip is the number of frames skipped between captures. For 60fps video, a frameskip of 30 captures two frames per second.
