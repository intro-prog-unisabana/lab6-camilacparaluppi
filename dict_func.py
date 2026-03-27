# Write your code here!
def employee_print(employee_info):
    print(employee_info.get("Name", "N/A"))
    print(employee_info.get("Salary", "N/A"))
    print(employee_info.get("Role", "N/A"))
    if "Name" == "" and "Salary" == "" and "Role" == "":
        print("No other info!")
    elif "Name" == "":
        print("N/A")
    elif "Salary" == "":
        print("N/A")
    elif "Role" == "":
        print("N/A")
    elif "keys" in employee_info:
        print("N/A")