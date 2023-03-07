def k(y,x): return[
        (y-1,x),
        (y,x-1),
        (y,x+1),
        (y+1,x),
        (y-1,x-1),
        (y-1,x+1),
        (y+1,x-1),
        (y+1,x+1),
]

def n(y,x): return[
        (y+2,x+1),
        (y+2,x-1),
        (y-2,x+1),
        (y-2,x-1),
        (y+1,x+2),
        (y-1,x+2),
        (y+1,x-2),
        (y-1,x-2),
]

def bp(y,x): return[
        (y+1,x),
        (y+2,x),
        (y+1,x-1),
        (y+1,x+1),
]

def wp(y,x): return[
        (y-1,x),
        (y-2,x),
        (y-1,x-1),
        (y-1,x+1),
]
    
straight = [
        lambda y,x,n: (y-n,x),
        lambda y,x,n: (y,x-n),
        lambda y,x,n: (y,x+n),
        lambda y,x,n: (y+n,x),
]

diagnol = [
    
        lambda y,x,n: (y-n,x-n),
        lambda y,x,n: (y-n,x+n),
        lambda y,x,n: (y+n,x-n),
        lambda y,x,n: (y+n,x+n),
]