class Duration:
    def __init__(self, weeks, days, hours):
        if type(weeks) is not int:
            raise TypeError("Cannot instantiate an object with non-int values.")
        if weeks < 0:
            raise ValueError("Values cannot be negative.")
        if type(days) is not int:
            raise TypeError("Cannot instantiate an object with non-int values.")
        if days < 0:
            raise ValueError("Values cannot be negative.")
        if type(hours) is not int:
            raise TypeError("Cannot instantiate an object with non-int values.")
        if hours < 0:
            raise ValueError("Values cannot be negative.")
        add_day = 0
        add_week = 0
        if hours >= 24:
            add_day = int(hours / 24)
            hours %= 24
        days += add_day
        if days >= 7:
            add_week = int(days / 7)
            days %= 7
        weeks += add_week
        self.hours = hours
        self.days = days
        self.weeks = weeks

    def __str__(self):
        result = "{0:02}W {1}D {2:02}H".format(self.weeks,self.days,self.hours)
        return result

    def getTotalHours(self):
        total = self.weeks * (7*24) + self.days * 24 + self.hours
        return total

    def __add__(self, other):
        if(type(other) is Duration):
            new_week = self.weeks + other.weeks
            new_days = self.days + other.days
            new_hours = self.hours + other.hours
            new_dur = Duration(new_week,new_days,new_hours)
            return new_dur
        else:
            raise TypeError("A Duration instance is expected.")

    def __radd__(self, other):
        if(type(other) is Duration):
            new_week = self.weeks + other.weeks
            new_days = self.days + other.days
            new_hours = self.hours + other.hours
            new_dur = Duration(new_week,new_days,new_hours)
            return new_dur
        else:
            raise TypeError("A Duration instance is expected.")


    def __mul__(self, other):
        if type(other) is not int:
            raise TypeError("A Duration need times int.")
        elif other > 0 :
            new_week = self.weeks * other
            new_days = self.days * other
            new_hours = self.hours * other
            new_dur = Duration(new_week,new_days,new_hours)
            return new_dur
        else:
            raise ValueError("A positive int needed.")

    def __rmul__(self, other):
        if type(other) is not int:
            raise TypeError("A Duration need times int.")
        elif other > 0 :
            new_week = self.weeks * other
            new_days = self.days * other
            new_hours = self.hours * other
            new_dur = Duration(new_week,new_days,new_hours)
            return new_dur
        else:
            raise ValueError("A positive int needed.")



if __name__ == "__main__":
    d = Duration(weeks=2,days=15,hours=49)
    d1 = Duration(3,1,1)
    print(d)
    print(d.getTotalHours())
    print(d+d1)
    #print(1+d)
    print(d1*2)
    print(2*d1)
    #print(2.1*d1)
    #print(-2 * d1)