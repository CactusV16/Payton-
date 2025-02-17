import datetime


Mode = int(input("Sara Khanoom Yeki Az In 2 Hallat Ro entekhab Kon:\n1. Vared Nemoodane Saat Be Shekl Dasti\n2. Darge Saat Az Khode computer\n"))

if Mode == 1:
    ClockTime = int(input("Sara Khanoom Saat Alan Ro Vared Kon:\n"))
    
    while ClockTime < 0 or ClockTime > 24:
        ClockTime = int(input("Sara Khanoom Saat Ro Dorost Vared Kon:\n"))
        
    if ClockTime >= 0 and ClockTime <= 6:
        print("nime Shab Be kheir")
    elif ClockTime > 6 and ClockTime <= 12:
        print("Sobhet Be kheir")
    elif ClockTime > 12 and ClockTime <= 18:
        print("Bade Zohr Be kheir")
    elif ClockTime > 18 and ClockTime <= 24:
        print("Shabet Be kheir")
    else:
        print("Sara Khanoom Addad Bein 0 Ta 24 Begoo Behem Ta Barname Kar kone")


if Mode == 2:
    ClockTime = datetime.datetime.now()
    print(ClockTime.microsecond)
    print(ClockTime.second)
    print(ClockTime.minute)
    print(ClockTime.hour)
    print(ClockTime.day)
    print(ClockTime.month)
    print(ClockTime.year)

    # if ClockTime >= 0 and ClockTime <= 6:
    #     print("nime Shab Be kheir")
    # elif ClockTime > 6 and ClockTime <= 12:
    #     print("Sobhet Be kheir")
    # elif ClockTime > 12 and ClockTime <= 18:
    #     print("Bade Zohr Be kheir")
    # elif ClockTime > 18 and ClockTime <= 24:
    #     print("Shabet Be kheir")