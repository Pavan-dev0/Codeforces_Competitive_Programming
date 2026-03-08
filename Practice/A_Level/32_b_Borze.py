n=input().strip()
i=0
result=[]

while i<len(n):
    if n[i]=='.':
        result.append('0')
        i+=1
    elif n[i]=='-':
        if i+1<len(n)and n[i+1]=='.':
            result.append('1')
            i+=2
        elif i+1<len(n) and n[i+1]=='-':
            result.append('2')
            i+=2
        else:
            print("invalid"); 
            break
    else:
        print("Invalid")
        break

print("".join(result))