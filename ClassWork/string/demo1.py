'''abc ="cmr technical campus"
print("Intial string:")
print(abc)

list1 =list(abc)
list1[2] ='p'
string =''.join(list1)
print("\n updating character in the list")
print(string)

string2 =string[0:2] + 'p' +abc[3:]
print(string2)


str1 ="I am Shiva"
print("Intial string")
print(str1)

del str1
print("\n Deleting")
print(str1)'''

#Escape Sequencing

#str='''shivaa'''
'''print("Initial string use of triple quote")
print(str)'''


#string alighment


'''word ="shiva"

sorted_word =sorted(word)
#combine this into a single line
sorted_word =''.join(sorted_word)
sorted_word1 =''.join(sorted(sorted_word.lower()))
print(sorted_word)
print(sorted_word1)'''




'''word ="Datagy"
sorted_word =''.join(sorted(set(word)))
print(sorted_word)'''



word ='da ta ?gy!'
sorted_word = ' '.join(filter(lambda x:x.isalpha(),sorted(word,key=lambda x:x.lower())))
print(sorted_word)




