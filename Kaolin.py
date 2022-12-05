from tokens import *
from ObjectsClass import *
from Node import Node
from sys import argv

try :
    filename = argv[1]
except :
    filename = "file2.txt"

file = open(filename,"r")
code = file.readlines()

rootNode = Node()
actualNode = rootNode
functionList = []
error = False

if __name__ == '__main__':
    for line in code:
        line = line.strip().split(" ")
        if EnumFunction.has_value(line):
            functionList.append(line[1])
            actualNode = actualNode.addNode(Function(line))
        elif EnumDeclaration.has_value(line):
            actualNode.addInstruction(Declaration(line))
        elif EnumCondition.has_value(line):
            if Condition.IsSimpleInstruction(line):
                actualNode.addInstruction(Condition(line))
            else:
                actualNode = actualNode.addNode(Condition(line))
        elif line[0] == BREAK:
            actualNode.addInstruction(Break())
        elif line[0] == RETURN:
            actualNode.addInstruction(Return(line))
        elif line[0] in functionList:
            actualNode.addInstruction(CallFunction(line))
        elif line[0] == str(EnumBLOCK.END):
            actualNode = actualNode.parentNode
        elif line[0] == "{" or line[0] == "":
            pass
        elif len(line)>=1:
            if line[1] == str(EnumAffectation.DECLARATION):
                actualNode.addInstruction(Affectation(line))
        else:
            error = True
            break
    
    if error :
        print("Error Synthaxe")
    else:
        for i in rootNode.instructions:
            print(i)