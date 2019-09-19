komplementarne_kod = {'A': 'T',
                  'T': 'A',
                  'G': 'C',
                  'C': 'G'}

RNA_kod = {'A': 'A',
       'T': 'U',
       'G': 'G',
       'C': 'C'}

def zmieniaj(co, jak):

    DNA = co
    mod_lista = []
    for n in DNA:
        mod_lista.append(jak[n])
    if jak == komplementarne_kod:
        mod_lista.reverse()
    mod = ''.join(mod_lista)
    return mod



