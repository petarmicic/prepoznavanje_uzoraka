from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 

def search_fun():

    query = input() + " imdb"
    
    url = search(query, num=1, stop=1).__next__()

    print(url)

    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get(url)

    driver.get_screenshot_as_file("slika.png")

    driver.quit()
    print("end...")

search_fun()