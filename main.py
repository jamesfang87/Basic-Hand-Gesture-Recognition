from util import *
from classification import classify

video_path = "2.mov"
data = detect(1, video_path)

classify([data])  # put in an array of data
