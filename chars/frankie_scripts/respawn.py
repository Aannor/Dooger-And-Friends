'''
This script restores frankie to his original location
restores properties and updates the hud.
'''
import GameLogic

def main(cont):
	own = cont.owner
	
	# If somthing is carrying us. tell it to not bother anymore.
	parent = own.parent
	if parent:
		if 'carrying' in parent:
			parent['carrying'] = 0
		else:
			print '\twarning, parented to a non "carrying" object. should never happen'
		
		own.removeParent()
	
	own.restoreDynamics() # only needed for reviving from lava
	
	own.localPosition = [float(num) for num in own['orig_pos'].split()]
	own.setLinearVelocity((0.0, 0.0, 0.0), True)
	
	props = GameLogic.globalDict['PROP_BACKUP'][own['id']]
	
	# We backed these up, see frank_init
	for prop, value in props.iteritems():
		own[prop] = value
	
	# Update the HUD
	hud_dict = GameLogic.globalDict['HUD']
	if own['id'] == 0:	hud_dict['life_p1'] = own['life']
	else:				hud_dict['life_p2'] = own['life']
	
