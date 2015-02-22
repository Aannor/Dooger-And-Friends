'''
whenever the "hit" property changes
deal with adjustring the life, changing to dead state and updating the HUD

we dont need to know why the hit propert changes, this can be done by touching a kill property or
some other character attacking us could do this.
'''
import GameLogic

def main(cont):
	
	own = cont.owner
	
	# See frank_stat_hit, this sets the hit property that triggers this script
	hit = own['hit']
	
	if hit == 0 or own['revive_time'] < 1.0:
		return
	
	own['hit'] = 0
	
	own['life']= max(0, own['life'] - hit)
	own['revive_time']= 0.0
		
	# Update the HUD
	hud_dict = GameLogic.globalDict['HUD']
	if own['id'] == 0:	hud_dict['life_p1'] = own['life']
	else:			hud_dict['life_p2'] = own['life']
	cont.activate('send_healthchange') # send message to hud telling it to update health

	# are we dead?
	if own['life'] == 0:
		cont.activate('dead_state')
		return
	
	# Play Hit Anim
	if own['carrying']:
		cont.deactivate('hit')
		cont.activate('hit_carry')
	else:
		cont.deactivate('hit_carry')
		cont.activate('hit')
	
	# Always flash color
	cont.activate('hit_flashred')
