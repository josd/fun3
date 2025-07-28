from pathlib import Path
from ast import dump, unparse, parse
from n3.parse import parse_n3
from n3.objects import ANY
from n3.fun.gen import gen_py, InputData, QueryFn
from n3.fun.utils import unique_sorted

def __proc_inputs(query, rules, data):
    query_str = query.open('r').read() if isinstance(query, Path) else query
    query = parse_n3(query_str).data.triple_at(0)
    
    rules_str = rules.open('r').read() if isinstance(rules, Path) else rules
    rules = parse_n3(rules_str).rules
    
    data = InputData(path=data) if isinstance(data, Path) else InputData(data_str=data)    
    
    # print(query); print(rules); print(data)
    return (query, rules, data)

def run_py(query, rules, data, print_code=False):
    query, rules, data = __proc_inputs(query, rules, data)
    
    mod = gen_py(rules, query, data, call_query=False)
    if print_code:
        print(unparse(mod) + "\n\n")
    
    exec_ret = __get_exec(mod)
    return __exec_query(exec_ret, query)
       
def save_py(query, rules, data, out_path, print_code=False, add_tracing=False, code_dir=False):
    query, rules, data = __proc_inputs(query, rules, data)
    
    mod = gen_py(rules, query, data)
    unparsed = unparse(mod)
    if print_code:
        print(unparsed)
    
    if add_tracing:
        unparsed = __add_tracing(unparsed)
        
    if code_dir:
        unparsed = __use_code_dir(unparsed, code_dir)
    
    with open(out_path, 'w') as fh:
        fh.write(unparsed)
       
def __get_exec(mod):
    mod_code = compile(mod, "<fun3>", "exec")
    
    new_refs = {}
    exec(mod_code, globals(), new_refs)
    
    for name, code in new_refs.items():
        globals()[name] = code
        
    return new_refs

# def __unparse_with_lineno(ast):
#     code = unparse(ast)
#     return "\n".join([ f"{i+1}. {line}" for i, line in enumerate(code.split("\n")) ])

def __exec_query(exec_ret, query):
    fn_name = QueryFn.fn_name()
    variables = unique_sorted(query.recur_vars())
    
    query_fn = exec_ret[fn_name]
    
    out = []
    query_fn(*[ANY for _ in variables], lambda *args: out.append(str(query.instantiate({ var: args[idx] for idx, var in enumerate(variables) }))))
    
    return "\n".join(out)

def __use_code_dir(code, parent_dir):
    return f"""import sys # noqa
sys.path.insert(0, "{parent_dir}") # noqa

""" + code

# assumed that code_dir will point to folder with "lib/trace"
def __add_tracing(code):
    return """from lib.trace import trace_calls # noqa
sys.settrace(trace_calls) # noqa
""" + code