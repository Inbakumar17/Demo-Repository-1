# ISSUE 72
#
# Problem:
# Write a program that accepts a list of products containing category, price and quantity and calculates the total value of products in each category.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def category_values(products):
    totals = {}
    for product in products:
        category = product["category"]
        # TODO: Check how quantity and price combine into product value.
        value = product["price"] + product["quantity"]
        # TODO: Check how multiple products in a category are accumulated.
        totals[category] = totals.get(category, 0) + value
    # TODO: Check the result for an empty product list.
    return totals

def check_solution():
    products = [{"category":"food","price":4,"quantity":3},{"category":"food","price":2,"quantity":5},{"category":"home","price":8,"quantity":1}]
    assert category_values(products) == {"food":22,"home":9}
    assert category_values([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
