from os import walk
from sys import exit
import random
import time
import cv2

xd = 0
yd = 0


def stop(event, x, y, flags, param):
    global xd
    global yd
    xd = xd + abs(xd - x)
    yd = yd + abs(yd - y)
    print(xd + yd)
    if event == cv2.EVENT_MOUSEMOVE and xd + yd > 1000:
        exit()


def play_video(video):
    cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Frame", cv2.WINDOW_KEEPRATIO, cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback("Frame", stop)

    for v in video:
        cap = cv2.VideoCapture("E:/MOVIES/C64/" + v)
        while cap.isOpened():
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow("Frame", frame)

                if cv2.waitKey(25) & 0xFF == ord("q"):
                    exit()
            else:
                break
        cap.release()
    cv2.destroyAllWindows()


def main():
    videos = next(walk("E:/MOVIES/C64/"), (None, None, []))[2]  # [] if no file
    sampled = random.sample(videos, len(videos))
    while True:
        play_video(sampled)


if __name__ == "__main__":
    main()
