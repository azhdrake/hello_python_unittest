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
        # TODO raise exception if two employees with same ID are added
        for empl in self.employees:
            if empl.id == employee.id:
                raise PhoneError('There is already an employee with that ID.')
        self.employees.append(employee)


    def add_phone(self, phone):
        # TODO raise exception if two phones with same ID are added
        for old_phone in self.phones:
            if old_phone.id == phone.id:
                raise PhoneError('There is already an phone with that ID.')
        self.phones.append(phone)


    def assign(self, assigning_phone_id, employee):
        # Find phone in phones list
        # TODO if phone is already assigned to an employee, do not change list, raise exception
        # TODO if employee already has a phone, do not change list, and raise exception
        # TODO if employee already has this phone, don't make any changes. This should NOT raise an exception.
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
        # find phone for employee in phones list

        # TODO  should return None if the employee does not have a phone
        # TODO  the method should raise an exception if the employee does not exist

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone


        return None


class PhoneError(Exception):
    pass
