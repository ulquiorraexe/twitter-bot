import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 20
PROMISED_UP = 10
MAIL = "minniethepuf@gmail.com"
PASSWORD = "yasemin1"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(5)
        accept_button = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        accept_button.click()
        time.sleep(1)
        go_button = self.driver.find_element(By.CSS_SELECTOR, value="span.start-text")
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")

        time.sleep(60)
        login = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
        login.click()
        time.sleep(60)
        number_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label')
        number_input.click()
        number_input.send_keys(MAIL, Keys.ENTER)
        time.sleep(3)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(PASSWORD, Keys.ENTER)
        time.sleep(5)
        tweet_input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet_input.click()
        tweet_input.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up?")
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        post_button.click()



bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()

