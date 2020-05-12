class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0
    def computeDifference(self):
        for i in self.__elements:
            for j in self.__elements:
                dif=abs(i-j)
                if dif>self.maximumDifference:
                    self.maximumDifference=dif
        return