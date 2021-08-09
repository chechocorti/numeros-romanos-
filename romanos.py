simbolos ={
    'unidades' : ['', 'I' ,'II' ,'III' ,'IV' ,'V' ,'VI' ,'VII' ,'VIII' ,'IX'],
    'decenas' : ['', 'X','XX','XXX','XL','L','LX' ,'LXX' ,'LXXX' ,'XC'],
    'centenas' : ['', 'C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
    'millares' : ['', 'M','MM','MMM']
}

digitos_romanos = {
    'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
}

def a_numero(cadena):
    acumulador = 0
    valor_ant = 0
    for caracter in cadena:
        valor = digitos_romanos[caracter]
        if valor > valor_ant:
            if valor_ant % 5 == 0:
                raise ValueError("No se pueden restar V, L o D")

            if valor_ant > 0 and valor > 10 * valor_ant:
                raise ValueError("No se admiten restas entre digitos 10 veces mayores")

            acumulador = acumulador - valor_ant
            acumulador = acumulador + valor - valor_ant
        else:
            acumulador = acumulador + valor

        valor_ant = valor 

    return acumulador



def validar(n):
    if not isinstance(n, int):
        raise ValueError("¨{}debe ser un entero".format(n))

    if n < 0 or n > 3999: 
        raise ValueError("¨{}debe estar entre 0 y 3999".format(n))
def a_romano(n):

    validar(n)
    c = str(n)
    
    unidades = 0
    decenas = 0
    centenas = 0
    millares = 0

    if len(c) >= 1:
        unidades = int(c[-1])
        
    if len(c) >= 2:
        decenas = int(c[-2])

    if len(c) >=3:
        centenas = int(c[-3])

    if len(c) >= 4: 
        millares = int(c[-4])
    
    componentes = (millares,centenas,decenas,unidades)
    texto=simbolos['millares'][millares] + simbolos['centenas'][centenas] + simbolos['decenas'][decenas] + simbolos['unidades'][unidades]
    return simbolos['millares'][millares] + simbolos['centenas'][centenas] + simbolos['decenas'][decenas] + simbolos['unidades'][unidades]

def b_romano(texto):
    numeroma=0
    encontrado=False
    for x in range(1, 3999):   
        texto2=a_romano(x)
        if texto2==texto:
            encontrado=True
            numeroma=x
    if encontrado:
        print(numeroma)    
    else:
        print("No existe")
    return numeroma
