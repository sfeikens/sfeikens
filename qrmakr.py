import qrcode
from qrcode.constants import ERROR_CORRECT_H

URL = "https://sfeikens.github.io/sfeikens/"
OUT_FILE = "qr.png"

# The QR box in your CSS is 9rem x 9rem.
# With your print base (21px), that is about 189px.
TARGET_PX = 180  # a bit smaller so it fits comfortably
BORDER = 4       # standard quiet zone

# Build QR once to find how many modules it needs
qr = qrcode.QRCode(
    version=None,  # let it choose the smallest version that fits
    error_correction=ERROR_CORRECT_H,
    box_size=10,   # temporary, will be recalculated
    border=BORDER,
)
qr.add_data(URL)
qr.make(fit=True)

modules = qr.modules_count
total_modules = modules + (BORDER * 2)

# Pick a box size that keeps the final image within TARGET_PX
box_size = max(1, TARGET_PX // total_modules)

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=box_size,
    border=BORDER,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
img.save(OUT_FILE)

print(f"Saved {OUT_FILE} ({img.size[0]}x{img.size[1]} px)")
