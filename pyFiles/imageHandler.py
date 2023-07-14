from windowCapture import WindowCapture
from time import time
import cv2 as cv
import numpy as np
import os

window = WindowCapture('Grand Theft Auto V')

loop_time = time()
while(True):
    screenshot = window.takeScreenshot()

    cv.imshow('CV SEES', screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done')