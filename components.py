
#與門 或門 非門

#其中與門 或門是 接收兩個input輸出一個output ， 非門是接收一個input,輸出一個output

class LogicGate:

    def __init__(self,n):
        self.label=n
        self.output=None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None
    def getPins(self,pinA,pinB):
        self.pinA = pinA
        self.pinB = pinB
        print(f"{self.label} current input states ---> pinA: {self.pinA} pinB: {self.pinB}")


# a = BinaryGate('G3')
# a.getPins(1,0)

class UnaryGate(LogicGate):
    def __init__(self,n):
        super().__init__(n)
        self.pin = None
    def getPin(self,pin):
        self.pin = pin
        print(f"{self.label} current input states ---> pin: {self.pin}")
