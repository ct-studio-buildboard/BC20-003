import math

def get_donut_lines(pct_list, inner_radius=98, outer_radius=126):

	lines = []
	pct_subtotal = 0
	prev_label_y = 0
	for p in pct_list:
		pct_subtotal += p

		x_base = math.cos(math.pi/2 - pct_subtotal*math.pi)
		y_base = -math.sin(math.pi/2 - pct_subtotal*math.pi)

		a = [inner_radius*x_base, inner_radius*y_base]

		label_y = outer_radius*y_base
		if abs(label_y - prev_label_y) < 25:
			label_y = prev_label_y - 25
		prev_label_y = label_y

		b = [outer_radius*x_base, label_y]
		if pct_subtotal > math.pi:
			c = [outer_radius, label_y]
		else:
			c = [-outer_radius, label_y]

		lines.append([a, b, c])

		pct_subtotal += p

	return lines

print(get_donut_lines([0.85, 0.14, 0.01]))


