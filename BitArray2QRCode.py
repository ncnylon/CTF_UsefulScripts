import sys
import io
from PIL import Image, ImageDraw

file_path = './flag.txt'
data = []

with open(file_path, 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		line = line[0:len(line)-1] # remove last char
		data.append(line)
		
#print(data)
scale = 8
w,h = (len(data),len(data[0]))
qr_img = Image.new('RGB',(w*scale,h*scale),'red')
qr_draw = ImageDraw.Draw(qr_img)
black_color = (0,0,0)
white_color = (255,255,255)

for i in range(0, w):
	for j in range(0, h):
		pixel = white_color if data[i][j] == '1' else black_color
		
		# fill all adjacents
		for x in range(scale):
			for y in range(scale):
				qr_draw.point((i*scale+x,j*scale+y),fill=pixel)
		
fmt = 'png'
qr_img.save('qr_code.'+fmt,format=fmt)