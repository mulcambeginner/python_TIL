# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

print('hello world')

name='파이쏭'
print(name)

a=1024
print(a)

# name 변수의 값을 '파이쏭' 대신 다른 값으로 바꿔보세요!
name='파이쏭'
print(name+'님 안녕하세요!')

name='원더키디' #주석은 코드 오른쪽에 쓸 수도 있습니다.
print(2020,name,'화이팅!!')

name=input()
print(name+'님! 안녕하세요!')

name=input('이름을 입력해주세요 : ')
print(name+'님! 안녕하세요!')

age=input('나이를 입력해주세요! : ')
print(int(age)-4)

name=input('이름을 입력해주세요 : ')
age=int(input('나이를 입력해주세요 : '))
print('안녕하세요!',name+'님! 저는 처음에 +'+int(age-4)+'살인 줄 알았어요!!')

print(5//2)

print(10%4)

print(10>=3)

print(10<=3)

print(10==3)

print(10!=3)

print(3%2==1)

print(10=!3)

names = ['쵸파','루피','상디','조로']
for g in name :
    print(g)

for i in (0,1,2,3) :
    print(i**2)

for i in range(101) :
    print(i ** 2)

for i in range(4,10,3) :
    print(i*2)

if 10<0 :
    print('안녕하세요?')

passwd = int(input('비밀번호 4자리를 입력하세요 : '))
if passwd == 1531 :
    print('비밀번호가 일치합니다.')
if passwd == 2468 :
    print('불일치')

names = ['쵸파','루피','상디','조로']
for name in names :
    print(a)
del name
for names in name:
    print(name)

names = ['쵸파','루피','상디','조로']
print

a = input("숫자입력을 하세요")
if int(a) < 0:
    print( "a는 음수입니다")
elif 1<int(a)<10:
    print("a는 한자리 양수입니다")
else:
    print("a는 두자리이상 양수입니다")

names = ['쵸파','루피','상디','조로']
print(names[-3])

names=['쵸파','루피','상디','조로']
print(names[0:2])
print(names[1:3])
print(names[1:])
print(names[:])

names=['쵸파','루피','상디','조로']
names.append('나미')
print(names)

print(len(names))

print(len(' q'))

names=['쵸파','루피','상디','조로']
names.append('해적왕')
for i in names :
    if len(i)>0 :
        print(i,'왔나요?')

print("안녕하세요")

print('hi')

a=9 
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

print('파이썬','데이터분석입문','playwithdata','데이터수집')

print('귤','사과','배',sep='/')

# +
print('1번','2번','3번','4번','5번','6번','7번','8번','9번','10번')

class1= ['1번','2번','3번','4번','5번','6번','7번','8번','9번','10번']
print(class1)

# +
k = ['a','b','c','d','e']

print(k[1:3])
print(k[-4:-1])
# -

l1= ['a']
l2= ['b','c','d']
print(l1+l2)
print(l2+l1)

l1= ['a']
l2= ['b','c','e']
l2.append(l1)
print(l2)

fruits= ['바나나','사과','딸기','배','감']
for fruit in fruits :
    print(fruit)

a='사과'
b='망고,파인애플'
ab=b+a
print(ab)

z='*'
print(z*8)

month='2월'
day='20일'
say='{} {}은 일요일입니다.'.format(month,day)
print(say)

# +
k = "가나다라마바"
#index 012345
#index -6-5-4-3-2-1

print(k[2])
print(k[-1])
print(k[2:5])
print(k[3:])
# -

t1 = ' hp010-0000-0000 '
print(t1)
t2=t1.strip()
print(t2)
t3=t2.replace('hp','')
print(t3)
t4=t3.split('-')
print(t4)

# +
price=int(input('가격을 입력하세요 : '))
if price > 3000:
    print('비싸다')
else:
    print('저렴하다')

print(price)


# -

def 함수명(매개변수):
    실행부분


# +
def say(name):
    print('안녕하세요,')
    print('제 이름은 '+name+' 입니다')

say('홍길동')


# +
def cal(a,b):
    result= a**b
    return result
    
    
test= cal(10,3)  
print(test)
# -






