import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+919347466487")
phone_number2 = phonenumbers.parse("+918143209499")
phone_number3 = phonenumbers.parse("+917993400147")
phone_number4 = phonenumbers.parse("+917680821278")
phone_number5 = phonenumbers.parse("+919866551468")
phone_number6 = phonenumbers.parse("+919866787998")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))
print(geocoder.description_for_number(phone_number5,"en"))
print(geocoder.description_for_number(phone_number6,"en"))