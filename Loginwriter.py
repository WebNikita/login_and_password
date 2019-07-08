#Программа для записи логинов и паролей
#Ввод паролья логина и названия сайта
def write_pass_login():
    global site_name, login, password, logfile, pasfile
    #Для чего нужно запомнить логин или пароль
    print('Для чего запоминаем логин и пароль')
    site_name = str(input())
    #Вводим логин
    print('Введите логин')
    login = str(input())
    #Вводим пароль
    print('Введите пароль')
    password = str(input())#Программа для записи логинов и паролей
    #Для чего нужно запомнить логин или пароль
#Запись даных в файл
def write_in_file(login, password, site_name):
    logfile = open('log.txt','a')
    if login != None or password != None:
        #Работа с данными
        logfile.write('Название: ' + site_name + '\n')
        logfile.write('Логин: ' + login + ';' + '\n')
        logfile.write('Пароль: ' + password + ';' + '\n')
        logfile.close()
#Выдаём даные с файла
def read_file():
    with open('log.txt', 'r') as fd:
        date = fd.read()
        print(date)
        fd.close()
#Удаление файлов
def delite_date():
    logfile = open('log.txt', 'w')
    logfile.close()
#Вход в программу
#Добавляем счётчик ошибок
count_error = 0
print('Для входа в программу необходимо авторизироваться!')
while True:
    print('Введите логин:')
    main_login = str(input())
    print('Введите пароль:')
    main_password = str(input())
    #Проверка данных
    if main_login == '1' and main_password == '1':
        print('Вход выполнен успешно!')
        print('Введите 1 для добавления данных')
        print('Введите 2 для выдачи информации')
        chois = input()
        if chois == '1':
            print('Добавляем данные')
            #Запускаем ввод данных
            write_pass_login()
            #Записываем в файл данные
            write_in_file(login, password,site_name)
        elif chois == '2':
            print('Выши данные:')
            #Выдаем данные
            read_file()
    else:
        count_error += 1
        print('Вы ошиблись! У вас есть: ' + str(4 - count_error) + ' попытки до удаления всех файлов с даными!')
        if count_error == 4:
            print('Данные будут полностью удалены!')
            #Удаление данных
            delite_date()
            exit()
