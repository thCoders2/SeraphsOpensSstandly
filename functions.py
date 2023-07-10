import time
# Essa função divide a string grande em linhas usando o método split() com o argumente ‘\n’ para separar as linhas. Em seguida, para cada linha, divide a linha em partes usando o método split() com o argumento ‘\t’ para separar as partes. A primeira parte é usada como chave e a segunda parte como valor em um dicionário. O dicionário resultante é retornado pela função.
def bigStringToObject(bigStringWithTabEnter):
    lines = bigStringWithTabEnter.strip().split('\n')
    result = {}
    for line in lines:
        parts = line.split('\t')
        key = parts[0].strip()
        value = parts[1].strip()
        result[key] = value
    return result

# Essa função aceita dois parâmetros: database e index. O parâmetro database pode ser uma string grande ou um dicionário grande. O parâmetro index é responsável por indicar qual índice deve ser retornado. O valor padrão é 0, o que significa que, se a função for chamada apenas com uma string grande, apenas o primeiro elemento (antes do primeiro ‘\t’ de cada linha) aparecerá. Se um dicionário grande for fornecido, apenas as chaves serão salvas se o segundo parâmetro for None, 0 ou não fornecido.
def bigStringOrBigObjectToSimpleArray(database, index=0):
    result = []
    if isinstance(database, str):
        lines = database.strip().split('\n')
        for line in lines:
            parts = line.split('\t')
            result.append(parts[index].strip())
    elif isinstance(database, dict):
        if index == 0:
            result = list(database.keys())
        else:
            result = [database[key] for key in database]
    return result

#Essa função aceita dois parâmetros: arr e ticks_per_second. O parâmetro arr é a lista de itens a serem impressos. O parâmetro ticks_per_second define quantos ticks (impressões) ocorrem em um segundo. O valor padrão é 5 ticks por segundo
#Esse daqui é pra aparecer no console, mas futuramente vai rodar no tkinter ou outra parada, tudo tem um começo
def arrPrinter(arr, ticks_per_second=5):
    while True:
        for item in arr:
            print(item)
            time.sleep(1/ticks_per_second)

#função pra ver se todos do array tem o mesmo  tamanho
#A ideia é as animações por caracteres terem sempre o mesmo tamanho, então aqui checa o os caracteres!
def checkSizeLockArr(arr, size=None):
    if size == None:
        size = len(arr[0])

    retorno = ''
    for str in arr:
        if len(str) != size:
            retorno += f'{str} | Com problema. lenLocked: {size} | lenThis: {len(str)}'
    
    if retorno == '':
        retorno = 'Parabens todos os elementos desse array tem o mesmo tamanho!!!'
        print(retorno)
        return retorno
    else:
        print(retorno)
        return retorno
