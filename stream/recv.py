import cv2


if __name__ == '__main__':
    cap = cv2.VideoCapture('udp://127.0.0.1:5000', cv2.CAP_FFMPEG)
    if not cap.isOpened():
        print('VideoCapture not opened')
        exit(-1)

    while True:
        ret, frame = cap.read()
        # frame = cv2.flip(cv2.flip(frame, 0), 1)

        if not ret:
            print('frame empty')
            break

        cv2.imshow('image', frame)

        if cv2.waitKey(1) & 0XFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
