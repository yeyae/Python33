#리스트 내포 사용하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

#위의 코드를 리스트 내포를 사용할 때
a=[1,2,3,4]
result = [num * 3 for num in a]
print(result)

#[1,2,3,4] 중에 짝수에만 3을 곱하고 싶을 때
a=[1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

#리스트내포의 표현식
#[표현식 for 항목 in 반복 가능 객체 if 조건]
