import datetime
k = datetime.datetime.now()
for i in range(-1,2):
    print((k+datetime.timedelta(days = i)).strftime("%A"))