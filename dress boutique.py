dress_catalog = { 
    'Eliana' : { 'size' : {'XS' : 3, 'S' : 5, 'M' : 4, 'L' : 4, 'XL' : 3 }, 'price' : 1600},
    'Evelyn' : { 'size' : {'XS' : 2, 'S' : 4, 'M' : 5, 'L' : 3, 'XL' : 3 }, 'price' : 2300}, 
    'Amelia' : { 'size' : {'XS' : 4, 'S' : 3, 'M' : 4, 'L' : 5, 'XL' : 2 }, 'price' : 2100},
    'Cecily' : { 'size' : {'XS' : 2, 'S' : 3, 'M' : 3, 'L' : 5, 'XL' : 2 }, 'price' : 1800},
    'Vivien' : { 'size' : {'XS' : 5, 'S' : 2, 'M' : 3, 'L' : 4, 'XL' : 5 }, 'price' : 2600},
    'Yvette' : { 'size' : {'XS' : 2, 'S' : 4, 'M' : 5, 'L' : 3, 'XL' : 3 }, 'price' : 1400},
    'Daphne' : { 'size' : {'XS' : 0, 'S' : 5, 'M' : 2, 'L' : 5, 'XL' : 4 }, 'price' : 2200}
}

for dress, details in dress_catalog.items():
    details['rent_price'] = details['price'] // 2


user_acc = {}
user_cart = {}
user_invent = {}
admin_user = 'admin'
admin_pass = 'password'

def main_menu():
    print()
    print("YEN'S DRESS BOUTIQUE")
    print()
    print('(1) Sign-up')
    print('(2) Log-in')
    print('(3) Exit')

    while True:
        try:
            choice = int(input('\nChoose an option: '))
            if choice == 1:
                sign_up()
                break
            elif choice == 2:
                login()
                break
            elif choice == 3:
                exit()
            else:
                print('\nInvalid input.')
                
        except ValueError:
            print('\nInvalid input.')

def sign_up():
    print('\nREGISTER TO CREATE AN ACCOUNT (Leave blank to go back)\n')
    username = input('Enter username: ')
    while username in user_acc:
        print('\nUsername already taken.\n')
    
    if username == '':
        main_menu()

    password = input('Enter password: ')
    while len(password) < 8:
        if password == '':
            main_menu()
        else:
            print('\nPassword must be at least 8 characters.\n')
            password = input('Enter password: ')

    cont_num = input('Enter contact number: ')
    while len(cont_num) != 11 or (not cont_num.startswith("09")):
        if cont_num == '':
            main_menu()
        else:
            print('\nInvalid contact number.\n')
        cont_num = input('Enter contact number: ')

    balance = 0
    
    user_acc[username] = {
        'username' : username,
        'password' : password,
        'number' : cont_num,
        'balance' : balance
        }
    
    print(f'\nWelcome {username}!')
    while True:
            choice = input('Press enter to continue or N to return to menu: ')
            if choice == '':
                login()
            elif choice.lower() == 'n':
                main_menu()
            else:
                print('Invalid input.')

def login():
    print('\nLOG IN TO YOUR ACCOUNT (Leave blank to go back)\n')
   
    while True:
            username = input('Enter username: ')

            if username == '':
                main_menu()

            password = input('Enter password: ')

            if password == '':
                main_menu()

            if username == admin_user and password == admin_pass:
                admin_menu()
            elif username in user_acc and user_acc[username]['password'] == password:
                print(f'\nWelcome {username}!')
                user_menu(username)
            else:
                print('\nIncorrect username or password.\n')

def user_menu(username):
    print("\nYEN'S DRESS BOUTIQUE\n")
    print('(1) View E-Wallet')
    print('(2) View dresses')
    print('(3) Return a dress')
    print('(4) View cart')
    print('(5) Exit')

    while True:
        try:
            choice = int(input('\nChoose an option: '))
            if choice == 1:
                e_wallet(username)
            elif choice == 2:
                view_dresses(username)
            elif choice == 3:
                return_dress(username)
            elif choice == 4:
                cart(username)
            elif choice == 5:
                main_menu()
            else:
                print('\nInvalid input.')

        except ValueError:
            print('\nInvalid input.')

