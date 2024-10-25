import qrcode

def generate_qr(data, file_name="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(file_name)
    print(f"QR code saved as {file_name}")

# Example usage
data = "https://www.example.com"
generate_qr(data)
