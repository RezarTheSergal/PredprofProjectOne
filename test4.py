import csv


def get_avg_for_job_type(job_list):
    avg_job_list = [[], []]
    for i in range(len(job_list[0])):
        avg_job_list[0].append(job_list[0][i])
        avg_job_list[1].append(sum(job_list[1][i][0]) / job_list[1][i][1])
    return avg_job_list


def get_avg_salaries_by_type(vc_list):
    job_type_salaries = [[], []]
    for i in range(len(vc_list)):
        vc_1 = vc_list[i][1].strip().lower()
        if vc_1 not in job_type_salaries[0]:
            job_type_salaries[0].append(vc_1)
            job_type_salaries[1].append([[int(vc_list[i][0])], 1])
        else:
            for j in range(len(job_type_salaries[0])):
                if job_type_salaries[0][j] == vc_1:
                    job_type_salaries[1][j][0].append(int(vc_list[i][0]))
                    job_type_salaries[1][j][1] += 1

    return get_avg_for_job_type(job_type_salaries)


with open("vacancy.csv", encoding="UTF-8", mode="r") as infile:
    csv_reader = csv.reader(infile, delimiter=";")
    vac_list = list(csv_reader)
    vac_list.pop(0)
    avg_salaries_by_type = get_avg_salaries_by_type(vac_list)

    for j in range(len(avg_salaries_by_type[0])):
        for k in range(len(vac_list)):
            one = avg_salaries_by_type[0][j].strip().lower()
            two = vac_list[k][1].strip().lower()
            if avg_salaries_by_type[0][j].strip().lower() == vac_list[k][1].strip().lower():
                vac_list[k].append(f"{int(vac_list[k][0]) / avg_salaries_by_type[1][j] * 100}%")

    with open("vacancy_procent.csv", encoding="UTF-8", mode="w") as outfile:
        csv_writer = csv.writer(outfile, delimiter=";")
        row = ["Salary", "Work_Type", "Company_Size", "Role", "Company", "Percent"]
        csv_writer.writerow(row)
        for k in range(len(vac_list)):
            csv_writer.writerow(vac_list[k])



