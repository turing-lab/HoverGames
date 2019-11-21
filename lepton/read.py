import cv2
import numpy as np
from pylepton import Lepton


def main():
    img, _ = l.capture()
    # extend contrast
    cv2.normalize(img, img, 0, 65535, cv2.NORM_MINMAX)
    # fit data into 8 bits
    np.right_shift(img, 8, img)
    # conver np array to uint8 type
    img = np.uint8(img)
    # create an output image
    cv2.imwrite("out.jpg", img)


if __name__ == '__main__':
    main()
