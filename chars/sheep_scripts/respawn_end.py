import GameLogic

def main(cont):
	own = cont.owner
	
	# be careful here, whatever is our parent should probably be told we're detaching.
	# they are not right now.
	own.removeParent()
	
	own.restoreDynamics() # only needed for reviving from lava
	
	if 'carried' in own:
		own['carried'] = 0
	
	own['grounded'] = 0
	own['attack_type'] = ''
	own['life'] = own['lifemax']
	
	if 'projectile_id' in own:
		own['projectile_id'] = -1
	
	own['target_time'] = 0.0
	own['revive_time'] = 0.0
	
	own.setLinearVelocity((0.0, 0.0, 0.0), 1)
	own.localPosition = (own['x_orig'], own['y_orig'], own['z_orig'])
	# print "respawn"
