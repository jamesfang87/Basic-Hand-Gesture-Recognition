from util import *
from classification import classify, examples

video_path = ""
data = detect("out", 0)


print(data)

classify([data], examples)
