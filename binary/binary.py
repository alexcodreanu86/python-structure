class Binary:
    def __init__(self,value=0):
        self._value = int(value)

    def __int__(self):
        return int(self._value)
