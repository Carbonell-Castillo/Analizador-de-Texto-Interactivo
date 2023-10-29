class Printer:
    def __init__(self):
        self.text = ">>"

    def add(self, text):
        self.text += text

    def addLine(self, text):
        self.text +="\n>>"+ text  

    def print(self):
        return self.text
    
        



