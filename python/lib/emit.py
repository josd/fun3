emitted = set()
def emit(t, inst_dict):
    global emitted
    t = t.instantiate(inst_dict)
            
    if t not in emitted:
        print(t)
        emitted.add(t)
    # else:
    #     print("skipping duplicate")