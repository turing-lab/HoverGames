import sys
import cv2
import torch
import random
from PIL import Image
from models import Darknet
import matplotlib.pyplot as plt
from torchvision import transforms

import cfg
from sort import Sort
from utils.utils import load_classes
from utils.utils import rescale_boxes
from utils.utils import non_max_suppression


def main():
    # load model
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model = Darknet(cfg.MODEL, img_size=cfg.SIZE).to(device)
    model.load_darknet_weights(cfg.WEIGHTS)
    model.eval()

    # coco classes
    classes = load_classes(cfg.CLASSES)

    # animals and person
    app_classes = [0, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    # tensor type
    Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

    # create video capture
    cap = cv2.VideoCapture('udp://127.0.0.1:5000', cv2.CAP_FFMPEG)
    if not cap.isOpened():
        print('VideoCapture not opened')
        exit(-1)

    # preprocess pipeline
    t = transforms.Compose([
        transforms.Resize((cfg.SIZE, cfg.SIZE)),
        transforms.ToTensor()
    ])

    # tracker
    tracker = Sort()

    # bbox colors
    colors=[
        (255,0,0),
        (0,255,0),
        (0,0,255),
        (255,0,255),
        (128,0,0),
        (0,128,0),
        (0,0,128),
        (128,0,128),
        (128,128,0),
        (0,128,128)
    ]

    # process stream
    while True:
        # read frame
        ret, frame = cap.read()
        # frame = cv2.flip(cv2.flip(frame, 0), 1)
        orig = frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)

        # process image
        img = t(img).unsqueeze(0).type(Tensor)
        with torch.no_grad():
            detections = model(img)
            detections = non_max_suppression(detections, cfg.CONF, cfg.NMS)
            detections = detections[0]
            if detections is not None:
                # track objects
                tracked_objects = tracker.update(detections.cpu())
                det = rescale_boxes(tracked_objects, cfg.SIZE, frame.shape[:2])
                for x1, y1, x2, y2, obj_id, cls_pred in det:
                    # ignore not necessary classes
                    if int(cls_pred) not in app_classes:
                        continue
                    # draw bbox
                    color = colors[int(obj_id) % len(colors)]
                    cls = classes[int(cls_pred)]
                    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
                    cv2.rectangle(orig, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(
                        orig,
                        cls + '-' + str(int(obj_id)),
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 255, 255),
                        3
                    )

        cv2.imshow('YoloV3', orig)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
