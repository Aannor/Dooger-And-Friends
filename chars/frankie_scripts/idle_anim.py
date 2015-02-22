'''
Play an actuator randomly
this runs in its own state and is disabled when frankie does anything
'''
import GameLogic
from Mathutils import Rand
def main(cont):
	own = cont.owner
	
	# Positive pulse happens on entering the state,
	# In this case the timer is not set so ignore it.
	if cont.sensors['generic_true_pulse'].positive:
		return
	
	actu_list = cont.actuators
	
	i = int(Rand(0,1) * len(actu_list))
	
	if i >= len(actu_list):
		i = len(actu_list) - 1 # unlikely but possible?
	
	for ii, actu in enumerate(actu_list):
		
		if ii==i:	cont.activate(actu)
		else:		cont.deactivate(actu)
		
