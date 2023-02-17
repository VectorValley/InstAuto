import json
import random
import time
from .core import Core
from selenium.webdriver.common.by import By

class Follow(Core):
    def __init__(self, username, password):
        super().__init__(username, password)

    def follow_followers_of_user(self, target_users, no_of_follower):
        if self.is_loggedin:
            try:
                # Starting follow process
                for target_uname in target_users:
                    try:
                        self.driver.get(f"https://www.instagram.com/{target_uname}/followers/")
                        try:
                            self.scroll_followers_container(no_of_follower)

                            time.sleep(2)
                            follower_btns = self.driver.find_elements(By.XPATH, "//div[@class='_aano']/div/div/div/div[3]/button/div/div[contains(text(), 'Follow')]")
                            i = 0
                            for button in follower_btns:
                                if button.text == "Following" or button.text == "Requested" or button.text == "Remove":
                                    pass
                                else:
                                    button.click()
                                    try:
                                        time.sleep(random.randint(1, 3))
                                        alert_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'OK')]")

                                        if alert_btn is not None:
                                            i += 1
                                            alert_btn.click()
                                        if i >= 3:
                                            print("[ERROR] Facing trouble to follow. Terminating process")
                                            print("Try again later...")
                                            break

                                    except:
                                        pass

                                    time.sleep(random.randint(1, 3))

                        except Exception as e:
                            print(e)
                    except Exception as e:
                        print(f"[ERROR] user '{target_uname}' in not valid")
                        print(e)
            except:
                pass
