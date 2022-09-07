from paddleocr import PaddleOCR,draw_ocr
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False) # need to run only once to download and load model into memory
img_path = './OCR_temp.png'
result = ocr.ocr(img_path, cls=True)
word_infos = []
for i, line in enumerate(result):
	word_info = {}
	#get the top-left and bottom right corner
	if line[1][1] > 0.75:
		word_info['boundingBox'] = [line[0][0][0], line[0][0][1], line[0][1][0], line[0][1][1], line[0][2][0], line[0][2][1], line[0][3][0], line[0][3][1]]
		word_info['text'] = line[1][0]
		word_infos.append(word_info)
print(word_infos)
