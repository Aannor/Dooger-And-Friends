# This file has almost an exact copy in sheep.blend - sheep_sense_hit
'''
Run when we touch a kill or projectile object,
this sets own.hit which the 'frank_health' script then deals with.
'''
import GameLogic

def main(cont):
	PROJECTILE_SPEED = 5.0
	
	own = cont.owner
	
	HIT_PLAYED = False
	try:	actu_hit = cont.actuators['sfx_hit']
	except:	HIT_PLAYED = True
	
	
	#sens = cont.sensors['projectile_touch']
	for sens in cont.sensors:
		hit_ob = sens.hitObject
		if not hit_ob:
			continue
		
		if ('projectile' in hit_ob) and hit_ob['projectile_id'] != own['id']:
			s = hit_ob.getLinearVelocity()
			s = s[0]*s[0] + s[1]*s[1] + s[2]*s[2]
			# print 'hit_speed', s
			# Is this going to hit us???
			if s > PROJECTILE_SPEED:
				if 'kill' in hit_ob:
					own['hit'] = max(hit_ob['kill'], own['hit'])
				else:
					own['hit'] = max(1, own['hit'])
						
		elif 'kill' in hit_ob:
			own['hit'] = max(hit_ob['kill'], own['hit'])
			
			# Play the hit sound if we havnt played it and if its not liquid
			if HIT_PLAYED == False and ('liquid' not in hit_ob):
				cont.activate(actu_hit)
