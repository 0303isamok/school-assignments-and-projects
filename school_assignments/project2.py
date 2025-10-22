
info = {
    "username": "M",
    "password": "P"
    }

def quiz():
    count = 0
    print("#"*11)
    print("#QUIZ TIME#")
    print("#"*11)
    print("What is the capital of Norway? \n a. Bergen \n b. Oslo \n c. Stavanger \n d. Trondheim")
    awnser_1 = str(input("Awnser:   ")).strip().capitalize()
    if awnser_1 == "Oslo":
        print("that's correct!")
        count += 1
    else:
        print("What is the capital of Norway? \n a. Bergen \n b. Oslo \n c. Stavanger \n d. Trondheim")
        print(f"You awnsered {awnser_1}", end=" | ")
        print("the right awnser was Oslo.")


def login_info(username_input, password_input):
    if username_input == info["username"] and password_input == info["password"]:
        print("login succeeded")
        return True
    else:
        print("invalid username and/or password")
        return False

while True:
    username_input = str(input("type your username here")).strip()
    username_input = username_input.upper()
    login_input = str(input("type your password here:")).strip()
    login_input = login_input.capitalize()

    if login_info(username_input, login_input) == True:
        quiz()
        break