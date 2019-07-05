ha,sea=map(int,input().split())
tik=list(map(int,input().split()[:ha]))
tok=0
for i in tik:
   if(i==sea):
      tok=tok+1
print(tok) 
