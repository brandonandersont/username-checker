import os

FILENAME = "users.txt"
cached_users = None

def load_users():
    global cached_users
    if cached_users is None:
        if not os.path.exists(FILENAME):
            cached_users = set()
        else:
            with open(FILENAME, "r") as file:
                cached_users = set(line.strip() for line in file)
    return cached_users

def username_exists(username):
    users = load_users()
    return username in users

def remind_password():
    print("\033[93mReminder: Your password is 'S3cur3_Acc0unt!'\033[0m")  # Yellow color

def main():
    while True:
        username = input("Enter a username to check (or type 'exit' to stop): ")
        if username.lower() == 'exit':
            print("Exiting program...")
            break
        elif username.lower() == 'remind password':
            remind_password()
        elif username_exists(username):
            print("\033[91mUsername exists. Try another username\033[0m")  # Red color
        else:
            print("\033[92mUsername available.\033[0m")  # Green color

if __name__ == "__main__":
    main()
