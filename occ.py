a,b=map(int,input().split())
c=list(map(int,input().split()))
count=0
for i in c:
    if(i==b):
        count=count+1
print(count)
      
