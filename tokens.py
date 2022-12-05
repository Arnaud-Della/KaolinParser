from enum import Enum

class Detection(Enum):
    @classmethod
    def has_value(self,value):
        if type(value) == list:
            for i in value:
                if i in self._value2member_map_:
                    return True
        else:
            return value in self._value2member_map_
    @classmethod
    def get(self,value):
        if type(value) == list:
            for i in value:
                if i in self._value2member_map_:
                    return i
        else:
            return value

class EnumCondition(Detection):
    IF = "if"
    ELSE = "else"
    WHILE = "while"
        
class EnumDeclaration(Detection):
    INT = "int"
    BOOL = "bool"
    CHAR = "char"
    DOUBLE = "double"        

class EnumAffectation(Detection):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"
    DECLARATION = "="

class EnumLogiqueOperator(Detection):
    AND = "&&"
    OR = "||"
    NOT = "!"

class EnumCompareOperator(Detection):
    STRICTLY_INFERIOR = "<" 
    STRICTLY_HIGHTER = ">"
    INFERIOR_OR_EQUAL = "<="
    HIGHTER_OR_EQUAL = ">="
    EQUAL = "=="
    DIFFERENT = "!="

class EnumFunction(Detection):
    FUNC = "func"

class EnumBLOCK(Detection):
    END = "}"
    def __str__(self):
        return str(self.value)

BREAK = "break"
RETURN = "return"