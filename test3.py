"""
Данная программа ищет по названию компании вакансии до тех пор, пока не будет остановлена кодовым словом None
infinite_loop - Бесконечный цикл
get_company_jobs - Поиск вакансий по названию компании
"""

import csv


def get_company_jobs(vc_list, comp_name):
    """
    Поиск вакансий по названию компании
    :param vc_list: список состоящий из всех вакансий
    :param comp_name: название компании
    :return: новый список из вакансий в указанной компании
    """
    new_vc_list = list()
    for vc in vc_list:
        if vc[4].strip().lower() == comp_name.strip().lower():
            new_vc_list.append(vc)

    if len(new_vc_list) == 0:
        return None
    else:
        return new_vc_list


def infinite_loop(vc_list):
    """
    Тело программы, бесконечный цикл
    :param vc_list: список вакансий
    :return: None
    """
    while True:
        comp_name = input()
        if comp_name == "None":
            break
        else:
            jobs = get_company_jobs(vc_list, comp_name)
            if jobs is None:
                print("К сожалению, ничего не удалось найти")
            else:
                for job in jobs:
                    print(f"В {job[4]} найдена вакансия: {job[3]}. З/п составит: {job[0]}")


with open("vacancy.csv", encoding="UTF-8", mode="r") as infile:
    csv_reader = csv.reader(infile, delimiter=";")
    vac_list = list(csv_reader)
    vac_list.pop(0)
    # Запускаем прогу
    infinite_loop(vac_list)
