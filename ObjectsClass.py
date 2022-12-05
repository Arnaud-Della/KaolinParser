
import json
from tokens import *

class Instruction:
    def __str__(self):
	    return json.dumps(self.__dict__)

class Declaration(Instruction):
    def __init__(self,line) -> None:
        self.Instruction = type(self).__name__
        self.Type = line[0]
        self.Variable = line[1]

class Affectation(Instruction):
    def __init__(self,line) -> None:
        self.Instruction = type(self).__name__
        self.Variable = line[0]
        line.remove(';')
        self.NewData = " ".join(line[line.index("=")+1:len(line)])
        
class Function(Instruction):
    def __init__(self,line) -> None:
        self.Instruction = type(self).__name__
        self.Name = line[1]
        tamp = " ".join(line)
        self.Parametre = self.find_between_r(tamp,"(",")")
        #self.Condition = NULL;

    def find_between_r(self, s, first, last ):
        try:
            start = s.rindex( first ) + len( first )
            end = s.rindex( last, start )
            return s[start:end]
        except ValueError:
            return ""

class Condition(Instruction):
    def __init__(self,line) -> None:
        self.Instruction = type(self).__name__
        self.Name = line[0]
        if self.Name != "else":
                tamp = " ".join(line)
                self.Condition = self.find_between_r(tamp,"(",")")
        if line[len(line) - 1] == ";":
            self.SimpleInstruction = self.find_between_r(" ".join(line),")",";").strip()

    def find_between_r(self, s, first, last ):
        try:
            start = s.rindex( first ) + len( first )
            end = s.rindex( last, start )
            return s[start:end]
        except ValueError:
            return ""
    @staticmethod
    def IsSimpleInstruction(line):
        if line[len(line) - 1] == ";":
            return True
        else:
            return False

class Break(Instruction):
    def __init__(self) -> None:
         self.Instruction = type(self).__name__

class Return(Instruction):
    def __init__(self,line) -> None:
         self.Instruction = type(self).__name__
         line.remove("return")
         line.remove(";")
         self.Value = " ".join(line)

class CallFunction(Instruction):
    def __init__(self,line) -> None:
        self.Instruction = type(self).__name__
        self.Name = line[0]
        self.Parameters = self.find_between_r(" ".join(line),"(",")")
    def find_between_r(self, s, first, last ):
        try:
            start = s.rindex( first ) + len( first )
            end = s.rindex( last, start )
            return s[start:end]
        except ValueError:
            return ""