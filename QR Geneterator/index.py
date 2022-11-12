import qrcode
text=input('enter any text.....')
img=qrcode.make(text)
type(img)
result=img.save('result.png')
