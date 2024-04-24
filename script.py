class Data:
    def __init__(self,data,nem ):
        self.data = 'C:\\games\\{self.data}'
        self.nem = nem

    def __str__(self):
        return ({self.data},{self.nem})

try:
    with open('C:\\games\\q.txt','r') as f:
        data = f.read()
        nem = data.split()[0].strip()
        pt=Data(data,nem)
except:
    print('f')
print(pt.__str__())
