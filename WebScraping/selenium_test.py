

from selenium import webdriver
CHROME_PATH = r'chromedriver.exe'

if __name__ == '__main__':
    driver = webdriver.Chrome(CHROME_PATH)
    url = 'https://vancouver.craigslist.org/'
    driver.get(url)

    driver.find_element_by_xpath("""//*[@id="sss0"]/li[23]/a""").click()

    posts = driver.find_elements_by_class_name('result-heading')
    for post in posts:
        print(post.text)
