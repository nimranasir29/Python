employee_file = open(r"E:\NIMRA NASIR\5th Semester\Python\employees.txt", "r")     
                                              
print(employee_file.readlines()[1])     #  read the first line by index                 
    
employee_file.close()
