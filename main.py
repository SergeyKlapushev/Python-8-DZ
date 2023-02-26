file = 'Guide.txt'

# Функцуия для добавления данных
def WriteInGuide( surname, name, middle_name, phone_num):

    with open(file, 'a', encoding='utf-8') as guide:

        guide.writelines(surname+ ' ' + name+ ' ' + middle_name + ' ' + phone_num+ '\n')

    return '\n*Данные добавлены'

# Функция для чтения данных справочника
def ReadGuide():
    with open(file, 'r', encoding='utf-8') as data:
        for line in data:
            print(line)

# Функция поиска в справочнике
def FindDataInGuide(find_arg):
    with open(file, 'r', encoding='utf-8') as data:
        for line in data:
            if line.split()[0:4].count(find_arg) > 0 :
                print(line)


# Функция изменения данных
def ChangeDataInGuide(change_arg_old, change_arg_new):
    with open (file, 'r', encoding='utf-8') as old:
        old_data = old.read()

    new_data = old_data.replace(change_arg_old, change_arg_new)

    with open(file, 'w', encoding='utf-8') as new:
        new.writable(new_data)
        return '+'

# Функция удаления данных
def DeleteDataFromGuide(delete_line):
    with open (file, 'r', encoding='utf-8') as old:
        old_data = old.read()

    new_data = old_data.replace(delete_line, '')

    with open(file, 'w', encoding='utf-8') as new:
        new.write(new_data)


# Основной код

print('Нажмите: \n r - чтобы посмотреть справочник\n a - чтобы дополнить справочник \n f - чтобы найти данные \n c - изменить данные \n d - чтобы удалить запись')

action = input()

if (action == 'a'): 
    print('Введите Фамилию:')
    surname = input()
    print('Введите Имя:')
    name = input()
    print('Введите Отчество:')
    middle_name = input()
    print('Введите Номер телефона:')
    phone_num = input()
    print(WriteInGuide(surname, name, middle_name, phone_num))

if (action == 'r'):
    ReadGuide()

if(action == 'f'):
    print('Введите параметр поиска(Фамилия, Имя, Отчество или Телефон):')
    find_arg = input()
    FindDataInGuide(find_arg)

if(action == 'c'):
    print('Введите данные которые хотите изменить:')
    change_arg1 = input()
    print('Введите новые данные:')
    change_arg2 = input()
    ChangeDataInGuide(change_arg1, change_arg2)

if(action == 'd'):
    
    print('Введите данные которые хотите удалить:')
    print(' Фамилия:')
    surname = input()
    print(' Имя:')
    name = input()
    print(' Отчество:')
    middle_name = input()
    print(' Номер телефона:')
    phone_num = input()
    delete_line = f"{surname} {name} {middle_name} {phone_num}"
    DeleteDataFromGuide(delete_line)
    



