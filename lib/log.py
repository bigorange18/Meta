import logging

LOGGING_NAME = "yolov5"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='./logger/my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
