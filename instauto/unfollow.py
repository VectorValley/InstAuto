import json
import random
import time
from .core import Core
from selenium.webdriver.common.by import By


class Unfollow(Core):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.username = username

    def unfollow(self, ignore_list: list | None, no_of_user: int):
        if self.is_loggedin:
            try:
                self.driver.get(f"https://www.instagram.com/{self.username}/following/")
                try:
                    self.scroll_followers_container(no_of_user)
                    time.sleep(2)

                    following_obj = self.driver.find_elements(By.XPATH, "//div[@class='_aano']/div/div/div")
                    user_names = self.driver.find_elements(By.XPATH, "//div[@class='_aano']/div/div/div/div[2]/div/div/div/div/span/a/span/div")
                    followeing_btns = self.driver.find_elements(By.XPATH, "//div[@class='_aano']/div/div/div/div[3]/button/div/div[contains(text(), 'Following')]")
                    time.sleep(1)

                    for i in range(len(following_obj)):
                        uname = user_names[i].text
                        btn = followeing_btns[i]
                        if uname in ignore_list:
                            continue
                        else:
                            btn.click()
                            time.sleep(1)
                            conf_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Unfollow')]")
                            conf_btn.click()
                            time.sleep(random.randint(1, 3))
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
