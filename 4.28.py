def get_price(product): 
return product[1]['price'] 
def sort_products_by_price(products_dict): 
sorted_products = sorted(products_dict.items(), key=get_price) 
return sorted_products 
products_details = { 
'apple': {'price': 1.50, 'quantity': 10}, 
'banana': {'price': 0.75, 'quantity': 20}, 
'orange': {'price': 1.20, 'quantity': 15}, 
'grapes': {'price': 2.00, 'quantity': 12}, 
'watermelon': {'price': 3.50, 'quantity': 5} 
} 
sorted_products = sort_products_by_price(products_details) 
print("Products sorted by price in ascending order:") 
for product_name, details in sorted_products: 
print(f"Product: {product_name}, Price: ${details['price']}, Quantity: {details['quantity']}")
