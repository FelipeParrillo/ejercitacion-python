lista = ['Auto', '123', 'Viaje', '50', '120']
n_lista = []

for x in lista:
    if(x.isdecimal()):
        n_lista.append(int(x))
n_lista.sort()
print(n_lista)
