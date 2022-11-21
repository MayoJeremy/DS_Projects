import management.config as cfg
from management.dbman import Dbman
from budgeter.user import User
from budgeter.wallet import Wallet
from budgeter.transaction import Transaction


def is_Registered():
    return True


def main():
    user_dbman = Dbman()

    isreg = is_Registered()
    user_data_from_db = User.is_user_in_db("Test")
    if user_data_from_db:
        user = User(user_data_from_db[0], user_data_from_db[1])
    else:
        print("User not in DB")
        #user = User.register_user_from_form("Test")
    # user_wallet_1 = Wallet.create_and_add_wallet_to_db(
    #     user, "Geldbeutel", 102.4)
    # print(user_wallet_1)
    print(user_dbman)
    print(user)
    print(user.wallet_list)
    testtrans = Transaction.create_and_add_transaction_to_db(1, 1, 100)
    


if __name__ == "__main__":
    main()
