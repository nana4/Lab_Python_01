
print "###########################"
print "NOTE: The year starts from March"
print "ie. March = 1"
print " April = 2"
print " May = 3"
print " June = 4"
print " July = 5"
print " August = 6"
print " September = 7"
print " October = 8"
print " November = 9"
print " December = 10"
print " January = 11"
print " February = 12"
print "###########################"
print " "
f_name=raw_input('Enter your first name: ')
s_name=raw_input('Enter your last name: ')
print "Enter your date of birth"
month = raw_input('Month (1-12)?')
day = raw_input('Day?')
year = raw_input('Year?')

A = int(month)
B = int(day)
C = int(year)/100
D = int(year)%100


if A == 11 or A == 12:
    C=C-1
    
W=(13*A - 1)/5
X=C/4
Y=D/4
Z = W + X + Y + B + C - 2*D
R =  Z % 7
while R<0:
    R=R+7  
if (R == 0):
    day = "Sunday"
elif (R == 1):
    day = "Monday"
elif (R == 2):
    day = "Tuesday"
elif (R == 3):
    day = "Wednesday"
elif (R == 4):
    day = "Thursday"
elif (R == 5):
    day = "Friday"
else:
    day = "Saturday"
    
print f_name+" "+s_name+",your day is",day









