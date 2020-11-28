#!/usr/bin/env python3

CAM_NUMBER = 4
FOCUS = 20

import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol as symbol

class Tracker:
    cam = None
    # Set focus values: 0..255, increment: 5
    focus = 0
    show_window = False

    # Webcam number: /etc/videoN.
    def __init__(self, cam_number, focus, show_window = False):
        self.cam = cv2.VideoCapture(cam_number)
        self.focus = focus
        self.show_window = show_window

    def run(self):
        self.cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        self.__set_focus(self.focus)
        while True:
            ret_val, img = self.cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            proc = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
            if self.show_window:
                if self.__window_output(proc):
                    return
            self.__scan(proc)

    def __window_output(self, img):
        cv2.imshow('ttrckr', img)
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            return True
        elif key == 105:
            self.__set_focus(self.focus + 5)
            print(f"increase focus to {self.focus}")
        elif key == 100:
            self.__set_focus(self.focus - 5)
            print(f"decrease focus to {self.focus}")
        pass

    def __scan(self, img):
        height, width = img.shape[:2]
        results = decode((img.tobytes(), width, height)) 
        # print(results)
        if len(results) == 0:
            print("-")
        for result in results:
            print(result.data.decode("utf-8"))

    def __set_focus(self, value):
        if value < 0:
            print(f"requested focus value {value} is below 0")
            return
        elif value > 255:
            print(f"requested focus value {value} is above 255")
            return
        elif value % 5 != 0:
            print(f"requested focus value {value} ha to be a multiple of 5")
            return
        self.cam.set(28, value)
        self.focus = value


if __name__ == "__main__":
    tracker = Tracker(CAM_NUMBER, FOCUS, show_window=True)
    print("Press <esc> in the window to exit.")
    tracker.run()

