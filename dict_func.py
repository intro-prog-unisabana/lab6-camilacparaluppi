# Write your code here!
def employee_print(employee_info):
    employee_info = {"Name": "", "Salary": "", "Role": ""}
    if "Name" == "" and "Salary" == "" and "Role" == "":
        print ("No other info!")
    elif "Name" == "":
        print ("N/A")
    elif "Salary" == "":
        print ("N/A")
    elif "Role" == "":
        print ("N/A")
    elif "keys" in employee_info:
        print ("N/A")