# examples.py

def run():
    # Aliasing
    a = [1, 2]
    b = a

    alias_state = {"a": a, "b": b}

    def alias_mutate():
        a.append(99)

    # Nested Mutability 
    t = ([1, 2], [3, 4])
    inner = t[0]

    nested_state = {"t": t, "inner": inner}

    def nested_mutate():
        inner.append(88)

    return {
        "aliasing": (alias_state, alias_mutate),
        "nested_mutability": (nested_state, nested_mutate)
    }
