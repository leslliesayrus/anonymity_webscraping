from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

# To run this code you gotta install the selenium (and the webdriver.exe), and the webdriver_manager


# There's a lot proxys and IP avalaible in the internet
proxy = '159.197.128.41:3128'

# setings the parameters
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy}')

# running the webdriver
browser = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
browser.get('https://en.wikipedia.org/wiki/Python_(programming_language)')

