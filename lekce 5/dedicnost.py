class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    
	# dunder method  -  doube under - "dvojite podtrzitko"
    def __str__(self):
        return f'Zaměstnanec {self.name} pracuje jako {self.position}.'
 
    def take_holiday(self, days):
        """Vem pocet dni dovolene"""
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            print('Užij si to!')
        else:
            print(f'Nemáš nárok, zbývá ti jen {self.holiday_entitlement} dní.')
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        super().__init__(name, position, holiday_entitlement)
        self.subordinates = subordinates
        self.car = car
    def __str__(self):
        return super().__str__() + f'Má {self.subordinates} podřízených.'

employee_1 = Employee('František', 'konstruktér', 25)
employee_2 = Employee("Klára Nová", "konstruktérka", 25)

manazer = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 2,"Škoda Octavia 1.5 TSI")
manazer.take_holiday(10)
