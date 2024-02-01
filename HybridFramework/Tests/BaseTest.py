import pytest
from datetime import datetime


@pytest.mark.usefixtures("init_driver", "log_on_failure")
class BaseTest:

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "amotoori" + time_stamp + "@gmail.com"
