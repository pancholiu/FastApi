def custom_fence(fence: str = '+'):
    # 3. custom_fence('-') retorna add_fence(func) y func = log(text) se guarda en memoria
    def add_fence(func):
        # 4. wrapper(text) = log('balloon')
        #   a estas alturas están todas las variables asignadas
        def wrapper(text: str):
            # 5. Ya todo asignado: fence = '-' y text = 'balloon'
            print(fence * len(text))
            func(text)
            print(fence * len(text))
        return wrapper
    return add_fence

# 2. Primero se ejecuta custom_fence('-') y guarda en memoria fence = '-'
@custom_fence('-')
def log(text: str):
    print(text)

# 1. Se llama a la función
log('balloon')

