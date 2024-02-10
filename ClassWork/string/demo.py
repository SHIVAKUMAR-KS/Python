text ='cmr technical campus'
print(text)

text1="cmr technical campus"
print(text1)

text2 ='''cmr technical campus'''
print(text2)


t1="""a string with special character" and ' inside """
print(len(t1))
print(t1)

s="cmr technical"
#s[2]='t'
#print(s)

txt="The rain in spain"
x="ain" in txt
print(x)


#string with loop
for achar in "cmr technical":
            print(achar)


s="Python data stucture"
print(len(s))
for ch in s:
        print(ch)

s="Python data stucture"
for ch in s[3:8]:
        print(ch)

s="Heloo shiva"
print(s.upper())
print(s.lower())



ss="        Hello world      "
print(ss)
els =ss.count("l")
print(els)
print(ss.strip())

print("***"+ss+"****")
print("***"+ss.strip()+"****")

news =ss.replace("o","***")
print(news)
print(ss)


sss="Cmr technical"
print(sss[1]*sss.index("n"))
print(sss.index("n"))


'''str1="Cmr1234"

d=0
l=0
u=0

for i in str1:
        if i.isdigit():
                d=d+1
            elif i.islower():
                l=l+1
            else:
                u=u+1
            print("No of digit in given string :",d)
'''

#string reversing

abc ="Cmr tech,nical, campus"
print(abc[::-1])
#split
k=abc.split(',')
print(k)

song ="The rain in spain.."
wds=song.split('ai')
print(wds)




