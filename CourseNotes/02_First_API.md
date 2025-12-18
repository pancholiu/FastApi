## 1. Have defined a getter

We need to have a method that returns some information, let's say for example

> get_something() {}

## 2. import fastapi package and use it as decorator

> from fastapi import FastAPI
>
> app = FastAPI()
>
> @app.get("/relative_route")
> get_something() {}

## 3. Run the server in CLI

> fastapi dev < app dir >

## 4. Documentations

It can be used these following docs

> - Standard fast api
> - pip module scalar_fastapi
> - Complement Postman for VS Code
