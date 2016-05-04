class MiniGoogle:
    def __init__(self):
        self.index={}
    def add_to_index(self,url, body):
        self.index[url]=body

    def search(self, term):
        return [(url,body) for url,body in self.index if term in body]
