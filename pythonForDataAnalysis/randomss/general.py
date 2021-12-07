import pandas as pd
frame = pd.DataFrame({'State':['Punjab','Punjab','Haryana','Haryana','JK','JK','JK'],
      'Year':[2000,2001,2000,2001,2000,2001,2002],
      'Population':[12,32,10,30,10,27,31]})
print(frame.T)
