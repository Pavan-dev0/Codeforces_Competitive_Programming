"""
k bottles 
each bottles has l millimeters 
c limes => D Slices

for toast
needs nl=> Millimeters of dring
slice of lime
np grams of slats

"""

n,k,l,c,d,p,nl,np=map(int,input().split())
mil_drink=k*l
enough_toasts=mil_drink//nl
limes=c*d
salts=p/np 
results=min(enough_toasts,limes,salts)//n
print(int(results))