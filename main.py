#!/usr/bin/env python3
"""
Simple QR Code and OTP generator for Google Authenticator and the like

Fill in global variables ACCOUNT, ISSUER, SECRET_KEY with your own values.

Install requirements:
pip install requirements.txt

Run the program with the following command:

Windows:
To generate qr code: python3 main.py --generate-qr
To get otp: python3 main.py --get-otp

Linux:
To generate qr code: ./main.py --generate-qr
To get otp: ./main.py --get-otp

"""
import qrcode
import pyotp
import argparse
import time

# Global variables: fill in your own values
ACCOUNT = 'Account_name_placeholder'
ISSUER = 'Issuer_name_placeholder'
SECRET_KEY = 'Secret_key_placeholder'

# OTP Auth URI
OTP_AUTH = f'otpauth://totp/{ACCOUNT}?secret={SECRET_KEY}&issuer={ISSUER}'


# Generate QR Code
def generate_qr():
    # Create a QRCode object
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    # Add data to QR Code
    qr.add_data(OTP_AUTH)
    # Create an image from the QR Code instance
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    # Save it somewhere, change the extension as needed:
    img.save('qr.png')


# Get OTP
def generate_totp(secret_key=SECRET_KEY):
    # Create a TOTP object
    totp = pyotp.TOTP(SECRET_KEY)
    # Generate a current OTP
    otp = totp.now()
    return otp


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--generate-qr", action="store_true", help="Generate QR Code")
    parser.add_argument("--get-otp", action="store_true", help="Get OTP")

    args = parser.parse_args()  # Correctly parse the arguments

    # Run the program
    # If --generate-qr is passed, generate QR Code
    if args.generate_qr:
        generate_qr()
    # If --get-otp is passed, generate OTP
    elif args.get_otp:
        while True:
            # Generate OTP
            otp = generate_totp(SECRET_KEY)
            print(otp)
            # Sleep until next interval: Synchronize with Google Authenticator
            time_until_next_interval = 30 - (int(time.time()) % 30)
            time.sleep(time_until_next_interval)
    else:
        print("Invalid input. Terminating program.")
        return -1


if __name__ == '__main__':
    main()
