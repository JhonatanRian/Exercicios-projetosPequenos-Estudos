import phonenumbers
from phonenumbers import geocoder

num = "+5596991473026"

phone = phonenumbers.parse(num)

print(geocoder.description_for_number(phone, "pt"))