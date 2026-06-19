def esPar(num):
    if num == 0:
        return True
    elif num == 1:
        return False
    else:
        return esPar(num - 2)
print(esPar(48))