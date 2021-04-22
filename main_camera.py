import cv2

# define a video capture object
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.resizeWindow('frame', 200, 150)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = cap.read()

    # if ret == False:
    #     print("Webcam Issue")
    #     break

    # Display the resulting frame
    cv2.imshow('frame',frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) &0XFF == ord('q'):
        break


# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
