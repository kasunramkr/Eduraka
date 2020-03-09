import numpy

a = numpy.array([1, 2, 3])
print(a)

b = numpy.arange(1, 100)
print(b)

c = numpy.zeros((5, 5))
print(c)

d = c.ravel()
print(d)

e = c.reshape(5, 5)
print(e)

ar = numpy.array([[1, 2, 3, ], [4, 5, 6], [7, 8, 9]])
print(ar)

print(ar[0:2, 0:2])
