import random

number = random.randint(1, 100)
min_value = 1
max_value = 100

while True:
    hads = input(f"pleas enter your number")

    if not hads.isdigit():
        print ("enter your number")
        continue

    hads = int(hads)

    if hads < min_value or hads > max_value:
        print(f"faghat bin adad vared konid {min_value} and {max_value}.")
        continue

    if hads == number:
        print("dorost hads zadi")
        break
    elif hads > number:
        print("adad bozorg ast!")
        max_value = hads - 1
    else:
        print("adad bala tar hads bzanid")
        min_value = hads + 1    


