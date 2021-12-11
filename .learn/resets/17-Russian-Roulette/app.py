import random

bullet_position = 1

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
	global bullet_position
	x = spin_chamber()

	if x == bullet_position:
		return 'You are dead!'
	else:
		bullet_position=bullet_position+1
		return 'Keep playing!'


print(fire_gun())