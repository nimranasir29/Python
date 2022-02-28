employee_file = open(r"E:\NIMRA NASIR\5th Semester\Python\employees.txt", "r")     
for employee in employee_file.readlines():              # by using for loop                                
    print(employee)                 
    
employee_file.close()
