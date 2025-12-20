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
