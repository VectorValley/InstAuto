# InstAuto

Let's grow on Instagram automating some borring task. _InstAuto_ will help you to get more followers on instagram, more reach on Instagram.
<br><br><br>


# Features
- Scrap all followers of any given user
- Follow all followers of any given user
- Unfollow all your following (except selected users)
<br><br><br>


# Installation
Before dive into installation process, make sure you have Python installed on your system & also you have a text editor to make little changes.

## Using Git
Open Command Prompt (windows) or Terminal (Linux/MAC) & follow the following commands.

    git clone https://github.com/the-sam963/InstAuto.git
    cd InstAuto
    python setup.py install


## Using GUI
- Download zip file of the repository
- Extract
- Open directory
- Double on _`setup.py`_

It will installed all the required dependencies.
<br><br><br>


# Getting Start
<p>On the root directory you'll find two main directories, instauto(package) & test (implimentation).</p>

>Open test/main.py, replace _`username`_ & _`password`_ with your Instagram username & password. Also change other informations with your requirements & run any function of them.

<br>
You can also write your own script. Here is some demo bellow. 
<br><br>

## Follow all followers of user
    from instauto import Follow
    
    # Credentials
    username = ""        # ENTER YOUR USERNAME HERE
    password = ""        # ENTER YOUR PASSWORD HERE

    # Arguments
    target_uname = ["acepicstudio", "the_sam963"]
    no_of_follower = 60     # [Recomended 12 to 800]

    follow = Follow(username, password)
    follow.follow_followers_of_user(target_uname, no_of_follower)

The function _`follow_followers_of_user`_ takes two parameters,
- <b>_`target_uname`_<b> - list of usernames. Our script will go through all profile of list and follow all followers of them one by one.
-  <b>_`no_of_follower`_<b> - How many number of followers you wont to follow of each user added in _target_uname_ list. But there is a restriction also, don't input more than 800. Otherwise you may face some trouble.
<br><br>

## Scrap all followers of user
It is same as above method. But it has some more features. It will store all followers of selected users insted of following them.

After storring them you can use them as you want. But do not use this trick for any illegal purpose.
<br><br>

## Unfollow all your following
This method will go through all you following and will _Unfollow_ them. Also you can add a list of users not to _Unfollow_ them.

    from instauto import Unfollow

    # Credentials
    username = ""        # ENTER YOUR USERNAME HERE
    password = ""        # ENTER YOUR PASSWORD HERE

    ignore_list = ["acepicstudio", "the_sam963"]
    no_of_uaer = 60     # [Recomended 12 to 800]

    unfollow = Unfollow(username, password)
    unfollow.unfollow(ignore_list, no_of_uaer)

So, the method will ignore all users of _`ignore_list`_. Means it will not unfollow any user of the ignore_list. So put the usernames here yoy want not to unfollow.
<br><br><br>



# Follow me
[YouTube](https://www.youtube.com/@acepicstudio) <br>
[Instagram](https://www.instagram.com/acepicstudio/) <br>
[Discord](https://discord.gg/We68tgsx2f) <br>

