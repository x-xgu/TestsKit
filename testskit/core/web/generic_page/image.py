import base64
from io import BytesIO
from pathlib import Path
from typing import Union

import ddddocr
from PIL import Image
from selene import Element, query
from skimage.metrics import structural_similarity as ssim

from testskit import common

TRANSLATE_CANVAS_TO_PNG = \
    'var canvas = self; ' \
    'return canvas.toDataURL("image/png");'
TRANSLATE_CANVAS_TO_PNG_WITH_WHITE_BACKGROUND = \
    'var canvas = self;' \
    'var context = canvas.getContext("2d");' \
    'context.globalCompositeOperation="destination-over";' \
    'context.fillStyle="white";' \
    'context.fillRect(0,0,canvas.width,canvas.height);' \
    'context.globalCompositeOperation="source-over";' \
    'return canvas.toDataURL("image/png");'


def get_canvas_bytes(
        element: Element,
        add_background: bool = False
) -> bytes:
    """
    Get canvas bytes
    """
    img_data = element.execute_script(
        TRANSLATE_CANVAS_TO_PNG
        if not add_background
        else TRANSLATE_CANVAS_TO_PNG_WITH_WHITE_BACKGROUND
    )
    img_base64 = img_data.split(',')[1]
    img_bytes = base64.b64decode(img_base64)
    return img_bytes


def pic_compare_with_ssim(
        image1,
        image2
):
    """
    Compare two images with SSIM
    """
    score, _ = ssim(
        image1,
        image2,
        full=True
    )
    return score


def compare_canvas_similarity(
        canvas: Element,
        origin_image: Union[bytes, str, Path]
):
    """
    Compare canvas with origin image
    """
    img_bytes = get_canvas_bytes(canvas)
    img_numpy = common.convert.bytes_to_numpy(img_bytes)

    if isinstance(origin_image, Union[str, Path]):
        with open(origin_image, 'rb') as f:
            origin_image = f.read()

    origin_img_numpy = common.convert.bytes_to_numpy(origin_image)

    return pic_compare_with_ssim(img_numpy, origin_img_numpy)


def recognize_img_text(
        img_bytes: bytes,
        recognize_area=None
) -> str:
    """
    Recognize image text
    """
    with Image.open(BytesIO(img_bytes)) as img:
        recognize_part = img.crop(recognize_area) if recognize_area else img
        ocr = ddddocr.DdddOcr(show_ad=False)
        return ocr.classification(recognize_part) or None


def recognize_canvas_text_with_area(
        element: Element,
        w1: float = 0,
        w2: float = 1,
        h1: float = 0,
        h2: float = 1
):
    """
    Recognize canvas text with area
    """
    width_str = element.get(query.attribute('width'))
    height_str = element.get(query.attribute('height'))
    if width_str.isdigit() and height_str.isdigit():
        width, height = eval(width_str), eval(height_str)
        recognize_area = (
            w1 * width,
            h1 * height,
            w2 * width,
            h2 * height
        )
        img_bytes = get_canvas_bytes(element, add_background=True)
        text = recognize_img_text(img_bytes, recognize_area)
        return text
    else:
        return None
