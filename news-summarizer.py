from bs4 import BeautifulSoup
from requests import get
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

def get_only_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    title = ' '.join(soup.title.stripped_strings)
    return title, text

text = get_only_text('https://www.cnn.com/2022/08/19/politics/fulton-county-lindsey-graham-testimony/index.html')
print("Title" + text[0])
print("Summary : ")
print(summarize(repr(text), word_count = 100))
