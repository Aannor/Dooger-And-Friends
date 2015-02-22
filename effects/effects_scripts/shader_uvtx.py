MaterialIndexList = [0,1]

VertexShader = """
varying vec2 Texcoord;
void main( void )
{
    gl_Position = ftransform();
    Texcoord    = gl_MultiTexCoord0.xy;
    
}
"""

FragmentShader = """
uniform sampler2D Texture1;
uniform float time;

varying vec2 Texcoord;
void main( void )
{
vec4 noise = texture2D( Texture1,Texcoord);
vec2     T1=  Texcoord+vec2(1.5,-1.5)*time*0.02;
vec2     T2=  Texcoord+vec2(0.1,-1.0)*time*1.0;
T1.x+=(noise.x)*0.0;
T1.y+=(noise.y)*0.0;
T2.x-=(noise.y)*0.0;
T2.y+=(noise.z)*0.0;
float p=  texture2D( Texture1,T1*1.0).a;  
vec4 color =  texture2D( Texture1, T2*1.0); 
vec4 temp= color*(vec4(p,p,p,p)*0.7)+(color*color-0.0);
if(temp.r > 1.0){temp.bg+=clamp(temp.r-0.9,0.0,100.0);}
if(temp.g > 1.0){temp.rb+=temp.g-1.0;}
if(temp.b > 1.0){temp.rg+=temp.b-1.0;}
    gl_FragColor = temp;
}
"""


def main(cont):
	own = cont.owner
	
	time = own['time']
	meshes = own.meshes

	for mesh in meshes:

		for mat in mesh.materials:
			# only GLSL
			try:
				mat_index = mat.getMaterialIndex()
			except:
				return

			# find an index				
			found = 0
			for i in xrange(len(MaterialIndexList)):
				if mat_index == MaterialIndexList[i]:
					found=1
					break
			if not found: continue

			shader = mat.getShader()
			if shader != None:
				if not shader.isValid():
					shader.setSource(VertexShader, FragmentShader,1)
				shader.setUniform1f('time', time)
				shader.setSampler('Texture1', 0)
