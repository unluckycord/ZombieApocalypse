attribute vec3 position;
attribute vec4 color;
varying vec4 v_color;
uniform mat4 vp;
uniform float pointSize;
void main()
{
	gl_Position = vp * vec4(position, 1);
	gl_PointSize = pointSize;
	v_color = 0.0039215*color;
}