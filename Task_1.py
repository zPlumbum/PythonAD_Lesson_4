documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }


def get_person(doc_num):
    print('*Информация о владельце*')

    # document_number = input('Пожалуйста, введите номер документа: ')
    document_number = doc_num

    for document in documents:
        if document_number in document.values():
            print(f'Владелец: {document["name"]}.\n')
            return document["name"]
    print('Человека с таким номером документа нет.\n')


def get_shelf():
    print('*Поис полки*')
    document_number = input('Пожалуйста, введите номер документа: ')
    doc_exist = False

    for document in documents:
        if document_number in document.values():
            doc_exist = True

    for shelf in directories:
        if (document_number in directories[shelf]) and (doc_exist is True):
            print(f'Документ с таким номером находится на {shelf} полке.\n')
            return
        elif (document_number in directories[shelf]) and (doc_exist is False):
            directories[shelf].remove(document_number)
            print('Документа с таким номером нет в базе, поэтому он был удален с полки.\n')
            return
    print('Документа с таким номером не существует.\n')


def get_list():
    print('*Вывод элементов списка*')
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')
    print()


def add_document(doc_type, doc_num, name, shelf_number):
    print('*Добавление*')
    # document_type = input('Пожалуйста, введите тип документа: ')
    # document_number = input('Введите номер документа: ')
    # name = input('Введите Фамилию и Имя владельца: ')
    # shelf_number = input('Введите номер полки: ')

    document_type = doc_type
    document_number = doc_num
    name = name
    shelf_number = shelf_number

    if shelf_number in directories.keys():
        directories[shelf_number].append(document_number)
        dict_temp = {"type": document_type, "number": document_number, "name": name}
        documents.append(dict_temp)
        print('Данные владельца успешно добавлены в список.\n')
        return True
    else:
        print('Полки, на которую Вы хотите добавить элемент, не существует.\n')
        return False


def del_document(doc_num):
    print('*Удаление*')

    # document_number = input('Пожалуйста, введите номер документа: ')
    document_number = doc_num

    for document in documents:
        if document_number in document.values():
            documents.remove(document)

            for value in directories.values():
                if document_number in value:
                    value.remove(document_number)
                    print('Элемент успешно удален!\n')
                    return True
    print('Документа с таким номером не существует.\n')


def move_document():
    print('*Перемещение элемента*')
    document_number = input('Пожалуйста, введите номер документа: ')
    shelf_number = input('Введите номер полки, на которую хотите переместить элемент: ')
    doc_exist = False

    if shelf_number not in directories.keys():
        print('Полки с таким номером не существует.\n')
        return

    for shelf, value in directories.items():
        if document_number in value:
            doc_exist = True
            if shelf_number == shelf:
                print('Элемент уже находится на этой полке.\n')
                return
            value.remove(document_number)

    if not doc_exist:
        print('Документа с таким номером не существует.\n')
        return

    directories[shelf_number].append(document_number)
    print('Элемент успешно перемещен.\n')


def add_shelf():
    print('*Добавление полки*')
    shelf_number = input('Введите номер полки, которую хотите создать: ')

    if shelf_number in directories.keys():
        print('Полка с таким номером уже существует.\n')
        return

    temp_value = []
    directories.setdefault(shelf_number, temp_value)
    print('Полка успешно создана.\n')


def main():
    print('Добрый день!')
    print('Для получения информации о владельце введите - "p"')
    print('Для того, чтобы узнать, на какой полке находится документ, введите - "s"')
    print('Для того, чтобы вывести список всех документов, введите - "l"')
    print('Для добавления нового документа введите - "a"')
    print('Для удаления документа введите - "d"')
    print('Для перемещения документа на другую полку введите - "m"')
    print('Для создания новой полки введите - "as"')
    print('Для выхода из программы введите - "q"\n')

    while True:
        user_input = input('Ввод: ')
        print()

        if user_input == 'p':
            get_person()
        elif user_input == 's':
            get_shelf()
        elif user_input == 'l':
            get_list()
        elif user_input == 'a':
            add_document()
            print(documents)
            print(directories)
        elif user_input == 'd':
            del_document()
            print(documents)
            print(directories)
        elif user_input == 'm':
            move_document()
            print(documents)
            print(directories)
        elif user_input == 'as':
            add_shelf()
            print(documents)
            print(directories)
        elif user_input == 'q':
            break
