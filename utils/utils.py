
import chromedriver_binary
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import Tuple


class DriverSetting():
    def __init__(self, is_headless: bool, module_name: str):
        self.is_headless = is_headless
        self.module_name = module_name

    def setting_driver(self) -> webdriver.Chrome:
        options = Options()

        if self.is_headless:
            options.headless = True
        
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)

        return driver
    
    def setting_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.module_name)
        logger.setLevel(logging.INFO)

        sh = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        sh.setFormatter(formatter)

        return logger
    
    def __call__(self) -> Tuple[webdriver.Chrome, logging.Logger]:
        return (
            self.setting_driver(),
            self.setting_logger()
        )

