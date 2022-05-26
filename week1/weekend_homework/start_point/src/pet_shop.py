# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"] = get_total_cash(pet_shop) + cash_amount


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, number_of_pets_sold):
    pet_shop["admin"]["pets_sold"] = (
        pet_shop["admin"]["pets_sold"] + number_of_pets_sold
    )


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    results = []
    for x in pet_shop["pets"]:
        if x["breed"] == breed:
            results.append(x)
    return results


def find_pet_by_name(pet_shop, pet_name):
    for x in pet_shop["pets"]:
        if x["name"] == pet_name:
            return x


def remove_pet_by_name(pet_shop, pet_name):
    for x in pet_shop["pets"]:
        if x["name"] == pet_name:
            pet_shop["pets"].remove(x)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, cash_amount):
    customer["cash"] = customer["cash"] - cash_amount


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


# Optional
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False


def sell_pet_to_customer(pet_shop, new_pet, customer):
    if new_pet is not None:
        # if customer can afford pet
        if customer_can_afford_pet(customer, new_pet):
            # Remove pet from pet shop, add pet to customer
            pet_shop["pets"].remove(new_pet)
            add_pet_to_customer(customer, new_pet)

            # Take maney from customer, add to pet shop
            remove_customer_cash(customer, new_pet["price"])
            add_or_remove_cash(pet_shop, new_pet["price"])

            # increase pets sold number
            increase_pets_sold(pet_shop, 1)
