import bs4 as bs
import urllib.request

if __name__ == '__main__':
    url = 'https://pythonprogramming.net/parsememcparseface/'
    src = urllib.request.urlopen(url).read()

    soup = bs.BeautifulSoup(src, 'lxml')

    # print(soup) # print all html

    print(f'=== {soup.title.string} ===')

    print(f'first paragraph: \n{soup.p}\n\n')

    print(f'all paragraphs: \n{soup.find_all("p")}')

    for par in soup.find_all("p"):
        print(par.text)


    print(f'\n\nall the text: \n {soup.get_text()}\n\n')

    for url in soup.find_all('a'):
        print(f'found url: {url.get("href")}')