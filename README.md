# Basic-Hand-Gesture-Recognition

A program that takes in a video of a person drawing the 10 Arabic numerals with their hands and classifies the video by which Arabic numeral the person is drawing.

Dynamic Time Warping (DTW):

For classificaiton, we used dynamic time warping.  A key motivation was the differing in gesture performance length that needed to be accomodated.  Given two signals, if we simply calculated the Euclidean distance between two points in time, even if both signals have the exact same "features" but one was more stretched out than the other, we would get a large error back as corresponding features in the signal would not be compared to each other but instead other features.  With DTW, we match each point in a signal to its equivalent in the other signal and also return a cost of aligmnent which is the euclidean distance between all matched data points.  The signal with the lowest alignment cost is the most similar signal (and thus the label of the video).

We can take advantage of certain "norms" in the data.  Most notably, the vertical displacement of all arabic numerals is the same.  We can normalize these to [0, 1].  However, we do not have the same trend for the horizontal part of arabic numerals, where we in fact see large differences between all of them (there is always little to no horizontal displacement for the number 1 while there is a large displacement for 0 or 8). To preserve these differences, when we compare two gestures, we normalize their data points with the collective maximum and minimum from both gestures.  In addition, we "start" all gestures at the same point so differences in where the user does the gestures does not matter and the said normalization that we will be performing "works better".

We also do not need to care about the distance between hand landmarks as:
1. it does not tell us any information (for this dataset at least)
2. hand shape generally stays in the same position: where the hand is in a pointing position