dist = float(input("คุณต้องการส่งของระยะทางเท่าไหร่"))
if dist >= 500:
    print("45 บาท")
elif dist >= 301:
    print("ค่าส่ง 35 บาท")
elif dist >= 101:
    print("ค่าส่ง 25 บาท")
elif dist >= 51:
    print("ค่าส่ง 15 บาท")
elif dist >= 5:
    print("ค่าส่ง 10 บาท")
else:
    print("ไม่ส่งไปส่งเอง")