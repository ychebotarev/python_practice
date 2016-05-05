__author__ = 'yuriic'
"""
Implement a Big Integer class with an addition operation.
"""

class BigInt:

    def __init__(self):
        self.buffer=[]

    def to_string(self,base=10):
        output=[]
        for v in self.buffer:
            output.append(str(v))
        output.reverse()

        return ''.join(output)

    def add(self, value):
        if type(value) is not BigInt:
            b = BigInt(value)
            return self.__add(b)
        else:
            return self.__add(value)


    def __add(self, value):
        #what does overflow mean? carry 1 to next digit

        result=BigInt();

        curry = 0
        for i in range(max(len(self.buffer), len(value.buffer))):
            v1= self.buffer[i] if i<len(self.buffer) else 0;
            v2 = value.buffer[i] if i < len(value.buffer) else 0

            result_digit = v1+v2+curry;
            curry = 1 if self.__owerflow(v1,v2,result_digit ) else 0
            result.buffer.append(result_digit)

        if curry > 0:
            result.buffer.append(curry)

        return result


    def __owerflow(self,v1,v2,result):
        return False