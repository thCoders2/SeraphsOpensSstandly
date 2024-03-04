

def contar_numeros(entrada):
    numeros = entrada.split("\n")
    contador = {}
    counter = 0
    
    for numero in numeros:
        numero = numero.strip()
        if numero:
            counter += 1
            if numero in contador:
                contador[numero] += 1
            else:
                contador[numero] = 1
    
    resultado = f"Total: {counter} "  
    for numero, quantidade in contador.items():
        resultado += f"{numero}: {quantidade} vezes - "
    
    # Remover o último traço e espaço
    resultado = resultado[:-2]
    
    return resultado

entrada = """950
1180
932
940
922
935
930
947
917
1220
1193
953
1185
927
930
940
940
942
922
922
935
920
962
1135
890
890
895
888
898
885
1125
963
965
1165
925
940
930
935
925
1172
953
965
1080
830
840
847
843
845
842
1085
968
950
1130
892
885
885
887
885
887
1222
960
932
1165
932
930
927
937
920
1173
945
930
935
952
933
950
927
935
1215
962
940
930
927
927
937
930
925
933
1185
950
972
1155
936
920
930
932
932
932
932
1175
1160
930
932
940
930
943
935
930
940
1185
965
930
1193
1182
928
943
935
940
933
935
935
960
1175
930
935
930
935
935
935
940
933
1160
968
1185
927
930
940
940
942
922
922
935
920
"""

resultado = contar_numeros(entrada)
print(resultado)
