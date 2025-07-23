# # haverice = True
# # havespoon = False
# # havehand = True
# # if haverice :
# #     if havespoon :
# #         print("กินช้าว")
# #     elif havehand:
# #         print("กินข้าวเหนียว")
# score = float(input("คะแนนของคุณ : "))
# if score >= 0 :
#     if score <= 100:
#         if score >=80 :
#             print("A")
#         if score >= 70 :
#             if score  < 80:
#                 print("Grade B")
#         if score >= 60:
#             if score  < 70 :
#                 print("C")
#         if score >= 50:
#             if score < 60: 
#                 print("Grade D")
#         if score < 50 :
#             print("F")

# for i in range(1,10,2):
#     print (i)

# i = 0
# while i < 5 :
#     print("สวัสดี")
#     i = i + 1 


# while True :
#     choice = int(input("กรอก 1 เพื่อบวกเลข, กรอก 2 เพื่อ ออก "))

#     if choice == 1 :
#         num = int(input("จำนวนเลขที่ต้องการจะบวก"))
#         sumation = 0 

#         for i in range (num):
#             num1 = int(input("กรอกเลข"))
#             sumation = sumation + num1 

#         print("ผลลัพธ์",sumation)
#     if choice == 2:
#         print("บาย บาย ")
#         break
# monhp = 20
# w1 = 10
# w2 = 5 
# w3 = 15

while True :
    monhp = 20
    w1 = 10
    w2 = 5 
    w3 = 15
    choice1 = int(input("กด 1 เพื่อ สู้ , กด 2 เพื่อออก :"))
    if choice1 == 1 :
        print ("มอนเตอร์เลือด 20 hp")
        num = int(input("จะตีกี่รอบ"))
        summation = monhp

        for i in range (num):
            num1 = int(input("เลือกอาวุธ 1.ดาบ(10) 2.ปืน(5) 3.หมัด(15)"))
            if num1 == 1 :
                summation = summation - w1
                print ("เลือดเหลือ ",summation)
            elif num1 == 2 :
                summation = summation - w2
                print ("เลือดเหลือ",summation)
            elif num1 == 3 :
                summation = summation - w3   
                print ("เลือดเหลือ",summation)
            
            if summation == (0) :
                print("ชนะ")
                break

            elif summation < (0):
                summation = 20
        if i == num and summation > 0 :
                print("แพ้")
            
    if choice1 == 2 :
        print(" bye bye")
             
                
            # sum = s - num1
            # print ("เลือดมอนเหลือ ",sum)

