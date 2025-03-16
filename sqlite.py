import sqlite3
from employee import Employee

#conn object that connects our databse
conn = sqlite3.connect('employee_list.db') #creates file

c = conn.cursor() #cursor allows to execute sql commands

# c.execute("""CREATE TABLE employee (
#             first text,
#             last text,
#             pay integer,
#             unique (first)
#             )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(fname):
    c.execute("SELECT * FROM employee WHERE first=:last", {'last': fname})
    return c.fetchall()


def update_pay(fname, pay):
    with conn:
        c.execute("""UPDATE employee SET pay = :pay 
            WHERE first = :first """,
            {'first': fname, 'pay': pay})
    # with conn:
    #     c.execute("UPDATE employee SET pay = :pay WHERE first = :last",{'last': name})

    # with conn:
    #     c.execute("""UPDATE employee SET pay = :pay 
    #         WHERE first = :first AND last = :last""",
    #         {'first': fname, 'last': lname, 'pay': pay})





def remove_emp(name):
    with conn:
        c.execute("DELETE from employee WHERE first = :first",
                  {'first': name})



emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Stanley', 90000)
emp_3 = Employee('Sakshi', 'Utturi', 100000)
emp_4 = Employee('Sneha', 'Patil', 120000)

# insert_emp(emp_1)
# insert_emp(emp_2)
# insert_emp(emp_3)
# insert_emp(emp_4)


# emps = get_emps_by_name('Doe')
# print(emps)
# emps = get_emps_by_name('Stanley')
# print(emps)



# emps = get_emps_by_name('Sakshi')
# print(emps)
# emps = get_emps_by_name('Sneha')
# print(emps)

# update_pay(emp_2, 95000)
# remove_emp(emp_3)
i=0
while True:
    print("1.display by name, 2.update pay, 3.remove employee 4.Exit")
    i=int(input())
    if i==1:
        name=input("Enter name: ")
        emps = get_emps_by_name(name)
        print(emps)
    elif i==2:
        name=input("Enter name: ")

        newpay=int(input("Enter new pay: "))
        # update_pay(name,"Utturi", newpay)
        update_pay(name, newpay)
    elif i==3:
        name=input("Enter name: ")
        remove_emp(name)
    else:
        break

conn.commit()  #commits the current transaction, commiting the changes
conn.close()   #close database
