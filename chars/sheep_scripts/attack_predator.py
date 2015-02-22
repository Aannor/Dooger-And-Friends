import GameLogic

HIT_MAXDIST = 0.8

def main(cont):
	own = cont.owner
	
	actu_track = cont.actuators['track_predator']
	predator_ob = actu_track.object # 0 is so we get the object, not the name
	
	if not predator_ob:
		# print "the predator must have been removed"
		return
		
	# Who are we attacking?
	
	# print predator_ob, type(predator_ob)
	'''
	# See what state of the animation 
	sens_attack_time = cont.sensors['action_frame_hit']
	
	# 
	if not sens_attack_time.positive:
		print 'Cant hit yet!'
		return
	'''
	
	# Frankie may have escaped! see if we can still get him
	predator_dist = own.getDistanceTo(predator_ob)
	if predator_dist < HIT_MAXDIST:
		# print "Hitting frabnkie", predator_ob.name, predator_dist
		predator_ob['hit'] = 1
	#else:
	#	print 'frankie got away at!', predator_dist
	
	actu_track.object = None # stop tracking the predator
