import time
import sys
dress_catalog = { 
    'Eliana': {'size': {'XS': 3, 'S': 5, 'M': 4, 'L': 4, 'XL': 3}, 'price': 1600},
    'Evelyn': {'size': {'XS': 2, 'S': 4, 'M': 5, 'L': 3, 'XL': 3}, 'price': 2300}, 
    'Amelia': {'size': {'XS': 4, 'S': 3, 'M': 4, 'L': 5, 'XL': 2}, 'price': 2100},
    'Cecily': {'size': {'XS': 2, 'S': 3, 'M': 3, 'L': 5, 'XL': 2}, 'price': 1800},
    'Vivien': {'size': {'XS': 5, 'S': 2, 'M': 3, 'L': 4, 'XL': 5}, 'price': 2600},
    'Yvette': {'size': {'XS': 2, 'S': 4, 'M': 5, 'L': 3, 'XL': 3}, 'price': 1400},
    'Daphne': {'size': {'XS': 0, 'S': 5, 'M': 2, 'L': 5, 'XL': 4}, 'price': 2200}
}

for dress, details in dress_catalog.items():
    details['rent_price'] = details['price'] // 2

user_acc = {}
user_cart = {}
user_invent = {}
user_history = {}
admin_user = 'admin'
admin_pass = 'password'
x = '*'
seperator = '-'*82

