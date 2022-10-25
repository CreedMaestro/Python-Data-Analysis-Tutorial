# number = int(input('숫자를 입력하세요'))

# if number < 5 :
#     print('숫자가 5보다 작습니다.')
# # if True :
# #     print('숫자가 5보다 작습니다.')
# elif 5 < number < 10:
#     print('숫자가 5보다 크고 10보다 작습니다.')
# else: 
#     print('숫자가 10보다 큽니다.')

# money = int(input("숫자를 입력하세요"))

# if money == 70000:
#     print('비행기를 타고 가세요')
# elif money == 50000:
#     print('기차를 타고 가세요')
# elif money <= 30000:
#     print('버스를 탄다')

# print(range(10))  #0 <= x < 10

# countries = ['kor', 'usa', 'china']

# for country in countries:
#     if country == 'kor':
#         print('한글로 분석해주세요')
#     elif country == 'china':
#         print('중국어로 분석해주세요')
#     elif country == 'usa' :
#         print('영어로 분석해주세요')

# a = 0
# while a < 5:   #무한 반복 조건문에 많이 사용. 현업에선 거의 사용 x
#     a = a+1
#     print(a)

# Q. 1 부터 5까지 더하는 프로그램을 만들어보시오.
# (1) for (2) while

# b = 0
# while b < 5:
#     b = b+1
#     print(b+1)

# a = [1+2+3+4+5]
# result = 0
# for i in range(1,6):
#     # result = result + i
#     result +=1
#     print(i)

for i in range(10): # 0 ~ 9
    if 3 <= i <= 5:
        # continue #반복문 코드의 처음으로 돌아간다.
        break # 반복문의 종료
    print(i)