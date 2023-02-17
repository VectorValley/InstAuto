from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time






class Core:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.options = Options()
        self.options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.maximize_window()

        self.is_loggedin = self.login(self.username, self.password)

    def login(self, username, password):
        try:
            self.driver.get("https://www.instagram.com/accounts/login/")

            try:
                # Getting input fields
                username_field = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
                password_field = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

                # Make sure that there is no input already
                username_field.clear()
                password_field.clear()

                # Input credentials
                username_field.send_keys(username)
                password_field.send_keys(password)

                # click login
                login_btn = WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
                login_btn.click()

            except:
                print("[ERROR] Input fields not found...")

            time.sleep(3)
            try:
                save_info_alert = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]')))
                save_info_alert.click()

                notification_alert = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]')))
                notification_alert.click()
            except:
                pass

            if self.driver.current_url == "https://www.instagram.com/" or self.driver.current_url == "http://www.instagram.com/":
                return True
            else:
                return False
        except:
            print("[ERROR] Loging page not found...")

    def scroll_followers_container(self, follower_count):
        for i in range(follower_count // 12):
            f_window = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='_aanq']")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", f_window)
            time.sleep(2)

