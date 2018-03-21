class EBI:
    results = []
    digits = 4
    def __init__(self):
        with open("seed.txt", 'r+') as file:
            c = file.readlines()
            self.seed = [x.strip() for x in c]

    def nextRand(self):
        for x in range(len(self.seed)):
            new = int(self.seed[x]) ** 2
            if(new <= 1):
                new += 1
            self.seed[x] = str(new)[2:-2]
            while(len(self.seed[x]) < self.digits):
                self.seed[x] = '1' + self.seed[x]

    def appResult(self):
        new = int(''.join(self.seed))
        self.nextRand()
        while(new not in self.results):
            self.results.append(new)
            self.nextRand()
            new = int(''.join(self.seed))
        return(len(self.results))

def main():
    e = EBI()
    print(e.appResult())

if __name__ == '__main__':
    main()
