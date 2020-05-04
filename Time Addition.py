hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

addmins = (mins+dura)%60
addhours = (mins+dura)//60
days = (addhours+hour)//24

hours=hour + addhours
if days>0:
   hours -= (days*24)
print(hours, ":", (mins+dura)-(60*addhours))