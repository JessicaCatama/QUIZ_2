n=int(input())
inq=0
outu=0
for i in range (n):
    x=int(input())
    if 10<=x<=20:
        inq=inq+1
    else:
        outu=outu+1
print(f"{inq} in")
print(f"{outu} out")