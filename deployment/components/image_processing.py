import cv2
import numpy as np
from logger import logging
from exception import CustomException

class ImageProcessing:
    def __init__(self):
        pass

    def process_image(self, image):
        """
        Process the in-memory image passed from the PredictionPipeline.
        """
        try:
            logging.info("Processing image in-memory...")

            # Convert to grayscale
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Resize the image to the required dimensions (e.g., 128x128 for consistency)
            image_resized = cv2.resize(image_gray, (128, 128))

            logging.info("Image processing completed.")
            return image_resized  # Return the processed image for further steps

        except Exception as e:
            raise CustomException(e, sys)
