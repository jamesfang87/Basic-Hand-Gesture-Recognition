from preprocess import process, normalize
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import numpy as np

testing_data = []
examples = []

for i in range(len(testing_data)):
    process(testing_data[i])
for i in range(len(examples)):
    process(examples[i])

for test in testing_data:
    prediction, min_dist = -1, 10000000
    for i, example in enumerate(examples):
        process(example)
        g1, g2 = normalize(test, example)
        distance, _ = fastdtw(g1, g2, dist=euclidean)
        if distance < min_dist:
            prediction = i
            min_dist = distance

    print(prediction)
