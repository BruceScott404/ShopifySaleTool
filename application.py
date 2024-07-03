import pandas as pd

data = pd.read_csv('input/input.csv', header=0)

def add_sale():
    sale_multiplier = 1 - (float(input("Enter sale percentage: "))/100)
    data['Variant Compare At Price'] = data['Variant Price']
    data['Variant Price'] *= sale_multiplier

    data.to_csv("output/output.csv", index=False)

def remove_sale():
    data['Variant Price'] = data['Variant Compare At Price']
    data['Variant Compare At Price'] = ''
    data.to_csv("output/output.csv", index=False)

print("Shopify Sale Tool\n1) Add a sale\n2) Remove a sale")
choice = 0
while choice < 1 or choice > 2:
    try:
        choice = int(input("Choice: "))
    except:
        pass

if choice == 1:
    add_sale()
else:
    remove_sale()

print("Complete")