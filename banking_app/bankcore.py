branch_id = 2057
users_info = {}

def create_account(name, password):
    user_number = len(users_info) + 1
    customer_id = str(branch_id) + "-" + str(user_number)

    users_info[customer_id] = {
        "name": name,
        "password": password
    }

    print("Account created successfully")
    print("Your Customer ID is:", customer_id)

    return customer_id


def login(customer_id, password):

    if customer_id in users_info and users_info[customer_id]["password"] == password:
        print("Login Successful")
        return True
    else:
        print("Invalid Login")
        return False