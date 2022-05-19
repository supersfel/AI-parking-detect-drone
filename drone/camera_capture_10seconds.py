import camera_test
import time

cnt = 0

while(True):
    
    camera_test.capture_img(cnt)
    time.sleep(10)
    cnt+=1

camera_test.capture.release()
camera_test.cv2.destroyAllWindows()
