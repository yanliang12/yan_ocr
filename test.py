
#############test.py##########
import easyocr

print('chinese example')
reader = easyocr.Reader(['ch_sim','en']) 
o = reader.readtext('chinese_ocr.jpeg')
for r in o:
	print(r)

print('arabic example')
reader = easyocr.Reader(['ar','en']) 
o = reader.readtext('arabic_road_sign.jpg')
for r in o:
	print(r)
#############test.py##########
