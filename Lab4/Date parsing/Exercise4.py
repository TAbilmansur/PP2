def Difference(date1,date2):
    if (date1 > date2) :
        date1,date2 = date2,date1
    return (date2-date1).total_seconds()
import datetime
date1 = datetime.datetime.now()
date2 = datetime.datetime.now()+datetime.timedelta(days = 1)
print(Difference(date1,date2))