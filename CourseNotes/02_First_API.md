## 1. Have defined a getter

We need to have a method that returns some information, let's say for example

`get_something() {}`

## 2. import fastapi package and use it as decorator

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/relative_route")
get_something() {}
```

## 3. Run the server in CLI

- The original command is > uvicorn main:app --reload

  - uvicorn: It's the engine to run the server
  - main: Refers to the file in which the python code is located
  - app: It's the instance of the variable assigned to FastApi()
  - --Reload: Option to rebot the server on every change

- This is an abstraction layer `fastapi dev < app dir >`

## 4. Documentations

It can be used these following docs

> - Standard fast api
> - pip module scalar_fastapi
> - Complement Postman for VS Code
