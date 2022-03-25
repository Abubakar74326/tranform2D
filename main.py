import transformations

import visualization
print("translation")
a, b = transformations.translation(3, 2, 1, 1)
print ([a,b])

print("scaling new coordinates")
a, b = transformations.scaling(3, 2, 1, 1)
print([a,b])

print("rotation new coordinates ")
a,b =transformations.rotation(2,4,30)
print(a,b)



print("shearing new x coordinates")
a = transformations.sheringX(3,2,1)
print(a)
print("shearing new y coordinates")
b = transformations.sheringY(3,2,1)
print(b)

