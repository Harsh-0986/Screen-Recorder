import cv2
import pyautogui
import numpy as np

video_codec = cv2.VideoWriter_fourcc(*"XVID")

# 1366,768 resolution
out = cv2.VideoWriter("Recorded.avi", video_codec, 10, (1366, 768))

# Creating window for live viewing of the screen recording
cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 480, 270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('Recording', frame)
    out.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()