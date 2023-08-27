# Function = a block of reusable code
#            place () afeter the function name to invoke it
#            arguments can be 1. positional, 2. Default, 3. keyword, 4. arbitrary

# Positional arguenmts function
# ---------  EXAMPLE 1  --------- 
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("BroCode", 42.50, "01/02")
# display_invoice("JoeSchmo", 100.99, "02/03")

# ---------  EXAMPLE 2  --------- 
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)

# default arguments = A defaut value for certain parameters 
#                     default is used when that argument is omitted
#                     make your function more flexible, reduces # of arguments
# ---- EXAMPLE ----
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 - tax)

# print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))

# ---- EXERCISE ----
import time

def count(end, start=0): 
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

# count(10)
count(30, 15)

# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary
# ---- EXAMPLE 1 ----
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="John", first="James")

# ---- EXAMPLE 2 ----
for number in range(1, 11):
    print(number, end=" ")

print("1", "2", "3", "4", "5", sep="-")

# ---- EXERCISE ----
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)

# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#          * unpacking operator

# ---- *ARGS Example 1 ----

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4))

# ---- *ARGS Example 2 ----

def display_name(*args):
    print("Hello", end=" ")
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# ---- **KWARGS ----
def print_address(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")

print_address(street="123 Fake St.",
              pobox="P.O Box 777",
              city="Detroit",
              state="MI",
              zip="54321")

# ---- EXERCISE ----
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")

