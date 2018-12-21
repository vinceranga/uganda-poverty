from google.cloud import storage
from google.cloud import exceptions
import os
import logging
from PIL import Image
import numpy as np
import pandas as pd


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="poverty.json"
bucket_name = 'uganda'


def open_images(img_id, sqs):
    """Downloads a blob from the bucket."""
    if not isinstance(sqs, list):
        sqs = [sqs]
    
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    
    for sq in sqs:
        img_name = 'dg_lsms_uganda_1000x1000_' + str(img_id) + '_' + str(sq) + '.jpeg'
        blob_name = 'LSMS_dg/' + img_name
        target_name = 'LSMS_dg/' + img_name
        if os.path.exists(target_name): continue  # file already downloaded

        blob = bucket.blob(blob_name)
        blob.download_to_filename(target_name)
    
        # print("Image downloaded!")
    
    
def display_image(img_id, sq):
    img_name = 'dg_lsms_uganda_1000x1000_' + str(img_id) + '_' + str(sq) + '.jpeg'
    target_name = 'LSMS_dg/' + img_name
    
    img = Image.open(target_name)
    img.show()
    

def get_lat_lon(img_id, sq):
    (index,) = np.where(serials[0] == img_id)
    index = index[sq]
    
    lat = np.mean([serials[1, index], serials[3, index]])
    lon = np.mean([serials[2, index], serials[4, index]])
    return lat, lon