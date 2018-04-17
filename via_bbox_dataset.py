import numpy as np
import os
import warnings
import xml.etree.ElementTree as ET

import chainer

from chainercv.datasets.voc import voc_utils
from chainercv.utils import read_image

import json
from pathlib import Path
from via_utils import via_bbox_label_names

class BboxDataset(chainer.dataset.DatasetMixin):

    def __init__(self, data_dir='auto', split='train', year='2012',
                 use_difficult=False, return_difficult=False):
        id_list_file = os.path.join(
            data_dir, 'ImageSets/Main/{0}.txt'.format(split))

        self.ids = [id_.strip() for id_ in open(id_list_file)]

        self.data_dir = data_dir
        self.use_difficult = use_difficult
        self.return_difficult = return_difficult

    def __len__(self):
        return len(self.ids)

    def get_example(self, i):
        """Returns the i-th example.

        Returns a color image and bounding boxes. The image is in CHW format.
        The returned image is RGB.

        Args:
            i (int): The index of the example.

        Returns:
            tuple of an image and bounding boxes

        """
        id_ = self.ids[i]

        json_path = Path('auto','Annotations','via_region_data.json')
        json_loaded = json.load(json_path.open('r'))
        png_path = Path('auto', 'PNGImages', id_ + '.png')
        png_size = png_path.stat().st_size
        anno = json_loaded[id_ + '.png' + str(png_size)]

        bbox = []
        label = []
        difficult = []
        for obj in anno['regions']:
            # when in not using difficult split, and the object is
            # difficult, skipt it.
            if not self.use_difficult and 0 == 1:
                continue

            difficult.append(0)
            # subtract 1 to make pixel indexes 0-based
            bndbox_anno = anno['regions'][obj]['shape_attributes']
            bbox.append([
                bndbox_anno['y'],
                bndbox_anno['x'],
                bndbox_anno['y'] + bndbox_anno['height'],
                bndbox_anno['x'] + bndbox_anno['width']])
            name = anno['regions'][obj]['region_attributes']['shape'].lower().strip()
            label.append(via_bbox_label_names.index(name))
        bbox = np.stack(bbox).astype(np.float32)
        label = np.stack(label).astype(np.int32)
        # When `use_difficult==False`, all elements in `difficult` are False.
        difficult = np.array(difficult, dtype=np.bool)

        # Load a image
        img = read_image(png_path.as_posix(), color=True)
        if self.return_difficult:
            return img, bbox, label, difficult
        return img, bbox, label
