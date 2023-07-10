creator = 'mafloCasa'


backgroundArr2 =    [[
f'                                              ',
f'                       _______________________',
f'             _________|                      |',
f'_____________|                               |',
f'_____________________________________________|'],[
f'                                              ',
f'                    __________________________',
f'                ___/                         |',
f'_______________/                             |',
f'_____________________________________________|'],[
f'             .                               .',
f'                ,-.._________________________|',
f'               /                             |',
f'_________.    /                              |',
f'_________ "- |_______________________________|'],[
f'                                           .__',
f'             "         ____________________|__',
f'                .-",,"                       |',
f'__________.   /                              |',
f'__________",  |______________________________|'],[
f'                                              ',
f'                        ______________________',
f'                   /""""                     |',
f'__________       ,;                          |',
f'__________\     /*;__________________________|'],]

sizedLockArrs = [fearArr, lilFearArr]

arrAllFacesArr = sizedLockArrs

def testSizeAnimation(arr,sizedLock=true, lenDef=len(arr[0])):
    falhas = ''
    if sizedLock:
        i = 0
        for strin in arr:
            if len(strin) == lenDef:
                print(f'size of postion {i} pfct wth locked sized: {lenDef} caracteres')
            else:
                falhas = falhas.join(f"size of postion {i}. nmr caracteres: {len(strin)}.||| esperado: {lenDef}   ")
                print(f'{i} FALHA FALHA FALHA FALHA FALHA FALHA {i}')
        
        if falhas == '':
            print('nenhuma falha apresentada, parabens')
        else:
            print('algumas falhas olha ai')
            print(falhas)

print('rodando testes!')
testSizeAnimation(arrAllFacesArr)
