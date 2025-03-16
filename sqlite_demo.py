import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE First (
#             first text,
#             last text,
#             pay integer
#             )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO First VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM First WHERE first=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE First SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from First WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
emp_3 = Employee('Sakshi', 'utturi', 100000)

# insert_emp(emp_1)
# insert_emp(emp_2)
# insert_emp(emp_3)

# emps = get_emps_by_name('utt')
# print(emps)

# update_pay(emp_2, 95000)
# remove_emp(emp_3)

emps = get_emps_by_name('John')
print(emps)
conn.commit()
conn.close()
