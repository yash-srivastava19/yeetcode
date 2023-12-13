## Update : More things and extra sassy things will be added later. Open a PR and we'll discuss.

def _dec(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return res
    return wrapper

CAP = False
NO_CAP = True

@_dec
def hype_check(x, *args, **kwargs):
    return abs(x)

@_dec
def squad_goals(iterable, *args, **kwargs):
    return all(iterable)

@_dec
def levels(stop, *args, **kwargs):
    return range(stop)

@_dec
def spill_the_tea(prompt, *args, **kwargs):
    return input(prompt, *args, **kwargs)

@_dec
def show_dat(mes, *args, **kwargs):
    print(mes, *args, **kwargs)

@_dec
def lowkey(iterable, *args, **kwargs):
    return min(iterable)

@_dec
def peak(iterable, *args, **kwargs):
    return max(iterable)

@_dec
def stacks(iterable, *args, **kwargs):
    return sum(iterable, *args, **kwargs)

@_dec
def welp(request,*args, **kwargs):
    help(request, *args, **kwargs)

@_dec
def ded(object, name):
    delattr(object, name)

@_dec
def vibe_check(x, *args, **kwargs):
    return type(x)

@_dec
def roll_call(iterable,*args, **kwargs):
    return enumerate(iterable)
