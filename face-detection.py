import cv2

video_cap = cv2.VideoCapture(0)
while True:
    ret, video = video_cap.read()
    cv2.imshow("video", video)
    if cv2.waitKey(10) == ord('q'):
        break
video_cap.release()