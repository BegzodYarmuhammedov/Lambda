#vaqtinchalik nomsiz funksiya

# def kv():
#     print("Hi bu kvadratni topadigan function")
#     (lambda a:print(a*a))(10)

# kv()


#map bilan
# def aa(a):
#     return a*a
# a,b = map(aa,[2,4])
# print(a,b) #4 16


#lambda bilan
# a,b = map(lambda a:a**2,[2,5])
# print(a,b) #4 16



# def map1(func,ls):
#     for i in ls:
#         print(func(i),end="  ")
# map1(lambda a:a*a,[1,2,3,4])



# val = lambda name:f"Mening ismim {name}"
# print(val("OTASHSATANA"))


#amaliyot

#1
# a= lambda ism,yosh :print(f"Mening ismim {ism} yoshim {2024-yosh}")
# print(a("Diyor",13))

#2
# b =  lambda a:print(a**2,a**3)
# b(5)

#3
# son = lambda a,b: print(a)if a>b  else print(b)
# son(3,4)

#4
# son = lambda a,b:print(a) if a>b  else(print("Sonlar teng ekan") if a==b else print(b))
# son(4,4)

#5
# son = lambda x,y:print(x**y)
# son(4,5)

#6
# son = lambda x,y=2:print(x**y)
# son(4)

#7
son = lambda a:[ print(f"{a} {i} ga qoldiqsiz bo'linadi") for i in range(2,11) if a%i==0  ]
son(4)