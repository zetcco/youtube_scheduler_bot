from datetime import datetime, timedelta

def getNewDateTime(prevDateTime):
    newDateTime = prevDateTime + timedelta(hours=6)
    return newDateTime

x = datetime(2020, 8, 13, 18, 0)
print(x.strftime("%b %d,%Y | %I:%M %p Original"))
#print(x.strftime("%I:%M %p"))

x = getNewDateTime(x)
print(x.strftime("%b %d,%Y | %I:%M %p"))