def e_wallet(username):
    print('\nWELCOME TO YOUR E-WALLET\n')
    print(f'Balance: {user_acc[username]['balance']}\n')
    print('(1) Deposit')
    print('(2) Withdraw')
    print('(3) Exit')
    
    while True:
        try:
            choice = int(input('\nChoose an option: '))

            if choice == 1:
                add_balance = int(input('Enter the amount to be deposited: '))
                user_acc[username]['balance'] += add_balance
                print(f'\nUpdated balance: {user_acc[username]['balance']}')
            elif choice == 2:
                draw_balance = int(input('Enter amount to be withdrawn: '))
                user_acc[username]['balance'] -= draw_balance
                print(f'\nUpdated balance: {user_acc[username]['balance']}')
            elif choice == 3:
                user_menu(username)
            else:
                print('Invalid input.')
        except ValueError :
            print('Invalid input.')   

def view_dresses(username):
    print('\nDRESS CATALOG')
    for dress, details in dress_catalog.items():
        print(f"\nStyle: {dress}")
        print(f"Price: {details['price']}")
        print(f"Rent Price: {details['rent_price']}")

        available_sizes = [size for size, quantity in details['size'].items() if quantity > 0]
        if available_sizes:
            print("Sizes available:", ", ".join(available_sizes))
        else:
            print("No sizes available")
    
    print('\n(1) Select a dress')
    print('(2) View cart')
    print('(3) Exit')

    while True:
        try:
            choice = int(input('\nChoose an option: '))
            if choice == 1:
                select_dress(username)
            elif choice == 2:
                cart(username)
            elif choice == 3:
                user_menu(username)
            else:
                print('\nInvalid input.\n')
        except ValueError:
            print('\nInvalid input.\n')

def select_dress(username):
    if username not in user_cart:
        user_cart[username] = {}

    while True:
        selected_dress = input('Select a dress: ').capitalize()
        if selected_dress not in dress_catalog:
            print('\nDress not in system.\n')
        elif selected_dress == '':
            view_dresses(username)
        else:
            break

    while True:
        details = dress_catalog[selected_dress] 
        available_sizes = [size for size, quantity in details['size'].items() if quantity > 0]

        selected_size = input('Select a size: ').upper()
        if selected_size not in details['size']:
            print('\nInvalid size.\n')
        elif selected_size not in available_sizes:
            print('\nSize out of stock.\n')
        elif selected_size == '':
            view_dresses(username)
        else:
            break

    while True:
        try:
            selected_quantity = int(input('Enter quantity: '))
            
            if selected_quantity <= 0:
                print('\nQuantity must be greater than zero.\n')
            elif selected_quantity > details['size'][selected_size]:
                print('\nYou have reached the maximum quantity available for this item.\n')
            else:
                dress_catalog[selected_dress]['size'][selected_size] -= selected_quantity
                break

        except ValueError:
            print('\nInvalid input. Please enter a valid integer for quantity.\n')

    user_cart[username].setdefault(selected_dress.capitalize(), {}).update({
        'size': selected_size,
        'quantity': selected_quantity,
        'price': details['price'],
        'rent_price': details['rent_price']
    })

    print(f'\n{selected_quantity} of {selected_dress} in the size {selected_size} has been added to your cart.')

    while True:
        choice = input('Press enter to continue shopping or N to return to menu or C to proceed to cart: ')
        if choice == '':
            view_dresses(username)
        elif choice.lower() == 'n':
            user_menu(username)
        elif choice.lower() == 'c':
            cart(username)
        else:
            print('Invalid input.')

def cart(username):
    print('\nWELCOME TO YOUR CART')
    
    if not user_cart.get(username):
        print('Cart is empty')
        input('\nPress enter to go back.')
        user_menu(username)
        return
        
    for dress, details in user_cart[username].items():
        print(f'\n{dress}')
        print(f'Size: {details["size"]}')
        print(f'Quantity: {details["quantity"]}')
        print(f'Price: {details["price"]}')
        print(f'Rent price: {details["rent_price"]}')
    
    print('\n(1) Edit cart')
    print('(2) Checkout')
    print('(3) Exit')
    
    while True:
        try:
            choice = int(input('\nChoose an option: '))
            if choice == 1:
                edit_cart(username)
            elif choice == 2:
                checkout(username)
            elif choice == 3:
                user_menu(username)
            else:
                print('\nInvalid input.')
        except ValueError:
            print('\nInvalid input.')


