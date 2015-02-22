# this script is applied to one empty,
# using multiple collision sensors on water surfaces to detect the splash
# the empty will be moved to the collision location and instantly add the object
# this needs to be done because groups cant be moved once added by addObject actuators.

# Warning, this module must be reloaded between scenes of the objects will become invalid
import GameLogic

SPLASH_LS = [None, None, None, None]

def splash_init():
	sce = GameLogic.getCurrentScene()
	SPLASH_LS[0] = sce
	try:		SPLASH_LS[1] = sce.objectsInactive['OBfx_splash']
	except:	SPLASH_LS[1] = None
	
	try:		SPLASH_LS[2] = sce.objectsInactive['OBfx_splash_small']
	except:	SPLASH_LS[2] = None
	
	try:		SPLASH_LS[3] = sce.objectsInactive['OBfx_lava_splash']
	except:	SPLASH_LS[3] = None

def main(cont):
	own= cont.owner
	
	sce = SPLASH_LS[0]
	# Incase we switch scenes
	if sce.invalid:
		splash_init()
		sce = SPLASH_LS[0]
	
	is_lava = ('lava' in own)
	
	
	for sens in cont.sensors: # one or more water surface meshes	
		if sens.positive:
			for ob in sens.hitObjectList:
				pos = ob.worldPosition
				
				if is_lava:
					ob_add = SPLASH_LS[3]
				else:
					if 'pickup' in ob:
						ob_add = SPLASH_LS[1]
					else:
						ob_add = SPLASH_LS[2]
				if ob_add:
					sce.addObject(ob_add, ob, 300)
				else:
					print "splash add error, object is not available in this level"
				

# Initialize for the first time
splash_init()
