from extract_data import extract_data
from PIL import Image
import requests
from io import BytesIO
import zipfile
import pathlib 
import random
import os

def visualise_image():
    url = extract_data()
    url_response = requests.get(url)
    with zipfile.ZipFile(BytesIO(url_response.content)) as z:
        z.extractall('.')
    # print("------------",os.listdir(os.path.join(os.getcwd(),"Training/pituitary_tumor")))
    path = pathlib.Path(os.path.join(os.getcwd(),"Training"))
    def open_random_image(path):
        # Get a list of all files in the folder
        all_files = os.listdir(path)
        random_image_file = random.choice(all_files)
        image_path = os.path.join(path, random_image_file)
        image = Image.open(image_path)
        return image
    glioma_tumor_image = open_random_image(os.path.join(os.getcwd(),"Training/glioma_tumor"))
    meningioma_tumor_image = open_random_image(os.path.join(os.getcwd(),"Training/meningioma_tumor"))
    no_tumor_image = open_random_image(os.path.join(os.getcwd(),"Training/no_tumor"))
    pituitory_tumor_image = open_random_image(os.path.join(os.getcwd(),"Training/pituitary_tumor"))
    glioma_tumor_image.save('glioma_tumor.jpg')
    meningioma_tumor_image.save('meningioma_tumor.jpg')
    no_tumor_image.save('no_tumor.jpg')
    pituitory_tumor_image.save('pituitory_tumor.jpg')
    return path

visualise_image()
