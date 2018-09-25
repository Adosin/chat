
def read_file(filename): # 投幣口
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		# utf-8 產生中文字
		# utf-8-sig 文字前引的 \ufeff 隱藏
		for line in f:
			lines.append(line.strip())
			# strip() 隱藏 \n 換行符號
	return lines

def convert(lines): # 投幣口改為內容清單
	new = [] 
	person = None # 宣告 person，預設值是無
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue 
		elif line == 'Tom':
			person = 'Tom'
			continue

		if person: # 沒有被設值，執行下一段
			new.append(person + ': ' + line) 
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main(): 
	lines = read_file('input.txt') # 投幣口名稱
	lines = convert(lines)  # 把 lines 內容,投入 convert
	write_file('output.txt', lines) 

main()  # 程式的進入點 