"""
Данная программа создаёт новый файл vacancy_new.csv в котором записаны все професси по возрастанию ЗП
Затем она выводит первые 3 профессии с наибольшей ЗП
"""


import csv


with open("vacancy.csv", encoding="UTF-8", mode="r") as infile:
    csv_reader = csv.reader(infile, delimiter=";")
    vac_list = list(csv_reader)
    vac_list.pop(0)

    # Сортировка по ЗП
    vac_list.sort(key=lambda x: x[0], reverse=True)

    # Записываем в новый файл
    with open("vacancy_new.csv", encoding="UTF-8", mode="w") as outfile:
        csv_writer = csv.writer(outfile, delimiter=";")
        row = ["Company", "Role", "Salary"]
        csv_writer.writerow(row)
        for vac in vac_list:
            row = [vac[4], vac[3], vac[0]]
            csv_writer.writerow(row)

    # Выводим 3 самых больших элемента
    for vac in vac_list[0:3]:
        print(f"{vac[4]} - {vac[3]} - {vac[0]}")
