import time

questions=["1. Who is the father of the nation?","2. Who was the first Prime Minister of independent India?",
           "3. What is the currency of India?",
           '''4. Who composed the Indian national anthem, "Jana Gana Mana"?''',
           "5. Who is known as the Father of the Indian Constitution?"]

options=[["a. Jawaharlal Nehru","b. Mahatma Gandhi","c. Narendra Modi","d. Bhagat Singh"],
         ["a. Mahatma Gandhi","b. Dr. Rajendra Prasad","c. Jawaharlal Nehru", "d. B.R Ambedkar"],
         ["a. Dollar","b. Rupee","c. Euro","d. Yen"],
         ["a. Rabindranath Tagore","b. Bankim Chandra Chatterjee","c. Lata Mangeshkar","d. Satyajit Ray"],
         ["a. Jawaharlal Nehru","b. Sardar Vallabhbhai Patel","c. Rajendra Prasad","d. B.R Ambedkar"]]

answers=['b','c',"b","a", "d"]

score=0
total_score=0

for i in range(len(questions)):
    start_time=time.time()
    print(questions[i])
    for option in options[i]:
        print(option)
    user_answer=input("Answer: ")
    end_time=time.time()

    if end_time-start_time<=10:
        if user_answer==answers[i]:
            score=score+1
            print('Correct. Score:', score)
        else:
            print('Incorrect. Score:', score)
    else:
        print('Time out!')
        print('Score:', score)

total_score += score
print(f'Total Score:{total_score}/5')
if total_score >= 3:
    print('You Successfully Passed')
else:
    print('Better Luck Next Time')
