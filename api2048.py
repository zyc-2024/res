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
    if k[4*i+3]+k[2+4*i]+k[1+4*i]+k[4*i]==0:
      o666=4
    elif k[3+4*i]+k[2+4*i]+k[1+4*i]==0:
      k[4*i]=k[3+4*i]
      k[3+4*i]=k[2+4*i]=0
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
      k[12+i]=k[i]
      k[i]=k[4+i]=0
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
  return k
