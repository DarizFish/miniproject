import re

def validate_pin(pin):
    pincode4 = re.compile(r'^\d{4}$')
    pincode6 = re.compile(r'^\d{6}$')
    p4 = pincode4.match(pin)
    p6 = pincode6.match(pin)
    if p4 or p6:
        return True
    else:
        return False

print(validate_pin('1234\n'))