import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()        
    
    # Our operations on the frame come here    
    #img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # BGR color to gray level
    
    # Display the resulting image
    cv2.imshow('Gray',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()