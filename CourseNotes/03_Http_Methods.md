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

## 2. In a Http request

> DEFINITIONS
>
> - Path parameter: The ones indicated in the URL that are pointing to a specific resource in the system, they are coming before the question mark
> - Query parameters: They are more like filters or additional information that doesn't identify a unique resource, but helps to refine a search or an action, like the color or size of a product. They are coming after the question mark

## 3. HTTP methods

- Get: Retrieve data
- Post: Create data
- Put: Update the entire record
- Patch: Only update part of ther records
- Delete: Deletes a record
