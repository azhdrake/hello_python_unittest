import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # Adds a phone, adds another phone with the same id, and verifies an PhoneError exception is thrown
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        testEmployee = Employee(1, 'Test Name')
        testAssignmentMgt = PhoneAssignments()

        testAssignmentMgt.add_employee(testEmployee)

        self.assertIn(testEmployee, testAssignmentMgt.employees)


    def test_create_and_add_employee_with_duplicate_id(self):
        #Tests that duplicate IDs raises error.
        testEmployee1 = Employee(1, 'Test Name 1')
        testEmployee2 = Employee(1, 'Test Name 2')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(testEmployee2)


    def test_assign_phone_to_employee(self):
        testEmployee = Employee(1, 'Test Name 1')
        testPhone = Phone(1, 'Test Brand', 'Test Model')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.add_phone(testPhone)

        testAssignmentMgr.assign(1, testEmployee)

        self.assertTrue(testPhone.employee_id == testEmployee.id)


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # Attempts to assign one phone to multiple employees and ensures it raises error.
        testEmployee1 = Employee(1, 'Test Name 1')
        testEmployee2 = Employee(2, 'Test Name 2')
        testPhone = Phone(1, 'Test Brand', 'Test Model')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)
        testAssignmentMgr.add_phone(testPhone)

        testAssignmentMgr.assign(1, testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(1, testEmployee2)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # Assigns a phone to an employee who already has a phone and ensures an error is raised.
        testEmployee = Employee(1, 'Test Name 1')
        testPhone1 = Phone(1, 'Test Brand', 'Test Model')
        testPhone2 = Phone(2, 'Test Brand', 'Test Model')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(1, testEmployee)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(2, testEmployee)


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.
        try:
            testEmployee = Employee(1, 'Test Name 1')
            testPhone = Phone(1, 'Test Brand', 'Test Model')

            testAssignmentMgr = PhoneAssignments()
            testAssignmentMgr.add_employee(testEmployee)
            testAssignmentMgr.add_phone(testPhone)

            testAssignmentMgr.assign(1, testEmployee)
        except PhoneError:
            self.fail('Phone error raised by assigning same phone to employee twice.')


    def test_un_assign_phone(self):
        # Assigns a phone, unasigns the phone, verifies the employee_id is None
        testEmployee = Employee(1, 'Test Name 1')
        testPhone = Phone(1, 'Test Brand', 'Test Model')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee)
        testAssignmentMgr.add_phone(testPhone)

        testAssignmentMgr.assign(1, testEmployee)
        testAssignmentMgr.un_assign(1)

        self.assertTrue(testPhone.employee_id == None)


    def test_get_phone_info_for_employee(self):
        # Checks that the method returns None if the employee does not have a phone
        # Checks that the method raises an PhoneError if the employee does not exist

        testEmployee1 = Employee(1, 'Test Name 1')
        testEmployee2 = Employee(2, 'Test Name 2')
        fakeEmployee = Employee(3, 'Fake Name')
        testPhone1 = Phone(1, 'Test Brand 1', 'Test Model 1')
        testPhone2 = Phone(2, 'Test Brand 2', 'Test Model 2')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(1, testEmployee1)

        self.assertTrue(testAssignmentMgr.phone_info(testEmployee1) == testPhone1)
        self.assertTrue(testAssignmentMgr.phone_info(testEmployee2) == None)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.phone_info(fakeEmployee)
        
