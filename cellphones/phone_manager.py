# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        # Raises exception if two employees with same ID are added
        for empl in self.employees:
            if empl.id == employee.id:
                raise PhoneError('There is already an employee with that ID.')
        self.employees.append(employee)


    def add_phone(self, phone):
        # Raises exception if two phones with same ID are added
        for old_phone in self.phones:
            if old_phone.id == phone.id:
                raise PhoneError('There is already an phone with that ID.')
        self.phones.append(phone)


    def assign(self, assigning_phone_id, employee):
        # Find phone in phones list
            # Checks if phone is already assigned to the employee - if so exits out of method.
            # Checks if phone is already assigned to a different employee - if so raises exception.
        # Checks if given employee already has different phone assigned to them - if so raises exception
        # If all of that ^ doesn't trigger any problems, assigns employee to phone.
        for phone in self.phones:
            if phone.id == assigning_phone_id:
                assigning_phone = phone
                if phone.employee_id == employee.id:
                        return
                if phone.employee_id is not None:    
                    raise PhoneError('Phone is already assigned to an employee.')
            if phone.employee_id == employee.id:
                raise PhoneError('Employee already has phone assigned to them.')                
        assigning_phone.assign(employee.id)


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # Find phone for employee in phones list
        # Checks given ID against all valid IDs. If the ID is valid, method attempts to find a phone with that employee assigned to it.
        #If the given ID is not found in the employees list, raises excepetion.
        for existing_employee in self.employees:
            if existing_employee.id == employee.id:
                for phone in self.phones:
                    if phone.employee_id == employee.id:
                        return phone
                return None
        raise PhoneError("There is no employee with that ID.")


class PhoneError(Exception):
    pass
