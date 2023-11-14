No compilation needed. 

WINDOWS:
To install requirements:
pip install -r requirements.txt

To run on a windows machine, in the terminal: 
To generate QR code:
python3 main.py --generate-qr
To generate OTP on 30 second loop:
python3 main.py --get-otp

LINUX:

(Unfortunatey I'm unable to test and validate this process on my machine)

Use "dos2unix {file}" if any \r errors are thrown during the following
Use "chmod +x {file}" if permissions need to be elevated

To install requirements:
pip install -r requirements.txt

To run on a windows machine, in the terminal: 
To generate QR code:
./main.py --generate-qr
To generate OTP on 30 second loop:
./main.py --get-otp