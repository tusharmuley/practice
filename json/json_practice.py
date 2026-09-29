response = {
    "status": "success",
    "data": {
        "company": "Tech Solutions",
        "employees": [
            {
                "id": 101,
                "name": "Tushar",
                "department": "Engineering",
                "salary": 75000,
                "skills": ["Python", "Django", "React"],
                "address": {
                    "city": "Pune",
                    "state": "Maharashtra"
                },
                "is_active": True
            },
            {
                "id": 102,
                "name": "Rahul",
                "department": "HR",
                "salary": 50000,
                "skills": ["Communication", "Recruitment"],
                "address": {
                    "city": "Mumbai",
                    "state": "Maharashtra"
                },
                "is_active": False
            },
            {
                "id": 103,
                "name": "Priya",
                "department": "Engineering",
                "salary": 90000,
                "skills": ["Python", "FastAPI", "AWS"],
                "address": {
                    "city": "Pune",
                    "state": "Maharashtra"
                },
                "is_active": True
            }
        ]
    }
}




def sanitize_json_data(object_data):
    employee_names=[]
    employe_with_eng=[]
    salary_data=[]
    know_python =[]
    pune_emp=[]
    total_active_emp =0
    for emp in object_data['data']['employees']:
        employee_names.append(emp['name'])
        if emp['department'] == "Engineering":
            employe_with_eng.append(emp['name'])

        # for > 60000 salary employese 
        if emp['salary'] > 60000:
            salary_data.append(emp['name'])

        # know python 
        if "Python" in emp['skills']:
            know_python.append(emp['name'])

        # pune emplouyees 
        if emp['address']['city'] == 'Pune':
            pune_emp.append(emp['name'])
        
        # total salary of all the active emp 
        if emp['is_active']:
            total_active_emp += emp['salary']
    
    return employee_names, employe_with_eng, salary_data, know_python, pune_emp,total_active_emp

# print(sanitize_json_data(response))
employee_names, employe_with_eng, salary_data, know_python, pune_emp,total_active_emp = sanitize_json_data(response)
print("Employee Names:", employee_names)    
print("Employees in Engineering Department:", employe_with_eng)
print("Employees with Salary > 60000:", salary_data)
print("Employees who know Python:", know_python)
print("Employees in Pune:", pune_emp)
print("Total Salary of Active Employees:", total_active_emp)




