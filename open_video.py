import numpy as np
import cv2

# Para grabar con camaras conectadas al PC
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('video.mp4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
