import pandas as pd

class Model:
    
    def __init__(self, triples=None):
        self.__triples = triples if triples is not None else []
        
    def add(self, triple):
        self.__triples.append(triple)
        return self
        
    def done(self):
        # self.df = pd.DataFrame([ [ t[0].idx_val(), t[1].idx_val(), t[2].idx_val(), t ] for t in self.__triples if not t.has_graph() ], columns=list("spot"))
        # self.__triples = None
        return self
        
    def __iter__(self):
        return self.__triples.__iter__()
        
    def __len__(self):
        return len(self.__triples)
    
    def triple_at(self, i):
        return self.__triples[i]
    
    def contains(self, t):
        return t in self.__triples
    
    def triples(self):
        return self.__triples
    
    def find(self, s, p, o, ctu):
        # print("find - ", s, p, o)
        
        for t in self.__triples:
            # if state.stop: break
            if (t.s == s) and (t.p == p) and (t.o == o):
                # print("t -", t)
                ctu(t.s, t.p, t.o)
        
        # needle = pd.Series([ True ] * len(self.df))
        # if s is not None:
        #     needle &= self.df['s']==s.idx_val()
        # if p is not None:
        #     needle &= self.df['p']==p.idx_val()
        # if o is not None:
        #     needle &= self.df['o']==o.idx_val()
        
        # # print("needle:", needle)
        # for t in self.df.loc[needle, 't']:
        #     # if state.stop: break
        #     # print("t -", t)
        #     ctu(t.s, t.p, t.o)
    
    def __hash__(self):
        return hash(self.__triples)
    
    def __eq__(self, other):
        if not isinstance(other, Model):
            return False # NotImplemented
        return self.__triples == other.__triples
    
    def __str__(self):
        return "\n".join([ str(t) for t in self.__triples ])
    def __repr__(self):
        return self.__str__()