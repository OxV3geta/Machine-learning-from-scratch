import logging

## create logging settings
logging.basicConfig(
    level= logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app23.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithmethicApp')

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def sub(a,b):
    result = a-b
    logger.debug(f"substracting {a}-{b} = {result}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplying {a}*{b} = {result}" )
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"dividing {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(4,4)
sub(20,4)
multiply(5,4)
divide(20,4)