# Функция для получения редирект ссылки
def get_downloadLink(page_link, version=None, type_version=None):
   from bs4 import BeautifulSoup as bs
   import requests
   # Указываем заголовки для эммитации браузера
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      'Referer': 'https://minecraft-inside.ru/'
   }

   r_sub = requests.get(page_link)

   soup_sub = bs(r_sub.text, 'html.parser')

   download_link = ""

   for td_links in soup_sub.find_all("td", class_ = "dl__info"):
      download_link = td_links.find("a").get("href")
    # Создаем ссесию
      session = requests.Session()
      session.max_redirects = 1

      try:
         # Пробуем получить ответ с звгвловками введеными выше а также с отключенными редиректами
         response = session.get(download_link, headers=headers, allow_redirects=False)

         # Проверяем наличие Location header
         if response.status_code in [301, 302, 303, 307, 308] and 'Location' in response.headers:
            direct_url = response.headers['Location']
            return direct_url
         else:
            return "Не найдено прямой ссылки!"

      except requests.exceptions.TooManyRedirects:
         return "Слижком много редиректов!!!"

