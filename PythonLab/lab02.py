import random
#18 연봉계산
# 결혼여부
# isMarried = "Y","N"
# salary=int(input('연봉을 입력하세요'))
# isMarried=input('결혼여부를 입력하세요(미혼:0, 기혼:1)')
# if isMarried == '0':
#     if salary < 3000:
#         tax = salary * 0.1
#     else: tax = salary * 0.25
#
# elif isMarried == '1':
#     if salary < 6000: tax = salary * 0.1
#     else:
#         tax = salary * 0.25
#
# print(isMarried,salary, tax)
#
# #19 윤년 계산(2012년은 윤년)
# year = int(
#     input('윤년여부를 알고 싶은 년도를 입력하세요 '))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('%d는 윤년입니다.' % year)
# else:
#     print('%d는 윤년이 아닙니다'% year)

#20 복권발행
#20 복권밣ㅇ
#3자리수 , 모두일치 100만, 2개일치1만, 1개일치 1천 지급
# lotto = random.randint(100,999)
# lucky= input('복권번호를 입력하세요')
# match=0	#일치여부
#
# if (lucky[2] == lotto[0] or
#         lucky[2] == lotto[1] or
#         lucky[2] == lotto[2]) :
#     match +=1
#
# print(lotto,lucky,match)
# if match == 3:
#     print("1등 당첨 : 백만원!")
# elif match == 2:
#     print("2등 당첨 : 만원!")
# elif match == 1:
#     print("3등 당첨 : 천원!")
# else:
#     print("꽝!1!")

#
# #21 구구단
# #숫자만 입력받기
# #문자 - ASCII 코드값 : ord()
# #ASCII 코드값 - 문자 : chr()
# #0 : ASCII - 48, 9 : ASCII -57
#
# dan = input('출력할 단을 입력하세요 ')
# if ord(dan[0]) >= ord('0') \
#         and ord(dan[0]) <=ord('9'):
#     print('구구단출력')
# else:
#     print('입력오류 - 숫자만 입력하세요!')
#
# #22 소문자를 대문자로 변환
# #숫자나 대문자 입력시 오류메시지 출력
# lower = input('소문자를 입력하세요~')
# if ord(lower[0]) >= ord('a') and \
#         ord(lower[0])<=ord('z'):
#     print(lower.upper())
# else:
#     print('소문자만 입력가능!!')
#
#
# #23 숫자 맞추기
# #1~100 사이 난수 생성 후 맞추는 게임
# key = str(random.randint(1,100))
#
# while True:
#     lucky = int(input('1-100 사이 숫자 입력하세요 '))
#     if key == lucky:
#         print('빙고!! 숫자를 맞췄습니다.!')
#         break
#         elif key < lucky:
#             print('으음... 숫자가 크네요 :(')
#         else:
