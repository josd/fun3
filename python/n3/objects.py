from enum import Enum
from n3.model import Model
# from n3.ns import NS

class Terms(Enum):
    IRI = 1
    LITERAL = 2
    COLLECTION = 3
    GRAPH = 4
    VAR = 5
    BNODE = 6
    ANY = 7

    
class Node:
    
    def is_any(self):
        return False

    # implemented by subclasses
    
    # NOTE: meant to support the semantics of unification
    # def __eq__(self, other):  
    #     pass
    
    # NOTE: use this value to index term for retrieval
    # def idx_val(self):
    #     pass

class Any(Node):
    
    def type(self):
        return Terms.ANY
    
    def is_any(self):
        return True
    
    def is_concrete(self):
        return False
    
    def is_grounded(self):
        return False
    
    def idx_val(self):
        return self.__str__()
    
    # yes
    
    def __iter__(self):
        return iter([])
    
    def __len__(self):
        return 0
    
    def __getitem__(self, key):
        return self
    
    def __setitem__(self, key, value):
        pass
    
    def __eq__(self, other): 
        return True
        
    def __str__(self):
        return "ANY"
    def __repr__(self):
        return self.__str__()
    
    def copy_deep(self):
        return self
   
    
class ConcreteNode(Node):
    
    def is_concrete(self):
        return True


class Iri(ConcreteNode):

    # iri
    
    def __init__(self, iri):
        self.iri = iri
        
    def type(self):
        return Terms.IRI
    
    def is_grounded(self):
        return True
    
    def idx_val(self):
        return self.iri
    
    @staticmethod
    def get_ns(iri):
        return iri[0:Iri.__sep_idx(iri)+1]
    
    @staticmethod
    def get_ln(iri):
        return iri[Iri.__sep_idx(iri)+1:]
    
    @staticmethod
    def __sep_idx(iri):
        return iri.rfind('#') if '#' in iri else iri.rfind('/')
    
    def __getattr__(self, name):
        match name:
            case 'ns': return Iri.get_ns(self.iri)
            case 'ln': return Iri.get_ln(self.iri)
            case _: raise AttributeError(f"unknown attribute: {name}")
            
    def __eq__(self, other):  
        if other.type()==Terms.VAR or other.is_any():
            return True
        if not isinstance(other, Iri):
            return False # NotImplemented
        return self.iri == other.iri
        
    def __str__(self):
        # if NS.has(self.ns):
        #     return f"{NS.get(self.ns).name}:{self.ln}"
        # else:
        return f"<{self.iri}>"
    def __repr__(self):
        return self.__str__()
    
    def copy_deep(self):
        return self
        
        
class Literal(ConcreteNode):
    
    def __init__(self, value, dt, lng=None):
        self.value = value
        self.dt = dt
        self.lng = lng
        
    def type(self):
        return Terms.LITERAL
    
    def is_grounded(self):
        return True
    
    def idx_val(self):
        return self.value
        
    def __eq__(self, other):
        if other.type()==Terms.VAR or other.is_any():
            return True
        if not isinstance(other, Literal):
            return False # NotImplemented
        return self.value == other.value
        
    def __str__(self):
        value = self.value; suffix = None
        if isinstance(self.value, str):
            quote = "\"" if "\n" not in self.value else "\"\"\""
            value = quote + value + quote
            if self.lng is not None:
                suffix = f"@{self.lng}"
            elif self.dt is not None and self.dt != Iri("http://www.w3.org/2001/XMLSchema#string"):
                suffix = f"^^{self.dt}"
        return str(value) + (suffix if suffix is not None else "")
    def __repr__(self):
        return self.__str__()
    
    def copy_deep(self):
        return self


class VariableNode(Node):
    
    # id
            
    def is_concrete(self):
        return False

    def is_grounded(self):
        return False
    

class Var(VariableNode):
    
    def __init__(self, name):
        self.name = name
                
    def type(self):
        return Terms.VAR    
    
    def idx_val(self):
        return self.name
        
    def __eq__(self, other):  
        return True
        
    def __str__(self):
        return f"?{self.name}"
    def __repr__(self):
        return self.__str__()
    
    def __getattr__(self, name):
        match name:
            case 'var_id': return self.name
    
    def copy_deep(self):
        return self
    

class BlankNode(VariableNode):
        
    cnt = 0
        
    def __init__(self, label=None):
        if label is None:
            # self.label = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            self.label = f"b{BlankNode.cnt}"
            BlankNode.cnt += 1
        else:
            self.label = label
        
    def type(self):
        return Terms.BNODE
    
    def idx_val(self):
        return self.label
    
    # needed for unification
    # (blank node only matches var nodes)
    def __eq__(self, other):
        return not other.is_concrete()
        
    def __str__(self):
        return f"_:{self.label}"
    def __repr__(self):
        return self.__str__()
    
    def __getattr__(self, name):
        match name:
            case 'var_id': return self.label
    
    def copy_deep(self):
        return self
    
    
