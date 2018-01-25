#총점 getTotal
#평균 getAverage()
#함수 getGrade()


def getTotal():
    tot = kor + eng + mat
    return tot

def getAverage():
    tot = kor + eng + mat
    avg = tot / 3
    return avg

def getGrade():
    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if avg > 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'
    return grd

name = input('이름입력 :')
kor = int(input('국어성적 :'))
eng = int(input('영어성적 :'))
mat = int(input('수학성적 :'))
fmt='%s %d %d %d %d %.2f %s'
print(fmt % (name,kor,eng,mat,getTotal(),getAverage(),getGrade()))