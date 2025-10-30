#made by Isam kartit and Hussain Ghulam
info_dict = {
    "username": "MEK1300",
    "password": "Python"
    }

def quiz():
    quiz_info_list = [{
        "question": "What is the capital of Norway?",
        "options": ["a. Bergen", "b. Oslo", "c. Stavanger", "d. Trondheim"],
        "awnser": "b"
    },
    {
        "question": "what is the currency of Norway?",
        "options": ["a. Euro", "b. Pound", "c. Krone", "d. Deutsche Mark"],
        "awnser": "c"
    },
    {
        "question": "what is the largest city in Norway?",
        "options": ["a. Oslo", "b. Stavanger", "c. Bergen", "d. Trondheim"],
        "awnser": "a"
    },
    {
        "question": "when is constitution day (the national day) of Norway?",
        "options": ["a. 27.May", "b. 17.May", "c. 17.April", "d. 27.April"],
        "awnser": "b"
    },
    {   
        "question": "what color is the background of the Norwegian flag?",
        "options": ["a. Red", "b. White", "c. Blue", "d. Yellow"],
        "awnser": "a"
    },
    {
        "question": "how many countries does Norway boarder?",
        "options": ["a. 1", "b. 2", "c. 3", "d. 4"],
        "awnser": "a"
    },
    {
        "question": "what is the name of the university in Trondheim?",
        "options": ["a. UiS", "b. UiO", "c. NMBU", "d. NTNU"],
        "awnser": "d"
    },
    {
        "question": "How long is the boarder between Norway and Russia?",
        "options": ["a. 96km", "b. 196km", "c. 296km", "d. 396km"],
        "awnser": "b"
    },
    {
        "question": "Where in norway is stavanger?",
        "options": ["a. North", "b. South", "c. South-west", "d. South-east"],
        "awnser": "c"
    },
    {
        "question": "From which Norwegian city did the world’s famous composer Edvard Grieg come?",
        "options": ["a. Oslo", "b. Bergen", "c. Stavanger", "d. Tromsø"],
        "awnser": "b"

    }]
    total_awnser_wrong = []
    total_awnser_right = []
    count = 0
    wrong_awnser = 0
    right_awnser = 0
    print("#"*11)
    print("#QUIZ TIME#")
    print("#"*11)

    for q in quiz_info_list:
        print(f"Question {count + 1}")
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        user_awnser = input("Awnser with (a/b/c/d):").strip().lower()
        print("_"*24)
        if user_awnser == q["awnser"]:
            right_awnser += 1
            count += 1
            total_awnser_right.append(user_awnser)
        else:
            wrong_awnser += 1
            count += 1
            total_awnser_wrong.append(user_awnser)

        if count == 10:
            print("Score:")
            print(f"You got {right_awnser} right awnser's!")
            print(f"You got {wrong_awnser} wrong awnser's!")
            print("_"*24)
            for i in quiz_info_list:
                print(i["question"])
                print("Options:")
                for opt in i["options"]:
                    print(opt)
                if user_awnser == i["awnser"]:
                    print(f"You guessed {}!")
                    print(f"the correct awnser was {user_awnser}")
                    print("_"*24)
                else:
                    print(f"Wrong awnser!")
                    print(f"You guessed {user_awnser}")
                    wrong = i["awnser"]
                    print(f"the right awnser was {wrong}")
                    print("_"*24)
                    



def login_info(log_dict, username_input, password_input):
    username_ok = username_input == log_dict["username"]
    password_ok = password_input == log_dict["password"]
    if username_ok == True and password_ok == True:
        print("login succeeded")
        return True
    else:
        print("Invalid username and/or password")
        return False


while True:
    username_input = str(input("type your username here:")).strip()
    login_input = str(input("type your password here:")).strip()

    if login_info(info_dict, username_input, login_input) == True:
        quiz()
        break