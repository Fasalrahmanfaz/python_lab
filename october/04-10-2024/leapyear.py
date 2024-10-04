current_year = 2024
end_year = int(input("enter a range"))
for i in range(current_year,end_year+1):
    if (i%4==0 and i%100!=0)or (i%400 ==0 and i%100==0):
        print(f"{i} is a leap year")
