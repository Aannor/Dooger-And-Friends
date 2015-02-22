'''
This script records franks location periodically 
when he is on the ground.

Use this when restoring his position from the water
'''

def main(cont):
	own = cont.owner
	
	# Not especially efficient but we only run this every 2 sec or so
	if own['grounded']:
		# to be sure we never use ground position a milisecond before falling	
		# keep 2 and and push the recent one back.
		own['ground_pos_old'] = own['ground_pos']
		own['ground_pos'] = '%.3f %.3f %.3f' % tuple(own.worldPosition)
