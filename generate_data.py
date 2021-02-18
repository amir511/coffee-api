"""
Script to quickly generate inital_data.json that will be used to fill the db with initial data.
"""

# machines
machines = [
    ("CM001", "small", "base", False),
    ("CM002", "small", "premium", False),
    ("CM003", "small", "deluxe", True),
    ("CM101", "large", "base", False),
    ("CM102", "large", "premium", True),
    ("CM103", "large", "deluxe", True),
    ("EM001", "espresso", "base", False),
    ("EM002", "espresso", "premium", False),
    ("EM003", "espresso", "deluxe", True),
]
# pods
pods = [
    ("CP001", " small", "1", "vanilla"),
    ("CP003", "small", "3", "vanilla"),
    ("CP011", "small", "1", "caramel"),
    ("CP013", "small", "3", "caramel"),
    ("CP021", "small", "1", "psl"),
    ("CP023", "small", "3", "psl"),
    ("CP031", "small", "1", "mocha"),
    ("CP033", "small", "3", "mocha"),
    ("CP041", "small", "1", "hazelnut"),
    ("CP043", "small", "3", "hazelnut"),
    ("CP101", "large", "1", "vanilla"),
    ("CP103", "large", "3", "vanilla"),
    ("CP111", "large", "1", "caramel"),
    ("CP113", "large", "3", "caramel"),
    ("CP121", "large", "1", "psl"),
    ("CP123", "large", "3", "psl"),
    ("CP131", "large", "1", "mocha"),
    ("CP133", "large", "3", "mocha"),
    ("CP141", "large", "1", "hazelnut"),
    ("CP143", "large", "3", "hazelnut"),
    ("EP003", "espresso", "3", "vanilla"),
    ("EP005", "espresso", "5", "vanilla"),
    ("EP007", "espresso", "7", "vanilla"),
    ("EP013", "espresso", "3", "caramel"),
    ("EP015", "espresso", "5", "caramel"),
    ("EP017", "espresso", "7", "caramel"),
]

product_list = []
for machine in machines:
    d = {
        "model": "product.coffeemachine",
        "fields": {
            "SKU_number": machine[0],
            "product_type": machine[1],
            "water_line_compatible": machine[3],
            "model_type": machine[2],
        },
    }
    product_list.append(d)

for pod in pods:
    d = {
        "model": "product.coffeepod",
        "fields": {"SKU_number": pod[0], "product_type": pod[1], "coffee_flavor": pod[3], "pack_size": pod[2]},
    }
    product_list.append(d)

import json

json_str = json.dumps(product_list)
with open("initial_data.json", "w") as f:
    f.write(json_str)
