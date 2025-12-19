def custom_fence(fence: str = '+'):
    # 2. custom_fence('-') se ejecuta.
    #    devuevlve la función add_fence.
    #    fence = '-' queda guardado en memoria (closure).
    def add_fence(func):
        # 4. add_fence(log) se ejecuta.
        #    Aquí recién func = log (la función original).
        def wrapper(text: str):
            # 6. Cuando se ejecute log('balloon'),
            #    wrapper('balloon') recibe text = 'balloon'
            #    y fence todavía vale '-'
            print(fence * len(text))
            func(text)   # llama a la función original log
            print(fence * len(text))
        return wrapper
    return add_fence

# 1. Python llega al decorador.
#    Ejecuta custom_fence('-') y obtiene add_fence.
@custom_fence('-')
def log(text: str):
    print(text)

# 3. Ahora Python aplica el decorador: log = add_fence(func = log) 
#    y cuando se ejectua add_fence, queda log = wrapper

# 5. Cuando se llama log('balloon'), en realidad se llama wrapper('balloon').
log('balloon')
