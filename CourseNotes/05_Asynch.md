## 1. To make a method async

We need to prefix the word "async" im the method

    `async def example_method()`

## 2. Return result of an asunc method

An asynch method will not return or execute directly the process we want, because it is going to return a co-routine.
We need to execute that routine to execute the explicit logic on the function

# 3. To run a co-routine

We 2 ways to do it depending of the scenario

> If it is not a nested co-routine, we can use the "asyncio" library
> If it is a nested co-routine, meaning that is inside another routine, we can use the word "await"
