import easyocr
reader = easyocr.Reader(['ch_sim','en']) 
print(reader.readtext('chinese_ocr.jpeg'))
