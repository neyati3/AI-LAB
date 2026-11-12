def is_variable(x):
    return x[0].islower()

def unify(x, y, subst):
    if x in subst:
        x = subst[x]
    if y in subst:
        y = subst[y]
        
    if x == y:
        return True
        
    if is_variable(x):
        if x in y:
            return False
        subst[x] = y
        return True
        
    if is_variable(y):
        if y in x:
            return False
        subst[y] = x
        return True
        
    return False

def main():
    p1 = input("Enter first predicate: ")
    p2 = input("Enter second predicate: ")
    
    name1 = p1[:p1.index("(")]
    name2 = p2[:p2.index("(")]
    
    a = p1[p1.index("(")+1 : p1.index(")")].split(",")
    b = p2[p2.index("(")+1 : p2.index(")")].split(",")
    
    if name1 != name2 or len(a) != len(b):
        print("FAILURE")
        return
        
    subst = {}
    for i in range(len(a)):
        if not unify(a[i].strip(), b[i].strip(), subst):
            print("FAILURE")
            return
            
    if len(subst) == 0:
        print("NIL")
    else:
        print("Substitution:", subst)

main()
