import json
import time
from typing import Tuple, List

import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use("TkAgg")

# Data settings
CALCULATE_DATA_FROM_VIDEO = False
FILE_WITH_DATA_SAMPLES = "temp/tests-1666381736.json"

# Video settings
VIDEO_PATH = "videos"
VIDEO_NAMES = [
    "20_1.mp4",
    "20_2.mp4",
    "20_3.mp4",
    "30_1.mp4",
    "30_2.mp4",
    "30_3.mp4"
]


def resize_with_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


def capture(filename: str, show_video: bool = False) -> Tuple[List[float], List[float]]:
    cap = cv2.VideoCapture(VIDEO_PATH + "/" + filename)
    movement_x = []
    movement_y = []
    while cap.isOpened():
        # Capture frame-by-frame
        success, frame = cap.read()
        if not success:
            break
        # print(frame.shape)
        frame_ref = frame[750:frame.shape[0] - 335, 300:1200]

        # Resize the frame to normal display
        resize = resize_with_ratio(frame_ref, height=900)

        # Compute the center of Yo-Yo
        gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        movement_x.append(cX)
        cY = int(M["m01"] / M["m00"])
        movement_y.append(cY)

        # Display the video
        if show_video:
            cv2.drawContours(resize, [c], 0, (0, 255, 0), 3)
            cv2.circle(resize, (cX, cY), 7, (0, 0, 255), -1)

            # Display the resulting frameq
            cv2.imshow('Frame', resize)
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

    return movement_x, movement_y


def normalization(data):
    vector = np.array(data, copy=True)

    # Take first value to set zero point
    zero_point = vector[0]
    vector = zero_point - vector

    # Crop the draggable data
    line = vector[:300]
    idx_zero = np.where(line == 0)[0][::-1][0]
    idx_one = np.where(line == 1)[0][::-1][0]
    idx_two = np.where(line == 2)[0][::-1][0]

    vector = vector[idx_one:] if idx_zero + 1 == idx_one else vector[idx_two:]

    return vector / 24


def plot(datas, labels, title, filename, save_file=True):
    for v in datas:
        plt.title(title)
        T = np.array(range(len(v))) / 60
        plt.plot(T, v)
        plt.grid()
        plt.xlabel("Time(s)")
        plt.ylabel("Distance(cm)")
    plt.legend(labels)
    if save_file:
        plt.savefig(filename, format="jpeg")
    plt.show()


if __name__ == '__main__':
    # Read data from the video
    tests = []
    if CALCULATE_DATA_FROM_VIDEO:
        for filename in VIDEO_NAMES:
            print(f"INFO: Started video streaming of the file {filename}")
            _, y = capture(filename)
            tests.append(normalization(y))

        with open(f"temp/tests-{int(time.time())}.json", "w") as f:
            d = []
            for el in tests:
                d.append(list(el))
            json.dump(d, f)
    else:
        with open(FILE_WITH_DATA_SAMPLES, "r") as f:
            tests = json.load(f)

    # Plots
    plot(tests[:3], VIDEO_NAMES[:3], "Real sample with Yo-Yo 20cm", "out/20cm.jpg")
    plot(tests[3:], VIDEO_NAMES[3:], "Real sample with Yo-Yo 30cm", "out/30cm.jpg")
