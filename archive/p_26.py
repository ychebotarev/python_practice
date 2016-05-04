'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.
For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].
A solution is ["cats and dog", "cat sand dog"].'''

class problem_1:
    def __init__(self):
        self.result=[]

    def _solve(self, current, pos):
        if pos == len(self.s):
            self.result.append(current)
        for prefix in self.wordDict:
            if self.s.startswith(prefix,pos):
                l = list(current)
                l.append(prefix)
                self._solve(l, pos + len(prefix))


    def solve(self, s, wordDict):
        self.wordDict = wordDict
        self.s = s
        self._solve([],0)
        return [' '.join(x) for x in self.result]

d = problem_1()
print(d.solve("catsanddog",["cat", "cats", "and", "sand", "dog"]))

