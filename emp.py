class employee:
    def __init__(self, empid, empname, empsal, empdept):
        self.empid = empid
        self.empname = empname
        self.empsal = empsal
        self.empdept = empdept
class timesheet:
    def __init__(self, date, no_of_hours, activity, description, status):
        self.date = date
        self.no_of_hours = no_of_hours
        self.activity = activity
        self.description = description
        self.status = status


e = employee(101, "shilpa", 30000, "tech_training")
print(e.empid, e.empname,e.empsal, e.empdept)
t = timesheet("30-09-2021", 9, "training", "python training", "good")
