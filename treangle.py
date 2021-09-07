a, b, c = map(int, iput().split())
if a == 0 and b == 0 and c == 0:
	print("besk resh")
else:
	if ((b) ** 2 - 4*a*c) <= 0:
		print("resh net")
	else:
		if b == 0:
			x1 = (c*(-1) / a) ** 0.5
			x2 = -1 * x1
			print(x1, x2)
		else:
			if a == 0:	
				x1 = (c * (-1)) / b
				print(x1)
			else:
				if c == 0:
					x1 = 0
					x2 = ((b*(-1)) / a)
					print(x1, x2)
				else:
					d = (b) ** 2 - 4*a*c
					if d == 0:
						x1 = (b * (-1)) / (2*a)
						print(x1)
					else:
						x1 = (b * (-1) + d ** 0.5) / (2*a)
						x2 = (b * (-1) - d ** 0.5) / (2*a)
						print(x1, x2)
