import base64

chars = '126 062 126 163 142 103 102 153 142 062 065 154 111 121 157 113 122 155 170 150 132 172 157 147 123 126 144 067 124 152 102 146 115 107 065 154 130 062 116 150 142 154 071 172 144 104 102 167 130 063 153 167 144 130 060 113 012'
chars = chars.split(' ')
flag = ''
for i in chars:
	flag += chr(int(i,8))

print base64.b64decode(flag)