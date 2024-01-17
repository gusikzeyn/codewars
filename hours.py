def past(h, m, s):
  #h=hours, m=minute, s=second  
  print( (s + (m + h * 60) * 60) * 1000)
    
past(0,1,1)