def text_appear_Time(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

def main_menu():
    print()
    print(f"{x*30} YEN'S DRESS BOUTIQUE {x*30}\n")
    print('\t(1) Sign-up')
    print('\t(2) Log-in')
    print('\t(3) Exit')
    print()
    print(seperator)

    while True:
        try:
            choice = input('\nChoose an option: ').strip()
            if not choice:
                continue
            choice = int(choice)
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
    print()
    print(f'{x*25} REGISTER TO CREATE AN ACCOUNT {x*26}')
    print()
    username = input('Enter username: ').strip()
    while username in user_acc:
        print('\nUsername already taken.\n')
        username = input('Enter username: ').strip()
    
    if not username:
        main_menu()

    password = input('Enter password: ').strip()
    if not password:
        main_menu()
    else: 
        while len(password) < 8:
            print('\nPassword must be at least 8 characters.\n')
            password = input('Enter password: ').strip()
      
    balance = 0
    
    user_acc[username] = {'username': username, 'password': password, 'balance': balance}
    
    print()
    print(seperator)
    text_appear_Time(f'\nWelcome {username}! Thank you for joining us. ', 0.03)
    input('\nPress enter to continue.')
    login()

def login():
    print(f'\n{x*29} LOG IN TO YOUR ACCOUNT {x*29}\n')
   
    while True:
        username = input('Enter username: ').strip()

        if not username:
            main_menu()

        password = input('Enter password: ').strip()

        if not password:
            main_menu()

        if username == admin_user and password == admin_pass:
            admin_menu()
        elif username in user_acc and user_acc[username]['password'] == password:
            print()
            print(seperator)
            text_appear_Time(f'\nWelcome back {username}! Thank you for joining us. ', 0.03)
            input('\nPress enter to continue.')
            user_menu(username)
        else:
            print('\nIncorrect username or password.\n')

def user_menu(username):
    print(f"\n{x*30} YEN'S DRESS BOUTIQUE {x*30}\n")
    print('\t(1) View E-Wallet')
    print('\t(2) Browse dresses')
    print('\t(3) Return a dress')
    print('\t(4) View cart')
    print('\t(5) View Purchase History')
    print('\t(6) Exit')
    print()
    print(seperator) 

    while True:
        try:
            choice = input('\nChoose an option: ').strip()
            if not choice:
                continue
            choice = int(choice)
            if choice == 1:
                e_wallet(username)
            elif choice == 2:
                view_dresses(username)
            elif choice == 3:
                return_dress(username)
            elif choice == 4:
                cart(username)
            elif choice == 5:
                purchase_history(username)
            elif choice == 6:
                main_menu()
            else:
                print('\nInvalid input.')

        except ValueError:
            print('\nInvalid input.')

def e_wallet(username):
    while True:
        print(f'\n{x*28} WELCOME TO YOUR E-WALLET {x*28}\n')
        print(f'\tBalance: {user_acc[username]["balance"]}')
        print()
        print('\t(1) Deposit')
        print('\t(2) Withdraw')
        print('\t(3) Exit')
        print()
        print(seperator)

        try:
            choice = input('\nChoose an option: ').strip()

            if not choice:
                user_menu(username)

            choice = int(choice)

            if choice == 1:
                add_balance = int(input('\nEnter the amount to be deposited: '))
                if add_balance < 0:
                    text_appear_Time('\nYou cannot deposit a negative number.\n', 0.03)
                    input('Press enter to return to wallet.')
                    continue
                else:
                    user_acc[username]['balance'] += add_balance
            elif choice == 2:
                draw_balance = int(input('\nEnter amount to be withdrawn: '))
                if draw_balance > user_acc[username]['balance']:
                    text_appear_Time('\nYou cannot withdraw amount exceeding your current balance.\n', 0.03)
                    input('Press enter to return to wallet.')
                    continue
                else:
                    user_acc[username]['balance'] -= draw_balance
            elif choice == 3:
                user_menu(username)
            else:
                print('\nInvalid input.')
                input('\nPress enter to return to wallet.')
                continue 
        except ValueError:
            print('\nInvalid input.')
            input('\nPress enter to return to wallet.')
            continue  


def view_dresses(username):
    print(f'\n{x*34} DRESS CATALOG {x*34}')
    for dress, details in dress_catalog.items():
        text_appear_Time(f"\n\t{dress}", 0.03)
        text_appear_Time(f"\t\tPrice: {details['price']}", 0.03)
        text_appear_Time(f"\t\tRent Price: {details['rent_price']}", 0.03)

        available_sizes = [size for size, quantity in details['size'].items() if quantity > 0]
        if available_sizes:
            text_appear_Time("\t\tSizes available: " + ", ".join(available_sizes), 0.03)
        else:
            text_appear_Time("\t\tNo sizes available", 0.03)

    print(seperator)
    print('\n\t(1) Select a dress')
    print('\t(2) View cart')
    print('\t(3) Exit')
    print(seperator)

    while True:
        try:
            choice = input('\nChoose an option: ').strip()
            if not choice:
                continue
            choice = int(choice)
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
        print(seperator)
        selected_dress = input('\nSelect a dress: ').capitalize().strip()
        if not selected_dress:
            user_menu(username)
            break
        if selected_dress not in dress_catalog:
            print(seperator)
            text_appear_Time('\nDress not in system.', 0.03)
            continue  
        else:
            selected_size = input('Select size: ').upper().strip()
            if not selected_size:
                view_dresses(username)
                break
            if selected_size not in dress_catalog[selected_dress]['size']:
                print(seperator)
                text_appear_Time('\nSize not available.', 0.03)
                continue  
            elif dress_catalog[selected_dress]['size'][selected_size] == 0:
                print(seperator)
                text_appear_Time('\nSelected size is out of stock.', 0.03)
                continue 
            else:
                quantity = input('Enter quantity: ').strip()
                if not quantity:
                    view_dresses(username)
                    break
                quantity = int(quantity)
                if quantity > dress_catalog[selected_dress]['size'][selected_size]:
                    print(seperator)
                    text_appear_Time('\nRequested quantity exceeds available stock.', 0.03)
                    continue 
                else:
                    if selected_dress not in user_cart[username]:
                        user_cart[username][selected_dress] = {'size': selected_size, 'quantity': quantity, 'price': dress_catalog[selected_dress]['price'], 'rent_price': dress_catalog[selected_dress]['rent_price']}
                    else:
                        user_cart[username][selected_dress]['quantity'] += quantity
                    dress_catalog[selected_dress]['size'][selected_size] -= quantity
                    print(seperator)
                    text_appear_Time('\nItem successfully added to cart.', 0.03)

                    while True:
                        print(seperator)
                        print('\t(1) Keep Shopping')
                        print('\t(2) View Cart')
                        print('\t(3) Return to User Menu')
                        print('\t(4) Proceed to Checkout')
                        print(seperator)

                        try:
                            choice = input('\nChoose an option: ').strip()
                            if not choice:
                                continue
                            choice = int(choice)
                            if choice == 1:
                                break  
                            elif choice == 2:
                                cart(username)
                                break
                            elif choice == 3:
                                user_menu(username)
                                break 
                            elif choice == 4:
                                checkout(username)
                                break 
                            else:
                                print('\nInvalid input.')
                        except ValueError:
                            print('\nInvalid input.')


def cart(username):
    print(f'\n{x*30} WELCOME TO YOUR CART {x*30}')

    if username not in user_cart or not user_cart[username]:
        text_appear_Time("\n\t\t\t\tYour cart is empty.", 0.03)
        input("\nPress enter to return to the menu.")
        user_menu(username)
        return

    total_price = 0

    for dress, details in user_cart[username].items():
        text_appear_Time(f'\n\t{dress}', 0.03)
        text_appear_Time(f'\t\tSize: {details["size"]}', 0.03)
        text_appear_Time(f'\t\tQuantity: {details["quantity"]}', 0.03)
        text_appear_Time(f'\t\tPrice: {details["price"]}', 0.03)
        text_appear_Time(f'\t\tRent Price: {details["rent_price"]}', 0.03)
        total_price += details["price"] * details["quantity"]

    text_appear_Time(f'\n\tTotal Price: {total_price}', 0.03)

    
    
    while True:
        print(seperator)
        print('\n\t(1) Edit cart')
        print('\t(2) Checkout')
        print('\t(3) Exit')
        print(seperator)

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
    print(f'\n{x*37} EDIT CART {x*37}')

    while True:
        edit_dress = input('\nEnter the dress to be edited: ').capitalize()
        if not edit_dress:
            cart(username)
            return
        elif edit_dress not in user_cart[username]:
            if edit_dress in dress_catalog:
                print('\nDress not in cart.')
            else:
                print('\nInvalid input.')
            continue

        info = user_cart[username][edit_dress]

        while True:
            print(f'\n{x*30} EDIT {edit_dress.upper()} {x*30}')
            print('\nt\(1) Edit size')
            print('\t(2) Edit quantity')
            print('\t(3) Remove dress from cart')
            print('\t(4) Exit')
            print(seperator)

            try:
                choice = int(input('\nChoose an option: '))
                if choice == 1:
                    while True:
                        print(seperator)
                        print(f'\nCurrent size: {info["size"]}')
                        new_size = input('\nEnter new size: ').upper()
                        available_sizes = [size for size, quantity in dress_catalog[edit_dress]['size'].items() if quantity > 0]
                        
                        if not new_size:
                            cart(username)
                            return
                        elif new_size in available_sizes:
                            quantity_for_new_size = dress_catalog[edit_dress]['size'].get(new_size, 0)
                            if quantity_for_new_size < info['quantity']:
                                print(seperator)
                                text_appear_Time('\nThis size does not have enough stock for the quantity you have in your cart.', 0.03)
                            else:
                                info['size'] = new_size
                                print(seperator)
                                text_appear_Time(f'\nSize of {edit_dress} has been updated to {new_size}!', 0.03)
                        else:
                            print(seperator)
                            text_appear_Time('\nSize out of stock.', 0.03)

                elif choice == 2:
                    print(seperator)
                    print(f'\nCurrent quantity: {info["quantity"]}')
                    while True:
                        try:
                            new_quantity = int(input('\nEnter new quantity: '))
                            catalog_quantity = dress_catalog[edit_dress]['size'][info['size']]

                            if new_quantity <= 0:
                                print(seperator)
                                text_appear_Time('\nQuantity must be greater than zero.\n', 0.03)
                            elif new_quantity > catalog_quantity + info['quantity']:
                                print(seperator)
                                text_appear_Time('\nYou have reached the maximum quantity available for this item.\n', 0.03)
                            else:
                                dress_catalog[edit_dress]['size'][info['size']] += info['quantity']
                                info['quantity'] = new_quantity
                                dress_catalog[edit_dress]['size'][info['size']] -= new_quantity
                                print(seperator)
                                text_appear_Time(f'\nQuantity of {edit_dress} Updated to {new_quantity}!', 0.03)
                                input('\nPress enter to go back to cart.')
                                cart(username)
                        except ValueError:
                            print(seperator)
                            text_appear_Time('\nInvalid input. Please enter a valid integer for quantity.\n', 0.03)

                elif choice == 3:
                    dress_catalog[edit_dress]['size'][info['size']] += info['quantity']
                    user_cart[username].pop(edit_dress)
                    print(seperator)
                    text_appear_Time(f'\n{edit_dress} has been removed from the cart.', 0.03)

                elif choice == 4:
                    cart(username)
                    return
                
                elif not choice:
                    cart(username)
                    return
                else:
                    print('\nInvalid input.\n')
            except ValueError:
                print('\nInvalid input.\n')

def checkout(username):
    print(f'\n{x*36} CHECKOUT {x*36}')
    total_price = 0
    total_rent_price = 0

    if username not in user_cart:
        user_cart[username] = {}

    if not user_cart[username]:
        text_appear_Time("\t\t\tYour cart is empty.", 0.03)
    else:
        for dress, details in user_cart[username].items():
            text_appear_Time(f'\n\t{dress}', 0.03)
            text_appear_Time(f'\t\tSize: {details["size"]}', 0.03)
            text_appear_Time(f'\t\tQuantity: {details["quantity"]}', 0.03)
            text_appear_Time(f'\t\tPrice: {details["price"]}', 0.03)
            text_appear_Time(f'\t\tRent Price: {details["rent_price"]}', 0.03)
            total_price += details["price"] * details["quantity"]
            total_rent_price += details["rent_price"] * details["quantity"]

        text_appear_Time(f'\n\tTotal Purchasing Price: {total_price}', 0.03)
        text_appear_Time(f'\tTotal Renting Price: {total_rent_price}', 0.03)

        while True:
            print(seperator)
            purchase_option = input('\nWould you like to rent or buy? (R/B): ').strip().lower()
            if purchase_option == 'r':
                print(f'\n{x*33} ITEMS TO RENT {x*34}')
                for dress, details in user_cart[username].items():
                    text_appear_Time(f'\n\t{dress}', 0.03)
                    text_appear_Time(f'\t\tSize: {details["size"]}', 0.03)
                    text_appear_Time(f'\t\tQuantity: {details["quantity"]}', 0.03)
                    text_appear_Time(f'\t\tPrice: {details["price"]}', 0.03)
                    text_appear_Time(f'\t\tRent Price: {details["rent_price"]}', 0.03)
                
                total_rent_price += 1000
                text_appear_Time('\n\tSafety Deposit: 1000', 0.03)
                text_appear_Time(f'\n\tTotal Rent Price: {total_rent_price}', 0.03) 
                print(seperator)
                print('\n\t(1) Proceed with the rent')
                print('\t(2) Go back to cart')
                print(seperator)
                proceed_option = input('\nChoose an option: ').strip()
                if proceed_option == '1':
                    if user_acc[username]['balance'] < total_price:
                        print(seperator)
                        text_appear_Time("\nInsufficient balance. Please deposit more funds.", 0.03)
                        input('\nPress enter to go back to menu.')
                        user_menu(username)
                    else:
                        total_price = process_rent(username)
                    break
                elif proceed_option == '2':
                    cart(username)
                else:
                    print('Invalid option. Please choose 1 or 2.')

            elif purchase_option == 'b':
                print(f'\n{x*30} ITEMS TO PURCHASE {x*30}')
                for dress, details in user_cart[username].items():
                    text_appear_Time(f'\n\t{dress}', 0.03)
                    text_appear_Time(f'\t\tSize: {details["size"]}', 0.03)
                    text_appear_Time(f'\t\tQuantity: {details["quantity"]}', 0.03)
                    text_appear_Time(f'\t\tPrice: {details["price"]}', 0.03)
                    text_appear_Time(f'\t\tRent Price: {details["rent_price"]}', 0.03)
                    text_appear_Time(f'\n\tTotal Price: {total_price}', 0.03)
                    print(seperator)
                print('\n\t(1) Proceed with the purchase')
                print('\t(2) Go back to cart')
                print(seperator)
                proceed_option = input('\nChoose an option: ').strip()
                if proceed_option == '1':
                    if user_acc[username]['balance'] < total_price:
                        print(seperator)
                        text_appear_Time("\nInsufficient balance. Please deposit more funds.", 0.03)
                        input('\nPress enter to go back to menu.')
                        user_menu(username)
                    else:
                        total_price = process_purchase(username)
                    break
                elif proceed_option == '2':
                    cart(username)
                else:
                    text_appear_Time('Invalid option. Please choose 1 or 2.', 0.03)
            else:
                text_appear_Time('Invalid option. Please choose "R" to rent or "B" to buy.', 0.03)

        input('\nPress enter to go back to the menu.')

def process_purchase(username):
    total_price = 0
    if username not in user_history:
        user_history[username] = {}
        for dress, details in user_cart[username].items():
            if dress not in user_history[username]:
                user_history[username][dress] = {'size': details['size'], 'quantity': details['quantity'], 'rented': False, 'bought': True}
            else:
                user_history[username][dress]['quantity'] += details['quantity']
                user_history[username][dress]['bought'] = True
            total_price += details['price'] * details['quantity']

    print(seperator)
    text_appear_Time('\nPurchase Processing.....', 0.08)

    print(f'\n{x*33} RECEIPT FOR RENT {x*33}')
    text_appear_Time('\n\tQuantity\t\tStyle\t\t\tPrice\n', 0.03)
    for dress, details in user_cart[username].items():
        text_appear_Time(f'\t   {details["quantity"]}\t\t\t\t\t{dress}\t\t\t{details["price"]*details["quantity"]}', 0.03)
    
    text_appear_Time(f'\n\tTotal:\t\t\t\t\t\t\t{total_price}', 0.03)
    print(seperator)
    text_appear_Time('\nThank you for your purchase!', 0.03)
    user_cart[username] = {}

    user_acc[username]['balance'] -= total_price
    input("\nPress enter to return to menu.")
    user_menu(username)

def process_rent(username):
    total_price = 0
    
    if username not in user_history:
        user_history[username] = {}
        for dress, details in user_cart[username].items():
            if dress not in user_history[username]:
                user_history[username][dress] = {'size': details['size'], 'quantity': details['quantity'], 'rented': True, 'bought': False}
            else:
                user_history[username][dress]['quantity'] += details['quantity']
                user_history[username][dress]['rented'] = True
            total_price += details['rent_price'] * details['quantity']

    print(seperator)
    text_appear_Time('\nRent Processing.....', 0.08)

    print(f'\n{x*33} RECEIPT FOR RENT {x*33}')
    text_appear_Time('\n\tQuantity\t\t\tStyle\t\t\tPrice\n', 0.03)
    for dress, details in user_cart[username].items():
        rent_price = details["price"]//2
        text_appear_Time(f'\t   {details["quantity"]}\t\t\t\t{dress}\t\t\t{rent_price*details["quantity"]}', 0.03)
    
    total_price += 1000
    text_appear_Time("\n\tSafety Deposit:\t\t\t\t\t\t1000", 0.03)
    text_appear_Time(f'\n\tTotal:\t\t\t\t\t\t\t{total_price}', 0.03)
    print(seperator)
    text_appear_Time('\nThank you for renting!', 0.03)
    user_cart[username] = {}

    user_acc[username]['balance'] -= total_price
    input("\nPress enter to return to menu.")
    user_menu(username)

def return_dress(username):
    print(f'\n{x*35} RETURN A DRESS {x*35}')
    if username not in user_history:
        text_appear_Time("\n\t\tYou haven't rented any dresses yet.", 0.03)
        input("\nPress enter to return to menu.")
        user_menu(username)
    else:
        text_appear_Time('\nItems Currently Rented:', 0.03)
        for dress, details in user_history[username].items():
            if details['rented'] == True:
                text_appear_Time(f'\n\t{dress}', 0.03)
                text_appear_Time(f'\t\tSize: {details["size"]}', 0.03)
                text_appear_Time(f'\t\tQuantity: {details["quantity"]}', 0.03)

        while True:
            print(seperator)
            return_choice = input('\nEnter the name of the dress you want to return (leave blank to go back): ').capitalize().strip()
            if not return_choice:
                user_menu(username)
                break
            elif return_choice not in user_history[username]:
                text_appear_Time('\nYou have not rented or purchased this dress.', 0.03)
                continue
            elif return_choice in user_history[username] and user_history[username][return_choice]['quantity'] == 0:
                text_appear_Time('\nYou have returned all quantities of this dress.', 0.03)
                continue
            else:
                return_quantity = int(input('Enter the quantity you want to return: '))
                if return_quantity > user_history[username][return_choice]['quantity']:
                    text_appear_Time("\nYou don't have that many dresses to return.", 0.03)
                    continue
                elif return_quantity <= 0:
                    print("\nInvalid quantity.")
                    continue
                else:
                    user_history[username][return_choice]['quantity'] -= return_quantity
                    dress_catalog[return_choice]['size'][user_history[username][return_choice]['size']] += return_quantity
                    text_appear_Time("\nDress successfully returned!", 0.03)
                    break

        input("\nPress enter to return to menu.")
        user_menu(username)

def purchase_history(username):
    print(f'\n{x*32} PURCHASE HISTORY {x*33}')
    if username not in user_history:
        text_appear_Time("\n\t\tYou haven't rented or purchased any dresses yet.", 0.03)
        input("\nPress enter to return to menu.")
        user_menu(username)
    else:
        for dress, details in user_history[username].items():
            text_appear_Time("\nDresses Purchased:", 0.03)
            if details['bought'] == True:
                    text_appear_Time(f'\n\t{dress}', 0.03)
                    text_appear_Time(f'\t\tSize: {details["size"]}', 0.03)
                    text_appear_Time(f'\t\tQuantity: {details["quantity"]}', 0.03)
                    text_appear_Time('')
            else:
                text_appear_Time('\n\tiNo Dresses Purchased.', 0.03)

            text_appear_Time("\nDresses Rented:", 0.03)
            if details['bought'] == False:
                    text_appear_Time(f'\n\t{dress}', 0.03)
                    text_appear_Time(f'\t\tSize: {details["size"]}', 0.03)
                    text_appear_Time(f'\t\tQuantity: {details["quantity"]}', 0.03)
            else:
                text_appear_Time('\n\tNo Dresses Rented.', 0.03)

        input("\nPress enter to return to menu.")
        user_menu(username)

def admin_menu():
    print(f"\n{x*35} ADMIN MENU {x*35}\n")
    print("\t(1) Add Dress to Catalog")
    print("\t(2) Edit Dress Quantity")
    print("\t(3) Edit Dress Price")
    print("\t(4) View Dress Catalog")
    print("\t(5) View User Accounts")
    print("\t(6) View User Purchase History")
    print("\t(7) Logout")
    print(seperator)

    while True:
        try:
            choice = int(input("\nChoose an option: "))
            if choice == 1:
                add_new_dress()
            elif choice == 2:
                edit_dress_quantity()
            elif choice == 3:
                edit_dress_price()
            elif choice == 4:
                view_dress_catalog()
            elif choice == 5:
                view_user_accounts()
            elif choice == 6:
                view_user_purchase_history()
            elif choice == 7:
                main_menu()
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_new_dress():
    print(f'\n{x*28} ADD NEW DRESS TO CATALOG {x*28}')
    dress_name = input('\nEnter dress name: ').capitalize()
    print()

    while dress_name in dress_catalog:
        text_appear_Time('Dress already exists in the catalog.', 0.03)
        continue
    
    if not dress_name:
        admin_menu()
        return

    dress_catalog[dress_name] = {'size': {'XS': 0, 'S' : 0, 'M' : 0, 'L' : 0, 'XL': 0}, 'price': 0}

    while True:
        all_sizes_filled = True
        for size in dress_catalog[dress_name]['size']:
            quantity = input(f'Enter quantity for size {size}: ').strip()
            if not quantity:
                admin_menu()
                return
            try:
                quantity = int(quantity)
                if quantity < 0:
                    text_appear_Time('\nQuantity must be a non-negative integer.', 0.03)
                    all_sizes_filled = False
                    break
                dress_catalog[dress_name]['size'][size] = quantity
            except ValueError:
                text_appear_Time('\nInvalid input. Please enter a valid integer for quantity.', 0.03)
                all_sizes_filled = False
                break
        if all_sizes_filled:
            break

    while True:
        try:
            price = int(input('\nEnter price of the dress: '))
            if price <= 0:
                text_appear_Time('\nPrice must be greater than zero.', 0.03)
            else:
                dress_catalog[dress_name]['price'] = price
                dress_catalog[dress_name]['rent_price'] = price // 2
                break
        except ValueError:
            text_appear_Time('\nInvalid input. Please enter a valid integer for price.', 0.03)

    print(seperator)
    text_appear_Time(f'\n{dress_name} has been added to the catalog.', 0.03)
    input('\nPress enter to go back to menu.')
    admin_menu()

def edit_dress_quantity():
    print(f'\n{x*32} EDIT DRESS QUANTITY {x*32}')

    dress_name = input('\nEnter dress name: ').capitalize()
    if dress_name not in dress_catalog:
        text_appear_Time('Dress not found in the catalog.', 0.03)
        return

    size = input('Enter size to be edited: ').upper()
    if size not in dress_catalog[dress_name]['size']:
        text_appear_Time('Size not found for this dress.', 0.03)
        return

    while True:
        try:
            quantity_to_add = int(input('Enter quantity to be added: '))
            if quantity_to_add <= 0:
                text_appear_Time('\nQuantity must be greater than zero.', 0.03)
                continue
            else:
                dress_catalog[dress_name]['size'][size] += quantity_to_add
                print(seperator)
                text_appear_Time(f'\nSize {size} for {dress_name} has added {dress_catalog[dress_name]["size"][size]} to its quantity.', 0.03)
                break
        except ValueError:
            text_appear_Time('\nInvalid input. Please enter a valid integer for quantity.', 0.03)
            continue

    input('\nPress enter to return to menu: ')
    admin_menu()

def edit_dress_price():
    print(f'\n{x*33} EDIT DRESS PRICE {x*33}')

    dress_name = input('\nEnter dress name: ').capitalize()
    if dress_name not in dress_catalog:
        text_appear_Time('Dress not found in the catalog.', 0.03)
        return

    while True:
        try:
            new_price = int(input('Enter new price: '))
            if new_price <= 0:
                text_appear_Time('Price must be greater than zero.', 0.03)
                continue
            else:
                dress_catalog[dress_name]['price'] = new_price
                dress_catalog[dress_name]['rent_price'] = new_price // 2
                print(seperator)
                text_appear_Time(f'\nPrice for {dress_name} updated to {new_price}.', 0.03)
                break
        except ValueError:
            text_appear_Time('\nInvalid input. Please enter a valid integer for price.', 0.03)
            continue
    
    input('\nPress enter to return to menu: ')
    admin_menu()

def view_dress_catalog():
    print(f'\n{x*34} DRESS CATALOG {x*34}')
    for dress, details in dress_catalog.items():
        text_appear_Time(f"\n\t{dress}", 0.03)
        text_appear_Time(f"\t\tPrice: {details['price']}", 0.03)
        text_appear_Time(f"\t\tRent Price: {details['rent_price']}", 0.03)

        available_sizes = [size for size, quantity in details['size'].items() if quantity > 0]
        if available_sizes:
            text_appear_Time("\t\tSizes available: " + ", ".join(available_sizes), 0.03)
        else:
            text_appear_Time("\t\tNo sizes available", 0.03)
    
    print(seperator)
    input('\nPress enter to return to menu: ')
    admin_menu() 

def view_user_accounts():
    print(f"\n{x*36} USER ACCOUNTS {x*36}")
    if not user_acc:
        text_appear_Time("\n\t\t\t\tNo user accounts in system.", 0.03)
        input("\nPress enter to return to the menu.")
        admin_menu()
        return

    for username, details in user_acc.items():
        text_appear_Time(f"\n\t\tUsername: {username}", 0.03)
        text_appear_Time(f"\t\tPassword: {details['password']}", 0.03)
        text_appear_Time(f"\t\tBalance: {details['balance']}", 0.03)

    print(seperator)
    input('\nPress enter to return to menu: ')
    admin_menu()

def view_user_purchase_history():
    print(f"\n{x*36} USER PURCHASE HISTORY {x*36}")
    if not user_history:
        text_appear_Time("\n\t\t\t\tNo purchase history available.", 0.03)
        input("\nPress enter to return to the menu.")
        admin_menu()
        return
    
    for username, history in user_history.items():
        text_appear_Time(f"\n\t{username}'s Purchase History:", 0.03)
        for dress, details in history.items():
            text_appear_Time(f"\n\t\t{dress}", 0.03)
            text_appear_Time(f"\t\t\tSize: {details['size']}", 0.03)
            text_appear_Time(f"\t\t\tQuantity: {details['quantity']}", 0.03)
            if details['rented']:
                text_appear_Time("\t\t\tTransaction Type: Rent", 0.03)
            elif details['bought']:
                text_appear_Time("\t\t\tTransaction Type: Purchase", 0.03)

    print(seperator)
    input('\nPress enter to return to menu: ')
    admin_menu()

main_menu()
