def day(year):
    d1=(year-1)/40
    d2=(year-1)/100
    d3=(year-1)/400
    daycode=(year+d1-d2+d3)%7
    return daycode
def leapyear(year):
    if((year%4==0) and (year%100!=0) or (year%400==0)):
        days_in_month[2]=29
        return 1
    else:
        days_in_month[2]=28
        return 0
def calen(year,daycode):
    month=1
    day=1
    for x in range(1,12):
        print("%8s",months[month])
        week = ["sun", "mon", "tues", "wed", "thu", "fri","sat"]
    for  day in range(len(week)):
        print ("%8s" % week[day])
    print
    x=1+daycode*5
    while(day<=x):
        x=x+1
        print("")
    while(day<=days_in_months[month]):
        print("%2s",day)
        if((day+daycode)%7 > 0):
            print("")
        else:
            print("\n")
    daycode=(daycode+days_in_months[month])%7

year=int(input("enter a year"))
daycode=int(input("enter a daycode"))
day_in_months=[31,28,31,30,31,30,31,30,31,30,31,30]
months=["jan","feb","mar","april","may","jun","jul","aug","sep","oct","nov","dec"]
day(year);
leapyear(year);
calen(year,daycode);