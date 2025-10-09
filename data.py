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
        "question": "A stack is a data structure that follows the First-In-First-Out (FIFO) principle.",
        "correct_answer": "False",
    },
    {
        "question": "Stacks operate on a Last-In-First-Out (LIFO) basis.",
        "correct_answer": "True",
    },
    {
        "question": "The push operation removes an element from the top of the stack.",
        "correct_answer": "False",
    },
    {
        "question": "The peek method retrieves the top element of a stack without removing it.",
        "correct_answer": "True",
    },
    {
        "question": "A stack can be implemented using a linked list.",
        "correct_answer": "True",
    },
    {
        "question": "You do not need to import anything to instantiate a linked list in java.",
        "correct_answer": "False",
    },
    {
        "question": "Push and pop are common operations in stacks.",
        "correct_answer": "True",
    },
    {
        "question": "Postfix expressions do not require parentheses to determine order of operations.",
        "correct_answer": "True",
    },
    {
        "question": "A queue is a linear data structure that follows the Last-In-First-Out (LIFO) principle.",
        "correct_answer": "False",
    },
    {
        "question": "A queue operates based on the First-In-First-Out (FIFO) rule.",
        "correct_answer": "True",
    },
    {
        "question": "In a queue, elements are added at the front and removed at the rear.",
        "correct_answer": "False",
    },
    {
        "question": "In Python, the method q.put(item) is used to enqueue an element into a queue.",
        "correct_answer": "True",
    },
    {
        "question": "In Java, the method q.poll() is used to remove an element from the front of the queue.",
        "correct_answer": "True",
    },
    {
        "question": "Queues are often used in job scheduling and network routing applications.",
        "correct_answer": "True",
    },
    {
        "question": "The front of the queue is the position where new elements are inserted.",
        "correct_answer": "False",
    },
    {
        "question": "The rear of the queue is where new elements are added.",
        "correct_answer": "True",
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
        "question": "What will be the output of the following pseudocode?\n\nStep 1. Set x = 10\nStep 2. while x > 0\nStep 3. \tprint x\nStep 4. \tx = x - 2",
        "correct_answer": "10 8 6 4 2",
        "incorrect_answers": ["10 8 6 4 2", "10 9 8 7 6 5 4 3 2 1", "10 5 0", "Error"]
    },
    {
        "question": "What is recursion?",
        "correct_answer": "A technique where a function calls itself",
        "incorrect_answers": ["A technique where a function calls another function",
                              "A loop structure that repeats a process", "A technique where a function calls itself",
                              "A method that does not return a value"]
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
        "question": 'What will be the result if I run the following java code inside psvm?\n\nLinkedList<String> songs = new LinkedList<>();\nsongs.add("Golden"); \nsongs.add("Shameless");\nSystem.out.print(songs.get(1)+" ");',
        "correct_answer": "Shameless ",
        "incorrect_answers": ["Shameless ", "Golden ", "Golden Shameless", "Shameless Golden"]
    },
    {
        "question": "Which type of recursion involves two or more functions calling each other?",
        "correct_answer": "Mutual Recursion",
        "incorrect_answers": [
            "Tail Recursion", "Linear Recursion", "Binary Recursion", "Mutual Recursion"
        ]
    },
    {
        "question": "In a linked list, each node typically contains:",
        "correct_answer": "Data and a pointer to the next node",
        "incorrect_answers": [
            "Data only",
            "Data and a pointer to the next node",
            "Memory address only",
            "A stack reference"
        ]
    },
    {
        "question": "Which of the following statements about linked lists is TRUE?",
        "correct_answer": "Elements are not stored in contiguous memory locations.",
        "incorrect_answers": [
            "Elements are stored in contiguous memory.",
            "Each node has only one data field.",
            "Elements are randomly arranged.",
            "Elements are not stored in contiguous memory locations."
        ]
    },
    {
        "question": "What is the output of the following Python code?\n\nlist = []\nlist.append(10)\nlist.append(20)\nlist.append(30)\nprint(list[1])",
        "correct_answer": "20",
        "incorrect_answers": ["10", "20", "30", "Error"]
    },
    {
        "question": "Which linked list type allows traversal in both directions?",
        "correct_answer": "Doubly Linked List",
        "incorrect_answers": [
            "Singly Linked List", "Circular Linked List", "Linear Linked List", "Doubly Linked List"
        ]
    },
    {
        "question": "What will happen if you try to pop from an empty stack in Java?",
        "correct_answer": "EmptyStackException is thrown",
        "incorrect_answers": [
            "The program terminates silently",
            "The top element is returned as null",
            "EmptyStackException is thrown",
            "The stack resets automatically"
        ]
    },
    {
        "question": "Which of the following correctly describes a stack?",
        "correct_answer": "Last-In, First-Out (LIFO)",
        "incorrect_answers": ["First-In, First-Out (FIFO)", "Last-In, First-Out (LIFO)", "Circular access",
                              "Random access"]
    },
    {
        "question": "What is the output of this Java code?\n\nStack<Integer> s = new Stack<>();\ns.push(1);\ns.push(2);\ns.push(3);\nSystem.out.println(s.pop());",
        "correct_answer": "3",
        "incorrect_answers": ["1", "2", "3", "Error"]
    },
    {
        "question": "Which stack method returns the top element without removing it?",
        "correct_answer": "peek()",
        "incorrect_answers": ["pop()", "poll()", "peek()", "get()"]
    },
    {
        "question": "Given a stack with elements [A, B, C] where C is on top, after pop() and push('D'), what are the elements?",
        "correct_answer": "[A, B, D]",
        "incorrect_answers": ["[D, A, B]", "[A, D, C]", "[A, B, D]", "[A, B, C, D]"]
    },
    {
        "question": "Which of the following applications typically uses a stack?",
        "correct_answer": "Undo/Redo functionality",
        "incorrect_answers": ["Printer queue", "Undo/Redo functionality", "Customer service line", "Job scheduling"]
    },
    {
        "question": "Which of the following is an incorrect declaration of a linked list in java?",
        "correct_answer": "LinkedList<String> full basket = new LinkedList<>();",
        "incorrect_answers": ["LinkedList<String> full basket = new LinkedList<>();",
                              "LinkedList<String> fullBasket = new LinkedList<>();",
                              "LinkedList<String> fullbasket = new LinkedList<String>();",
                              "LinkedList<String> basket = new LinkedList<>();"]
    },
    {
        "question": "What flowchart symbol is typically used to indicate the start or end of a process",
        "correct_answer": "Oval",
        "incorrect_answers": ["Oval", "Rectangle", "Parallelogram", "Diamond"]
    },
    {
        "question": "This is the basic building block of a linked list.",
        "correct_answer": "Node",
        "incorrect_answers": ["Node", "Attributes", "Data", "Pointer"]
    },
    {
        "question": "Which of the following correctly describes a queue?",
        "correct_answer": "First-In, First-Out (FIFO)",
        "incorrect_answers": ["Last-In, First-Out (LIFO)", "First-In, First-Out (FIFO)", "Random access",
                              "Circular order"]
    },
    {
        "question": "In a queue, elements are added at the ______ and \nremoved from the ______.",
        "correct_answer": "rear, front",
        "incorrect_answers": ["front, rear", "rear, front", "top, bottom", "bottom, top"]
    },
    {
        "question": "What is the output of the following Python code?\nq = []\nq.append('A')\nq.append('B')\nq.pop(0)\nprint(q.pop(0))",
        "correct_answer": "B",
        "incorrect_answers": ["A", "B", "A B", "Error"]
    },
    {
        "question": "Which of the following methods is used to enqueue an item in a Java queue?",
        "correct_answer": "offer()",
        "incorrect_answers": ["get()", "put()", "offer()", "poll()"]
    },
    {
        "question": "Which queue operation removes and returns the front element in Python?",
        "correct_answer": "pop(0)",
        "incorrect_answers": ["peek()", "offer()", "pop(0)", "clear()"]
    },
    {
        "question": "What is the correct syntax to create an empty list in python?",
        "correct_answer": "fruits = []",
        "incorrect_answers": [
            "fruits = list", "fruits = []", "fruit[] = 0", "fruits = [' ']"
        ]
    },
    {
        "question": "What is the role of base case in a recursive function?",
        "correct_answer": "to define the condition at which the recursion stops",
        "incorrect_answers": ["to define the condition at which the recursion stops",
                              "to speed up the recursive process",
                              "to reduce the number of recursive calls made by the function",
                              "to call the function repeatedly until the problem is solved"]
    },
    {
        "question": "Which of the following queue operations checks if the queue is empty in Java?",
        "correct_answer": "isEmpty()",
        "incorrect_answers": ["peek()", "clear()", "isEmpty()", "poll()"]
    },
    {  # change this
        "question": "Given this declaration:\n\nStack<Integer> numbers = new Stack<>();\n\nWhich of the following is the correct way to add 28 as new element to the stack?",
        "correct_answer": 'numbers.push(28);',
        "incorrect_answers": [
            'numbers.push(28);', 'stack.push(28);', 'numbers.pop(28);', 'stack.pop(28);'
        ]
    },
    {
        "question": "The following are types of linked list except one.",
        "correct_answer": "Linear Linked List",
        "incorrect_answers": ["Linear Linked List", "Singly Linked List", "Doubly Linked List", "Circular Linked List"]
    },
    {
        "question": "Which Java code snippet correctly creates an empty Stack of Strings?",
        "correct_answer": "Stack<String> s = new Stack<String>();",
        "incorrect_answers": [
            "Stack s = Stack<String>();",
            "Stack<String> s = Stack();",
            "Stack<String> s = new Stack<String>();",
            "Stack s = new Stack<>;"
        ]
    },
    {
        "question": "Which of the following is an advantage of linked lists over arrays?",
        "correct_answer": "dynamic memory allocation",
        "incorrect_answers": ["dynamic memory allocation", "fixed size", "direct access to elements",
                              "no extra memory usage"]
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
