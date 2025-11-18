# Импортирую библеотеки BeautifulSoup, requests и func_mine_pars
from bs4 import BeautifulSoup as bs
import requests
import func_mine_pars

print("||////////////////////////////////////||")
print("||      MINECRAFT-INSIDE PARSER       ||")
print("||////////////////////////////////////||")
print()
print()
print()
print()
# Задаю url-адресс
url , page_numbers = input("Input url (without / and page):"), int(input("How many pages? (min 2):"))

for page_number in range(1,page_numbers):
    try:
        URL = f'{url}/page/{page_number}/'
        print(f'Page {page_number} available mods:')
        # Получаю страничку
        headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      'Referer': 'https://minecraft-inside.ru/'
   }
        r = requests.get(URL, headers=headers)

        # Преобразую в текст
        page_text = r.text

        # Выбираю html.parser
        soup = bs(page_text, "html.parser")

        # Задаю списки ссылок, текстов ссылок и описания
        links = []
        text_links = []
        description = []

        # Прохожусь по всем блочным элементам с классом "box box_grass post"
        for divs in soup.find_all("div", class_ = "box box_grass post"):
         # Нахожу ссылки с добовлением якоря #forge и тексты ссылок
            links.append(f'http://minecraft-inside.ru/{divs.find("a").get("href")}#forge')
            text_links.append(divs.find("a").get_text())

        # Прохожусь по всем блочным элементам со стилем "text-align: center" внутри блочного элемента с классом "box box_grass post"
            for text_divs in divs.find_all("div", style = "text-align: center"):
                # Прохожусь по всем элементам внутри "div", style = "text-align: center"
                    for div in text_divs:
                        # Извлекаю весь текст из text_divs с разделителем '' и удаляю пробелы в начале каждого узла strip=True
                        text = div.get_text(separator='', strip=True)
                        description.append(text)
        # Удаляю пустые элементы и убираю ненужный текст
        description = [x for x in description if x != '' and not x.startswith("Добавлена fabric") and not x.startswith("Добавлена forge") and not x.startswith("Добавлена neoforge") and not x.startswith("Мод для майнкрафт") and not x.startswith("Мод обновлен")]

        for i in range(len(links)):
            print(text_links[i])
            print("Description:")
            print(description[i])
            print("Link for download:")
            print(func_mine_pars.get_downloadLink(links[i]))
            print('_' * 100)

    except:
        print("END")





