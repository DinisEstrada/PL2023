from Entry import Entry

class Model:
    def __init__(self):
        self.header = []
        self.data = []
        self.maxs = {}
        self.mins = {}
    
    def add(self, entry):
        self.pessoas.__add__(entry)

    def readFile(self, filename):
        file = open(filename,"r",encoding="utf8")
        line = file.readline()
        self.header = line.replace('\n', '').split(',')
        while line:
            line = file.readline()
            if(len(line) > 0):
                content = line.replace('\n', '').split(',')
                idade      = int(content[0])
                sexo       = content[1]
                tensao     = int(content[2])
                colesterol = int(content[3])
                batimento  = int(content[4])
                temDoenca  = int(content[5])
                self.data.append(Entry(idade,sexo,tensao,colesterol,batimento,temDoenca))
        self.maxs['idade'] = max(self.data, key=lambda e: e.idade).idade
        self.mins['idade'] = min(self.data, key=lambda e: e.idade).idade
        self.maxs['colesterol'] = max(self.data, key=lambda e: e.colesterol).colesterol
        self.mins['colesterol'] = min(self.data, key=lambda e: e.colesterol).colesterol

    #rever isto
    def dist_sex(self):
        res = {
            'M': 0,
            'F': 0
        }

        for entry in self.data:
            res[entry.sexo]+= 1
        return res 


