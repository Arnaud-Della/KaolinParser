import json

class Node:
    def __init__(self, Type = 0, parentNode = 0)-> None:
        self.Type = Type
        self.parentNode = parentNode
        self.instructions = []
    def addInstruction(self,instruction):
        self.instructions.append(instruction)
    def addNode(self,types):
        tamp = Node(types,self)
        self.instructions.append(tamp)
        return tamp
    def __str__(self):
        tamp = json.loads(str(self.Type))
        tamptab = []
        for i in self.instructions:
            if type(i) != Node:
                tamptab.append(json.loads(str(i)))
            else:
                tamptab.append(json.loads(str(i)))
        tamp["instruction"] = tamptab
        return json.dumps(tamp, indent=4)