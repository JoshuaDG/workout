 # Joshua D. Gonzlaez
# 70-245: Object-Oriented Programming 
# Workout Warrior 
'''
this program takes a files line and split them between
a run class and a zumba class were they would get the 
calories burn and then stores them in a
list to print out the results
'''
 
 
''' 
precondition: takes the line of the order of the file's 
(parts[1], parts[0],parts[2],and parts[3])
postcondition: it passes the def Calories_burn to the children 
and prints out the line's parts if called to_string
'''
class Workout:
    def __init__(self,nickname='none',Type = 'none', Date='none', Time = 'none'):
        self.name = nickname
        self.worktype = Type
        self.date = Date
        self.time = Time
    def Calories_burn(self):
        pass
    def to_string(self):
        return " %-10s %s %10s %5s" % (self.name, self.worktype, self.date, self.time)
 
'''
precondition: takes the part's (parts[0 - 5]), 
parts[0 - 3] are given by the parent class
parts[4] must be a float were parts[5] most be a str for it to work
postcondition: Calories_burn gives the calories burn by using parts [4 and 5]
and to_string prints the parents to_string and parts[4-5] and calories_burn
'''
class Run(Workout):
    def __init__(self,nickname='none',Type = 'none', Date='none', Time = 'none',Minutes=0,Detail=0):
        super().__init__(nickname,Type,Date, Time)
        self.minutes = Minutes
        self.miles = Detail
        self.pace = self.minutes/self.miles
    def Calories_burn(self):
        return self.pace * self.minutes
    def to_string(self):
        return "%s %9.2f %9.2f %9.2f" % (super().to_string(),self.minutes,self.Calories_burn(),self.miles)

class Zumba(Workout):
    def __init__(self,nickname='none',Type = 'none', Date='none', Time = 'none',Minutes=0,Detail='none'):
        super().__init__(nickname,Type,Date, Time)
        self.minutes = Minutes
        self.detail= Detail
        self.calmin = 0
    def Calories_burn(self):
        if self.detail == 'hi':
            self.calmin = 6
            return self.minutes * self.calmin
        elif self.detail == 'med':
            self.calmin = 4
            return self.minutes * self.calmin
        else:
            self.calmin = 2
            return self.minutes * self.calmin
    def to_string(self):
        return "%s %7.2f %9.2f %9s" % (super().to_string(),self.minutes,round(self.Calories_burn(),3),self.detail)
        
WT =[]
print("***************************** Workout Warrior *****************************\n")      
filename = input("Enter the name of the file:")
fileline = open(filename,"r")
print("These are the workouts you've completed:")
print()
print("%-12s%s%10s%6s%10s%10s%10s" % \
    (" Name","Type","Date","Time","Duration","Calories","Details"))
        
for line in fileline:
        line = line.strip()
        if line != "":
            parts = line.split(" ")
            # put in the informtaion from the line to see if it go into the run class or zumba class
            if parts[0] == 'r':
                parts[0] = 'run'
                run=Run(parts[1],parts[0],parts[2],parts[3],float(parts[4]),float(parts[5]))
                WT.append(run)
            else:
                parts[0] = 'zumba'
                zumba =Zumba(parts[1],parts[0],parts[2],parts[3],float(parts[4]),parts[5])
                WT.append(zumba)

fileline.close()
for w in WT:
    print(w.to_string())
    
print()
print('******************************** Thank You ********************************')