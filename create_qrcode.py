import qrcode

def create_qrcode(item_sku: str):
    qr = qrcode.QRCode(
        version=None,
        box_size=10,
        border=4,
    )
    qr.add_data(item_sku)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'qrcodes/{item_sku}.png')

create_qrcode('123456testing')