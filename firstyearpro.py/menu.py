import matplotlib.pyplot as pyplot
  
def create_menu():
    print("Menu")
    print("1. Create a new question")
    print("2. Select an existing question")

##Chapter 1: Questions 1 & 2 + 4 Answer Options Each
quiz_chapters = {
    "Chapter 1": {
        "Which of the following characters is used to give single-line comments in Python?": {
            "options": ["//", "#", "!", "/*"],
            "correct": "b"
        },
        "What will be the output of the following Python code snippet if x=1?: x<<2": {
            "options": ["4", "2", "1", "8"],
            "correct": "a"
        }
    },
    "Chapter 2": {
        "Which of the following is the correct extension of the Python File?": {
            "options": [".python", ".pl", ".py", ".p"],
            "correct": "c"
        },
        "Which of the following is used to define a block of code in Python language?": {
            "options": ["Indentation", "Key", "Brackets", "All of the above"],
            "correct": "a"
        }
    }
}


def create_question():
    chapter = input("Enter Chapter (e.g., 'Chapter 3'): ")
    question = input("Enter Question: ")
    options = [input(f"Enter answer option {i+1}: ") for i in range(4)]
    correct_option = input("Enter correct answer (a, b, c, or d): ").lower()
    
    if chapter not in quiz_chapters:
        quiz_chapters
        [chapter] = {}
    
    quiz_chapters[chapter][question] = {
        "options": options,
        "correct": correct_option
    }
    
    print("\nQuestion Created Successfully!\n")

def select_question():
    chapter = input("Select a chapter (e.g., 'Chapter 1'): ")

    if chapter not in quiz_chapters:
        print("Invalid chapter selection.")
        return
    
    questions = list(quiz_chapters[chapter].keys())
    
    print("Select a question:")
    for idx, q in enumerate(questions):
        print(f"{idx + 1}. {q}")
    
    q_choice = int(input("Enter the number of the question: ")) - 1
    if 0 <= q_choice < len(questions):
        question = questions[q_choice]
        options = quiz_chapters[chapter][question]["options"]
        correct_answer = quiz_chapters[question]["correct"]
        
        print(f"\n{question}")
        for i, option in enumerate(options):
            print(f"  {chr(97 + i)}.) {option}")
        
        user_answer = input("Enter your answer (a, b, c, or d): ").lower()
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print("Incorrect.")
        
        # Visualizing the answer options
        plot_results(options, correct_answer, user_answer)
    else:
        print("Invalid question selection.")

def plot_results(options, correct_answer, user_answer):
    choices = ['a', 'b', 'c', 'd']
    correct = choices.index(correct_answer)
    user = choices.index(user_answer) if user_answer in choices else None

    answer_values = [0, 0, 0, 0]
    if correct is not None:
        answer_values[correct] = 1

    plt.bar(choices, answer_values, color="pink", width=0.5)
    plt.xticks(choices, options)
    plt.title('Correct Answer Visualization')
    plt.show()

# Main logic
create_menu()
menu_choice = input("Enter 1 to Create, 2 to Select: ")

if menu_choice == "1":
    create_question()
elif menu_choice == "2":
    select_question()
else:
    print("Invalid Entry")
