import datetime
import cv2

capture = cv2.VideoCapture(0) 
img_counter = 0

width = int(capture.get(3))  
height = int(capture.get(4))  
'''
while (capture.isOpened):

    ret, frame = capture.read()

    if ret == False:
        break

    cv2.imshow("VideoFrame", frame)
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    key = cv2.waitKey(33)  # 1) & 0xFF

    if key == 26:  # esc 종료
        break

    elif key == 27:  # ctrl + z(캡쳐됨)
        cv2.IMREAD_UNCHANGED
        cv2.imwrite("/home/pi/Capture/capture_{}.png".format(img_counter), frame) # frame=컬러 화면 출력
        print('Saved frame%d.jpg' % img_counter)
        img_counter += 1

'''
def capture_img(img_counter):
    if (capture.isOpened):

        ret, frame = capture.read()

        if ret == False:
            pass

        cv2.imshow("VideoFrame", frame)
        now = datetime.datetime.now().strftime("%d_%H-%M-%S")
        key = cv2.waitKey(33)  # 1) & 0xFF

        
        
        cv2.IMREAD_UNCHANGED
        cv2.imwrite("/home/pi/Capture/capture_{}.png".format(img_counter), frame) # frame=컬러 화면 출력
        print('Saved frame%d.jpg' % img_counter)
        img_counter += 1


    

"""
capture_img(1)

capture.release()
cv2.destroyAllWindows()
    
"""