def edit_cart(username):
    print('EDIT CART (leave blank to go back)')

    while True:
        edit_dress = input('Enter the dress to be edited: ').capitalize()
        if edit_dress == '':
            cart(username)
            return
        elif edit_dress not in user_cart[username]:
            if edit_dress in dress_catalog:
                print('\nDress not in cart.\n')
            else:
                print('\nInvalid input.\n')
            continue

        print('(1) Edit size')
        print('(2) Edit quantity')
        print('(3) Delete dress from cart')
        print('(4) Exit')

        info = user_cart[username][edit_dress]

        while True:
            try:
                choice = int(input('\nChoose an option: '))
                if choice == 1:
                    while True:
                        print(f'Current size: {info["size"]}')
                        new_size = input('Enter new size: ').upper()
                        available_sizes = [size for size, quantity in dress_catalog[edit_dress]['size'].items() if quantity > 0]
                        if new_size in available_sizes:
                            info['size'] = new_size
                            print(f'Size of {edit_dress} has been updated to {new_size}!')
                            break
                        elif new_size == '':
                            cart(username)
                            return
                        else:
                            print('Size out of stock.')

                elif choice == 2:
                    while True:
                        try:
                            print(f'Current quantity: {info["quantity"]}')
                            new_quantity = int(input('Enter new quantity: '))
                            cart_quantity = user_cart[username][edit_dress]['quantity']
                            catalog_quantity = dress_catalog[edit_dress]['size'][info['size']]

                            if new_quantity <= 0:
                                print('\nQuantity must be greater than zero.\n')
                            elif new_quantity > cart_quantity and new_quantity > catalog_quantity:
                                print('\nYou have reached the maximum quantity available for this item.\n')
                            elif new_quantity > cart_quantity:
                                difference = new_quantity - cart_quantity
                                dress_catalog[edit_dress]['size'][info['size']] -= difference
                                info['quantity'] = new_quantity
                                print('Quantity Updated!')
                                break
                            elif new_quantity > catalog_quantity:
                                print('\nYou have reached the maximum quantity available for this item in the catalog.\n')
                            else:
                                info['quantity'] = new_quantity
                                print('Quantity Updated!')
                                break
                        except ValueError:
                            print('\nInvalid input. Please enter a valid integer for quantity.\n')

                elif choice == 3:
                    user_cart[username].pop(edit_dress)
                    print(f'{edit_dress} has been removed from the cart.')

                elif choice == 4:
                    cart(username)
                    return
                
                elif choice == '':
                    cart(username)
                    return
                else:
                    print('\nInvalid input.\n')
            except ValueError:
                print('\nInvalid input.\n')


def checkout(username):
    print('\nCHECKOUT')
    total_price = 0

    print('\nItems in Cart:')
    for dress, details in user_cart[username].items():
        print(f'\n{dress}')
        print(f'Size: {details["size"]}')
        print(f'Quantity: {details["quantity"]}')
        print(f'Price: {details["price"]}')
        print(f'Rent Price: {details["rent_price"]}')
        total_price += details["price"] * details["quantity"]

    print('\nTotal Price:', total_price)

    while True:
        purchase_option = input('\nWould you like to rent or buy? (R/B): ').strip().lower()
        if purchase_option == 'r':
            total_price += 1000  
            print('\nSafety deposit of 1000 added.')
            print('\nTotal Price (including safety deposit):', total_price)
            print('\n(1) Proceed with the rent')
            print('(2) Go back to cart')
            while True:
                rent_option = input('Choose an option: ')
                if rent_option == '1':
                    if username not in user_invent:
                        user_invent[username] = {} 
                    for dress, details in user_cart[username].items():
                        if dress not in user_invent[username]:
                            user_invent[username][dress] = {'size': details['size'], 'quantity': details['quantity'], 'rented': True}
                        else:
                            user_invent[username][dress]['quantity'] += details['quantity']
                            user_invent[username][dress]['rented'] = True
                    break
                elif rent_option == '2':
                    return
                else:
                    print('Invalid option. Please choose 1 or 2.')
            break
        elif purchase_option == 'b':
            print('\nTotal Price:', total_price)
            print('\n(1) Proceed with the purchase')
            print('(2) Go back to cart')
            while True:
                buy_option = input('Choose an option: ')
                if buy_option == '1':
                    break
                elif buy_option == '2':
                    return
                else:
                    print('Invalid option. Please choose 1 or 2.')
            break
        else:
            print('Invalid option. Please choose "R" to rent or "B" to buy.')

    if user_acc[username]['balance'] < total_price:
        print("Insufficient balance. Please deposit more funds or remove items from your cart.")
        input('\nPress enter to go back to the menu.')
        user_menu(username)

    user_acc[username]['balance'] -= total_price
    print(f'\nTotal Price: {total_price}')
    print(f'Current Balance: {user_acc[username]["balance"]}')

    print('\nRECEIPT:')
    print('\nItems Purchased:')
    for dress, details in user_cart[username].items():
        print(f'\n{dress}')
        print(f'Size: {details["size"]}')
        print(f'Quantity: {details["quantity"]}')

    if purchase_option == 'r':
        print('\nSafety deposit of 1000 added.')

    print('\nTotal Price:', total_price)
    print('Thank you for your purchase!')

    user_cart[username] = {}

    input('\nPress enter to go back to the menu.')
    user_menu(username)

