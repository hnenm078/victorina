print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы: ")

score = 0

questions = ["1. Как называется компания, которая создается для развития новой идеи или инновационного продукта?",
             "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
             "3. Как называется капитал, который дают инвесторы на развитие стартапа?" ,
             "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?",
             "5. Какой план создают перед тем, как открывать стартап и занимать деньги?",
             "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?",
             "7. Как называется разница между выручкой и затратами компании?"]
answers = ["Стартап", "Инвестор", "Инвестиция", "MVP", "Бизнес-план", "Конкуренты", "Прибыль"]
number = 0

print(questions[number])
user_input = input("введите ответ: ")
if user_input.lower() == answers[number].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")
number += 1

print(questions[number])
user_input = input("введите ответ: ")
if user_input.lower() == answers[number].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")
number += 1

print(questions[number])
user_input = input("введите ответ: ")
if user_input.lower() == answers[number].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")
number += 1

print(questions[number])
user_input = input("введите ответ: ")
if user_input.lower() == answers[number].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")
number += 1

print(questions[number])
user_input = input("введите ответ: ")
if user_input.lower() == answers[number].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")
number += 1

print(questions[number])
user_input = input("введите ответ: ")
if user_input.lower() == answers[number].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")
number += 1

print(questions[number])
user_input = input("введите ответ: ")
if user_input.lower() == answers[number].lower():
    print("Правильно!")
    score += 1
else:
    print("Неправильно.")

if score > 5:
    print("Это отличный результат! Ты много знаешь о стартапах.")
elif score > 3:
    print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о стартапах.")
else:
    print("Видимо, ты только начинаешь свой путь к стартапам! Ты ещё много чего узнаешь о мире, где мы живём.")
