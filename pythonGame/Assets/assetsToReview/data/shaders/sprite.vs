attribute vec4 position;
attribute vec4 color;

uniform mat4 projMat;

varying vec2 v_texCoord;
varying vec4 v_color;

void main()
{
	gl_Position = projMat * vec4(position.x, position.y, 0, 1);
	v_texCoord = position.zw;
	v_color = color;
}