"""
This file contains the implementation of producer, who produces messages and publishes to file.

date: April 30, 2018
author: Mangu Singh Rajpurohit
"""
# imports
import time
import logging
from random import randrange
from sys import stdout

from constants import FILE_AS_BROKER_PATH

LOGGER = logging.getLogger()
LOGGER.addHandler(logging.StreamHandler(stream=stdout))

with open(FILE_AS_BROKER_PATH, "w") as handle:
    message_publish_count = 0
    while True:
        message_publish_count += 1
        time_to_sleep = randrange(1, 10)

        # Message Format:-  <id><random number of stars>#  (here # is the message separator in the file.
        message_content = str(message_publish_count) + "*" * time_to_sleep + "#"
        handle.write(message_content)
        # need to flush the message, as soon as it's written, otherwise, consumer
        # will have to wait till long, until buffer of 8K gets filled and get written
        # to disk.
        handle.flush()

        LOGGER.info("Published Message " + message_content)

        time.sleep(time_to_sleep)
