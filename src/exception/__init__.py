import sys
from src.logger.custom_logger import custom_logger

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line number, and the error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in [{file_name}] at line [{line_number}]: {str(error)}"
    
    custom_logger.error(error_message)
    return error_message

class CustomException(Exception):
    """
    Custom exception class for handling application-level errors.
    """
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
