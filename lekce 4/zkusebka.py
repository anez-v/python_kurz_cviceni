class Employee:
    #funkce ve třídě = metoda
    def __init__(self, name, position, holiday_entitlement, probation_period):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.probation_period = probation_period

    def __str__(self):
        if self.probation_period == True:
            return f"Zaměstnanec {self.name} pracuje na pozici {self.position} a je ve zkušební době."
        else:
            return f"Zaměstnanec {self.name} pracuje na pozici {self.position} a není ve zkušební době."
    
    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."


employee_1 = Employee ("František Novák", "konstruktér", 25, True)
employee_2 = Employee("Klára Nová", "konstruktérka", 25, False)

print(employee_1)
print(employee_2)
