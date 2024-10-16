# Leer el contenido del archivo de texto
texto ="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"

# Crear un diccionario para contar las apariciones de cada letra
apariciones = {}

# Recorrer el texto y contar las apariciones de cada letra
for letra in texto:
    if letra.isalpha():
        letra = letra.lower()  # Convertir la letra a minúscula
        if letra in apariciones:
            apariciones[letra] += 1
        else:
            apariciones[letra] = 1

# Convertir el diccionario en una lista de tuplas (letra, apariciones)
lista_apariciones = [(letra, contador) for letra, contador in apariciones.items()]

# Ordenar la lista por apariciones en orden descendente
lista_apariciones.sort(key=lambda x: x[1], reverse=True)

# Imprimir las apariciones de cada letra
for letra, contador in lista_apariciones:
    print(f'{letra}: {contador}')
ok = False
print("Aviso, si pones una letra con la capitalización incorrecta tendras que reiniciar el programa")
while not ok:
	print()
	print("Frecuencia del lenguaje español: eaolsndruitcpmyqbhgfvjñzxkw ")
	print()
	letra_a_cambiar = input("introduce la letra que quieres cambiar del texto en mayusculas: ")
	print()
	letra_a_reemplazar = input("introduce la letra nueva por la que la quieres cambiar en minusculas: ")
	texto = texto.replace(letra_a_cambiar, letra_a_reemplazar)
	print()
	print(texto)
	print()
	si_o_no = input("Has terminado con el texto?(s/n) ")
	if si_o_no == "s":
		ok = True
	else:
		ok = False

