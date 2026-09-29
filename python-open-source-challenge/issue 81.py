# ISSUE 81
#
# Problem:
# Write a program that accepts product records containing initial stock and sold quantity and identifies products that need to be restocked.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def products_to_restock(products):
    names = []
    for product in products:
        # TODO: Check how sold units change the remaining stock.
        remaining = product["stock"] + product["sold"]
        # TODO: Check the comparison with the reorder level.
        if remaining <= product["reorder_level"]:
            names.append(product["name"])
    # TODO: Check that products at the threshold are handled.
    return names

def check_solution():
    products = [{"name":"tea","stock":10,"sold":8,"reorder_level":5},{"name":"rice","stock":6,"sold":2,"reorder_level":4}]
    assert products_to_restock(products) == ["tea"]
    assert products_to_restock([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
