"""
ʹ��Pillow���ɺ���
"""
from PIL import Image, ImageDraw, ImageFont
import time

header = '001'
title = '��Ұ'
books = ['��Ұ','BINGBIAN����','��Ҳû��']
writes = ['��һ��̤��,�Ҿ�Ҫ��������','˭�����������ҷ��','����Ҳû�ж��������']
summary = 'û��ʲô���µģ���Ҫ����һ�ж���úõġ���ʹ��ܺ��£���ʹ�࣬����ã��Ҳ��Ҫ����ϣ����δ�������Ҹ����㣬�ڵ������ڵ���־���㡣'
n = 18
summary_list = [summary[i:i + n] for i in range(0, len(summary), n)]

# ����ͼ
img = './res/img/2.jpg'
# ���ɵ�ͼƬ
new_img = './res/img/2.png'
# ѹ�����ͼƬ
compress_img = './res/compress.png'

# ����������ʽ
font_type = './res/font/SimHei.ttf'
font_medium_type = './res/font/SimHei.ttf'
header_font = ImageFont.truetype("./res/font/SimHei.ttf", 40, encoding="utf-8")
title_font = ImageFont.truetype("./res/font/SimHei.ttf", 30, encoding="utf-8")
font = ImageFont.truetype(font_type, 24)
color = "#000000"

# ��ͼƬ
image = Image.open(img)
draw = ImageDraw.Draw(image)
width, height = image.size

# headerͷ
header_x = 130
header_y = 690
draw.text((header_x, height - header_y), u'%s' % header, color, header_font)

# ����
title_x = header_x
title_y = header_y - 80
draw.text((title_x, height - title_y), u'%s' % title, color, title_font)

# ��ǰʱ��
cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
cur_time_x = 590
cur_time_y = title_y - 25
cur_time_font = ImageFont.truetype(font_type, 25)
draw.text((cur_time_x, height - cur_time_y), u'%s' % cur_time, color, cur_time_font)

# ����
title_x = header_x
title_y = header_y - 80
draw.text((title_x, height - title_y), u'%s' % title, color, title_font)

# �Ķ�
book_x = title_x + 5
book_start_y = title_y - 190
book_y = 0
book_line = 50
for num, book in enumerate(books):
    y = book_start_y - num * book_line
    book_num = num + 1
    draw.text((book_x, height - y), u'%s, %s' % (book_num, book), color, font)

# д��
write_x = book_x
write_y = title_y - 450
write_line = 40
for num, write in enumerate(writes):
    write_num = num  + 1
    y = write_y - num * write_line
    draw.text((write_x, height - y), u'%s, %s' % (write_num, write), color, font)

# ��˼
summary_x = book_x + 300
summary_y = book_start_y
summary_line = 35
for num, summary in enumerate(summary_list):
    y = summary_x - num * summary_line
    draw.text((summary_x, height - y), u'%s' % summary, color, font)

# ����ͼƬ
image.save(new_img, 'png')

# ѹ��ͼƬ
sImg = Image.open(new_img)
w, h = sImg.size
width = int(w / 2)
height = int(h / 2)
dImg = sImg.resize((width, height), Image.ANTIALIAS)
dImg.save(compress_img)