li_a = list()
for band in range(4):
	li_values = list()
	a = (band+1)
	li_a.append(a)
	ar_a = np.array(li_a).astype(np.uint16)
	for feat in range(5):
		b = ar_a*(feat+1)
		c= b.tolist()
		li_values.append(c)

		ar_values = np.array(li_values).astype(np.uint16)
