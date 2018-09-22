#################################################
# rock_paper_scissors.py
#################################################
"""I wanna be the very best
Like no one ever was
To catch them is my real test
To train them is my cause"""

import random
from tkinker import *

def runWindow(winWidth=500, winHeight=500):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
  
def main():
    runWindow()

if __name__ == '__main__':
    main()
#
