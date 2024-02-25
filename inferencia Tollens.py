def modus_tollens(p, q):
    if p == True:
        if q == False:
            return False
        else:
            return True
    else:
        return True

# Ejemplo de uso
premisa = True  # P
conclusion = False  # Q

resultado = modus_tollens(premisa, conclusion)
print("La conclusión es:", resultado)