import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)




for i in data:
    print(i["question_text"])
    for index, al in enumerate(i["Alternatives"]):
        print(index+1, al)
    a = int(input("Enter the response: "))
    i["user_choice"]  = a -1 

score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["Correct_ans"]:
        score +=1 
        result = "Correct answer"
    else:
        result = "Wrong answer"

    message = f"{result} - {index + 1 } Your answer: {question["user_choice"] + 1}," \
                f"Correct answer: {question["Correct_ans"]+1 }"
    print(message)




