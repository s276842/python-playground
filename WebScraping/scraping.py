import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

if __name__ == '__main__':
    url = "https://docs.python.org/3/library/random.html"
    page = urllib.request.urlopen(url)

    soup = bs(page)
    print(soup)