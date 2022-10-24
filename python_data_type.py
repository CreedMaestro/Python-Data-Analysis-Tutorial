x = 'python' # 문자형
print(type(x))

a = 123 #숫자형
print(type(a))

b = [1, 2, 3, 4]  #리스트형
print(type(b))

c = {'name' : 'creed', 'age' : 37}  #딕셔너리형(key와 value가 있는 형태)
print(type(c))

d = True #참, 거짓을 표현하는 boolean형
print(type(d))

#  주석처리 단축키 :  " Ctrl + / "

e = 1 + 1
e = 100 - 1
print(type(e))  # 숫자형은 사칙연산이 가능, '' 문자형은 불가능

f = 'act as thouth it is impossible' # 줄바꾸기 방법 \n
print(f)
g = 'act as thouth \nit is impossible' # 줄바꾸기 방법 \n
print(g)
h = '''act as thouth 
it is impossible'''
print(h)  # ''' !@$! '''  따옴표 3개가 들어가면 문장의 띄워쓰기, 줄바꾸기가 모두 포함

i = """ "Failure is simply the opportunity to begin again." he says." """
print(i)
j = '"Failure is simply the opportunity to begin again." he says."'
print(j)
k = '\"Failure is simply the opportunity to begin again.\" he says.\"'
print(k)

l = 'a'
m = 'b'
print(l+m)
print(l-m)
print(l*m) #문자형끼리 곱셈은 안되지만,
print(l*10) #문자형에 숫자를 곱하면 표현이 된다.

n = '100'  # 세자리 숫자. 
print(len(n)) # 숫자의 문자수를 표현 length.

o = 'hello python!'
print(o[0])   # indexing 가져오기 [단일 지정]
print(o[0:5]) # slicing [범위 지정]  0 <= o < 5 (인덱싱 넘버 0 ~ 5사이 추출 )
print(o[0:])  # 처음부터 끝까지 지정
print(o[:])   # 처음부터 끝까지 지정

p = "Titanics James"  # 문장에서 slicing으로 제목과 감독을 추출
Title = print(p[0:7])
Director = print(p[9:])