# #1 print()를 이용 다음 내용이 출력
# print('*   *     *     ****    ****    *   *       /////')
# print('*   *    ***    *   *   *   *   *   *      | o o |')
# print('*****   *   *   ****    ****     * *      (|  ^  |')
# print('*   *   *****   *  *    *  *      *        | [_] |')
# print('*   *   *   *   *   *   *   *     *         -----')
#
# print("            +---+                              ")
# print("            |   |                              ")
# print("        +---+---+                              ")
# print("        |   |   |                             ")
# print("    +---+---+---+      /\\ _/\\       -----    ")
# print("    |   |   |   |     ( ' ' )       / Hello \\    ")
# print("+---+---+---+---+     (  -  )      <  Junior | ")
# print("|   |   |   |   |      | | |        \\ Coder!/   ")
# print("+---+---+---+---+     (__|__)         -----    ")
#
# #2 이름, 나이, 몸무게
# name = '혜교'
# weight = 36.5
# age =35
# print('이름{},몸무게{},나이{}'.format(name,weight,age))
#
# #3 수학식을 파이썬 표현식으로 작성
# x=2
# y=3
# z=4
# print('3x=',3*x)
# print(3*x+y)
# print((x+y)/7)
# print((3*x+y)/(z+2))
#
# #4 다음 문장의 실행결과는 무엇인지 서술하세요
# x=4
# y=8
# x *=y   #x=x*y
# print('x*=y',x)
# x -=y
# print('x-=y',x)
#
# #5 다음 수식을 파이썬으로 작성
# x=3
# print(x+7 ==10)
#
# #6 다음 표현식의 결과는?
# print((-32+95)*12/3)
# print(3*4 - ((-27 + 67) /4))
# print((512+1968-432)/2**4) +128
# print(256==(2**8))
# print(50+50 <= 10*10)
# print(99 !=10 ** 2-1)
# #7. 연산자 의미 파악
# x, y, m, n = 2.5, -1.5, 18, 4
#
# print( x+n*y-(x+n)*y)
# print(m/n+m%n)
# print(5*x - n/5)
# print(1-(1-(1-(1-n))))
#
# #8 생활속 문제를 파이썬으로 풀기
# a= (2.5 * 3) /27
# b=(4* 2) / 30
#
# print(a)
# print(b)
#8
x,y=2.5,3
print(x*y /27)
x,y=4,2
print(x*y/30)

#9
# print(3+4.5*2+27/8)
# print(True or False and 3<4 or not (5==7))
# print(True or (3<5 and 6>=2))
# print(not True >'A') #문자에 비교연산자
# print(7%4+3-2/6*) # 문자에 산술연산자
# print('D'+1+'ㅡ' %2/3) #문자에 산술연산자
#
# #10 이윤율 계산 - 도메인 문제
# # 지문만으로는 문제를 해결할 수 없음
# # 문제에 대한 배경 지식이 필요 - 이윤율 공식
# # 가변자본 = 15
# # 불변자본 =30
# # 잉여가치 = 45
# # 이윤율 = 잉여가치 /(불변자본 /+ 가변자본)
# # print('이윤율:',이윤율)
# #11 환율에 따른 노트북 구매
# #달러 : 780, 유로 : 650
# #달러 환율 : 1070,2018.01.22 현재
# #유로 환율 : 1309. 2018.01.22 현재
# 달러 노트북 = 780 * 1071
# 유로 노트북 =650 * 1309
# print('달러노트북 %d ,유로 노트북 %d' \ % (달러노트북, 유로노트북))
#
# #12 운동장 너비 계산
# #원의 둘레 계산식 : pi * 지름
# pi =3.14
# 바깥학생거리 = pi * 100
# 안쪽학생거리 = pi * 95
# distance=바깥학생거리 - 안쪽학생거리
# print('바깥학생이 %d 미터 더달렸음' % distance)

#13 표현식 확인하기
print("Check out this line")
#print("//hello there" + '9' + 7)
#print('H'+'I'+"is"+1+"more example")
#print('H'+6.5+'I'+"is"+1+"more example")
print("Print both of us","Me too")
print("Reverse"+'I'+'T')
# print("Nonot Here is " +1+ "more example")
#print("Here is" + 10*10)
#print("Not x is " + True)
print()
print # 함수의 유형 출력
#print("How about this one" ++'?'+'Huh?') # 증가연산자

# 14.값 계산
# print(True and False and True or True)
# print(True or True and True and False)
# print((True and False) or (True and not False) or (False and not False))
# print((2<3) or (5>2) and not (4==4) or 9!=4)
# print (6==9 or 5<6 and 8<4 or 4>3)
# # 16 증감연산자가 파이썬에도 있나?
# # 파이썬에서는 기본적으로 ++, --는 지원 X
# n = 3
# print(++n)
# print(--n)
# n +=1
# print(n)
# n=3
# n -=1
# print(n)
# 17 사칙연산프로그램 = input 함수 이용
# x=input("첫번째 정수를 입력하세요")
# y=input("두번째 정수를 입력하세요")
# tot=int(x) + int(y)
# print('x+y=',tot)
# minus= int(x)- int(y)
# print('x-y=' ,minus)
# mul=int(x) * int (y)
# print('x*y=',mul)
# div = int(x) / int(y)
# print('x/y=',div)
#
#
# print('***사칙연산 프로그램***')
# num1= int(input('첫번째 정수를 입력하세요 : '))
# num2= int(input('두번째 정수를 입력하세요 : '))
#
# print(' %d + %d = %d ' % (num1,num2,num1+num2))
# print(' %d - %d = %d ' % (num1,num2,num1-num2))
# print(' %d * %d = %d ' % (num1,num2,num1*num2))
# print(' %d / %d = %d ' % (num1,num2,num1/num2))

# flag = input('맘에 드는 옷을 골랐나요? (예/ 아니오)')
# if flag=='예': print(':) 축하드려요~')
# price=int(input('옷값은 얼마인가요?'))
# if price > 10000:print(' :( 비싸네요~')
# else:print(':) 하나 주세요!~')
# elif flag == '아니오'
# print(':( 어떡해요~')
# else:
# print('예/아니오로 입력하세요!')
