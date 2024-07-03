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

def set_prices():
    filename = input("Enter pricing filename: ")
    pricing_data = pd.read_csv(filename, header=0)
    price_dict = {}
    for index, row in pricing_data.iterrows():
        price_dict[row['sku']] = row['price']
    
    for index, row in data.iterrows():
        if row['Variant SKU'] in price_dict and not(row['Title'] == ''):
            print("Found")
            data.at[index, 'Variant Price'] = price_dict[row['Variant SKU']]
    
    data.to_csv("output/output.csv", index=False)

print("Shopify Sale Tool\n1) Add a sale\n2) Remove a sale\n3) Change prices in bulk")
choice = 0
while choice < 1 or choice > 3:
    try:
        choice = int(input("Choice: "))
    except:
        pass

if choice == 1:
    add_sale()
elif choice == 2:
    remove_sale()
else:
    set_prices()

print("Complete")