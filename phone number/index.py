import phonenumbers
from test import number
from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")
print("Country: ")
print(geocoder.description_for_number(ch_number, "sv"))

from phonenumbers import carrier

service_nmber = phonenumbers.parse(number, "RO")
print("Service: ")
print(carrier.name_for_number(service_nmber, "sv"))

print("Mobile: ")
print(carrier._is_mobile(phonenumbers.parse(number, "RO")))