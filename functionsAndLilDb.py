name = "FIRST LINE NAME	-	PACKOFFACES_ANDPOSSIBLENAMES.TXT	-	RESTO ARRAY OF {name}	-	lilSEPARATION TAB	-	bigSEPARATION ENTER"
bigStringWithTabEnter = """
0_0 zerol
P_P	pezol
S_S	essol
$_$	dinol
=_=	sonol
+_+	maiol
=,=	boial
9_9	nonal
*-*	asrol
?_?	queol
_-_	sonel
/:	tinel
:/	triel
(:	felol
):	gelol
d:	delol
D:	dleol
:D	dilal
:P	peiol	
o_o	oliol
P_P	peiol 
"""









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
import time

#Essa função aceita dois parâmetros: arr e ticks_per_second. O parâmetro arr é a lista de itens a serem impressos. O parâmetro ticks_per_second define quantos ticks (impressões) ocorrem em um segundo. O valor padrão é 5 ticks por segundo
def arrPrinter(arr, ticks_per_second=5):
    while True:
        for item in arr:
            print(item)
            time.sleep(1/ticks_per_second)


facesNames = rostosNomes = lilDbFace = firstDbPy = bigStringToObject(bigStringWithTabEnter)

faces = facesArr = arrFace = oldEmotis = bigStringOrBigObjectToSimpleArray(firstDbPy)

arrPrinter(arrFace)
