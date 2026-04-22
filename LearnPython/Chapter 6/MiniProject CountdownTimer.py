import time

count = int(input("Enter the count Number"))
print("Countdown Start now : ")
for i in range(count, 0, -1):
    print(i)
    time.sleep(1)
print("Happy New Year ")
