from turtle import color
import cv2
from threading import Thread
import numpy as np
from math import sqrt

isInput = True
needDetect = False
def getInput():
    global needDetect
    recordSide = False
    while(isInput):
        if not recordSide:
            answer = input("Detect?")
            needDetect = answer == "Y"
            recordSide = needDetect


def get_avg(frame):
    c1 = np.array(frame)[:, :, 0]
    c2 = np.array(frame)[:, :, 1]
    c3 = np.array(frame)[:, :, 2]
    avg_c1 = np.average(c1)//1
    avg_c2 = np.average(c2)//1
    avg_c3 = np.average(c3)//1

    return (avg_c1, avg_c2, avg_c3)


def get_color_distance(color1, color2):
    sum_d = 0
    for i in range(3):
        dc = (color1[i] - color2[i])
        sum_d += dc*dc
    return sqrt(sum_d)


RED = (60,20,220)
ORANGE = (80,127,255)

sideIsDone = False
def main():
    global isInput
    cap = cv2.VideoCapture(0)
    # t = Thread(target=getInput)
    close_key = ord('q')
    # t.start()
    unit_w = 120
    unit_h = 120
    unit_3w = 3*unit_w
    unit_3h = 3*unit_h
    unit_2h = unit_h*2
    unit_2w = unit_w*2
    # sw = int(1.5*unit_w)
    # sh = int(1.5*unit_h)
    thicc = 3
    COLOR_LINE = (0, 0, 0)
    while cap.isOpened:
        ret, frame = cap.read()
        # frame = cv2.flip(frame, 1)
        color_0 = get_avg(frame[unit_h: unit_2h, unit_w: unit_2w])
        # print(color_0)
        dRed = get_color_distance(color_0, RED)
        dOrange = get_color_distance(color_0, ORANGE)
        if(dRed > dOrange and dOrange < 127):
            print("IT IS SORTA ORANGE")
        elif(dRed < dOrange and dRed < 127):
            print("IT IS SORTA RED")
        # print(f'distance to red: {get_color_distance(color_0, RED)}')
        # print(f'distance to orange: {get_color_distance(color_0, ORANGE)}')
        # color_1 = get_avg(frame[unit_h: unit_3h, unit_w: unit_3w])
        # color_2 = get_avg(frame[unit_h: unit_3h, unit_w: unit_3w])
        # color_3 = get_avg(frame[unit_h: unit_3h, unit_w: unit_3w])
        # draw edges for cube placement
        cv2.line(frame, (unit_w, unit_h), (unit_w, unit_3h), COLOR_LINE, thicc)
        cv2.line(frame, (unit_3w, unit_h), (unit_3w, unit_3h), COLOR_LINE, thicc)
        cv2.line(frame, (unit_w, unit_h), (unit_3w, unit_h), COLOR_LINE, thicc)
        cv2.line(frame, (unit_w, unit_3h), (unit_3w, unit_3h), COLOR_LINE, thicc)

        # Make a cross
        cv2.line(frame, (unit_w, unit_2h), (unit_3w, unit_2h), COLOR_LINE, thicc)
        cv2.line(frame, (unit_2w, unit_h), (unit_2w, unit_3h), COLOR_LINE, thicc)
        # rect_avg = np.full((unit_w, unit_h, 3), RED, np.uint8)
        # ora_avg = np.full((unit_w, unit_h, 3), ORANGE, np.uint8)
        cv2.imshow('camera', frame)
        # cv2.imshow('avg', rect_avg)
        # cv2.imshow('ora', ora_avg)
        key = cv2.waitKey(1) & 0xFF
        if(key == close_key):
            isInput = False
            cv2.destroyAllWindows()
            cap.release()
            # t.join()
            break


if __name__ == "__main__":
    main()