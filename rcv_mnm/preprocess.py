from PIL import Image
from mtcnn.mtcnn import MTCNN
import io
import numpy as np
import numpy as np
import requests
import tempfile

IMAGE_SIZE = 224
#Method to extract Face
def extract_image_base(
    image,
):
    image    = image.convert("RGB")
    pixels   = np.asarray(image)
    detector = MTCNN()
    f        = detector.detect_faces(pixels)
    if len(f) > 0:
        x1, y1, w, h = f[0]["box"]
        x1, y1       = abs(x1), abs(y1)
        x2           = abs(x1+w)
        y2           = abs(y1+h)
        store_face   = pixels[y1:y2,x1:x2]
        image1       = Image.fromarray(store_face, "RGB")
        image1       = image1.resize((IMAGE_SIZE, IMAGE_SIZE))
        return image1
    else:
        return None

def get_url_image(
    img_url: str,
):
    buffer = tempfile.SpooledTemporaryFile(max_size=1e9)
    r      = requests.get(img_url, stream=True)
    if r.status_code == 200:
        downloaded = 0
        filesize   = int(r.headers["content-length"])
        for chunk in r.iter_content(chunk_size=1024):
            downloaded += len(chunk)
            buffer.write(chunk)
        buffer.seek(0)
        image = Image.open(io.BytesIO(buffer.read()))
    buffer.close()
    return image

def extract_image(
    input:      str,
    input_type: str = "file",
):
    if input_type == "file":
        img1 = Image.open(input)
    elif input_type == "url":
        img1 = get_url_image(input)
    else:
        raise ValueError("Unsupported input type; must be 'file' or 'url'.")
    return extract_image_base(img1)

def extract_image_to_nparray(
    input:      str,
    input_type: str = "file",
):
    return np.expand_dims(
        np.asarray(
            extract_image(
                input,
                input_type,
            )
        ),
        axis = 0,
    )