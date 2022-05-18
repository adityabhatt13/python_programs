a = {1,2,3,4,5}
b = {4,5,6,7,8}
# # INTERSECTION
# print(a.intersection(b))
# # UNION
# print(a.union(b))
# # DIFFERENCE
# print(a.difference(b))
# print(b.difference(a))
# # SYMMETRIC DIFFERENCE
# print(a.symmetric_difference(b))

# a.intersection_update(b)
# a.difference_update(b)
# a.symmetric_difference_update(b)
# print(a)

# SUBSET
print(a.issubset(b))
c = {1,2}
print(c.issubset(a))
# SUPERSET
print(a.issuperset(c))
# DISJOINT
print(c.isdisjoint(b))
