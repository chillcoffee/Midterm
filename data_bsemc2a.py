import requests


def get_questions():
    parameters = {
        "amount": 10,
        "difficulty": 'easy',
        "type": 'boolean',
    }
    response = requests.get("https://opentdb.com/api.php?", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["results"]


# --------function call to retrieve questions from API----------#
# question_data = get_questions()

question_data = [
    {
        "question": "An algorithm is a random set of steps used to solve a problem.",
        "correct_answer": "False",
    },
    {
        "question": "A good algorithm must be finite, definite, and have input and output.",
        "correct_answer": "True",
    },
    {
        "question": "Pseudocode is a graphical representation of an algorithm.",
        "correct_answer": "False",
    },
    {
        "question": "Recursion occurs when a function calls itself directly or indirectly.",
        "correct_answer": "True",
    },
    {
        "question": "Iteration and recursion are just the same.",
        "correct_answer": "False",
    },
    {
        "question": "Linear recursion occurs when a function makes a single recursive call each time.",
        "correct_answer": "True",
    },
    {
        "question": "Tail recursion performs its recursive call before executing any other operations.",
        "correct_answer": "False",
    },
    {
        "question": "Binary recursion involves two recursive calls in each activation.",
        "correct_answer": "True",
    },
    {
        "question": "Multiple recursion means that the recursive function calls itself more than once.",
        "correct_answer": "True",
    },
    {
        "question": "A linked list stores all its elements in contiguous memory locations.",
        "correct_answer": "False",
    },
    {
        "question": "Each node in a linked list contains data and a pointer to another node.",
        "correct_answer": "True",
    },
    {
        "question": "A singly linked list allows traversal in both directions.",
        "correct_answer": "False",
    },
    {
        "question": "In a circular linked list, the last node points back to the first node.",
        "correct_answer": "True",
    },
    {
        "question": "Insertion, deletion, and traversal are common operations on a linked list.",
        "correct_answer": "True",
    },
    {
        "question": "An algorithm must always produce at least one output.",
        "correct_answer": "True",
    },
    {
        "question": "The characteristics of an algorithm include being finite, definite, and unique.",
        "correct_answer": "True",
    },
    {
        "question": "A flowchart is written in plain English to represent an algorithm.",
        "correct_answer": "False",
    },
    {
        "question": "A flowchart uses shapes and arrows to visually represent the steps of an algorithm.",
        "correct_answer": "True",
    },
    {
        "question": "In pseudocode, ambiguous words such as 'well' or 'some' are acceptable to describe steps.",
        "correct_answer": "False",
    },
    {
        "question": "Divide and Conquer is one of the main algorithm design paradigms.",
        "correct_answer": "True",
    },
    {
        "question": "Recursion can be used as an alternative to iteration for repetitive tasks.",
        "correct_answer": "True",
    },
    {
        "question": "The base case in recursion ensures that the function eventually terminates.",
        "correct_answer": "True",
    },
    {
        "question": "Mutual recursion occurs when one function calls another, and that second function calls the first.",
        "correct_answer": "True",
    },
    {
        "question": "In the factorial function, the recursive call happens after the multiplication operation.",
        "correct_answer": "True",
    },
    {
        "question": "A doubly linked list node has pointers to both its previous and next nodes.",
        "correct_answer": "True",
    },
    {
        "question": "In a singly linked list, the last node always contains a null reference as its pointer.",
        "correct_answer": "True",
    },
    {
        "question": "Linked lists are stored sequentially in computer memory like arrays.",
        "correct_answer": "False",
    },
    {
        "question": "Traversal is the process of visiting each node in a linked list to perform an operation.",
        "correct_answer": "True",
    },
    {
        "question": "A circular linked list is a type of list where the last node connects back to the head node.",
        "correct_answer": "True",
    },
    {
        "question": "Each node in a linked list is an example of an abstract data type (ADT).",
        "correct_answer": "False",
    },
]

# Multiple Choice
question_MC = [
    {
        "question": "Which of the following characteristics is NOT required for a good algorithm?",
        "correct_answer": "Infinite steps",
        "incorrect_answers": [
            "Finite steps", "Definite instructions", "Unique steps", "Infinite steps"
        ]
    },
    {
        "question": "In algorithm design paradigms, which approach divides a problem into subproblems, solves them independently, and combines the results?",
        "correct_answer": "Divide and Conquer",
        "incorrect_answers": [
            "Greedy Algorithm", "Dynamic Programming", "Divide and Conquer", "Backtracking"
        ]
    },
    {
        "question": "What will be the output of the following pseudocode?\n\nStep 1. Set x = 10\nStep 2. while x > 0\nStep 3.\tprint x\nStep 4.\tx = x - 2",
        "correct_answer": "10 8 6 4 2",
        "incorrect_answers": ["10 8 6 4 2", "10 9 8 7 6 5 4 3 2 1", "10 5 0", "Error"]
    },
    {
        "question": "What is recursion?",
        "correct_answer": "A technique where a function calls itself",
        "incorrect_answers": [
            "A technique where a function calls another function",
            "A loop structure that repeats a process",
            "A technique where a function calls itself",
            "A method that does not return a value"
        ]
    },
    {
        "question": "In recursion, the condition that stops further recursive calls is known as the:",
        "correct_answer": "Base case",
        "incorrect_answers": ["Recursive call", "Termination loop", "Base case", "Return point"]
    },
    {
        "question": "What is the main difference between iteration and recursion?",
        "correct_answer": "Recursion calls itself, while iteration uses loops.",
        "incorrect_answers": [
            "Iteration calls itself, recursion uses loops.",
            "Recursion calls itself, while iteration uses loops.",
            "They are identical in execution.",
            "Recursion cannot return values."
        ]
    },
    {
        "question": "Which of the following best defines an Abstract Data Type (ADT)?",
        "correct_answer": "A logical description of data and operations, independent of implementation.",
        "incorrect_answers": [
            "A built-in data type in programming languages.",
            "A logical description of data and operations, independent of implementation.",
            "A data type defined only in C language.",
            "A primitive variable type."
        ]
    },
    {
        "question": "Which flowchart symbol represents the start or end of a process?",
        "correct_answer": "Oval",
        "incorrect_answers": ["Oval", "Rectangle", "Parallelogram", "Diamond"]
    },
    {
        "question": "Which flowchart symbol is used to represent a decision or conditional statement?",
        "correct_answer": "Diamond",
        "incorrect_answers": ["Diamond", "Oval", "Rectangle", "Parallelogram"]
    },
    {
        "question": "Which algorithm property ensures that it eventually stops after a number of steps?",
        "correct_answer": "Finiteness",
        "incorrect_answers": ["Finiteness", "Correctness", "Definiteness", "Output"]
    },
    {
        "question": "What does the following Java method compute?\n\npublic int factorial(int n) {\n    if (n == 0) return 1;\n    return n * factorial(n - 1);\n}",
        "correct_answer": "Factorial of n",
        "incorrect_answers": ["Factorial of n", "Fibonacci of n", "Sum of 1 to n", "Product of even numbers only"]
    },
    {
        "question": "Which of the following creates an empty list in Python?",
        "correct_answer": "my_list = []",
        "incorrect_answers": ["my_list = []", "my_list = list{}", "my_list = list[]", "my_list = empty()"]
    },
    {
        "question": "Which type of recursion involves two or more functions calling each other?",
        "correct_answer": "Mutual Recursion",
        "incorrect_answers": ["Tail Recursion", "Linear Recursion", "Mutual Recursion", "Indirect Recursion"]
    },
    {
        "question": "What do you call a function that is associated with an object in object-oriented programming?",
        "correct_answer": "Method",
        "incorrect_answers": ["Function", "Procedure", "Method", "Constructor"]
    },
    {
        "question": "What will the following Python function return?\n\ndef fact(n):\n    if n == 0:\n        return 1\n    return n * fact(n-1)\nprint(fact(4))",
        "correct_answer": "24",
        "incorrect_answers": ["12", "16", "24", "120"]
    },
    {
        "question": "In a linked list, each node typically contains:",
        "correct_answer": "Data and a pointer to the next node",
        "incorrect_answers": ["Data only", "A pointer only", "Data and a pointer to the next node", "Two data fields"]
    },
    {
        "question": "Which of the following is TRUE about linked lists?",
        "correct_answer": "Elements are not stored in contiguous memory locations.",
        "incorrect_answers": [
            "Elements are stored in contiguous memory.",
            "Elements are indexed like arrays.",
            "Elements are not stored in contiguous memory locations.",
            "All nodes are static."
        ]
    },
    {
        "question": "Which of the following linked lists allows traversal in both directions?",
        "correct_answer": "Doubly Linked List",
        "incorrect_answers": ["Singly Linked List", "Doubly Linked List", "Circular Linked List", "Linear Linked List"]
    },
    {
        "question": "In a circular linked list, the last node points to:",
        "correct_answer": "The first node",
        "incorrect_answers": ["Null", "The first node", "Itself", "The previous node"]
    },
    {
        "question": "What flowchart shape is used to represent a process or computation?",
        "correct_answer": "Rectangle",
        "incorrect_answers": ["Oval", "Rectangle", "Parallelogram", "Diamond"]
    },
    {
        "question": "What is the basic building block of a linked list?",
        "correct_answer": "Node",
        "incorrect_answers": ["Node", "Element", "Index", "Pointer"]
    },
    {
        "question": "Which of the following is NOT a type of linked list?",
        "correct_answer": "Linear Linked List",
        "incorrect_answers": ["Linear Linked List", "Singly Linked List", "Doubly Linked List", "Circular Linked List"]
    },
    {
        "question": "Which Java statement correctly creates an empty linked list of integers?",
        "correct_answer": "LinkedList<Integer> list = new LinkedList<Integer>();",
        "incorrect_answers": [
            "LinkedList<Integer> list = LinkedList();",
            "LinkedList list = new LinkedList[];",
            "LinkedList<Integer> list = new LinkedList<Integer>();",
            "LinkedList<Integer> list = new LinkedList;"
        ]
    },
    {
        "question": "The following are types of linked list except one.",
        "correct_answer": "Linear Linked List",
        "incorrect_answers": ["Linear Linked List", "Singly Linked List", "Doubly Linked List", "Circular Linked List"]
    },
    {
        "question": "Given this Java code:\n\nLinkedList<String> letters = new LinkedList<>();\nletters.add(\"A\");\nletters.add(\"B\");\nletters.addFirst(\"C\");\nSystem.out.println(letters);",
        "correct_answer": "[C, A, B]",
        "incorrect_answers": ["[A, B, C]", "[C, A, B]", "[B, A, C]", "[A, C, B]"]
    },
    {
        "question": "The following are parts of a linked list except:",
        "correct_answer": "Index counter",
        "incorrect_answers": ["Index counter", "Data field", "Pointer (link) to next node", "Node"]
    },
    {
        "question": "Which Java method adds an element to a LinkedList?",
        "correct_answer": "add()",
        "incorrect_answers": ["add()", "append()", "newElement()", "insert()"]
    },
    {
        "question": "What is the output of this Java code?\n\nLinkedList<Integer> list = new LinkedList<>();\nlist.add(10);\nlist.add(20);\nlist.add(30);\nSystem.out.println(list.get(1));",
        "correct_answer": "20",
        "incorrect_answers": ["10", "20", "30", "Error"]
    },
    {
        "question": "Which of the following describes the advantage of linked lists over arrays?",
        "correct_answer": "Dynamic memory allocation and easy insertion/deletion.",
        "incorrect_answers": [
            "Direct access to any element.",
            "Static memory allocation.",
            "Dynamic memory allocation and easy insertion/deletion.",
            "Less memory usage."
        ]
    },
    {
        "question": 'What is the output of this Java code inside psvm?\n\nLinkedList<String> basket = new LinkedList<String>();\nbasket.add("apple");\nbasket.add("banana");\nbasket.add("cherry");\nSystem.out.print(basket)',
        "correct_answer": "[apple, banana, cherry]",
        "incorrect_answers": ["apple banana cherry", "[apple, banana, cherry]", "apple, banana, cherry",
                              "[cherry, banana, apple]"]
    },
    {
        "question": "What will happen if a recursive function lacks a base case?",
        "correct_answer": "The recursion continues infinitely, causing a stack overflow.",
        "incorrect_answers": [
            "The recursion stops immediately.",
            "The recursion continues infinitely, causing a stack overflow.",
            "The compiler adds a base case automatically.",
            "The function returns null."
        ]
    },
    {
        "question": "What must you import in Java to use the LinkedList class?",
        "correct_answer": "import java.util.LinkedList;",
        "incorrect_answers": [
            "import java.util.LinkedList;",
            "import java.linkedlist.*;",
            "import java.io.LinkedList;",
            "import java.collections.*;"
        ]
    },
    {
        "question": "It is a linear data structure that follows the FIFO  principle.",
        "correct_answer": "Queue",
        "incorrect_answers": ["Queue", "Stack", "Linked List", "Trees"]
    },
    {
        "question": "Which of the following describes the process of visiting every node in a linked list?",
        "correct_answer": "Traversal",
        "incorrect_answers": ["Traversal", "Iteration", "Iteration and recursion", "Scanning"]
    },
    {
        "question": "What is a data structure?",
        "correct_answer": "a special format for organizing and storing data",
        "incorrect_answers": [
            "a special format for organizing and storing data", "a format for deleting data",
            "a method to sort data alphabetically", "a program used to analyze data"
        ]
    }
]

# print(f"TF Questions: {len(question_data)}")
# print(f"MC Questions: {len(question_MC)}")
# count = 0
# for question in question_data:
#     if question["correct_answer"] == "True":
#         count += 1
# print(count)
