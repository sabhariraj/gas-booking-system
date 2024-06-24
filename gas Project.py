import mysql.connector
con_o=mysql.connector.connect(host="localhost",user="root",password="",database="test")
cur_o=con_o.cursor()
a=input("Name: ")
b=input("Mobile: ")
c=input("Registration.No: ")
d=input("Expected delivering date: ")

#insert code
q2=f"INSERT INTO customer_details(`Name`, `Mobile`, `Registration.No`, `Expected delivering date`) VALUES ('{a}','{b}','{c}','{d}')"
cur_o.execute(q2)
con_o.commit()
##ending steps
cur_o.close()
con_o.close()
