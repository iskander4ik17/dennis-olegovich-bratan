# 4 задания: 2 по модулям и библиотекам, 2 по работе с файлами

# =====================================================
# МОДУЛИ И БИБЛИОТЕКИ
# =====================================================
import random

# --- Задача 11 (лёгкая) ---
print("Задача 11")
print(random.randint(1, 100))

# --- Задача 49 (сложная) ---
# Модуль geometry.py создаётся этой же программой, чтобы файлов было два.
geometry_code = '''import math


def circle_area(radius):
    return math.pi * radius ** 2


def rectangle_area(width, height):
    return width * height


def triangle_area(base, height):
    return base * height / 2


if __name__ == "__main__":
    print(circle_area(1))
    print(rectangle_area(2, 3))
    print(triangle_area(4, 5))
'''

with open("geometry.py", "w", encoding="utf-8") as file:
    file.write(geometry_code)

import importlib
import os
import sys

sys.path.insert(0, os.getcwd())
importlib.invalidate_caches()
import geometry

print("\nЗадача 49")
print("Площадь круга:", geometry.circle_area(5))
print("Площадь прямоугольника:", geometry.rectangle_area(4, 6))
print("Площадь треугольника:", geometry.triangle_area(3, 8))


# =====================================================
# РАБОТА С ФАЙЛАМИ
# =====================================================
import json
import os

# --- Задача 2 (лёгкая) ---
# Сначала создаём info.txt
with open("info.txt", "w", encoding="utf-8") as file:
    file.write("Иван\n25\nАлматы\n")

print("\nЗадача 2")
with open("info.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)

# --- Задача 50 (сложная) ---
LIBRARY_FILE = "library.json"


def load_books():
    if not os.path.exists(LIBRARY_FILE):
        return []
    with open(LIBRARY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_books(books):
    with open(LIBRARY_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author, "taken": False})
    save_books(books)
    print("Книга добавлена")


def give_book(title):
    books = load_books()
    for book in books:
        if book["title"] == title:
            if book["taken"]:
                print("Книга уже выдана")
            else:
                book["taken"] = True
                save_books(books)
                print("Книга выдана")
            return
    print("Такой книги нет")


def return_book(title):
    books = load_books()
    for book in books:
        if book["title"] == title:
            if not book["taken"]:
                print("Эта книга и так в библиотеке")
            else:
                book["taken"] = False
                save_books(books)
                print("Книга возвращена")
            return
    print("Такой книги нет")


def show_books():
    books = load_books()
    if not books:
        print("Библиотека пуста")
    for book in books:
        status = "выдана" if book["taken"] else "в наличии"
        print(book["title"], "-", book["author"], "(" + status + ")")


print("\nЗадача 50 - библиотека")
while True:
    print("\n1 - добавить книгу")
    print("2 - выдать книгу")
    print("3 - вернуть книгу")
    print("4 - показать все книги")
    print("0 - выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        title = input("Название: ")
        author = input("Автор: ")
        add_book(title, author)
    elif choice == "2":
        give_book(input("Название: "))
    elif choice == "3":
        return_book(input("Название: "))
    elif choice == "4":
        show_books()
    elif choice == "0":
        break
    else:
        print("Нет такого пункта")
