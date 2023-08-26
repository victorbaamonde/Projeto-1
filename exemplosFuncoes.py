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