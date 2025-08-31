import numpy as n
##comverting python list into a np array and finding its type
a=[1,4,6,8,4,8,9,0]
array=n.array(a)
print(array)
print(type(array))
##creating array of 0 and 1
z=n.zeros([4])
o=n.ones([2,3])
print(z)
print(o)
##creating a arrange x 2-10 with step 2
x=n.arange(2,11,2)
print(x)
##creating evenly spaced no b/w 0 and 1
s=n.linspace(0,1,5)
print(s)
##checking shape and dtype
arr=n.array([10,20,30])
print(arr.shape)
print(arr.dtype)
##slicing and extracting array
sl=n.array([5,10,15,20,25])
print(sl[1])
print(sl[3:5])
##adding 2 arrays
a1=n.array([1,2,3])
a2=n.array([4,5,6])
print(a1+a2)
##finding sum,mean and max
l=n.array([2,4,6,8])
print(n.sum(l))
print(n.mean(l))
print(n.max(l))
##SELECTING NO ONLY GRATER THAN 8
aarr=n.array([3,6,9,12,15])
print(aarr[aarr>8])
##reshaping array
r=n.array([1,2,3,4,5,6])
nr=r.reshape(2,3)
print(nr)
##stacking array
v1=n.array([1,2])
v2=n.array([3,4])
print(n.vstack([v1,v2]))
##adding 10 scaler to array
y=n.array([1,2,3])
print(y+10)
##generating 5 random int b\w 1 and 20
n.random.seed(42)
ro=n.random.randint(1,20,5)
print(ro)
##students marks
sm=n.array([45,67,89,32,76])
mean=n.mean(sm)
print(mean)
print('the anbow avrage markes are',sm[sm>mean])
##finding highest lowest temp
wt=n.array([30,32,29,35,29,33,31])
print('the max temp of the week',wt.max())
print('the min temp of the week',wt.min())
print('the temp this past week was',wt.reshape(7,1))