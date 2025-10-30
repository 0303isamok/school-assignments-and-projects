def quiz():
    quiz_info_list = [ ... ]  # your existing questions

    count = 0
    wrong_awnser = 0
    right_awnser = 0
    print("#"*11)
    print("#QUIZ TIME#")
    print("#"*11)

    user_answers = []  # <-- collect user answers

    for q in quiz_info_list:
        print(f"Question {count + 1}")
        print(q["question"])
        for opt in q["options"]:
            print(opt)

        user_awnser = input("Awnser with (a/b/c/d):").strip().lower()
        user_answers.append(user_awnser)  # <-- remember this answer
        print("_"*24)

        if user_awnser == q["awnser"]:
            right_awnser += 1
        else:
            wrong_awnser += 1
        count += 1

    if count == 10:
        print("Score:")
        print(f"You got {right_awnser} right awnser's!")
        print(f"You got {wrong_awnser} wrong awnser's!")
        print("_"*24)

        letter_to_index = {"a": 0, "b": 1, "c": 2, "d": 3}

        for idx, i in enumerate(quiz_info_list):
            print(i["question"])
            print("Options:")
            for opt in i["options"]:
                print(opt)

            correct_letter = i["awnser"]
            correct_option = i["options"][letter_to_index[correct_letter]]

            ua = user_answers[idx]
            user_option = (
                i["options"][letter_to_index[ua]] if ua in letter_to_index else f"{ua} (invalid)"
            )

            if ua == correct_letter:
                print(f"✅ Right awnser: {correct_option}")
            else:
                print(f"❌ Wrong awnser. You chose: {user_option}")
                print(f"✅ Correct awnser: {correct_option}")

            print("_"*24)
