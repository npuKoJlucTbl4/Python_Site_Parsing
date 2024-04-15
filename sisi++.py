from selenium import webdriver
from bs4 import BeautifulSoup


def parsing():
    url = "https://www.pepper.ru/"

    try:

        driver = webdriver.Edge()
        driver.get(url)
        page = driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        name = soup.findAll('strong' ,class_='thread-title')
        temp = soup.findAll('span', class_='vote-temp')
        link = soup.findAll('a', class_='thread-link')
        for i in range(len(name)):
            print(name[i].text)
            print(temp[i].text.strip())
            print(link[i].get('href') + "\n")

    finally:
        driver.quit()

if __name__ == "__main__":
    parsing()