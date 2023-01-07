import time


def writing_csv(contact):
    n_contact = contact.split()
    f = "Phonebook.csv"
    with open(f, 'a', encoding="utf-8") as data:
        data.write(f'{n_contact[0]},{n_contact[1]},{n_contact[2]},{n_contact[3]}\n')
    with open ("Log.txt", "a", encoding="utf-8") as data:
        data.write(f'Записан новый контакт {n_contact[0]};{n_contact[1]};{n_contact[2]};{n_contact[3]}; {time.asctime()}\n')