#从左往右

class cs1:
    cs = 'cs1'

class cs2:
    cs = 'cs2'

class cs(cs1,cs2):
    pass

cs = cs()
print(cs.cs)
