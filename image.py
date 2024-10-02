import cv2 as cv
from glob import glob
import os
import random
from ultralytics import YOLO

# read in video paths
videos = glob('C:\\SIH PROJECT\\models\\download.mp4')
print(videos)