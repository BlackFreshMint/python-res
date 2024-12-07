#strip se usa para remover de la variable el caracter que tenga entre parentesis

print('Prueba I: Strip usos\n')

var = '"gg"'
print("sin strip "+var)
print("con strip " + var.strip('""'))

print("\nPrueba II: Strip para limpiar una ruta\n")

var_path = "{C:/users/fresh}"
var_path2 = '"C:/users/fresh"'

print(var_path + '\n' + var_path2 + '\n')

print('strip para {} ' +var_path.strip('{}'))
print('strip para "" ' + var_path2.strip('"'))

print("\nPrueba III: Strip en caso practico\n")

input_path = "{C:/users/fresh}"

print("previo al strip: "+input_path)

input_path = input_path.strip('{}').strip('"')

print("\ninput_path.strip('{}').strip('""')\n")

print (".strip('{}') eliminara las llaves en caso de haberlas en la ruta \n.strip('""') eliminara las comillas en caso de haberlas en la ruta")

print("\npost-strip: " + input_path)
