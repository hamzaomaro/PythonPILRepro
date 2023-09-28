# # to start the code, you will need to load this .venv file

# # for windows: .venv\scripts\activate

# # for linux: source .venv/bin/activate

 

# import logging

# import json

 

# import azure.functions as func

# from .main.constant import *

# from .main.ffi_pipeline.finger_fold_analysis import finger_fold_anaylsis_pipeline

# from .main.utils import open_image_from_azure_bucket, prepare_images, send_results

 

 

# def main(msg: func.ServiceBusMessage):

#     logging.info(

#         "Python_message: %s",

#         msg.get_body().decode("utf-8"),

#     )

 

#     data = json.loads(msg.get_body())

#     logging.info("2nd message : %s", data,)

#     for image_data in data:

#         image_hand = open_image_from_azure_bucket(image_data["picture_location_in_bucket"])

#         analysis = finger_fold_anaylsis_pipeline(image_hand, which_hand=image_data['which_hand'])

#         analysis = prepare_images(analysis, image_data)

#         send_results(image_data, analysis)

#         logging.info("Task processed correctly")

 

#     return


import logging

import azure.functions as func

from PIL import Image

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # open method used to open different extension image file
    im = Image.open("428617.jpg")  

    return "opened image successfully"
