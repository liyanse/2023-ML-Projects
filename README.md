# 2023-ML-Projects
A collection of all the random projects I have been working on in 2023.
Hope this helps you even just a little bit
## Project 1: Djikistra's algorithm
## Project 2: Financial Statement Analysis
## Project 3: JobRequirements Analysis
## Project 4: Scrapping Random Websites
## Project 5: FASTAPI
API stands for application programming interface and it is a set of protocols and routines that allow two applications to communicate with each other. In today's world, APIs are becoming increasingly important as they allow businesses to quickly and easily access data and resources from other applications. With the rise of the internet and cloud computing, APIs are now a vital part of any modern business.

In this article, we'll look at Fast API, a popular framework for writing APIs that is both fast and easy to use. We'll explain what it is, how it works, and provide some code samples to get you started. 

Fast API is an open-source framework for creating APIs quickly and easily. It is built on top of the Python language and uses a combination of Python functions and type annotations to define the API endpoints. This makes Fast API much easier to use than other frameworks such as Flask or Django, which require more complex coding.

The main benefit of Fast API is its speed. It is designed to be extremely fast, allowing developers to quickly create and deploy APIs. It also has a wide range of features that make it easy to use, such as automatic documentation, API versioning, and input/output validation.

In order to use Fast API, you will need to install the Python package. You can do this by running the following command: 

`pip install fastapi`

Once you have installed the package, you can create an API by writing a function and adding the @app.get() decorator. This will allow you to define the endpoint and the parameters that the API should accept. For example, the following code will create an API that accepts two parameters and returns a string: 

`@app.get("/hello")
def hello(name: str, message: str):
return f"Hello {name}, {message}"`

You can also use Fast API to validate the input and output of your API. This allows you to ensure that the data returned by your API is valid and can be used correctly. For example, the following code will validate that the input is a string and the output is an integer: 

`@app.get("/sum")
def sum(a: str, b: str) -> int:
return int(a) + int(b)`

Finally, Fast API also provides automatic documentation of your API, which makes it easier for other developers to understand how to use it. You can generate the documentation by running the following command: 

`fastapi run --docs`

This will create a web page that displays the API documentation and allows developers to quickly understand how to use it.

In conclusion, Fast API is an incredibly powerful and easy to use framework for creating APIs quickly and easily. It is designed to be fast, feature-rich, and easy to understand. It also provides features such as input/output validation and automatic documentation, making it an ideal choice for any API project.
