#import os
#n = os.path.abspath("множество.txt")
#print(n)



try:
    with open('C:\\games\\q.txt','r') as f,open('C:\\games\\w.txt','a')as v:
        data = f.read()
        v.write(data)

except:
    print('f')

