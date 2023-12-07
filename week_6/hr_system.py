with open('hr_system.txt') as employees:
    for employee in employees:
        employee = employee.strip()
        info = employee.split(" ")
        name = info[0]
        id = info[1]
        job_title = info[2]
        salary = float(info[3])

        name_width = 10  
        id_width = 4
        job_width= 9
        salary_width = 10
        if job_title  == "Engineer":
            salary += 26000

        print(f"({id:<{id_width}}): {name:<{name_width}}, {job_title:<{job_width}} - ${salary / 26 :<{salary_width}.2f}")
        