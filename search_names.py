import csv


def search_names(s_name):
    f_name = ''
    with open("Phonebook.csv", encoding="utf-8") as f:
        f_reader = csv.reader(f, delimiter=",")
        for row in f_reader:
            if row[1] == s_name:
                f_name += f'{row[0]} {row[1]} {row[2]} {row[3]}\n'
    return f_name