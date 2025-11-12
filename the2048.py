#2048 v2.16
# from api2048 import *
from math import *
from random import *
sc=0
def p(typ,i,k):
  if typ==1:
    if k[12+i]+k[8+i]+k[4+i]+k[i]==0:
      o666=4
    elif k[12+i]+k[8+i]+k[4+i]==0:
      k[12+i]=k[i]
      k[i]=k[4+i]=0
    elif k[12+i]+k[4+i]==0:
      k[12+i]=k[8+i]
      k[8+i]=k[i]
      k[i]=k[4+i]=0
    elif k[8+i]+k[i]==0:
      k[8+i]=k[4+i]
      k[i]=k[4+i]=0
    elif k[12+i]+k[i]==0:
      k[12+i]=k[8+i]
      k[8+i]=k[4+i]
      k[i]=k[4+i]=0
    elif k[12+i]+k[8+i]==0:
      k[12+i]=k[4+i]
      k[8+i]=k[4+i]
      k[i]=k[4+i]=0
    elif k[8+i]+k[4+i]==0:
      k[8+i]=k[i]
      k[i]=0
    elif k[4+i]==0:
      k[4+i]=k[i]
      k[i]=0
    elif k[8+i]==0:
      k[8+i]=k[4+i]
      k[4+i]=k[i]
      k[i]=0
    elif k[12+i]==0:
      k[12+i]=k[8+i]
      k[8+i]=k[4+i]
      k[4+i]=k[i]
      k[i]=0
  elif typ==2:
    if k[i]+k[1+i]+k[2+i]+k[3+i]==0:
      o666=4
    elif k[i]+k[1+i]+k[2+i]==0:
      k[i]=k[3+i]
      k[3+i]=k[2+i]=0
    elif k[i]+k[2+i]==0:
      k[i]=k[1+i]
      k[1+i]=k[3+i]
      k[3+i]=k[1+i]=0
    elif k[1+i]+k[3+i]==0:
      k[1+i]=k[2+i]
      k[3+i]=k[2+i]=0
    elif k[i]+k[3+i]==0:
      k[i]=k[1+i]
      k[1+i]=k[2+i]
      k[3+i]=k[2+i]=0
    elif k[i]+k[1+i]==0:
      k[i]=k[2+i]
      k[1+i]=k[2+i]
      k[i]=k[4+i]=0
    elif k[1+i]+k[2+i]==0:
      k[1+i]=k[3+i]
      k[3+i]=k[2+i]=0
    elif k[2+i]==0:
      k[2+i]=k[3+i]
      k[3+i]=0
    elif k[1+i]==0:
      k[1+i]=k[2+i]
      k[2+i]=k[3+i]
      k[3+i]=0
    elif k[i]==0:
      k[i]=k[1+i]
      k[1+i]=k[2+i]
      k[2+i]=k[3+i]
      k[i]=0
  elif typ==3:
    if k[i]+k[4+i]+k[8+i]+k[12+i]==0:
      o666=4
    elif k[i]+k[4+i]+k[8+i]==0:
      k[i]=k[12+i]
      k[12+i]=k[8+i]=0
    elif k[i]+k[8+i]==0:
      k[i]=k[4+i]
      k[4+i]=k[12+i]
      k[12+i]=k[4+i]=0
    elif k[4+i]+k[12+i]==0:
      k[4+i]=k[8+i]
      k[12+i]=k[8+i]=0
    elif k[i]+k[12+i]==0:
      k[i]=k[4+i]
      k[4+i]=k[8+i]
      k[12+i]=k[8+i]=0
    elif k[i]+k[4+i]==0:
      k[i]=k[8+i]
      k[4+i]=k[8+i]
      k[i]=k[4+i]=0
    elif k[4+i]+k[8+i]==0:
      k[4+i]=k[12+i]
      k[12+i]=k[8+i]=0
    elif k[8+i]==0:
      k[8+i]=k[12+i]
      k[12+i]=0
    elif k[4+i]==0:
      k[4+i]=k[8+i]
      k[8+i]=k[12+i]
      k[12+i]=0
    elif k[i]==0:
      k[i]=k[4+i]
      k[4+i]=k[8+i]
      k[8+i]=k[12+i]
      k[i]=0
  elif typ==4:
    if k[3+i]+k[2+i]+k[1+i]+k[i]==0:
      o666=4
    elif k[3+i]+k[2+i]+k[1+i]==0:
      k[3+i]=k[i]
      k[i]=k[1+i]=0
    elif k[3+i]+k[1+i]==0:
      k[3+i]=k[2+i]
      k[2+i]=k[i]
      k[i]=k[1+i]=0
    elif k[2+i]+k[i]==0:
      k[2+i]=k[1+i]
      k[i]=k[1+i]=0
    elif k[3+i]+k[i]==0:
      k[3+i]=k[2+i]
      k[2+i]=k[1+i]
      k[i]=k[1+i]=0
    elif k[3+i]+k[2+i]==0:
      k[3+i]=k[1+i]
      k[2+i]=k[1+i]
      k[i]=k[1+i]=0
    elif k[2+i]+k[1+i]==0:
      k[2+i]=k[i]
      k[i]=0
    elif k[1+i]==0:
      k[1+i]=k[i]
      k[i]=0
    elif k[2+i]==0:
      k[2+i]=k[1+i]
      k[1+i]=k[i]
      k[i]=0
    elif k[3+i]==0:
      k[3+i]=k[2+i]
      k[2+i]=k[1+i]
      k[1+i]=k[i]
      k[i]=0
  return k

