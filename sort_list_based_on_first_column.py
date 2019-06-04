xs = [1467153, 1466231, 1478821]
ys = [12309, 21300, 10230]
l = sorted(zip(xs, ys), key=lambda x: x[0])
print(l)

#you can also change zip(xs,ys) into an existing list