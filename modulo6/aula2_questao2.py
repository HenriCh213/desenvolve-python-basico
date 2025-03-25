import random, numpy

num_elementos = ""
elementos = []
num_elementos += str(random.randint(5, 20))

for n in range(int(num_elementos)):
    elementos.append(random.randint(1, 10))

print(elementos)
print(sum(elementos))
print(round(numpy.average(elementos), 2))