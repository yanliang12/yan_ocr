############yan_ocr.py##########
import numpy
import easyocr
from PIL import Image, ImageDraw, ImageFont

fnt = ImageFont.truetype("MuseoSans_500.otf", 40)
reader_en = easyocr.Reader(['en']) 

def extract_text(
	image_path,
	output_image_path):
	o = reader_en.readtext(image_path)
	output = [{"text": r[1], "score": r[2], 
		"coordinate": [list(p) for p in numpy.array(r[0]).astype(int)]}
		for r in o]
	if output_image_path is not None:
		im = Image.open(image_path)
		draw = ImageDraw.Draw(im)
		for r in o:
			text = r[1]
			score = r[2]
			post = [tuple(p) for p in r[0]]
			line1 = post[0]+post[1]
			line2 = post[1]+post[2]
			line3 = post[2]+post[3]
			line4 = post[3]+post[0]
			draw.line(line1, fill=128, width = 5)
			draw.line(line2, fill=128, width = 5)
			draw.line(line3, fill=128, width = 5)
			draw.line(line4, fill=128, width = 5)
			#draw.text(post[3], text)
			try:
				draw.text(post[3], text, font = fnt) #
			except:
				pass 
			coordinate = [list(p) for p in r[0]]
		im.save(output_image_path)
	return output
############yan_ocr.py##########
