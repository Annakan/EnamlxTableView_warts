import os
from enaml.image import Image
from enaml.icon import Icon, IconImage

dir_path = os.path.dirname(os.path.realpath(__file__))


def icon_path(name):
    return os.path.join(dir_path, '..', 'images', 'icons', '%s.png' % name)


def load_image(name):
    with open(icon_path(name), 'rb') as f:
        data = f.read()
    return Image(data=data)


def load_icon(name):
    img = load_image(name)
    icg = IconImage(image=img)
    return Icon(images=[icg])
