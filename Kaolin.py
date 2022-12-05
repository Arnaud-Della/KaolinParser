from tokens import *
from ObjectsClass import *
from Node import Node
from sys import argv

#filename = argv[1]
filename = "file.txt"
file = open(filename,"r")
code = file.readlines()

rootNode = Node()
actualNode = rootNode

if __name__ == '__main__':
    for line in code:
        line = line.strip().split(" ")
        if EnumFunction.has_value(line):
            actualNode = actualNode.addNode(Function(line))
        elif EnumDeclaration.has_value(line):
            actualNode.addInstruction(Declaration(line))
        elif EnumCondition.has_value(line):
            actualNode = actualNode.addNode(Condition(line))
        elif line[0] == BREAK:
            actualNode.addInstruction(Break())
        elif line[0] == RETURN:
            actualNode.addInstruction(Return(line))
        elif line[0] == str(EnumBLOCK.END):
            actualNode = actualNode.parentNode

    for i in rootNode.instructions:
        print(i)