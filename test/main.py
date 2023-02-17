import os
from instauto import Scrapper
from instauto import Follow
from instauto import Unfollow
from dotenv import load_dotenv

load_dotenv()


username = os.getenv("INSTA_USERNAME")        # ENTER YOUR USERNAME HERE
password = os.getenv("INSTA_PASSWORD")        # ENTER YOUR PASSWORD HERE


def unfollowing():
    except_list = ["acepicstudio", "the_sam963"]
    unfollow = Unfollow(username, password)
    unfollow.unfollow(except_list, 12)


def following():
    print("Following...")
    target_uname = ["acepicstudio", "the_sam963"]
    follower = Follow(username, password)
    follower.follow_followers_of_user(target_uname, 30)


def scrapping():
    target_uname = ["acepicstudio", "the_sam963"]
    scrapper = Scrapper(username, password)
    scrapper.get_followers_of_user(target_uname, 30)




if __name__ == "__main__":
    # unfollowing()
    # following()
    # scrapping()
    pass

