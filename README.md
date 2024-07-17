# day54_100

# Introduction to Web Development with Python

Today, I embarked on an exciting journey into web development using Python. I explored the fundamentals of web development, focusing on three key components: client-side, server-side, and database interactions. I also delved into Flask, a powerful web framework, and gained a deeper understanding of the differences between libraries and frameworks.

## What I Learned

### Web Development Basics

Web development involves three primary components:
1. **Client-Side:** The front end of a web application where the user interacts with the application.
2. **Server-Side:** The back end of a web application where the server processes requests and handles business logic.
3. **Database:** The storage system where data is kept and managed.

### Flask: A Python Web Framework

Flask is a lightweight and flexible web framework for Python. It allows developers to build web applications quickly and easily. Here are some key takeaways from my experience with Flask:

1. **Creating a Minimal Flask Application:**
```python
from flask import Flask

app = Flask(__name__)

#The @app.route("/") is called Python Decorator
#Basically, functions that would give additional functionalities to a function

#Head over to the explain_file.py for better explanation

@app.route("/")
def hello():
    return "Hello, World!"

#if somebody goes to the URL /bye, this trigger
@app.route("/bye")
def say_bye():
    return "bye"



#Some thing but we don't to type the export FLASK_APP=hello.py
#and the flask run in terminal to start the server and manually end it using ctrl+c
if __name__ =="__main__":
    app.run()
```

    In this example, I learned how to set up a basic Flask application with routes that respond to different URLs.

2. **Understanding Decorators in Flask:**
    Decorators in Flask, such as `@app.route("/")`, are used to add additional functionality to functions. I also explored how decorators work in general Python functions.

### Libraries vs. Frameworks

Django and Flask are both frameworks. The key difference between a library and a framework lies in how they are used:

- **Library:** A collection of pre-written code that developers can use to optimize tasks. Libraries offer specific functionalities, such as data manipulation or making HTTP requests.
- **Framework:** A comprehensive tool that provides a structure for building applications. Frameworks include libraries, but they also enforce a particular way to design and structure an application.

### Practical Examples

1. **Python Functions and Decorators:**
    ```python
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def calculate(calc_function, n1, n2):
        return calc_function(n1, n2)

    result = calculate(add, 2, 3)
    print(result)
    ```

    I learned how functions can be passed as arguments, nested within other functions, and how decorators can enhance their behavior.

2. **Measuring Function Execution Time with Decorators:**
 ```python
    import time

    def speed_calc_decorator(function):
        def wrapper_function():
            start_time = time.time()
            function()
            end_time = time.time()
            print(f"{function.__name__} run speed: {end_time-start_time}s")
        return wrapper_function

    @speed_calc_decorator
    def fast_function():
        for i in range(1000000):
            i * i

    @speed_calc_decorator
    def slow_function():
        for i in range(10000000):
            i * i

    fast_function()
    slow_function()

#Output:
#1721213261.574354
#fast_function run speed: 0.07558703422546387s
#slow_function run speed: 0.6154699325561523s
```

This example helped me understand how to measure the execution time of functions using decorators.

### Popular Terminal Commands

Working with the terminal is an essential skill in web development. Here are some of the popular terminal commands I used:

| Command | Description |
|---------|-------------|
| `pwd`   | Print the current working directory |
| `ls`    | List the files and directories in the current directory |
| `cd`    | Change the current directory |
| `mkdir` | Create a new directory |
| `touch` | Create a new file |
| `rm`    | Remove a file |
| `cd ..` | Move up one directory level |
| `rm -rf`| Remove a directory and its contents recursively |

### Conclusion

Today's learning experience was enriching as I got introduced to the basics of web development and the powerful Flask framework. I also solidified my understanding of Python decorators and the differences between libraries and frameworks. Additionally, I practiced using essential terminal commands. This knowledge will be instrumental as I continue my journey into web development and build more complex applications.
