def group_func(fns, args):
    results = ()
    for fn in fns:
        results += (fn(*args),)

    return results
