'''
Adjust the run speed based on the 'boosted' option as well as the angle 
(so you can do fun loop-the-loops)
'''

def main(cont):
	# the normal speed for running
	BASE_SPEED = 3.0
	ANGLE_SPEED = 0.8 # 1.0 would run double BASE_SPEED when frank is upside down. this is probably too fast.
	
	# When frank collects boost's, he runs faster
	BOOSTED_FAC = 2.0
	BOOSTED_TIME = 10
	
	own = cont.owner
	
	# Z will be between 0 and 1.0
	Z = 1-((own.getAxisVect((0.0, 0.0, 1.0))[2] + 1.0) * 0.5)
	
	run_actu = cont.actuators['run_force']
	
	if own['boosted'] < 0.0:
		speed = BASE_SPEED*2
		#print "The Power is ON!"
	else:
		speed = BASE_SPEED
		#print "The Power is OFF!"
	
	speed += (BASE_SPEED*Z*ANGLE_SPEED)	
	
	run_actu.linV = (0.0, speed, 0.0) # local linv

