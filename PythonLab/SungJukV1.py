print('----성적 처리 프로그램 v1 ----')
# name= int(input('이름입력 :'))
# kor= int(input('국어성적 :'))
# eng= int(input('영어성적 :'))
# mat= int(input('수학성적 :'))
name=input('이름입력 :')
kor= int(input('국어성적 :'))
eng= int(input('영어성적 :'))
mat= int(input('수학성적 :'))

tot=kor+eng+mat
avg = tot / 3
grd='가'
if avg >90:
    grd='수'
elif avg >=80:
    grd='우'
elif avg >=70:
    grd='미'
elif avg >=60:
    grd='양'


print(name, kor, eng, mat, tot, avg, grd)
print('{0} {1} {2} {3} {4} {5:.2f} {6}'.format(name, kor, eng, mat, tot, avg, grd))
# print('%s %d %d %d %d %.2f %s'  \
#       % (name, kor, eng, mat, tot, avg, grd))