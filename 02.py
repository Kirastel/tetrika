import requests
from bs4 import BeautifulSoup


def scrapping_wikipedia():
    letters_list = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
                    'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
                    'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Э', 'Ю', 'Я']

    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    page = requests.get(url).text
    data = []
    while True:
        soup = BeautifulSoup(page, 'lxml')
        letters_from_page = soup.find_all('div', class_='mw-category-group')[-1].find_all('a')

        if letters_from_page[0].text[0] not in letters_list:
            break
        for letter in letters_from_page:
            letter = letter.text.capitalize()[0]
            data.append(letter)

        links = soup.find('div', id='mw-pages').find_all('a')
        for a in links:
            if a.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + a.get('href')
                page = requests.get(url).text

    for let in letters_list:
        print(f'{let}: {data.count(let)}')

