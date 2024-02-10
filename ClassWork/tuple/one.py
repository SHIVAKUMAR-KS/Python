'''type1 ={1,2,3,4,'test'}
print(type1)
print(type(type1))'''

#tuple packing and upacking
'''
T ='red','orange','cyan'
print(T)
print(T[2])'''

#unpacking
'''T =('red','orange','cyan')
(a,b,c,d) =T
print(a)
print(b)
print(c)
print(d)
'''

#swap
'''a=1
b=2
temp =a
a=b
b=temp
(a,b)=(b,a)
print(a,b)'''
'''
tuple=("apple","banana","cherry")
print(tuple)

y=list(tuple)
print(y)

y[1]="kiwi"
print(y)
'''

'''
tuple =(1,3,5,"test","print")
print(1 in tuple)
print(2 in tuple)'''


'''tuplekey ={}
tuplekey[('blue','sky')] ='Good'
tuplekey[('red,','cloud')] = 'fast'

print(tuplekey)'''

'''def circleInfo(r):
            c=2*3.12435 *r
            a=3.12435*r*r
            return(c,a)
print(circleInfo(10))

def add(x,y):
        return x+y
print(add(3,4))
z=(3,7)
print(add(*z))'''

def total_money_saved(n):
    total = 0
    current_deposit = 1
    for day in range(1, n + 1):
        total += current_deposit
        if day % 7 == 0:
            current_deposit += 1
    return total

# Example usage
print(total_money_saved(4))  # Output: 10
print(total_money_saved(10))  # Output: 37
 
