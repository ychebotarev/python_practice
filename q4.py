__author__ = 'yuriic'


class LSC:
    def __init__(self):
        self.result=[[]]
        self.size_x=0
        self.size_y=0

    def calc(self, sec1, sec2):
        if len(sec1) == 0 or len(sec2) == 0:
            return 0,0,0,0

        self.sec1 = sec1
        self.sec2 = sec2

        self.__calc(sec1, sec2, 0, 0);
        return self.__findmax();

    def __findmax(self):
        result = 0,0,0
        for i in range(self.size_x):
            for j in range(self.size_y):
                if self.result[i][j]>result[2]:
                    result=i,j,self.result[i][j]
        return result

    def __get(self, x, y):
            return 0 if x>=self.size_x or y >=self.size_y else self.result[x][y]

    def __calslcs(self, start1, start2):
        if start1>=len(self.sec1) or start2>=len(self.sec2):
            return

        if self.sec1[start1] == self.sec2[start2]:
            self.__calslcs(start1+1,start2+1)
            self.result[start1][start2]=self.__get(start1+1,start2+1) + 1
        else:
            self.__calslcs(start1,start2+1)
            self.__calslcs(start1+1,start2)
            self.result[start1][start2] = max(self.__get(start1,start2+1),self.__get(start1+1,start2))

class diff:
    def __init__(self):
        self.input1=""
        self.input2=""

    def produce(self, input1,input2):
        self.input1 = input1
        self.input2 = input2

        lcs = find LCS(self.input1,self.input1)

        return diff(self.input0[0:lcs[0][0]], self.input1[0:lcs[1][0]]) + ... + ... +