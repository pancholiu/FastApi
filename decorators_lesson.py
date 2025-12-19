# 0. It is called as log('balloon')
# 1. log_improved('balloon') = custom_fence(fence)(func)(text) -> Stores fence='-'
#    >> Executes first custom_fence(fence) and returns the add_fence function. 
#    >> At this level, the variable fence='-' is "captured".
# 2. log_improved('balloon') = add_fence(func)(text) -> Stores func = log
#    >> The decorator receives the original log function. 
#    >> It returns the wrapper function and "captures" the variable func=log.
# 3. log_improved('balloon') = wrapper(text)
#    >> The original log function is replaced by the wrapper. 
#    >> Now, when you call log('balloon'), you are actually calling wrapper('balloon').
# 4. It executes using all stored variables
#    >> The wrapper uses all variables captured in the previous steps 
#    >> to print the fence lines and the text.

def custom_fence(fence: str = '+'):
    def add_fence(func):
        def wrapper(text: str):
            print(fence * len(text))
            func(text) 
            print(fence * len(text))
        return wrapper
    return add_fence


@custom_fence('-')
def log(text: str):
    print(text)


log('balloon')