class Container(ConcreteNode):
    
    # (implemented by subclasses)
    def _iter_recur_atomics(self, pos):
        """
        Recursively yields all (nested) atomic elements in the container.
        The function calls _iter_atomic for each element in the container, which:
        - If the element is itself a collection, calls this function on it recursively
        - Else, returns the element.
        
        Args:
            pos (tuple): series of parent containers of element (here, current object)
                structure:
                    ( ..., ( idx_i, container_i ), ... ): 
                        container_i: a parent container of element
                        idx_i: index of element in container_i
            
        Yields:
            tuple:
                0: pos (tuple)
                1: term: (nested) atomic element
        """
        pass
    
    # (called by subclasses)
    # iterate over the atomic elements of this container
    def _iter_atomic(self, pos, term):
        """
        Utility function for iterating over container elements. Given an element:
        - If the element is itself a collection, call the _iter_recur_atomics function on it recursively
        - Else, return the element.
        
        Args:
            pos (tuple): series of parent containers of element
            term: the container element
        
        Yields:
            tuple:
                0: pos (tuple): series of parent containers of element
                1: term: (nested) atomic element
        """
        match term.type():
            case Terms.COLLECTION: yield from term._iter_recur_atomics(pos)
            case Terms.GRAPH: yield from term._iter_recur_atomics(pos)
            case _: yield (pos, term)
    
    
class VarContainer(Container):
    
    # TODO cache vars once code is fleshed out
    # (see parse.py)
    
    def __init__(self):
        # self.__vars = {}
        pass
        
    def is_grounded(self):
        return len([ v for v in self.recur_vars() ]) == 0
    
    # def _parsed_var(self, var):
    #     self.__vars[var] = True
    
    # def _parsed_vars(self, vars):
    #     self.__vars.update(vars)
    
    def instantiate(self, concr_terms):
        inst = self.copy_deep()
        
        # rules may have returned ANY for one of the variables
        # (if it was not bound in the query)
        for key, term in concr_terms.items():
            if term.is_any():
                concr_terms[key] = BlankNode()
            # ANY's may also be nested in collections or graph terms
            elif isinstance(term, VarContainer):
                term.replace_recur_vars(lambda id: BlankNode(),types=(Terms.ANY,))
        
        inst.replace_recur_vars_map(concr_terms, types=(Terms.VAR,))
        
        return inst
    
    def replace_recur_vars_map(self, repl_map, types=(Terms.VAR,)):
        self.replace_recur_vars(lambda id: repl_map[id], types)
    
    def replace_recur_vars(self, repl_fn, types=(Terms.VAR,)):
        """
            Replaces (nested) variables in this VarContainer.
            
            Args:
                types: the types of variables you're interested in (var, bnode)
                repl_fn (function)
        """
        for pos, term in self._iter_recur_atomics(()):
            if term.type() in types:
                repl = repl_fn(term.var_id)
                # get closest parent container & index of var therein
                parent = pos[-1][1]; i = pos[-1][0]
                # replace with new term
                parent[i] = repl
    
    def vars(self, types=(Terms.VAR,), get_id=True):
        """
        Returns a list of all non-nested variables in this VarContainer.
        
        Args:
            types: the types of variables you're interested in (var, bnode)
            get_id: whether we are interested in var names or the vars themselves.
            
        Returns:
            list:
                0: index of var in triple
                1: non-nested var or its name
        """
        
        return [ v.var_id if get_id else (i, v) for i, v in enumerate(self) if v.type() in types ]     
       
    def recur_vars(self, types=(Terms.VAR,), get_id=True):
        """
        Returns a list of all (nested) variables in this VarContainer. 
        
        Args:
            types: the types of variables you're interested in (var, bnode)
            get_id: whether we are interested in var names or the vars themselves.
            
        Returns:
            list:
                (nested) var or its name
        """
        
        # return self.__vars
        
        # return [ (v.name if get_id else v) for _, _, v in self._iter_recur_atomics() if v.type() == Terms.VAR ]
        # for _, _, v in self._iter_recur_atomics():
        #     if v.type() == Terms.VAR: yield v
        
        return [ v for _, v in self.__yield_recur_vars(types, get_id) ]
    
    def recur_vars_pos(self, types=(Terms.VAR,), get_id=True):
        """
        Returns a list of all (nested) variables and their positions in this VarContainer. 
        
        Args:
            types: the types of variables you're interested in (var, bnode)
            get_id: whether we are interested in var names or the vars themselves.
            
        Returns:
            list:
                tuple:
                    0: pos (tuple): series of parent containers of element
                    1: (nested) var or its name
        """
        
        return [ (pos, v) for pos, v in self.__yield_recur_vars(types, get_id) ]
    
    def __yield_recur_vars(self, types=(Terms.VAR,), get_id=True):
        """
        Recursively yields all (nested) variables in this VarContainer.
        
        Args:
            types: the types of variables you're interested in (var, bnode)
            get_id: whether we are interested in var names or the vars themselves.
            
        Yields:
            tuple:
                0: pos (tuple): series of parent containers of element
                1: (nested) var or its name
        """
                
        for pos, v in self._iter_recur_atomics(()):
            if v.type() in types: yield (pos, (v.var_id if get_id else v))


