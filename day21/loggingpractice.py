# import logging module
import logging

# basic configuration  
logging.basicConfig(level = logging.CRITICAL)

students = ['sam', 'shefali', 'reema', 'sidney', 'zach']
# log things
logging.debug("Hi, I'm a debug message.")
for x in range(10):
    logging.debug("x is currently %s" % x)
logging.info("Hi, I'm an informative message.")
logging.info("I counted to 10, make sure debug messages are showing to see")
logging.warning("Something appears to be wrong,be careful")
logging.error("Something is definitely wrong")
logging.critical("Something is very wrong, what have you done Sam?")
if 'gio' not in students:
    logging.critical("Gio is missing, where are you?")