from selenium import webdriver

NAME_FILE = "ss.txt"
#удаление данных из файла 
def deleteDataFile():
    f = open(NAME_FILE, 'w')
    f.close()    
#открытие сайта и получение h1
def OpenUrl(url):
    driver.execute_script(f"window.open('{url}')")
    one_window = driver.window_handles[0]
    handle = driver.window_handles[-1]
    driver.switch_to.window(handle)
    Tag_H1 = driver.find_elements_by_tag_name('h1')
    if (len(Tag_H1) <2):
        RecordInFile(NAME_FILE, f'Error: {url}')
    else:
        stringH1 = f'1.{Tag_H1[0].text} 2.{Tag_H1[1].text}'
        RecordInFile(NAME_FILE, stringH1)
    driver.switch_to.window(one_window)
#запись в файл полученных заголовков или ошибки
def RecordInFile(namefile, message):
    with open(namefile, 'a') as file:
        file.write(message + '\n')
#поиск <a>
def SearseTagsA(driver):
    Tag_A = driver.find_elements_by_tag_name('a')
    for i in Tag_A:
        if i.get_attribute('href') == None:
            Tag_A.remove(i)
    Tag_A = Tag_A[:5]
    return Tag_A
#цикл для основной работы проги
def OpenUrlsByTagA(Tag_A):
    for item in Tag_A:
        OpenUrl(item.get_attribute('href'))
#вывод данных в консоль
def PrintDataFromFileOnTerminal():
    with open(NAME_FILE, 'r') as file:
        stringLines = file.readlines()
        for line in stringLines:
            print(line)
    input()

#начало работы программы 

if (input('1-ввод/2-в коде: ')=='1'):
    URL = input('Введите URL(протокол://www.сайт.домен/): ')
else:
    #URL = 'https://selenium-python.com/locating-web-elements'
    URL = "https://yandex.ru/"
    #URL = "https://mail.ru/"
driver = webdriver.Chrome()

driver.get(URL)

deleteDataFile()
tag_a = SearseTagsA(driver)
OpenUrlsByTagA(tag_a)

PrintDataFromFileOnTerminal()

driver.quit()