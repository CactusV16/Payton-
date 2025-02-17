ClockTime = int(input("Sara Khanoom Saat Alan Ro Vared Kon:\n"))

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


#  ساعت ۰ تا ۶، نیمه شب، ۶ تا ۱۲، صبح، ۱۲ تا ۱۸، بعد از ظهر و ۱۸ تا ۲۴ شب می باشد.