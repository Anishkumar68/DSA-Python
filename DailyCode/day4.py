
# quiz 
questions = [
    {
        "question": "What is the capital of India?",
        "options": {
            "a": "Delhi",
            "b": "Kolkata",
            "c": "Gurugram",
            "d": "Mumbai"
        },
        "answer": "a"
    },
    {
        "question": "Which language are you learning?",
        "options": {
            "a": "Java",
            "b": "Python",
            "c": "C++",
            "d": "Go"
        },
        "answer": "b"
    }
]

records = []


def quiz_app():
    user_name = input("Enter your name: ")
    score = 0
    for question in questions:
        print(question['question'],"\n", question['options'])
        user_input = input("enter you choice[a-d]: ")
        if user_input == question["answer"]:
            print("correct Answer")
            score +=1
        else: 
            print(f"wrong answer, correct answer is {question['answer']}")
    records.append({"username":user_name, "score": score})

    return records

print(quiz_app())