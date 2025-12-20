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

If the input parameters is only one declared explicitly and the other is not declared

- If the same variable, it is sent via body and via query param
- What is going to happen is that will have priority, the explicitly declared method param
- If not explicitly declared, it will try to take the value from the query parasms

> In this example, the variable wight is explicitly declared
> `def submit_shipment(weight: float) `
