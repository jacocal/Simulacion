class EBI:
    results = []
    valid = []
    digits = 16
    def __init__(self):
        with open("seed.txt", 'r+') as file:
            c = file.readlines()
            self.seed = [x.strip() for x in c]

    def nextRand(self):
        for x in range(len(self.seed)):
            new = int(self.seed[x]) ** 2
            if(new <= 1):
                new += 1
            self.seed[x] = str(new)[8:-8]
            while(len(self.seed[x]) < self.digits):
                self.seed[x] = '1' + self.seed[x]

    def appResult(self):
        new = '0' * 16
        while(new not in self.results and len(self.valid) < 1000):
            cont = 0
            self.results.append(new)
            for d in range(self.digits-1, -1, -1):
                if(d % 2 == 0):
                    cont += int(new[d]) * 2
                else:
                    cont += int(new[d])
            if(cont % 10):
                self.valid.append(new)
            self.nextRand()
            new = ''.join(self.seed)
        with open("validas.txt", 'w') as file:
            for v in self.valid:
                file.write(v+"\n")
        return(self.valid[-10:])

def main():
    e = EBI()
    print(e.appResult())

if __name__ == '__main__':
    main()
