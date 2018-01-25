
#
# import random
#
# def intCalu():
#     num1=int(input('좌변값을 하나 입력하세요'))
#     num2=int(input('우변값을 하나 입력하세요'))
#     fmt = "%d + %d = %d \n %d -%d =%d \n"
#     fmt += "%d * %d =%d \n %d / %d =%d \n"
#     fmt += "%d ** %d =%d \n"
#     print(fmt % (num1,num2, num1 + num2, \
#                  num1,num2, num1 - num2, \
#                  num1,num2, num1 * num2, \
#                  num1,num2, num1 / num2, \
#                  num1,num2, num1 ** num2))
# intCalu()
#
# #19 윤년 계산(2012년은 윤년)
# def isLeapYear():
#     year = int(
#         input('윤년여부를 알고 싶은 년도를 입력하세요 '))
#     isleap = '윤년이 아닙니다'
#
#     if ( (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
#         isleap='윤년입니다.'
#
#     print('%d는 %s' % (year,isleap))
#
# isLeapYear()
#
# #20 복권발행
# def rouletteLotto():
#     lotto = str(random.randint(100, 999))
#     lucky = input('복권번호를 입력하세요')
#     match = 0  # 일치여부
#     prize = '꽝!! 다음기회에'
#
#     for i in[0,1,2]:
#         for j in [0,1,2]:
#             if (lucky[i] == lotto[j]) :
#                 match += 1
#
#     if match == 3:
#         prize='1등 당첨 : 백만원!'
#     elif match == 2:
#         prize='2등 당첨 : 만원!'
#     elif match == 1:
#         prize='3등 당첨 : 천원!'
#
#     print(lucky, lotto, prize)
# rouletteLotto()

#성적 데이터 저장
class SungJukVO:
    def __init__(self,name,kor,eng,mat):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat

#성적 처리용 클래스
class SungJukService:
    def getTotal(self,sj):
        tot= sj.kor + sj.eng + sj.mat
        return tot
    def getAverage(self,sj):
        avg= self.getTotal(sj)/3
        return avg
    def getGrade(self,sj):
        grdlist = '가가가가가가미양우수수'
        var = int(self.getAverage(sj)/10)
        grd = grdlist[var]
        return grd