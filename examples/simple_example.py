"""
Simple test for pickling a lambda.
"""

import pickle

from pickleablelambda import pickleable  # pylint: disable=import-error

print("Define L = lambda x: x+1")
L = lambda x: x+1

print("Execute lambda")
print("L(10)=" + str(L(10)))


print("Try to pickle lambda...")
try:
    with open('lambda.pickle', 'wb') as f:
        pickle.dump(L, f)
except pickle.PicklingError:
    print(".. unfortunately lambdas are not picklable :-(")

print("But if you import pickleablelambda and you wrap L with pickleable...")


with open('lambda.pickle', 'wb') as f:
    pickle.dump(pickleable(L), f)

print("... lambdas are pickleable!")
