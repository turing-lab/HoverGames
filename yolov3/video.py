import cv2
import torch
import random
from PIL import Image
from models import Darknet
import matplotlib.pyplot as plt
from torchvision import transforms

import cfg
from utils.utils import load_classes
from utils.utils import rescale_boxes
from utils.utils import non_max_suppression


def main():
    # load model
    device = torch.device('cpu')
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
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print('VideoCapture not opened')
        exit(-1)

    # preprocess pipeline
    t = transforms.Compose([
        transforms.Resize((cfg.SIZE, cfg.SIZE)),
        transforms.ToTensor()
    ])

    # process stream
    while True:
        # read frame
        ret, frame = cap.read()
        orig = frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)

        # process image
        img = t(img).unsqueeze(0).type(Tensor)
        with torch.no_grad():
            detections = model(img)
            detections = non_max_suppression(detections, cfg.CONF, cfg.NMS)

            # draw detections
            for i, det in enumerate(detections):
                if det is not None:
                    det = rescale_boxes(det, cfg.SIZE, frame.shape[:2])
                    unique_labels = det[:, -1].cpu().unique()
                    n_cls_preds = len(unique_labels)
                    for x1, y1, x2, y2, conf, cls_conf, cls_pred in det:
                        if int(cls_pred) not in app_classes:
                            continue
                        print('Label: %s, Conf: %.5f' % (classes[int(cls_pred)], cls_conf.item()))
                        orig = cv2.rectangle(orig, (x1, y1), (x2, y2), (255, 0, 0), 2)

        cv2.imshow('YoloV3', orig)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
