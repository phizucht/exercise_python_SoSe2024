
def cagr_berechnung(AK, EK, t):
    AK_abs = abs(AK)
    t_abs = abs(t)
    cagr = ((EK/AK_abs)**(1/t_abs)-1)
    return cagr
    
print(cagr_berechnung(100, 700, 30))

AK = 120
t = 30
cagr = cagr_berechnung(100, 700, 30)
EK = AK * (1 + cagr)**t
