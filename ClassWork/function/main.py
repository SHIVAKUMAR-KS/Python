#function

'''def greet():
            print('Hello function')
            print("Glad to meet you")
print(type(greet))#function
greet()'''


#add__function
'''def add_num(num1,num2):
            
            sum =num1+num2
            print(sum)
add_num(5,6)'''


'''def hello2(s):
        print("Hello"+s)
        print("glad to meet u ")
hello2("Iman"+" and Jackle")
hello2("class " *3)'''

'''
def hello(s,n):
        greeting ="Hello {}".format(s)
        print(greeting*n)

hello("Wei",4)
hello("",1)
hello("Kitty",11)'''


def print_many(x,y):
        for i in range(y):
                print(x)
print_many(2,5)
print_many("f",5)


def square(x):
        y =x*x
        return y
tosquare =10
squareResult =square(tosquare)
print("The result of {} squared is {} .".format(tosquare,squareResult))


def weired():
        print("here")
        return 5
        print("there")
        return 10
x=weired()
print(x)


def square(x):
        y=x*x
        return y
print(square(square(square(2))))


def find_square(num):
        product =num*num
        return product
                
         