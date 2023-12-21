"""
Equal:              ==
Not Equal:          !=
Grater Than:        >
Less Than:          <
Greater or Equal:   >=
Less or Equal:      <=
Object Identity:    is
"""
a = [1, 2, 3]
b = [1, 2, 3]

print("is a == b?", a == b)

print("id(a):", id(a))
print("id(b):", id(b))
print("a is b - behind the scene, it is comparing id(a) == id(b)?", a is b)

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. i.e., '', (), []
# Any empty mapping. i.e., {}.

condition = {}
if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
