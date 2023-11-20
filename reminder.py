import time
import winsound
from winsound import Beep
x=time.localtime()
y=time.strftime("%Y-%m-%d \n%H :%M :%S",x)
print("The Time is: \n ",y)
print("Enter the numerical of reminder time : \n")
n1=int(input())
user=input("Enter the units of the numerical(second,minute or hour): \n")
if(user=="minute"):
    new_user=n1*60
elif(user=="second"):
    new_user=n1
elif(user=="hour"):
    new_user=n1*60*60
time.sleep(new_user)
# Set frequency to 3000 Hertz
frequency = 3000
# Set duration to 200 milliseconds (0.2 seconds)
duration = 200
# Make beep sound on Windows
winsound.Beep(frequency, duration)
  #notes = {'C': 2635,
#          'D': 2835,
#          'E': 3060,
#          'S': 2945,
#          'F': 3183,
#          'G': 3450,
#          'A': 3750,
#          'B': 4087,
#          ' ': 137}
notes = {'C': 800,
        'D': 1000,
     
        }
melodie ='DDDDCCCCCDDCDCDCDC'
for note in melodie:
    Beep(notes[note], 500)

print("Done for now !!! ")    
