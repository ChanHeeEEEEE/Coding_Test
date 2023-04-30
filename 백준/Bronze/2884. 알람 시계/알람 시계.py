a = input().split()
c=["",""]
b=int(a[0])*60+int(a[1])-45
c[1]=b%60
c[0]=round((b-c[1]+60*24)%(60*24)/60)
print(c[0],c[1])