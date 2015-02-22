import GameLogic

def main(cont):
	own = cont.owner
	
	if own['type'] == 'shp':
		return
	
	sens_attack = cont.sensors['predator_collide']
	
	predator_ob = sens_attack.hitObject
	
	if not predator_ob:
		return
	
	if not ('hit' in predator_ob and predator_ob.has_key('life')):
		print '\tattack: predator missing "hit" or "life" property'
		return
	
	if predator_ob['life'] <= 0:
		# print '\tattack: predator alredy dead'
		return
	
	# face the predator, this is always activated
	# so we only need to spesify what to track to.
	actu_track = cont.actuators['track_predator']
	actu_track.object = predator_ob
	
	# Dont track, until we enter the state, only set the track ob
	# since the state does the tracking
	
	# Change to attacking state
	cont.activate('predator_attack_state')
