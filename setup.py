from setuptools import setup, find_packages
import codecs
import os



BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = '1.0.0'
DESCRIPTION = r"Automaticly scrap, follow other's followers; user followed hashtags. Also you can unfollow all your following with one click"



with codecs.open(os.path.join(BASE_DIR, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


# Setting up
setup(
    name="instauto",
    version=VERSION,
    author="Acepic Studio (Sam)",
    author_email="<sam@acepicstudio.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['webdriver-manager==3.8.5', "selenium==4.1.0", "python-dotenv"],
    keywords=['python', 'instagram', 'dev-tool', 'imsta-bot'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
    
)
