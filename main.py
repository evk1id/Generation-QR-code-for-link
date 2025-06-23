import qrcode
import sys

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, # Размер каждого квадратика в QR-коде в px
    border=4,
)

if __name__ == '__main__':
    # Инициализация
    try:
        link_to_convert = sys.argv[1]
    except IndexError:
        exit("USAGE: python3 main.py <lnk>")

    # Генерируем QR-код
    qr.add_data(link_to_convert)
    qr.make(fit=True)  # Автоматически определяет размер QR-кода

    # Генерируем изображение QR-кода и сохраняем
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("meme.png")
    img.show()