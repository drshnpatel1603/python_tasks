sales_data = {
    "Store_A": {
        "Laptop": 15,
        "Phone": 30,
        "Tablet": 10
    },
    "Store_B": {
        "Laptop": 25,
        "Phone": 20,
        "Tablet": 15
    },
    "Store_C": {
        "Laptop": 10,
        "Phone": 35,
        "Tablet": 5
    }
}

def space(fx):
    def wapper(*args,**kwargs):
        print("\n")
        result = fx(*args,**kwargs)
        return result
    return wapper

# @space
def total_sells(sales_data):
    """ Find the total sales for each product across all stores. """
    sale_each_produce = {}
    for value in sales_data.values():
        for key,val in value.items():
            if sale_each_produce.get(key):
                sale_each_produce[key] += val
            else:
                sale_each_produce.update({key : val})
    return sale_each_produce
total_sell = total_sells(sales_data)


@space
def highest_sales(sales_data):
    """ Identify the store with the highest total sales (sum of all products). """
    high_sale = {}
    for key,value in sales_data.items():
        total = 0
        for val in value.values():
            total += val
        high_sale.update({key : total})

    high_selling_store = max([(value, key) for key, value in high_sale.items()])
    return high_selling_store


@space
def find_best_product(total_sells):
    """ Find the best-selling product (i.e., the product with the highest total sales). """
    k = ""
    max = 0
    for key,val in total_sells.items():
        if val > max:
            max = val
            k = key
    return (k,max)

@space
def high_sale_store(sales_data):
    """ Sort the stores based on their total sales in descending order and print the sorted result. """
    list_store = {}
    for key,value in sales_data.items():
        total = 0
        for val in value.values():
            total += val
        list_store.update({key:total})
    # list_store = ({k : v for k,v in sorted(list_store.items(), key=lambda key: key[1], reverse=True)})
    list_store = (sorted(list_store.items(), key=lambda item: item[1], reverse=True))

    return list_store



print(f"Total Price each Product : {total_sell}")
print(f"highest sale store wise : {highest_sales(sales_data)}")
print(f"highset selling product : {find_best_product(total_sell)}")
print(f"store wise List : {dict(high_sale_store(sales_data))}")