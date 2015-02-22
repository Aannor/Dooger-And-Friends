'''
Similar to respawning, restore most properties and move back to a previous position
'''
import GameLogic
def restoreProps(own):
	# We could reset others but these are likely to cause problems
	PROPS = GameLogic.globalDict['PROP_BACKUP'][own['id']]
	# We backed these up, see frank_init
	# Only backup "life" and inventory -> "item_*"
	
	for propName in own.getPropertyNames():
		
		# IF 1: dont change our inventory
		# IF 2: dont change our life
		# IF 3: keep this incase we fall in the water soon after.
		if propName.startswith('item_') or \
		   propName == 'life' or \
		   propName.startswith('ground_pos'):	
		
			pass # Keep these props
		else:
			try:		own[propName] = PROPS[propName]
			except:	print '\trestore prop :', propName, 'did not work'
	
def main(cont):
	own = cont.owner
	
	# turn off timeoffset, almost
	own_rig = cont.sensors['rig_linkonly'].owner # The rig owns this! - cheating way ti get the rig/
	own_rig.timeOffset = own_rig['defTimeOffset']
	
	last_pos = own['ground_pos_old']
	if last_pos: # this may be false if we just started
		own.localPosition = [float(num) for num in last_pos.split()]
	else: # fallback
		own.localPosition = [float(num) for num in own['orig_pos'].split()]
	
	restoreProps(own)
	

