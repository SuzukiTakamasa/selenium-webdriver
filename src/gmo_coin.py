
import os
import sys
import time
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.pardir))

from utils.utils import DriverSetting

load_dotenv()

def gmo_coin(driver, logger):
    logger.info("Login to GMO coin")

    driver.get("https://coin.z.com/jp/member/login")

    enter_email_address = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/section/div/div[1]/form/div/p[1]/input')
    enter_email_address.send_keys(os.environ["GMAIL_ADDRESS"])

    enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    enter_password.send_keys(os.environ["GMAIL_PASSWORD"])

    login = driver.find_element(By.XPATH, '//*[@id="login_button"]')
    login.click()

    order_token = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/nav/ul/li[4]/p/a')
    order_token.click()

    amount_list = driver.find_elements(By.CLASS_NAME, 'col-amount cell')
    for amounts in amount_list:
        logger.info(amounts.text)


if __name__ == '__main__':
    ds = DriverSetting(is_headless=False, module_name=os.path.splitext(__file__)[0])
    driver, logger = ds()
    gmo_coin(driver, logger)