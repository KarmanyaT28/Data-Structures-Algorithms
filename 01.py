# print("Hello World")

# Calculate Average Temperature

numDays = int(input("How many day's temperature?"))

total=0

for i  in range(1 , numDays+1):
    nextDay = int(input("DAY " + str(i) + "s high temperature"))
    total += nextDay


avg = round(total/numDays , 2)
print("\nAverage = " + str(avg))