filename = "inventory.txt"
failed_attempts = 0
deliveries_processed = 0


def load_inventory():
    orders = []
    file = open(filename, "a")
    file.close()

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            orders.append(parts)

    return orders

def save_inventory(orders):
    file = open(filename, "w")
    for item in orders:
        file.write(item[0] + "," + item[1] + "," + item[2] + "\n")
    file.close()
    
def process_delivery(current_total,new_value):
    new_total = current_total +new_value    
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print('Final Summary:')
    print('Total deliveries processed:', total_units)
    print('number of failed entries:', failed_attempts)

orders = load_inventory()

print("Current Orders:\n")
if len(orders) == 0:
    print("No orders found in inventory.txt")
else:
    for item in orders:
        print(item[0] + ", " + item[1] + ", " + item[2])
    print()

def get_valid_input():
    global failed_attempts
    while True:
        product_name = input("How many stocks to add, or type 'quit' to leave: ")

        if product_name.lower() == "quit":
            return "quit"

        if not product_name.isdigit():
            print("type a valid integer.")
            failed_attempts +=1
            continue

        return int(new_stock)

while True:
    new_stock = get_valid_input()

    if new_stock =="quit":
        generate_report(deliveries_processed, failed_attempts)
        break

    inventory = process_delivery(inventory, new_stock)

    tax = calculate_tax(new_stock)

    print("new stock received")
    print("Total inventory:", inventory)
    print("Tax for this: {:.2f}".format(tax))

    deliveries_processed +=1