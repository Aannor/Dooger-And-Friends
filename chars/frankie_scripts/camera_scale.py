'''
Scale the cameras parent when there is an object infront of the camera
'''

def main(cont):
	MAX = 4.0
	MIN = 0.6
	THRESH = 0.6 # Ignore anything under this distance, frankie is probably carrying somthing.
	
	own = cont.owner
	
	# For sone annoying reason this happens when the scene is initialized
	sens_wall = cont.sensors['camera_ray']
	
	ob = sens_wall.hitObject
	#if ob:	print '\tcamera: rayhit object -', ob.name
	
	sorig = own.localScale[0] # assume uniform scale
	
	if not ob:
		scale = MAX # 1.0
	else:
		
		carry_obstructor = False
		# incase we are carrying an object, see if its logic 
		parent = ob.parent
		while parent:
			ob = parent
			parent = ob.parent
			
			if ob.get('carried', 0) != 0:
				carry_obstructor = True
				break
		
		if carry_obstructor:
			scale = MAX # this is not quite correct, we should really shoot another ray incase there is an obstructor
		else:
			scale = own.getDistanceTo(sens_wall.hitPosition)
			
			if scale < THRESH: scale = sorig
			elif scale > MAX: scale = MAX
			elif scale < MIN: scale = MIN
	
	# Let slow parent deal with interpolation
	own.localScale = [scale,scale,scale]

