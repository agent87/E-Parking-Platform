import cv2
rtsp_address = 'rtsp:/dashboard:parking2021@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1'

video= cv2.VideoCapture(rtsp_address)
# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = video.read()
    # 1. Object Detection
    mask = object_detector.apply(frame)
    cv2.imshow("RTSP", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


















