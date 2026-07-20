import logging

logging.basicConfig(
    filename = 'app.log',
    filemode='w',
    level = logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s', #s: Convert whatever value is found into a String (text) so it can be printed out.
    datefmt= '%y-%m-%d %H:%M:%S '
)