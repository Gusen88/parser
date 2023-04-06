from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    #proxies = {
    #   'http': 'http://proxy.omgtu:8080',
    #    'https': 'http://proxy.omgtu:8080'
    #}
    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div', id ='pagecontent') # находим  контейнер с нужным классом
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('a'): # находим тег
            description = data.text
            #description.append("\n".join(data.text.split()) )# записываем в переменную содержание тега

    with open("1488.txt", "w") as f:
        for el in range(len(description)-1):
            if description[el] == '\n':
                if description[el+1] != '\n':
                    f.write(description[el])
            else:
                f.write(description[el])







            #f.write('\n')

    print(description)