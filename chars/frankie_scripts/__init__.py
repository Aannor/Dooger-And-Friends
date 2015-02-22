# All frankies scripts

# Initialize game stuff, on the MainCam object
import init
# on the Camera_Scaler object
import camera_scale


# Run, State 3
import run_speed
import run_wall

# Fall, State 4
import fall
import fall_bounce

# Ledge grab, used in multiple states
import ledge_collide
import ledge_hang
# import ledge_test <- used by modules above

# Carry, State 11
import carry_drop

# Health and stats, State 15
import stat_health
import stat_hit
import stat_pickup
import stat_portal
import stat_ground_pos

# Action State 16
import action_all
import action_carry
import action_ground_test

# Others
import idle_anim		# state 8
import glide			# state 19
import respawn			# state 26
import drown_revive	# state 28
