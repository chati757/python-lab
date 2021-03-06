import pandas as pd

# ways to create dataframe
# initialize list of lists 
data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['Name', 'Age']) 
  
# print dataframe. 
print(df)
"""
   Name  Age
0   tom   10
1  nick   15
2  juli   14
"""
# Python code demonstrate creating  
# DataFrame from dict narray / lists  
# By default addresses. 
  
  
# intialise data of lists. 
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
  
# Create DataFrame 
df = pd.DataFrame(data) 
  
# Print the output. 
print(df)
"""
Age   Name
0   20    Tom
1   21   nick
2   19  krish
3   18   jack
"""
# Python code demonstrate creating  
# pandas DataFrame with indexed by  
  
# DataFrame using arrays. 
import pandas as pd 
  
# initialise data of lists. 
data = {'Name':['Tom', 'Jack', 'nick', 'juli'], 'marks':[99, 98, 95, 90]} 
  
# Creates pandas DataFrame. 
df = pd.DataFrame(data, index =['rank1', 'rank2', 'rank3', 'rank4']) 
  
# print the data 
print(df)
"""
       Name  marks
rank1   Tom     99
rank2  Jack     98
rank3  nick     95
rank4  juli     90
"""

#convert csv file to dataframe (Can be pull from url)
dataframe = pd.read_csv("data/timeseries.csv")
print(dataframe)
"""
         Date   High    Low   Open  Close
0  2017-12-22  85.50  83.75  84.00  85.25
1  2017-12-25  87.00  85.00  85.50  85.25
2  2017-12-26  86.50  84.50  85.25  86.25
3  2017-12-27  86.75  85.50  86.50  85.75
4  2017-12-28  85.50  84.00  85.25  85.00
5  2017-12-29  85.25  84.50  85.00  85.00
"""

#add colum to dataframe
dataframe['close_x2']=dataframe['Close']*2
#dataframe['close_x2']=dataframe.Close*2 #(Is the same)
print(dataframe.head()) #display in 5 first rows of dataframe
"""
         Date   High    Low   Open  Close  close_x2
0  2017-12-22  85.50  83.75  84.00  85.25     170.5
1  2017-12-25  87.00  85.00  85.50  85.25     170.5
2  2017-12-26  86.50  84.50  85.25  86.25     172.5
3  2017-12-27  86.75  85.50  86.50  85.75     171.5
4  2017-12-28  85.50  84.00  85.25  85.00     170.0
"""

#convert decimal
dataframe['close_x2_round_0']=dataframe['close_x2'].round(0)
print(dataframe.head())
"""
         Date   High    Low   Open  Close  close_x2  close_x2_round_0
0  2017-12-22  85.50  83.75  84.00  85.25     170.5             170.0
1  2017-12-25  87.00  85.00  85.50  85.25     170.5             170.0
2  2017-12-26  86.50  84.50  85.25  86.25     172.5             172.0
3  2017-12-27  86.75  85.50  86.50  85.75     171.5             172.0
4  2017-12-28  85.50  84.00  85.25  85.00     170.0             170.0
"""

#sub-dataframe of colum
dataframe['sub_date'] = dataframe['Date'].str[8:]
print(dataframe.head())
"""
         Date   High    Low   Open  Close  close_x2  close_x2_round_0 sub_date
0  2017-12-22  85.50  83.75  84.00  85.25     170.5             170.0       22
1  2017-12-25  87.00  85.00  85.50  85.25     170.5             170.0       25
2  2017-12-26  86.50  84.50  85.25  86.25     172.5             172.0       26
3  2017-12-27  86.75  85.50  86.50  85.75     171.5             172.0       27
4  2017-12-28  85.50  84.00  85.25  85.00     170.0             170.0       28
"""
#show simple data of statistic
print(dataframe.describe())
"""
            High        Low       Open      Close    close_x2  close_x2_round_0
count   6.000000   6.000000   6.000000   6.000000    6.000000          6.000000
mean   86.083333  84.541667  85.250000  85.416667  170.833333        170.666667
std     0.752773   0.640638   0.806226   0.491596    0.983192          1.032796
min    85.250000  83.750000  84.000000  85.000000  170.000000        170.000000
25%    85.500000  84.125000  85.062500  85.062500  170.125000        170.000000
50%    86.000000  84.500000  85.250000  85.250000  170.500000        170.000000
75%    86.687500  84.875000  85.437500  85.625000  171.250000        171.500000
max    87.000000  85.500000  86.500000  86.250000  172.500000        172.000000
"""

#show 2 column only in all dataframe
print(dataframe[['Close','Low']].head())
"""
   Close    Low
0  85.25  83.75
1  85.25  85.00
2  86.25  84.50
3  85.75  85.50
4  85.00  84.00
"""
print(dataframe[['Close']]) #display one column of dataframe
"""
   Close
0  85.25
1  85.25
2  86.25
3  85.75
4  85.00
5  85.00
"""
print(dataframe['Close']) #display one column of dataframe object or series
"""
0    85.25
1    85.25
2    86.25
3    85.75
4    85.00
5    85.00
Name: Close, dtype: float64
"""
dataframe['shift-close'] = dataframe['Close'].shift(-1)
print(dataframe)

print(dataframe.columns)
"""
Index(['Date', 'High', 'Low', 'Open', 'Close', 'close_x2', 'close_x2_round_0','sub_date', 'shift-close'],dtype='object')
"""

"""
#df
   a  b
0  1  4
1  3  5
2  4  6

#----------------- series -------------------

#df.loc[1] get series
a    3
b    5
Name: 1, dtype: int64

#df.loc[df['a']==3,'a'] get series
1    3
Name: a, dtype: int64

#df.loc[df['a']==3]['a'] get series
1    3
Name: a, dtype: int64

#-------------------------------------------

#---------------- dataframe ----------------

#df.loc[df['a']==3] get dataframe
   a  b
1  3  5

#df.loc[df['a']==3] get dataframe
   a  b
1  3  5

#df.loc[df['a']==3][['a']] get dataframe
   a
1  3

#-------------------------------------------
#Example condition syntax

df[df['A'] > 0]

#Example multi-condition syntax

df[(df['W'] > 0) & (df['Y'] > 1)]
"""