# Task 1:
# Given a dictionary of sales data and another dictionary of product prices, calculate total revenue for each store.
#
# Identify which store generated the highest revenue.

sales_data = {
    "Store_A": {"Laptop": 15, "Phone": 30, "Tablet": 10},
    "Store_B": {"Laptop": 25, "Phone": 20, "Tablet": 15},
    "Store_C": {"Laptop": 10, "Phone": 35, "Tablet": 5}
}

product_prices = {
    "Laptop": 1000,
    "Phone": 500,
    "Tablet": 300
}

def total_revanue(sales_data,product_prices):
    total_rev = {}
    for store,products in sales_data.items():
        total = 0
        for product,qun in products.items():
            total += (product_prices.get(product) * qun)
            # abc=sum(lambda product_prices:product_prices(product) * qun).get
        total_rev[store] = total
    print(f"Store vise Revenue : {total_rev}")
    key = None
    max = 0
    for name,val in total_rev.items():
        if max < val:
            max = val
            key = name
    return(key,max)

print(f"max Revenue : {total_revanue(sales_data,product_prices)}")


# Task 2
# The employee with the highest sales.
# The top 3 employees sorted in descending order.

employee_sales = {
    "Alice": 5000,
    "Bob": 7500,
    "Charlie": 4200,
    "Diana": 9100,
    "Ethan": 6200
}

def employee(employee_sales):
    highest_sell = sorted(employee_sales.items(), key=lambda item : item[1], reverse=True)
    return highest_sell
print(f"highest sell employees : {employee(employee_sales)[0][0]}")
print(f"Top 3 highest sell employees : {employee(employee_sales)[0:3]}")



"""  Task 3
Given a dictionary where complaint types are keys and their occurrence counts are values, determine:
The most common complaint type.
The percentage share of each complaint type"""

complaints = {
    "Late Delivery": 120,
    "Damaged Product": 95,
    "Wrong Item": 60,
    "Customer Service": 75,
    "Billing Issues": 50
}

def common_type(complaints):
    return max(complaints.items(), key=lambda itme : itme[1])


def complaints_percentage_count(complaints):
    total = sum(complaints.values())
    # new_percentage = sorted(complaints.items(), key=lambda item : (item[1]/total)*100)
    new_percentage = {key:f"{(val/total)*100}%" for key,val in complaints.items()}

    # for key,value in complaints.items():
    #     percentage = (value/total)*100
    #     new_percentage[key] = f"{percentage}%"
    return new_percentage

print(f"The most common complaint type : {common_type(complaints)}")
print(f"The percentage share of each complaint type : {complaints_percentage_count(complaints)}")


# Task 4
# Given a dictionary where marketing channels are keys and their conversion rates (as percentages) are values, find:
# The marketing channel with the highest conversion rate.
# The average conversion rate across all channels

marketing_performance = {
    "Facebook Ads": 3.2,
    "Google Ads": 4.8,
    "Email Marketing": 2.5,
    "Organic Search": 5.6,
    "Referral": 3.9
}

def high_conversionn_rate(marketing_performance):
    return max(marketing_performance.items(), key=lambda item : item[1])

def avg_conversion_rate(marketing_performance):
    total = sum(marketing_performance.values())
    avg_rate = total/len(marketing_performance)
    return avg_rate

print(f"The marketing channel with the highest conversion rate : {high_conversionn_rate(marketing_performance)}")
print(f"The average conversion rate across all channels : {avg_conversion_rate(marketing_performance)}")


# Task 5
# Given a dictionary where movie names are keys and their respective ratings (out of 10) are values, determine:
# The highest-rated movie.
# The top 3 movies sorted by rating.
# The average movie rating

movie_ratings = {
    "Inception": 8.8,
    "Interstellar": 8.6,
    "Parasite": 8.9,
    "The Dark Knight": 9.0,
    "Avengers: Endgame": 8.4
}

def highest_rate_movie(movie_ratings):
    high_rate = sorted(movie_ratings.items(), key=lambda item : item[1], reverse=True)
    return high_rate

def avg_rate_movie(movie_ratings):
    total = sum(movie_ratings.values())
    avg_rate = total/len(movie_ratings)
    return avg_rate


print(f"The highest-rated movie : {highest_rate_movie(movie_ratings)[0]}")
print(f"The top 3 movies sorted by rating : {highest_rate_movie(movie_ratings)[0:3]}")
print(f"The average movie rating : {avg_rate_movie(movie_ratings)}")



