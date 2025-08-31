import pandas as pd
##importing dataset to pandas and printing it
df=pd.read_csv("B.csv")
print(df)
##shape and size
print(df.shape)
print(df.columns)
##selecting coloms
print(df['age'])
##selecting row
print(df.iloc(0))
print(df.head(1))
##filtering rows
print(df['grade']>7)
##adding collumn with condition
df['passed']= df['grade']>=8
df.loc[df['grade']>=8,'passed']='yes'
df.loc[df['grade']<8,'passed']='no'
print(df)
##mean age and max grade
print(df['age'].mean())
print(df['grade'].max())
##soeting students by age 
ndf=df.sort_values(by="age", ascending=False)
print(ndf)
##filling a missing data
z=pd.read_csv('c.csv')
zn=z.fillna(0)
print(zn)
##group by basics
v=df.groupby('grade')
print(v)
print(v.size())
##valuee count
print(df['grade'].value_counts())
##merging df
df10=pd.DataFrame({"id":[1,2],"name":["amit","sara"]})
df20=pd.DataFrame({"id":[1,2],"marks":["80","95"]})
j=pd.merge(df10,df20,on="id")
print(j)
##student marks
sd=pd.read_csv('a.csv')
print('mean for math is',sd['math'].mean())
print('mean for science is',sd['science'].mean())
print('mean for english is',sd['eng'].mean())
##sales data set
dd=pd.read_csv('d.csv')
dd['total']=dd['quantity']*dd['price']
print(dd)
##weather data set
wd=pd.read_csv('e.csv')
print(wd['temp'].mean())
print(wd['rainfall'].max())
print(wd[wd['temp']>30])