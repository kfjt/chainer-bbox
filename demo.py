import argparse
import matplotlib.pyplot as plot

import chainer

from chainercv.datasets import voc_bbox_label_names
from via_utils import via_bbox_label_names
from chainercv.links import SSD300
from chainercv.links import SSD512
from chainercv import utils
from chainercv.visualizations import vis_bbox


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model', choices=('ssd300', 'ssd512'), default='ssd300')
    parser.add_argument('--gpu', type=int, default=-1)
    parser.add_argument('--pretrained_model', default='via_model')
    parser.add_argument('image')
    args = parser.parse_args()

    if args.model == 'ssd300':
        model = SSD300(
            n_fg_class=len(voc_bbox_label_names),
            pretrained_model=args.pretrained_model)
    elif args.model == 'ssd512':
        model = SSD512(
            n_fg_class=len(via_bbox_label_names),
            pretrained_model=args.pretrained_model)

    if args.gpu >= 0:
        chainer.cuda.get_device_from_id(args.gpu).use()
        model.to_gpu()

    img = utils.read_image(args.image, color=True)
    bboxes, labels, scores = model.predict([img])
    bbox, label, score = bboxes[0], labels[0], scores[0]

    names = []
    for item in label:
      names.append(via_bbox_label_names[item])
    cnt = {name:names.count(name) for name in names}
    print(cnt)

    vis_bbox(
        img, bbox, label, score, label_names=via_bbox_label_names)
    plot.show()


if __name__ == '__main__':
    main()
