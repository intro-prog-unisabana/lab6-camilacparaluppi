# Write your code here!
def employee_print(employee_info):
    print("Name:", employee_info.get("Name", "N/A"))
    print("Salary:", employee_info.get("Salary", "N/A"))
    print("Role:", employee_info.get("Role", "N/A"))
    for key in employee_info:
        if key != "Name" and key != "Salary" and key != "Role":
            print(key, ":", employee_info[key])
        keydiferente = True
    if keydiferente == False:
        print("No other info!")