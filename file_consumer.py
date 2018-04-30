"""
This file contains the implementation of consumer, who consumes messages from the file.

date: April 30, 2018
author: Mangu Singh Rajpurohit
"""
import time
import logging

from random import randrange
from constants import FILE_AS_BROKER_PATH

LOGGER = logging.getLogger()


with open(FILE_AS_BROKER_PATH, "r") as handle:
    while True:
        message = ""
        while True:
            read_char = handle.read(1)
            if not read_char or read_char == "#":
                break
            message += read_char

        LOGGER.info("READ: " + read_val)

        time_to_sleep = randrange(1, 10)
        time.sleep(time_to_sleep)
