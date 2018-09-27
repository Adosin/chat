
def read_file(filename): # 投幣口
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:	
	#  utf-8 產生中文字。 utf-8-sig 文字前引的 \ufeff 隱藏
		for line in f:
			lines.append(line.strip())
			# strip() 隱藏 \n 換行符號
	return lines

def convert(lines): # 投幣口改為內容清單
	person = None # 宣告 person，預設值是無
	Viki_word_count = 0
	Allen_word_count = 0
	for line in lines:
		s = line.split(' ') # 遇到空白鍵，做切割
		time = s[0]
		name = s[1] 
		if name == 'Viki':
			for msg in s[2:]: # 跳過time(陣列0) - name(陣列1) 從陣列2開始
				Viki_word_count += len(msg)
		elif name == 'Allen':
			for msg in s[2:]: # 跳過time(陣列0) - name(陣列1) 從陣列2開始
				Allen_word_count += len(msg)

	print('Viki 說了', Viki_word_count)
	print('Allen 說了', Allen_word_count)

	

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main(): 
	lines = read_file('LINE-Viki.txt') # 投幣口名稱
	lines = convert(lines)  # 把 lines 內容,投入 convert
	# write_file('output.txt', lines) 


main()  # 程式的進入點 
