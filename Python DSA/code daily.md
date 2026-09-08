| Task done | Level           | Project                   | What you'll practice                  |     |
| --------- | --------------- | ------------------------- | ------------------------------------- | --- |
| done      | 🟢 Beginner     | Number Guessing Game      | if/else, loops, random numbers        |     |
| Done      | 🟢 Beginner     | Rock Paper Scissors       | Conditions, functions, game logic     |     |
| Done      | 🟢 Beginner     | Password Generator        | Strings, lists, randomness            |     |
| Done      | 🟢 Beginner     | Quiz App                  | Dictionaries, scoring, loops          |     |
|           | 🟡 Intermediate | Expense Tracker           | Lists/dicts, calculations, CRUD logic |     |
|           | 🟡 Intermediate | To-Do CLI App             | Functions, files, validation          |     |
|           | 🟡 Intermediate | Banking System            | OOP, validation, transactions         |     |
|           | 🟡 Intermediate | Contact Book              | Searching, updating, deleting data    |     |
|           | 🟠 Advanced     | Text-Based Adventure Game | State management, complex conditions  |     |
|           | 🟠 Advanced     | Mini Search Engine        | Algorithms, dictionaries, ranking     |     |
|           | 🔴 Advanced     | Sudoku Solver             | Recursion + backtracking              |     |
|           | 🔴 Advanced     | Pathfinding Visualizer    | Graphs, BFS/DFS, algorithms           |     |

# string method projects 
### Real-World Practice

- Password validation
- Email extraction
- Text cleaning
- Word/character counters
- Log processing
- Data parsing
- Mini projects

Yes. That's the better way to learn it. We'll make **tiny projects**, not theory.

We'll start with `string` module concepts and gradually combine them.

## Project 1 — Password Analyzer

**Concepts:** `string.digits`, `ascii_uppercase`, `ascii_lowercase`, `punctuation`, `any()`

```python
import string


def analyze_password(password):

    result = {
        "uppercase": False,
        "lowercase": False,
        "digit": False,
        "special": False
    }

    # YOUR CODE
    # Check whether password has:
    # 1. uppercase
    # 2. lowercase
    # 3. digit
    # 4. punctuation

    return result


password = input("Enter password: ")

print(analyze_password(password))
```

For:

```text
Python@123
```

Expected:

```python
{
    "uppercase": True,
    "lowercase": True,
    "digit": True,
    "special": True
}
```

### Your task

Implement only this:

```python
# uppercase
# lowercase
# digit
# special
```

Use:

```python
any()
string.ascii_uppercase
string.ascii_lowercase
string.digits
string.punctuation
```

Don't use `.isupper()`, `.islower()`, `.isdigit()` yet.

Send me your code. I'll review it, then we'll build **Project 2: Dynamic Message Generator using `Template`**.



Yes. **Password Generator first** is better because we'll actually use the `string` constants.

## Mini Project 1 — Password Generator

We'll start simple:

```python
import string
import random


def generate_password(length):
    # Characters we can use
    characters = string.ascii_letters + string.digits + string.punctuation

    # Pick random characters
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


password = generate_password(12)

print(password)
```

Example output:

```text
k@8P#2x!Lm9$
```

### Now improve it

Current generator has a problem:

```text
Could generate:
aaaaaaaaaaaa
123456789012
!!!!!!!!!!!!
```

That's not a good password.

Let's make a better version where the password **must contain**:

```text
1 uppercase
1 lowercase
1 digit
1 special character
```

Start here:

```python
import string
import random


def generate_password(length):

    # 1. Pick one character from each category
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # 2. Put them together
    password = uppercase + lowercase + digit + special

    # 3. We still need remaining characters
    # YOUR CODE HERE

    # 4. Shuffle the final password
    # YOUR CODE HERE

    return password


print(generate_password(12))
```

### Your challenge

Complete **only these two parts**:

```python
# 3. remaining characters

# 4. shuffle
```

Hint:

```python
random.choice(...)
random.shuffle(...)
```

And remember: `random.shuffle()` works on a **list**, not directly on a string.

Send your version.