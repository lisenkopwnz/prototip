class Data:
    def __init__(self,data,nem ):
        self.data = data
        self.nem = nem

    def __enter__(self):
        self.log_file = open(nem, 'w')
        return self

    def write(self):
        self.log_file.write(data)

    def __exit__(self):
        self.log_file.close()

    def __str__(self):
        return ({self.data},{self.nem})

try:
    with open('C:\\games\\q.txt','r') as f:
        data = f.read()
        nem ='C:\\games\\' + data.split()[0].strip() +'.txt'
        pt=Data(data,nem)
except:
    print('f')

print(pt.__str__())
pt.__enter__()
pt.write()
pt.__exit__()
