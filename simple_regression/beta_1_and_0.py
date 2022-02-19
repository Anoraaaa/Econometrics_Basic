

# calculate mean
class Beta:
    def __init__(self,listy,listx):
        self.x = listx
        self.y = listy

    def meanx(self):
        sum = 0
        for i in self.x:
            sum = sum + i
        return sum/(len(self.x))

    def meany(self):
        sum = 0
        for i in self.y:
            sum = sum + i
        return sum/(len(self.y))

    def beta_1(self):
        up = 0
        down = 0
        for i in range(len(self.y)):
            up = up + (self.y[i]-self.meany())*(self.x[i]-self.meanx())
        print(up)
        for i in self.x:
            down = down + (i-self.meanx())**2
        print(down)
        return up/down

    def beta_0(self):
        beta_1 = self.beta_1()
        return self.meany() - self.meanx()*beta_1








