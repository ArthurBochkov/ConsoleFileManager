import os
import shutil
import platform
import sys

import account
import victory


def create_folder():
    folder_name = input("Введите название папки: ")
    try:
        os.mkdir(folder_name)
        print(f"Папка {folder_name} создана")
    except FileExistsError:
        print(f"Папка {folder_name} уже существует")


def delete_file_or_folder():
    file_or_folder_name = input("Введите название файла или папки: ")
    try:
        if os.path.isfile(file_or_folder_name):
            os.remove(file_or_folder_name)
            print(f"Файл {file_or_folder_name} удален")
        elif os.path.isdir(file_or_folder_name):
            shutil.rmtree(file_or_folder_name)
            print(f"Папка {file_or_folder_name} удалена")
        else:
            print(f"Файл или папка {file_or_folder_name} не найдены")
    except Exception as e:
        print(f"Ошибка: {e}")


def copy_file_or_folder():
    file_or_folder_name = input("Введите название файла или папки: ")
    new_name = input("Введите новое название файла или папки: ")
    try:
        if os.path.isfile(file_or_folder_name):
            shutil.copy(file_or_folder_name, new_name)
            print(f"Файл {file_or_folder_name} скопирован в {new_name}")
        elif os.path.isdir(file_or_folder_name):
            shutil.copytree(file_or_folder_name, new_name)
            print(f"Папка {file_or_folder_name} скопирована в {new_name}")
        else:
            print(f"Файл или папка {file_or_folder_name} не найдены")
    except Exception as e:
        print(f"Ошибка: {e}")


def view_directory_contents():
    print("Содержимое рабочей директории:")
    for item in os.listdir():
        print(item)


def view_folders():
    print("Папки в рабочей директории:")
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)


def view_files():
    print("Файлы в рабочей директории:")
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)


def view_os_info():
    print(f"Операционная система: {platform.system()}")
    print(f"Версия: {platform.version()}")
    print(f"Архитектура: {platform.machine()}")


def creator_info():
    print("Создатель программы: Ваше имя")

def change_directory():
    new_directory = input("Введите полный или относительный путь к новой директории: ")
    try:
        os.chdir(new_directory)
        print(f"Рабочая директория изменена на {new_directory}")
    except FileNotFoundError:
        print(f"Директория {new_directory} не найдена")


def main():
    while True:
        print("\nМеню:")
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")

        choice = input("Введите номер пункта меню: ")

        match choice:
            case "1":
                create_folder()
            case "2":
                delete_file_or_folder()
            case "3":
                copy_file_or_folder()
            case "4":
                view_directory_contents()
            case "5":
                view_folders()
            case "6":
                view_files()
            case "7":
                view_os_info()
            case "8":
                creator_info()
            case "9":
                victory.start()
            case "10":
                account.start()
            case "11":
                change_directory()
            case "12":
                sys.exit()
            case _:
                print("Неверный номер пункта меню")


if __name__ == "__main__":
    main()
