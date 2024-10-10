from pprint import pprint
import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
response = requests.get('https://habr.com/ru/articles')
soup = bs4.BeautifulSoup(response.text, features='lxml')

# Список статей
articles_list = soup.findAll("article", class_ = "tm-articles-list__item")

#Получаем текст статьи, доступный с текущей страницы
preview_text = " "
for article in articles_list:
    if article.find("div",class_ = "article-formatted-body article-formatted-body article-formatted-body_version-2") != None:
        preview_text = article.find("div",class_ = "article-formatted-body article-formatted-body article-formatted-body_version-2").text

    if article.find("div",class_="article-formatted-body article-formatted-body article-formatted-body_version-1") != None:
        preview_text = article.find("div",class_ = "article-formatted-body article-formatted-body article-formatted-body_version-1").text

#   Получаем необходимую информацию в каждой статье
    date = article.find('time')['datetime'][:10]
    title = article.h2.a.text.strip()
    link = f'https://habr.com{article.h2.a['href']}'
#   Поиск нужных слов в тексте статьи, доступном с текущей страницы
    for word in KEYWORDS:
        if word in preview_text:
            print(f'дата: {date}, заголовок: {title}, ссылка: {link}')


