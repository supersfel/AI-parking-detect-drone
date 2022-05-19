'''
웹캠을 불러내어 영상을 캡쳐하고 이를 이미지로 저장한다.
이미지는 capture_0부터 저장되고, 이 후 오름차순으로 저장됨.
저장루트는 맞게 바꿀것.
ctrl+z -> 캡쳐
esc -> 카메라 끄기
'''

import datetime
import cv2

capture = cv2.VideoCapture(0) #0은 내장캠, 1은 웹캠(젯슨나노는 1 사용)
img_counter = 0

width = int(capture.get(3))  # 가로
height = int(capture.get(4))  # 세로값 가져와서


while (capture.isOpened):

    ret, frame = capture.read()

    if ret == False:
        break

    cv2.imshow("VideoFrame", frame)
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    key = cv2.waitKey(33)  # 1) & 0xFF

    if key == 27:  # esc 종료
        break

    elif key == 26:  # ctrl + z(캡쳐됨)
        cv2.IMREAD_UNCHANGED
        cv2.imwrite("C:/Users/user/Desktop/camera_image/capture_{}.png".format(img_counter), frame) # frame=컬러 화면 출력
        print('Saved frame%d.jpg' % img_counter)
        img_counter += 1


capture.release()
cv2.destroyAllWindows()