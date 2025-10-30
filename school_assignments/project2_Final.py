#made by Isam kartit and Hussain Ghulam
info_dict = {
    "username": "MEK1300",
    "password": "Python"
}

def quiz():
    quiz_info_list = [{
        "question": "What is the capital of Norway?",
        "options": ["a. Bergen", "b. Oslo", "c. Stavanger", "d. Trondheim"],
        "answer": "b"
    },
    {
        "question": "what is the currency of Norway?",
        "options": ["a. Euro", "b. Pound", "c. Krone", "d. Deutsche Mark"],
        "answer": "c"
    },
    {
        "question": "what is the largest city in Norway?",
        "options": ["a. Oslo", "b. Stavanger", "c. Bergen", "d. Trondheim"],
        "answer": "a"
    },
    {
        "question": "when is constitution day (the national day) of Norway?",
        "options": ["a. 27.May", "b. 17.May", "c. 17.April", "d. 27.April"],
        "answer": "b"
    },
    {   
        "question": "what color is the background of the Norwegian flag?",
        "options": ["a. Red", "b. White", "c. Blue", "d. Yellow"],
        "answer": "a"
    },
    {
        "question": "how many countries does Norway boarder?",
        "options": ["a. 1", "b. 2", "c. 3", "d. 4"],
        "answer": "c"
    },
    {
        "question": "what is the name of the university in Trondheim?",
        "options": ["a. UiS", "b. UiO", "c. NMBU", "d. NTNU"],
        "answer": "d"
    },
    {
        "question": "How long is the boarder between Norway and Russia?",
        "options": ["a. 96km", "b. 196km", "c. 296km", "d. 396km"],
        "answer": "b"
    },
    {
        "question": "Where in norway is stavanger?",
        "options": ["a. North", "b. South", "c. South-west", "d. South-east"],
        "answer": "c"
    },
    {
        "question": "From which Norwegian city did the world’s famous composer Edvard Grieg come?",
        "options": ["a. Oslo", "b. Bergen", "c. Stavanger", "d. Tromsø"],
        "answer": "b"
    }]

    count = 0
    wrong_answer = 0
    right_answer = 0
    user_answers = []

    print("#"*11)
    print("#QUIZ TIME#")
    print("#"*11)

    for q in quiz_info_list:
        print(f"Question {count + 1}")
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        user_answer = input("answer with (a/b/c/d):").strip().lower()
        user_answers.append(user_answer)
        print("_"*24)
        if user_answer == q["answer"]:
            right_answer += 1
            count += 1
        else:
            wrong_answer += 1
            count += 1

        if count == 10:
            print("Score:")
            print(f"You got {right_answer} right answer's!")
            print(f"You got {wrong_answer} wrong answer's!")
            print("_"*24)
            
            ind = 0
            while ind < len(quiz_info_list):
                i = quiz_info_list[ind]
                print(i["question"])
                print("Options:")

                for opt in i["options"]:
                    print(opt)

                correct_answer = i["answer"]
                ua = user_answers[ind]

                if ua == correct_answer:
                    print(f"Your answer was: {ua}")
                    print("That's the right answer!")
                    print("_"*24)
                else:
                    print(f"Your answer was: {ua}")
                    print("That's the wrong answer!")
                    new_right_answer = i["answer"]
                    print(f"The right answer was: {new_right_answer}")
                    print("_"*24)
                ind += 1

def login_info(log_dict, username_input, password_input):
    username_ok = username_input == log_dict["username"]
    password_ok = password_input == log_dict["password"]
    if username_ok == True and password_ok == True:
        print("login succeeded!")
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
