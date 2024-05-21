# exception.py
import sys
from logger import logger

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"ERROR OCCURRED IN PYTHON SCRIPT NAME [{file_name}] LINE NUMBER [{exc_tb.tb_lineno}] ERROR MESSAGE [{str(error)}]"
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        logger.error(self.error_message)
        logger.info("defination error_message_detail: %s Created successfully" % error_message)
        logger.info("CustomException Class: %s Created successfully" % error_message)

    def __str__(self):
        return self.error_message

def do_something(value):
    try:
        if value <= 0:
            raise ValueError("Value must be positive ", {"value": value})
        result = value / 0
    except ZeroDivisionError as e:
        logger.info(f"Exception.py line 29 ",CustomException(str(e), sys))
        raise CustomException(str(e), sys) from e
        
    
    return value * 2

try:
    result = do_something(10)
except CustomException as e:
    
    logger.info("Logging Exception logs")
