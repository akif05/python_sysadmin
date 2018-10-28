import logging

# This print out: WARNING:root:Something's not right
# Which is warning, name of the loger which is root and the message
logging.warning("Something's not right")

# If we log at a lover level nothing happens
logging.info("some info")

# REconiguration of the logger
# Setting the lover level of the debuger
logging.basicConfig(level = logging.DEBUG, format = "%(levelname)s, %(asctime)s %(message)s")
logging.warning("This is a warning")

