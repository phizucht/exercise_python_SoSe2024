
def vokon_zählen(wort):
    

    vokale = 'aeiouäöü'
    wort_lower = wort.lower()
    
    bn =[i for i in wort_lower if i.isalpha()]
    vn = [k for k in wort_lower if k in vokale]
    

    print(f""""Es gibt {len(vn)} Vokale und {len(bn) - len(vn)} Konsonanten.""")

vokon_zählen("Berlin")