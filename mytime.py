import time
import datetime
import locale
import os




locale.setlocale(locale.LC_ALL, 'it_IT.utf8')

os.system('clear')
print()
print ("---------------------------------------------")
print(type(time.localtime()))
print("time.gmtime(): ",time.gmtime())
print("time.localtime(): ", time.localtime())
print ("---------------------------------------------")

print("time.daylight: ", time.daylight, "type: ", type(time.daylight))
print("time.altzone: ", time.altzone, "type: ", type(time.altzone))
print("time.timezone: ", time.timezone, "type: ", type(time.timezone))
print("time.tzname: ", time.tzname, "type: ", type(time.localtime))

print ("time.asctime(time.gmtime()): ", time.asctime(time.gmtime()), "type: ", type(time.asctime(time.gmtime())))
print ("time.asctime(time.localtime()): ",time.asctime(time.localtime()), "type: ", type(time.asctime(time.localtime())))
print ("---------------------------------------------")
print(type(time.strftime('%A %d %m %Y - %H:%M',time.gmtime())))
print("time.strftime('%A %d %m %Y - %H:%M',time.gmtime()): ", time.strftime('%A %d %m %Y - %H:%M',time.gmtime()))
print("time.strftime('%A %d %m %Y - %H:%M',time.localtime()): ",time.strftime('%A %d %m %Y - %H:%M',time.localtime()))
print("time.strftime('%c',time.gmtime()): ",time.strftime('%c',time.gmtime()))
print("time.strftime('%c',time.localtime()): ",time.strftime('%c',time.localtime()))
print ("---------------------------------------------")
print()
print ("Time in seconds since the epoch: %s" %time.time(), "type: ", type(time.time()))
print ("Current date and time: " , datetime.datetime.now(), "type: ", type(datetime.datetime.now()))
print ("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d  %H:%M"))
print ("---------------------------------------------")
print ("Current year: ", datetime.date.today().strftime("%Y"))
print ("Month of year: ", datetime.date.today().strftime("%B"))
print ("Week number of the year: ", datetime.date.today().strftime("%W"))
print ("Weekday of the week: ", datetime.date.today().strftime("%w"))
print ("Day of year: ", datetime.date.today().strftime("%j"))
print ("Day of the month : ", datetime.date.today().strftime("%d"))
print ("Day of week: ", datetime.date.today().strftime("%A"))
print ("---------------------------------------------")
print()

adesso=datetime.datetime.now()
print ("Data ed ora correnti: ", adesso)
mydate = datetime.date(1957,1, 20)  #year, month, day
print (type(mydate))
print ('La mia data: ', mydate)
print ("Per ottenere il giorno della settimana della data: 20-01-1957: ", mydate.strftime("%A"))
print()
t=(1957,1,20,21,10,00,0,0,0)
secs=time.mktime(t)

print ("time.mktime(t): %f" % secs, type(secs))
print ("time.mktime(t): ", secs)
print(time.localtime(secs))
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))
print ("asctime(localtime(secs)): ", time.asctime(time.localtime(secs)))

print()


print()
print()
ora=datetime.date.today()
passato=datetime.date(1957,1, 20)  #year, month, day
mybirthday=ora-passato

print(mybirthday, type(mybirthday))
mydays=mybirthday.days
myyear=mydays/365
myresto=mydays%365
print(myyear,myresto)

mydtobj=datetime.datetime.strptime("1957-1-20 21:10:00", '%Y-%m-%d %H:%M:%S')
print (mydtobj, type(mydtobj))

print()
print()


obj1=datetime.datetime.strptime("1957-1-20 21:10:00", '%Y-%m-%d %H:%M:%S')
obj2=datetime.datetime.strptime("1957-1-21 21:11:10", '%Y-%m-%d %H:%M:%S')

diffobj=obj2-obj1
print (diffobj, type(diffobj))

x=diffobj.seconds//3600
y=(diffobj.seconds//60)%60
z=x*3600+y*60
print ("days: ", diffobj.days)
print ("hours: ", diffobj.seconds//3600)
print ("minutes: ", (diffobj.seconds//60)%60)
print ("seconds: ", (diffobj.seconds-z))


#mydiff=time.localtime()-mybirthday
#print(mydiff)

