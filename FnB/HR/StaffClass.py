class Staff:
    def __init__(self, ID, name, title, supervisor, salary, entry_year, last_promotion_year, store_name):
        self.ID = ID
        self.name=name
        self.title=title
        self.supervisor=supervisor
        self.salary=salary
        self.entry_year=entry_year
        self.promotion_year=promotion_year
        self.store_name=store_name
    def info(self):
        print("ID ", self.ID, "Name: ", self.name, "Title: ", self.title, "Supervisor: ", self.supervisor, "Salary: ", self.salary, "Entry year: ", self.entry_year, "Last promotion year: ", self.last_promotion_year, "Store name: ", self.store_name)



class Management(FnB):
    def __init__(self, address, area, revenue, staffnum, stafflist):
        FnB.__init__(self, address, area, revenue, staffnum)
        self.stafflist=stafflist
    def info(self):
        FnB.info(self)
        print("Staff list: ", self.stafflist)





# Initial Staff class and Management class

Jim=Staff(12345, "Jim", "Cashier", "Catherine", 50000, 2013, 2015, "Tim Hortons")
Jim.info()




# Initial Management class




NumberOneKFC = DeliveryFnB("129 King street", 25, 85000, 3,"UberEat", 1423)
NumberOneKFC.info()
