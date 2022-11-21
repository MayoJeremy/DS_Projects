import management.config as cfg
from management.dbman import Dbman
from budgeter.user import User


def main():
    user_dbman = Dbman()
    #user = User(user_dbman, "Test")
    user = User.register_user_from_form(user_dbman, "Test")
    print(user_dbman)
    print(user)


if __name__ == "__main__":
    main()
