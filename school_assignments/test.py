info_dict = {
    "username": "M",
    "password": "P"
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

    score = 0
    count = 0
    print("#"*11)
    print("#QUIZ TIME#")
    print("#"*11)

    for q in quiz_info_list:
        print(f"question {count + 1}")
        print(q["question"])
        for opt in q:
            print(opt)
        user_awnser = input("Awnser (a/b/c/d):").strip().lower()
        if user_awnser == q["awnser"]:
            count += 1
            score += 1
            print(f"{user_awnser} is correct!")
            print("Good Job!")
            print("_"*24)
        else:
            count += 1
            print(f"{user_awnser} is the wrong awnser.")
            print("the right awnser was ", q["awnser"] + ".")
            print("_"*24)
        if count == 10:
            print(f"FINAL RATING \n {score} / {count}")




def login_info(username_input, password_input):
    if username_input == info_dict["username"] and password_input == info_dict["password"]:
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