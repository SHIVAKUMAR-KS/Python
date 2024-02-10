'''def longer_than_five(list_of_name):
            for name in list_of_name:
                    if len(name) > 5:
                            return True
            return False

list1 =["sam","Tera","sai","Anita"]
'''


'''def square(x):
            print("square")
            return x*x
def g(y):
        print("g")
        return y+3
print(square(g(2))) 
'''

'''def mylen(seq):
        c= 0
        for _in seq:
                c=c+1
        return c
print(mylen("Hello"))
print(mylen(1,2,7))
print(mylen(1,5,6,8))  '''

'''
def badsquare(x):
        y = x ** power
        return y
power =2
result = badsquare(10)
print(result)

def double(y):
        y = 2*y
        return y
def changeit(lst):
        lst[0] = "shiva"
        lst[1] = "kumar"

y=5
double(y)
print(y)'''

def changeit(list):
            list[0]="shiva"
            list[1]="kumar"

            return list
mylist =["106","student","hloo"]
newlist =changeit(list(mylist))
print(mylist)
print(newlist)


def square(x):
        y=x*x
        return y
def sum_of_square(x,y,z):
        a=square(x)
        b=square(y)
        c=square(z)

        return a+b+c
a,b,c =10,5,2
result=sum_of_square(a,b,c)
print(result)

'''inital =7
def f(x,y=2,z=inital):
        print("x,y,z are :"+str(x) +"," str(y)+","+str(z))

f(2)
f(2,5)
f(2,5,8)
f(x=2,z=8)'''

'''def adder(*num):
        sum=0

        for n in num:
                sum=sum+n
        print("Sum :",sum)

adder(5,3)

adder(2,6,8)
adder(2,4,6,7,7,4)


def avg(*args):
        return sum(args)/len(args)
av=avg(20,15,12)
print(av)


def intro(**data):
        print("/n Data type of argument:",type(data))

        for key,value in data.item():
                print("{} is {}".format(key,value))

intro(Firstname ="shiva",Lastname ="kumar",Age =22,phoneno =158526523)
intro(Firstname ="ak",Lastname ="pk",Age =20,phoneno =9484994,Email="ksiva@gmail.com")
'''


def add(x,y):
        return x+y
print(add(3,4))
print((lambda x,y:x+y)(3,4))












my_list =[1,5,4,6,8,11,3,12]
newlist =list(filter(lambda x:(x%2 ==0),my_list))
print(newlist)




