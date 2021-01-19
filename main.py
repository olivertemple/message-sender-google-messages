import pyautogui as pa
import time

file = open("text.txt",'r')
mylist = file.read()
#print(mylist)
newlist = []

mylist=mylist.split('.')
for item in mylist:
    newlist.append(item.replace('\n',''))

#pa.moveTo(100,100, duration=1)
#pa.click(x=None,y=None, interval=0.0, button='left',duration=0.0)
pa.press('win')
pa.typewrite("chrome")
pa.press('enter')
time.sleep(1)
pa.typewrite("https://messages.google.com/web")
pa.press('enter')
pa.keyDown('win')
pa.press('up')
pa.keyUp('win')
time.sleep(4)
pa.keyDown("ctrl")
pa.keyDown("alt")
pa.press("c")
pa.keyUp('ctrl')
pa.keyUp('alt')
time.sleep(1)
pa.typewrite(newlist[0])
time.sleep(4)
pa.press('enter')
time.sleep(1)
for line in range(1,len(newlist)):
    if newlist[line]!='':
        pa.typewrite(newlist[line])
        pa.press('enter')


        