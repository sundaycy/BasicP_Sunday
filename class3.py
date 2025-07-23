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


while True :
    choice = int(input("กรอก 1 เพื่อบวกเลข, กรอก 2 เพื่อ ออก "))

    if choice == 1 :
        num = int(input("จำนวนเลขที่ต้องการจะบวก"))
        sumation = 0 

        for i in range (num):
            num1 = int(input("กรอกเลข"))
            sumation = sumation + num1 

        print("ผลลัพธ์",sumation)
    if choice == 2:
        print("บาย บาย ")
        break
