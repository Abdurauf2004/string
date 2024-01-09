# # 09.01.2024
# # 19:09
# # ism='Ali'
# # fam="valiyev"
#
# # print('salom'+ism+fam)
# # print(f"Salom {ism} {fam}")
#
# # ism_uznlik=len(ism) # 3
# # print(ism_uznlik)
# #
# # print(f"Assalomu alaykum {ism},\nSizning ismingizni uzunligi {ism_uznlik}\tga teng  ")
#
#
# til='python'
# # print(len(til))
#
# # print(til[2::])
#
# # print(ism[::-1][::-1])
#
#
# # print(ism.upper()) # barcha hariflarni kattaga otkazadi
#
# # print(ism.lower()) # barcha hariflarni kichika otkazadi
#
# # print(ism.capitalize()) # faqar bosh harifini katta qilib beradi
#
#
# # print(ism.isalnum())
# # print(ism.isalpha())
# # print(ism.isascii())
# # print(ism.index('y'))
#
# ism='yashNarBek'  #yashnarBek
#
# # dd=ism[:4] #yash
# # n=ism[4] #N
# # mm=ism[5::]
# #
# # n=n.lower()
# #
# # print(f"{dd}{n}{mm}")
#
# # print(ism.replace('y','Y')) # joylashtirmoq
#
#
# # print(ism.count('a')) # count nechta harif qatnashganini sanash uchun
#
# # print(ism.find('a'))
# # print(ism.index('a'))
#
# # fam='abunazarov'
# #
# # fish=f"{ism} {fam}"
# #
# # print(fish.title())
#
# # harif='   A   '
# # print(f'salom {harif.lstrip()} nima gaplar')
# # print(f'salom {harif.rstrip()} nima gaplar')
# # print(f'salom {harif.strip()} nima gaplar')
#
# # son=1961680012
# # son1=196_168_00_12
# # print(son)
# # print(son1)
#
# pi=3.14
# e=2.71
#
#
# # son3=float(son) #1961680012.0
# # yil=2023.6
# # jj='45555'
# # jj2=int(jj)
# # print(type(jj))
# # yil1=int(yil) #2023
# # print(yil1)
# # print(type(son3))
#
# # yil=2023
# # kun=24
#
# # yil,kun,soat=2023,24,11
# # print(yil)
# # print(kun)
# # print(soat)
#
#
# # son1=7
# # son2=12
# # print(12**1000)
# # son3=2
#
# # natija=son1%son3
# # natija=son2**1000
# # print(natija)
#
#
# # import math
# # son1=7
# # son2=4
# #
# # natija=math.factorial()
# # print(natija)
#
#
# import random
# # a=int(input('a='))
# # b=int(input('b='))
# print(random.uniform(0,10))
# 1.  Input orqali yoshingizni so’rab olib, yoshingiz nechchidaligini ekranga chiqaradigan dastur tuzing;
# - f stringdan foydalaning.
# a=input("Yoshingizni kiriting->")
# print(f"Sizning yoshingiz {a} yoshda")
#
# 2.  O’zgaruvchi oching va qiymatiga quyidagi matnni ko’chirib yozing: “String – matn ko’rinishidagi ma’lumot turi.”
# a="String – matn ko’rinishidagi ma’lumot turi."
# print(a)
# -len() funksiyasidan foydalanib uning uzunligini, keyin esa 9-indeksdan oxirigacha bo’lgan harflarni ekranga chiqaring.
# a="String – matn ko’rinishidagi ma’lumot turi."
# print(f"Matn uzunligi- {len(a)} ga teng.\n {a[9:-1]}" )
# 3.  Input orqali ism va familiyangizni so’rab olib, siz bilan salomlashadigan dastur tuzing;
# -Satrlarni birlashtirishdan foydalaning
# - Ism-familya harflari qay ko’rinishda kiritilsa ham, ularning 1-harflari katta, qolganlari kichik ko’rinishda ekranga chiqsin, so’z boshi va oxiridagi bo’sh kataklarni ham olib tashlang.
# a=input("Familyangizni  va  Ismingizni kiriting->").title()
# print(f"Assalomu alaykum {a.strip()}")

# 4.  “John yaxshi talaba, u darsga kech qolmaydi, vazifalarni vaqtida bajaradi. Siz ham John kabi bo’ling!”
# -Bir o’zgaruvchi ochib unga yuqoridagi matnni yozing
# -Dasturingiz ism nomli o’zgaruvchini input orqali qabul qilsin va “John” ni inputda olingan ism bilan almashtirib ekranga chiqarsin.
# b="John yaxshi talaba, u darsga kech qolmaydi, vazifalarni vaqtida bajaradi. Siz ham John kabi bo’ling!"
# print(b)
# a=input("Ism kiriting->")
# print(f"{a} yaxshi talaba, u darsga kech qolmaydi, vazifalarni vaqtida bajaradi. Siz ham {a} kabi bo’ling!")
# 5. Dasturingiz foydalanuvchidan input orqali ism so’rasin va u ismning teskarisini ekranga chiqarsin.
# a=input("Ism kiriting->")[::-1].capitalize()
# print(a)
# 6. Foydalanuvchidan yashayotgan shahrini input orqali oling. Avval uning xotiradagi qiymatini to’lig’icha bosh harflarga o’zgartiring, keyin uni ekranga chiqaring.  (Farg’ona -> FARG’ONA)
# a=input("Ona shahrizngizni kiriting->").upper()
# print(a)
# 7.  (kocha,mahalla,tuman,viloyat) qiymatlarini foydalanuvchidan  so’rang va konsolga (Men <viloyat> viloyati,<tuman> tumani, <mahalla>mahallasi, <kocha> ko’chasida yashayman!) chiqsin(f-stringdan foydalaning)
# a=input("Viloyatingizni kiriting->").capitalize()
# b=input("Tumaningizni kiriting->").capitalize()
# c=input("Mahallangizni kiriting->").capitalize()
# d=input("Ko`changizni kiriting->").capitalize()
# print(f"Men {a} viloyati,{b} tumani, {c} mahallasi, {d} ko’chasida yashayman!")
# 8. O’z ism familiyangizni faqat bosh hariflarini katta hariflarda chiqaring.

