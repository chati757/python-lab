import pandas as pd

data = {'a':[1,1,1,3,4],'b':[2,2,2,2,4]}

df = pd.DataFrame(data)

df.loc[df['a']==1 , 'a'] = 0

print(df)

'''
   a  b
0  0  2
1  0  2
2  0  2
3  3  2
4  4  4
'''