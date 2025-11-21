def split_before_uppercases(formula):
    end = 1
    start = 0
    split_formula = []
    if formula != "":
        for i in range(1,len(formula)):
            if formula[i].isupper():
                end = i
                split_formula.append(formula[start:end])
                start = i
        split_formula.append(formula[start:len(formula)])
        return split_formula
    else:
        return []

def split_at_digit(formula):
    digit_location = None
    for i in range(len(formula)):
      if formula[i].isdigit() == True:
            digit_location = i
            break
  
    if digit_location is None:
      return formula, 1
    else:
      prefix = formula[:digit_location]
      numeric = int(formula[digit_location:])
      return prefix,numeric

def count_atoms_in_molecule(formula):
    atoms = {}
    parts = split_before_uppercases(formula)
    for i in range(len(parts)):
      prefix , num = split_at_digit(parts[i])
      if prefix in atoms:
        atoms[prefix] += num
      else:
        atoms[prefix] = num
    return atoms
