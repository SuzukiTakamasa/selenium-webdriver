
import os
import sys

sys.path.append(os.path.abspath(os.pardir))

from utils.utils import DriverSetting

def itoyokado_net_super():
    return None


if __name__ == '__main__':
    ds = DriverSetting(is_headless = True, module_name=os.path.splitext(__file__)[0])
    driver, logger = ds()