class Collection(VarContainer):
    
    # __elements
    
    def __init__(self, elements=None):
        self.__elements = [] if elements is None else elements
    
    def type(self):
        return Terms.COLLECTION
    
    def idx_val(self):
        return self.__to_nested_tuples()
    
    def append(self, coll):
        return Collection(self.__elements + coll.__elements)
    
    def __to_nested_tuples(self):
        return tuple(e.__to_nested_tuples() if e.type() == Terms.COLLECTION else e.idx_val() for e in self.__elements)
    
    def _parsed_el(self, el):
        self.__elements.append(el)
    
    def _iter_recur_atomics(self, pos):
        for i, el in enumerate(self): yield from self._iter_atomic(pos + ((i, self),), el)
    
    def __iter__(self):
        return self.__elements.__iter__()
    
    def __len__(self):
        return len(self.__elements)
    
    def __getitem__(self, key):
        return self.__elements[key]
    
    def __setitem__(self, key, value):
        self.__elements[key] = value
    
    def __eq__(self, other):
        if not other.is_concrete() or other.is_any():
            return True
        if not isinstance(other, Collection):
            return False # NotImplemented
        return self.__elements == other.__elements
        
    def __str__(self):
        if len(self.__elements) == 0:
            return "()"
        else:
            return "( " + " ".join(str(e) for e in self.__elements) + " )"
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other):
        if not isinstance(other, Collection):
            raise NotImplemented
        else:
            return Collection(self.__elements + other.__elements)
    
    def copy_deep(self):
        return Collection([ element.copy_deep() for element in self.__elements ])
    
    
class GraphTerm(VarContainer):
    
    # model
    
    def __init__(self, model=None):
        self.model = model if model is not None else Model()
        
    def type(self):
        return Terms.GRAPH
    
    def _iter_recur_atomics(self, pos):
        for t in self.model.triples(): yield from t._iter_recur_atomics(pos)
        
    def __str__(self):
        return "{ "  + "\n".join([ str(t) for t in self.model.triples() ])[:-2] + " }"
    def __repr__(self):
        return self.__str__()
    
    def copy_deep(self): # TODO
        pass


class Triple(VarContainer):
    
    spo = ['s', 'p','o']
    
    # s, p, o
    
    def __init__(self, s=None, p=None, o=None):
        self.s = s
        self.p = p
        self.o = o
    
    def has_graph(self):
        return any(r.type() == Terms.GRAPH for r in self)
    
    def _iter_recur_atomics(self, pos):
        for i, term in enumerate(self): yield from self._iter_atomic(pos + ((i, self),), term)
    
    def __len__(self):
        return 3
    
    def __iter__(self):
        return TripleIt(self)
    
    def __getitem__(self, key):
        match key:
            case 0: return self.s
            case 1: return self.p
            case 2: return self.o
            case _: print("inconceivable!"); return None
    
    def __setitem__(self, key, value):
        match key:
            case 0: self.s = value
            case 1: self.p = value
            case 2: self.o = value
            case _: print("inconceivable!");
    
    def __str__(self):
        return f"{self.s} {self.p} {self.o} ."
    def __repr__(self):
        return self.__str__()
        
    def copy_shallow(self):
        return Triple(self.s, self.p, self.o)
    
    def copy_deep(self):
        return Triple(self.s.copy_deep(), self.p.copy_deep(), self.o.copy_deep())
    
    
class TripleIt:
    
    def __init__(self, t):
        self.__t = t
        self.__cnt = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        cnt = self.__cnt
        self.__cnt += 1
        
        match cnt:
            case 0: return self.__t.s
            case 1: return self.__t.p
            case 2: return self.__t.o
            case _: raise StopIteration
            
ANY = Any()