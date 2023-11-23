import cv2
import mediapipe as mp
import numpy as np


def write(file_path, landmarks):
    f = open(file_path, "a")
    output = str(landmarks).split("landmark {")[9].split("}")[0].split('\n  ')[1:]
    output[-1] = output[-1].strip('\n')
    for i in range(len(output)):
        output[i] = float(output[i][3:])
    f.write(str(output[0]) + ',' + str(output[1]) + '\n')
    return output[0:2]


def detect(output_path, option, video_path=None):
    """
    :param output_path: path to the file to write the detection results
    :param option: value of 0 or 1 where 0 represents livestream and 1 represents video upload
    :param video_path: path to the video if option is video upload.  defaulted to None
    :return:
    """
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    if option == 0:
        cap = cv2.VideoCapture(0)
    elif option == 1:
        cap = cv2.VideoCapture(video_path)
    else:
        raise "Invalid value in parameter option"

    data = []
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)
            data.append(write(output_path, results.multi_hand_landmarks[0]))

        cv2.imshow('MediaPipe Pose', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return np.array(data)
