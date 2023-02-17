import json
import time
from .core import Core
from selenium.webdriver.common.by import By

class Scrapper(Core):
    def __init__(self, username, password):
        super().__init__(username, password)

        self.FILE_NAME = "instauto_followers.json"

    def get_followers_of_user(self, target_users: list, follower_count, filename=None):
        if self.is_loggedin:
            try:
                if filename is not None:
                    with open(filename, 'r') as file:
                        d_ = file.read()
                        data = json.load(d_)
                else:
                    with open(self.FILE_NAME, 'r') as file:
                        d_ = file.read()
                        data = json.load(d_)
            except:
                data = {}

            try:
                for target_uname in target_users:
                    try:
                        self.driver.get(f"https://www.instagram.com/{target_uname}/followers/")
                        try:
                            data[target_uname] = []
                            followers = []
                            self.scroll_followers_container(follower_count)

                            time.sleep(2)
                            followers_obj = self.driver.find_elements(By.XPATH, "//span/a/span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")

                            for follower in followers_obj:
                                if follower not in followers:
                                    followers.append(follower.text)

                            data[target_uname] = followers

                        except Exception as e:
                            print(e)
                    except Exception as e:
                        print(f"[ERROR] user '{target_uname}' in not valid")
                        print(e)


                # Saving Data
                json_obj = json.dumps(data)
                if filename is not None:
                    with open(filename, 'w') as file:
                        file.write(json_obj)
                else:
                    with open(self.FILE_NAME, 'w') as file:
                        file.write(json_obj)

            except:
                pass
