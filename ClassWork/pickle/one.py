'''import pickle
f=open("text2.txt",'wb')
dct={"name":"Ravi","age":23,"gender":"male"}
pickle.dump(dct,f)
f.close()
'''

import marshal
f=open("a.pyc","rb")
data=marshal.load(f)
exec(data)