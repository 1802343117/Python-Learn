"""
二维码
pip3 install qrcode
pip3 install myqr
"""
import qrcode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=8, border=4)
qr.add_data('Hello World')
img = qr.make_image()
img.save('./res/code.png')

qr.add_data('https://www.baidu.com')
img1 = qr.make_image(fill_color='rgb(50,150,250)',
                     back_color='rgb(255,255,255)')
img1.save('./res/code1.png')
