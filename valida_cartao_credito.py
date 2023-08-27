# remove any '-' or ' '
# add all digits in the odd places from right to left
# double every second digit from right to left
#   if result is a two-digit number,
#   add the two-digit number together to get a single digit
# sum the totals of steps 2 & 3
# if sum is divisible by 10, the credit card # is valid

credit_card_number = 0
odd_digits = 0
event_digits = 0

# Step 1
credit_card_number = input("Digite o numero do cartao: ")
credit_card_number = credit_card_number.replace("-","")
credit_card_number = credit_card_number.replace(" ","")
credit_card_number = credit_card_number[::-1]

# Step 2
for x in credit_card_number[::2]:
    odd_digits += int(x)

# Step 3
for x in credit_card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        event_digits += (1 + (x % 10))
    else:
        event_digits += x
# Step 4
total = odd_digits + event_digits

# Step 5
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")