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

If the same variable, it is sent via body and via path param

- If the variable is explixitly request as a param in the method, it is going to take the value from the path param
- If not explicitly declared as param in the method, it will try to take the value from the body

> In this example, the variable weight is explicitly declared
> If we use a dict and then get a variable from there, it is not considered an explicit declaration
>
> ```
> def submit_shipment(weight: float, data: dict[str, str])
> content = data["content"]
> ```

> DEFINITIONS
> Path parameter: The ones indicated in the URL
> Query parameters: The ones indicated in the body

Note: It is not recommended mix those both parameters in a method
