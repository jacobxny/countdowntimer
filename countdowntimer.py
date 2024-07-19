import time
from win10toast import ToastNotifier
import winsound

toaster = ToastNotifier()

x = int(input("Enter a number to countdown from. "))

while x > 0:
    time.sleep(1.00)
    x = x - 1
    print(x)
if x == 0:
    print("Countdown Finished. ")
    toaster.show_toast("Countdown Finished", "Timer finished it is now at 0")
    winsound.Beep(1000, 100)
                   
