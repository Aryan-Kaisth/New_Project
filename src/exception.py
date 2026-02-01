import sys
import traceback
from src.logger import logging


def get_detailed_error_message(error: Exception, error_details=sys) -> str:
    """
    Extracts detailed error information including filename,
    line number, and traceback.
    """
    _, _, exc_tb = error_details.exc_info()
    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno

    return (
        f"Error occurred in file [{file_name}], "
        f"line [{line_no}], "
        f"error [{str(error)}]"
    )


class CustomException(Exception):
    """
    Custom exception class that captures detailed error context
    and logs it automatically.
    """

    def __init__(self, error: Exception, error_details=sys):
        self.error_message = get_detailed_error_message(
            error=error,
            error_details=error_details
        )

        # Log immediately
        logging.error(self.error_message)

        super().__init__(self.error_message)

    def __str__(self) -> str:
        return self.error_message
