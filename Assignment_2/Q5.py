year=int(input("Enter Year"))
if(year%4==0 or year%100==0 or year%400==0):
    print("Leap Year")
else:
    print("Non-leap")