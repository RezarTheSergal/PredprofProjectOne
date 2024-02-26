import csv

# def get_max_salary_in_company(vc_list):
#     vc_list.sort(key=lambda x: x[0], reverse=True)
#     return vc_list[0]
#
#
# def get_max_salaries(vc_list):
#     pre_vc = ""
#     new_vc_list = [vc_list[0]]
#     max_salaries = list()
#     for vc in vc_list:
#         if vc[4] == pre_vc:
#             new_vc_list.append(vc)
#         else:
#             max_salaries.append(get_max_salary_in_company(new_vc_list))
#             new_vc_list = [vc]
#     return max_salaries


with open("vacancy.csv", encoding="UTF-8", mode="r") as infile:
    csv_reader = csv.reader(infile, delimiter=";")
    vac_list = list(csv_reader)
    vac_list.pop(0)
    vac_list.sort(key=lambda x: x[0], reverse=True)
    # new_val_list = get_max_salaries(vac_list)
    # print(new_val_list)
    with open("vacancy_new.csv", encoding="UTF-8", mode="w") as outfile:
        csv_writer = csv.writer(outfile, delimiter=";")
        row = ["Company", "Role", "Salary"]
        csv_writer.writerow(row)
        for vac in vac_list:
            row = [vac[4], vac[3], vac[0]]
            csv_writer.writerow(row)

    for vac in vac_list[0:3]:
        print(f"{vac[4]} - {vac[3]} - {vac[0]}")