def return_dress(username):
    print("\nDRESSES RENTED BY YOU:")
    if username in user_invent and user_invent[username]:
        for dress, details in user_invent[username].items():
            print(f"\n{dress}")
            print(f"Size: {details['size']}")
            print(f"Quantity: {details['quantity']}")
    else:
        print("You haven't rented any dresses.")

    while True:
        dress_to_return = input("\nEnter the dress you want to return (or press enter to go back): ").capitalize()
        if dress_to_return == "":
            user_menu(username)
            return
        elif dress_to_return not in user_invent.get(username, {}):
            print("You do not have this dress.")
        else:
            break
    
    returned_dress_details = user_invent[username].pop(dress_to_return)

    dress_catalog[dress_to_return]['size'][returned_dress_details['size']] += returned_dress_details['quantity']

    user_acc[username]['balance'] += 1000
    print("Safety deposit of 1000 returned to your balance.")

    print(f"Your current balance: {user_acc[username]['balance']}")

    print("Thank you for returning the dress. Happy shopping again!")

    input('\nPress enter to go back to the menu.')
    user_menu(username)


def admin_menu():
    print('\nADMIN MENU')
    print('(1) Add New Dress')
    print('(2) Edit Dress Quantity')
    print('(3) Edit Dress Price')
    print('(4) Exit')

    while True:
        try:
            choice = int(input('\nChoose an option: '))
            if choice == 1:
                add_new_dress()
            elif choice == 2:
                edit_dress_quantity()
            elif choice == 3:
                edit_dress_price()
            elif choice == 4:
                main_menu()
            else:
                print('Invalid input.')
        except ValueError:
            print('Invalid input.')


def add_new_dress():
    print('\nADD NEW DRESS')
    dress_name = input('Enter dress name: ').capitalize()

    if dress_name in dress_catalog:
        print('Dress already exists in the catalog.')
        return

    dress_catalog[dress_name] = {'size': {}, 'price': 0, 'rent_price': 0}

    while True:
        try:
            price = int(input('Enter price of the dress: '))
            if price <= 0:
                print('Price must be greater than zero.')
            else:
                dress_catalog[dress_name]['price'] = price
                dress_catalog[dress_name]['rent_price'] = price // 2
                break
        except ValueError:
            print('Invalid input. Please enter a valid integer for price.')

    print(f'{dress_name} has been added to the catalog.')

    while True:
        size_quantity = input('Enter size and quantity (e.g., "S 5", separate with space), or press enter to exit: ')
        if size_quantity == '':
            admin_menu()
        size, quantity = size_quantity.split()
        dress_catalog[dress_name]['size'][size.upper()] = int(quantity)
        print(f'{quantity} of size {size.upper()} has been added for {dress_name}.')


def edit_dress_quantity():
    print('\nEDIT DRESS QUANTITY')

    dress_name = input('Enter dress name: ').capitalize()
    if dress_name not in dress_catalog:
        print('Dress not found in the catalog.')
        return

    size = input('Enter size to be edited: ').upper()
    if size not in dress_catalog[dress_name]['size']:
        print('Size not found for this dress.')
        return

    while True:
        try:
            quantity_to_add = int(input('Enter quantity to be added: '))
            if quantity_to_add <= 0:
                print('Quantity must be greater than zero.')
            else:
                dress_catalog[dress_name]['size'][size] += quantity_to_add
                print(f'Quantity of size {size} for {dress_name} updated to {dress_catalog[dress_name]["size"][size]}.')
                break
        except ValueError:
            print('Invalid input. Please enter a valid integer for quantity.')


def edit_dress_price():
    print('\nEDIT DRESS PRICE')

    dress_name = input('Enter dress name: ').capitalize()
    if dress_name not in dress_catalog:
        print('Dress not found in the catalog.')
        return

    while True:
        try:
            new_price = int(input('Enter new price: '))
            if new_price <= 0:
                print('Price must be greater than zero.')
            else:
                dress_catalog[dress_name]['price'] = new_price
                dress_catalog[dress_name]['rent_price'] = new_price // 2
                print(f'Price for {dress_name} updated to {new_price}.')
                break
        except ValueError:
            print('Invalid input. Please enter a valid integer for price.')

    admin_menu()
    
main_menu()