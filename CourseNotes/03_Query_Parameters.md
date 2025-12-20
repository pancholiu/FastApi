## 1. Query parameters

There's an alternative way to pass a parameter in an Http decorator,
up to now, we know this option

```
@app.get("/relative_route/{variable}")
def get_something(variable) {}
```

However, we can omit the variable like this

```
@app.get("/relative_route")
def get_something(variable) {}
```

With this method, if the user input in the url, it is also possible to pass a parameter

> url/relative_route?variable=1

## 2. In a POST request

If the same variable, it is sent via body and via query param

- If the variable is explixitly request as a method param, it is going to take the value from the query param
- If not explicitly declared as method param, it will try to take the value from the body

> In this example, the variable weight is explicitly declared
> If we use a dict and then get a variable from there, it is not considered an explicit declaration
>
> ```
> def submit_shipment(weight: float, data: dict[str, str])
> content = data["content"]
> ```
