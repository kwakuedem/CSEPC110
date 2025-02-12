# Working with files

with open('hr_system.txt') as employee_data:
    for employee in employee_data:
        clean_emplyee_data=employee.strip()
        employee_data_parts=clean_emplyee_data.split(" ")

        employee_name=employee_data_parts[0]
        employee_id=employee_data_parts[1]
        employee_title=employee_data_parts[2]
        employee_salary=float(employee_data_parts[3])

        employee_pay_check_amount=employee_salary / 24

        if employee_title.lower()=='engineer':
            employee_pay_check_amount += 1000

        print(f"{employee_name} (ID: {employee_id}), {employee_title} - ${employee_pay_check_amount:.2f}")