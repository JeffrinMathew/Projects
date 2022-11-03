import qrcode
img = qrcode.make('https://github.com/JeffrinMathew/Projects')
img.save("GitHubQR.png")