def q():
  if sc<100000:return ceil(4-log10(sc+1.5))*"0"+str(sc)
  else:return str(sc)
def a(b):
  if b==0:return "    "
  elif b>=14:return "2^"+str(b)
  elif b>=100:raise Exception("\n\n\n========ERROR========\n Limitation reached")
  else:return (3-int(round(log10(2**b)-0.5)))*" "+str(2**b)
def c(d):
  f="+----"*4+"+"
  for _ in d:
    f+="\n|"
    f+=_[0]+"|"
    f+=_[1]+"|"
    f+=_[2]+"|"
    f+=_[3]+"|"
  ooo=f+"\n+----score:"+q()+"----+\ndirection:"
  return int(input(ooo))//2-1
def g(h):
  _=[]
  for i in range(4):
    z=[]
    for j in range(4):
      z.append(a(h[i*4+j]))
    _.append(z)
  return _
k=[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
def m():
  return randint(0,15)
while 1:
  www=0
  while 1:
    www+=1
    if www==80:
      raise Exception("lol u lose")
    n=m()
    if k[n]==0:
      k[n]=1
      break
  o=c(g(k))
  if o==0:
    for i in [0,1,2,3]:
      k=p(1,i,k)
      if k[12+i]==k[8+i] and k[8+i]:
        sc+=2**k[12+i]
        k[12+i]+=1
        k[8+i]=0
      if k[4+i]==k[8+i] and k[4+i]:
        sc+=2**k[8+i]
        k[8+i]+=1
        k[4+i]=0
      if k[i]==k[4+i] and k[i]:
        sc+=2**k[4+i]
        k[4+i]+=1
        k[i]=0
      k=p(1,i,k)
  if o==1:
    for i in [0,4,8,12]:
      k=p(2,i,k)
      if k[i]==k[1+i] and k[1+i]:
        sc+=2**k[i]
        k[i]+=1
        k[1+i]=0
      if k[2+i]==k[1+i] and k[2+i]:
        sc+=2**k[1+i]
        k[1+i]+=1
        k[2+i]=0
      if k[3+i]==k[2+i] and k[3+i]:
        sc+=2**k[2+i]
        k[2+i]+=1
        k[3+i]=0
      k=p(2,i,k)
  if o==2:
    for i in [0,1,2,3]:
      k=p(3,i,k)
      if k[i]==k[4+i] and k[4+i]:
        sc+=2**k[i]
        k[i]+=1
        k[4+i]=0
      if k[8+i]==k[4+i] and k[8+i]:
        sc+=2**k[4+i]
        k[4+i]+=1
        k[8+i]=0
      if k[12+i]==k[8+i] and k[12+i]:
        sc+=2**k[8+i]
        k[8+i]+=1
        k[12+i]=0
      k=p(3,i,k)
  if o==3:
    for i in [0,4,8,12]:
      k=p(4,i,k)
      if k[3+i]==k[2+i] and k[2+i]:
        sc+=2**k[3+i]
        k[3+i]+=1
        k[2+i]=0
      if k[1+i]==k[2+i] and k[1+i]:
        sc+=2**k[2+i]
        k[2+i]+=1
        k[1+i]=0
      if k[i]==k[1+i] and k[i]:
        sc+=2**k[1+i]
        k[1+i]+=1
        k[i]=0
      k=p(4,i,k)


