from phone_manager import Phone, Employee, PhoneAssignments

def main():

    assignments = PhoneAssignments()

    phone1 = Phone(1, 'Samsung', 'Galaxy Note 7')
    phone2 = Phone(2, 'Samsung', 'Galaxy S III')
    phone3 = Phone(3, 'Samsung', 'Galaxy A7')

    assignments.add_phone(phone1)
    assignments.add_phone(phone2)
    assignments.add_phone(phone3)

    employee1 = Employee(1, 'Alice')
    employee2 = Employee(2, 'Bill')
    employee3 = Employee(3, 'Ted')

    assignments.add_employee(employee1)
    assignments.add_employee(employee2)
    assignments.add_employee(employee3)

    assignments.assign(phone1.id, employee2)  # Assign phone 1 to employee 2
    assignments.assign(phone2.id, employee3)  # Assign phone 2 to employee 3

    print(assignments.phone_info(employee1))  # Employee 1, no phone. Prints None
    print(assignments.phone_info(employee2))  # Employee 2, has Phone 1
    print(assignments.phone_info(employee3))  # Employee 3 has Phone 2

    assignments.un_assign(phone2.id)          # un-assign phone 2 (which belonged to employee 3)
    print(assignments.phone_info(employee3))  # None

    assignments.assign(phone3.id, employee3)   # Assign phone 3 to employee 3
  #  assignments.assign(phone2.id, employee3)   # Reassign phone 3 to employee3. TODO this should fail; employee3 should not be able to have two phones



if __name__ == '__main__':
    main()
