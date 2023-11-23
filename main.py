from util import *

video_path = "three.mov"

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(video_path)
data = detect("out", 1, "three.mov")

cap.release()
cv2.destroyAllWindows()
print(data)
