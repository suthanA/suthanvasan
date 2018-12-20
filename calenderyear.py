def calender(n,day):
    day=1
    for month in momths:
        if(month<=12):
            print("%s",months[month])
            print("sun","","mon","","tue","","wed","","thur","","fri","","sat")
            for x in day_month:
                if(day<=1):
                    day=1+daycode*5;
                    day=day+1
                    print""
                else:
                    if(day>=day_month):
                        print("%2d",day)          
day_month={0,31,28,31,30,31,30,31,30,31,30,31,30,31};
months={"jan","feb","mar","april","may","jun","jul","aug","sep","oct","nov","dec"}
n=int(input("enter a month"))
day=int(input("enter a start_day"))
calender(n,day);