"""
Remove the redundant brackets from a mathematical expression.
e.g. input: (a + (b*c)) * (d * ( f * j) )
output should be: (a + b * c) *d * f * j

Assumptions:

String is properly formatted. I don’t check whether there is a correct number of parenthesis etc
There is no spaces between the characters
Only following operators are allowed: ‘+’, ‘-‘, ‘*’,’/’


"""


#d + (a + (b*c)) * (d * ( f * j) )
#d + (a + b*c) * d * f * j

#(a*b)+c

# if first operation after ( is * - don't need brackets
# if first operation after (  is '+' and both left and right are '+' or None - don't need brackets

from enum import Enum
class Operation(Enum):
    none = 0
    mul = 1
    add = 2

class Expression:
    def __init__(self, operation, left, right):
        self.operation = Operation.none
        self.left = None
        self.right= None
        self.val = None


class parser:
    def __init__(self,str):
        self.pos=0
        self.str=str
        self.expression = None

    def parseExpression(self):
        exp = Expression()

        if self.current()=='(':
            self.move()
            exp.left = self.parseExpression()
            #skip closing ')'
            self.move()
        else:
            exp.val = self.current()
            self.move()
            exp.operation = self.parseOperation()
            if exp.operation != Operation.none:
                exp.right = self.parseExpression()
        return exp


    def parseOperation(self):

        if self.current()=='*':
            return Operation.mul
        elif self.current()=='+':
            self.move()
            return Operation.add

        return Operation.None

    def move(self):
        self.pos+=1

    def current(self):
        return self.str[self.pos]


    def parse(self):
        if self.current()=='(':
            self.move()
            self.expression = self.parseExpression()
            self.move()
        else:
            self.expression = self.parseExpression()

