"""# # """
# # # a = int(input("请输入一个数字："))
# # # b = int(input("请输入另外一个数字："))
# # #
# # # def func(a,b):
# # #     if a>b:
# # #         print(a)
# # #     else:
# # #         print(b)
# # #
# # # print(func(3,4))
# # #
# # # print("1024 * 768 = ",1024 * 768)"""
# # #
# # # # print('hello\nworld')     # \n -->newline的首字母表示换行
# # # # print('hello\tworld')     # \t -->tab的首字母表示制表符
# # # # print('helloooo\tworld')  # \t -->tab的首字母表示制表符
# # # # print('hello\rworld')     # \r -->return的首字母表示返回
# # # # print('hello\bworld')     # \b -->backspace的首字母表示退一个格
# # # # print('http:\\\\www.baidu.com')
# # # # print('老师说：\"大家好\"')
# # # # print('老师说："大家好"')
# # # #错：
# # # # print('I'm "ok"')
# # # #对：
# # # # print('I\'m \"ok\"')
# # # # print("I'm ok")
# # # #错：
# # # #print('I 'am ok')
# # # # print('''line1 ...
# # # #         line2 ...
# # # #         line3 ''')
# # # # print('''line1
# # # # ... line2
# # # # ... line3''')
# # # PI = 3.14159265359
# # # # print(PI)
# # # PI = 3
# # # # print(PI)
# # # s3 = r'Hello, "Bart"'
# # # s4 = 'Hello, "Bart"'
# # # #只有一个格式化%，不需要加括号
# # # # print("hello %s，你好"%"李孝永")
# # # # #全部用%s代替
# # # # print("hello %s,你这个月的房租是%s，你应该在本月%s号之前交齐" %("李孝永","3740.7","4"))
# # # # #有多个格式化%，且包含%s %d %f
# # # # print("hello %s,你这个月的房租是%f，你应该在本月%d号之前交齐" %("李孝永",3740.76,400))
# # # #
# # # print("你的年龄是%02d岁"%7)
# # # print("你的年龄是%.2d岁"%7)
# # # # print("你的年龄是%2d岁"%7)
# # # # print("你的年龄是%-2d岁"%7)
# # # print('%2d-%02d' % (3, 1))
# # # # print('%.2f' % 3.1415926)
# # # r = 2.5
# # # s = 3.14 * r ** 2
# # # print(f'The area of a circle with radius {r} is {s:.2f}')
# # # a = 2
# # # b = a**2
# # # print(b)
# # # a = 85
# # # b = 72
# # # print("小明成绩的提升点是%.2f"%((85-72)/72))
# # # print("{0}，你的成绩提高了{1:.2f}%".format("小明",20.345))
# # # r1 = 2.5
# # # s = 3.14 * r1 ** 2
# # # print(f'The area of a circle with radius {r1} is {s:.2f}')
# #
# # list  = [1,"你好",2.4,True]
# # print(list)
# # for i in list:
# #     print(i)
# # print(type(list),len(list))
# # # print(list[0])
# # # print(list[-1])
# # # print(list[-5])
# # list.append("我是李孝永")
# # print(list)
# # list.insert(0,"我是新的第1位")
# # print(list)
# # list.pop(0)
# # print(list)
# # list[0] = "我是新的第一位"
# # print(list[0])
# # list.append([1,2,3])
# # print(list)
# # print(list[-1])
# # #二维数组获取列表中的列表
# # # print(list[-1][1])
# # # """
# # tuple = (1,"我是2",3.4)
# # print(tuple)
# # for i in tuple:
# #     print(i)
# # tuple1 = (1)
# # print(tuple1)
# # tuple2 = ("我是第一",2,[1,2,3])
# # print(tuple2[2][0])
# # print(tuple2[-1][0])
# # tuple2[2][0] = "我是新的第一"
# # print(tuple2)
# #
# # L = [
# #     ['Apple', 'Google', 'Microsoft'],
# #     ['Java', 'Python', 'Ruby', 'PHP'],
# #     ['Adam', 'Bart', 'Lisa']
# # ]
# #
# # # 打印Apple:
# # print(L[0])
# # # 打印Python:
# # print(L[0][1])
# # # 打印Lisa:
# # print(L[2][2])
# # print(len(L))
# #
# # tuple = (1,2,[1,2,3],(1,2))
# # print(tuple[2][1])
# # tuple[2][1] = "新的2"
# # print(tuple[2][1])
# # print(tuple)
#
# # age = 20
# # if age >= 6:
# #     print('adult')
# # elif age >= 18:
# #     print('teenager')
# # else:
# #     print('kid')
#
# # if 0:
# #     print("这里不会执行")
# # else:
# #     print("这里会执行")
# # list = []
# # if list:
# #     print("这里不会执行")
# # else:
# #     print("这里会执行")
# #
# # str =""
# # if list:
# #     print("这里不会执行")
# # else:
# #     print("这里会执行")
# #
# # tuple = ()
# # if list:
# #     print("这里不会执行")
# # else:
# #     print("这里会执行")
#
# """
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# """
#
# # a = int(input("请输入你的身高："))
# # b = int(input("请输入你的体重："))
# # if b/a**2<18.5:
# #     print("你的BMI结果为过轻")
# # elif 18.5<b/a**2<25:
# #     print("你的BMI结果为正常")
# # elif 28<b/a**2<32:
# #     print("你的BMI结果为肥胖")
# # else:
# #     print("你的BMI结果为严重肥胖")
# # list1 = [1,2,3,4,5,6]
# # sum = 0
# # for i in range(len(list1)):
# #     sum =sum+i
# # print(sum)
# # print(list(range(5)))
# # L = ['Bart','Lisa','Adam']
# # for l in L:
# #     print('Hello,',l,'!')
# '''
# 需求：计算1~100之间的偶数之和
# '''
# n = 0
# m = 0
# while m<101:
#     if n >2000:
#         break
#     n = m+n
#     m = m+2
#
# print(n)
"""
需求：使用while循环打印1~100以内的奇数
"""
m = 0
while m<101:
    m = m + 1
    if m%2 == 0:
        continue
    print(m)
# m = 0
# while 1:
#     m = m + 1
#     if m%2 == 0:
#         continue
#     print(m)

# n=12
# sum=0
# while n>10:
#     sum=sum+n
#     n=n-2
#     print(sum)
#     if n<=10:
#         sum=sum+n
#         n=n+2
#         print(sum)

# n=12
# sum=0
# while n>10:
#     sum=sum+n
#     n=n-2
#     print (sum)
#     while n<=10:
#         sum=sum+n
#         n=n+2
#         print (sum)