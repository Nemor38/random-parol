import json
import random
import string

notes = dict()


def add_note(title, text):
    notes[title] = text
    print("Пароль успешно добавлен!")


def update_notes():
    global notes
    try:
        with open('passwordsaver.json', 'r') as json_file:
            notes = json.load(json_file)
    except FileNotFoundError:
        notes = {}


def display_notes():
    update_notes()
    if len(notes) == 0:
        print("Сохраненных паролей пока нет.")
    else:
        for title, text in notes.items():
            print(f"{title}: {text}")


def delete_note(title):
    update_notes()
    if title in notes:
        del notes[title]
        print(f'Пароль "{title}" удален.')
    else:
        print('Такой пароль не сохранен.')


def save_notes():
    with open("passwordsaver.json", "w") as file:
        json.dump(notes, file)


def random_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def find_password(title):
    update_notes()
    title = title.lower()  # Для поиска без учета регистра
    if title in notes:
        print(f"Пароль для {title}: {notes[title]}")
    else:
        print(f"Пароль для сайта '{title}' не найден.")


def main():
    update_notes()  # Обновляем заметки при запуске программы
    while True:
        print(
            "\n1. Создать пароль\n2. Просмотреть все пароли\n3. Удалить пароль\n4. Найти пароль по названию сайта\n5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            note_title = input("Введите название пароля: ")
            length = int(input("Введите длину пароля: "))
            note_text = random_password(length)
            add_note(note_title, note_text)
            save_notes()
            print(f"Сгенерированный пароль: {note_text}")

        elif choice == "2":
            display_notes()

        elif choice == "3":
            update_notes()
            for title in notes.keys():
                print(title)
            title_to_del = input('Введите название пароля для удаления: ')
            delete_note(title_to_del)
            save_notes()

        elif choice == "4":
            title = input("Введите название сайта: ")
            find_password(title)

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Повторите попытку.")


main()