import time

repeatInput = input("Type something for me to repeat: ")
loopy = True

if repeatInput == "bunny":
    print("You found the easter egg! Therefore, I will not print 'bunny' alot ofr times.")

else:
    delay = input("Now, enter the time gap between repeats: ")
    delay = float(delay)
    while loopy:
        print(repeatInput)
        time.sleep(delay)