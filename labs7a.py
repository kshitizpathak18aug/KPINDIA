import random
snakes={11:2,25:4,38:9,65:46,89:70,93:64}
ladder={8:37,13:34,40:68,52:81,76:97}
p=0
while True:
	r=random.randint(1,6)
	p=r
	if(p in snakes):
		p=snakes[p]

	if(p in ladder):
		p=ladder[p]
		