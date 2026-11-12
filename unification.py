def is_variable(term):
  return isinstance(term, str) and term.islower()

def occurs_check(var, term, subst):
  if var == term:
    return True
  elif is_variable(term) and term in subst:
    return occurs_check(var, subst[term], subst)
  elif isinstance(term, (tuple, list)):
    return any(occurs_check(var, subterm, subst) for subterm in term)
  return False

def unify_var(var, x, subst):
  if var in subst:
    return unify(subst[var], x, subst)
  elif is_variable(x) and x in subst:
    return unify(var, subst[x], subst)
  elif occurs_check(var, x, subst):
    return None
  else:
    new_subst = subst.copy()
    new_subst[var] = x
    return new_subst

def unify(x, y, subst=None):
  if subst is None:
    subst = {}
  if x == y:
    return subst
  elif is_variable(x):
    return unify_var(x, y, subst)
  elif is_variable(y):
    return unify_var(y, x, subst)
  elif isinstance(x, (tuple, list)) and isinstance(y, (tuple, list)):
    if len(x) != len(y):
      return None
    for x_elem, y_elem in zip(x, y):
      subst = unify(x_elem, y_elem, subst)
      if subst is None:
        return None
    return subst
  return None
if __name__ == "__main__":
  expr1 = ("Knows", "John", "x")
  expr2 = ("Knows", "y", "Elizabeth")
  print("Test 1:", unify(expr1, expr2))
    
  expr3 = ("Knows", "John", "x")
  expr4 = ("Knows", "y", ("Mother", "y"))
  print("Test 2:", unify(expr3, expr4))
    
  expr5 = ("Knows", "x", "x")
  expr6 = ("Knows", "y", ("Mother", "y"))
  print("Test 3:", unify(expr5, expr6))
