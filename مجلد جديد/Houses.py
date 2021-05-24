class Houses:
    def __init__(self,area,positions):
        self._area=area
        self._positions=positions
    def setarea(self,area):
        self._area=area
    def setpositions(self,positions):
        self._positions=positions
    def getarea(self):
        return self._area
    def getpositions(self):
        return self._positions
    def __str__(self):
        return "area: "+str(self._area)+\
            " **positions: "+self._positions
class Villa(Houses):

    def __init__(self,area,positions,cladding):
        super().__init__(area,positions)
        self._cladding=cladding
    def adjective(self):
        print("adjective this house is:villa.")
    def __str__(self):
        return "area: "+str(self._area)+"__positions: "+self._positions+\
               "__cladding: "+self._cladding

class Home(Houses):
    def __init__(self,area,positions,heighest):
        super().__init__(area,positions)
        self._heighest=heighest
    def adjective(self):
        print("adjective this house is:home.")
    def __str__(self):
        return "area: "+str(self._area)+"__ positions: "+self._positions+\
            "__ heigh the home: "+self._heighest




