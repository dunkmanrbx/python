# Vstupni hodnotv
jmeno = input('Jak se jmenujes?:')
vaha = float(input('Zadej tvoji vahu: ')) 
vyska = float(input('Zadej tvoji vysku: ')) / 100


    

    


# Vypocet
bmi = vaha / (vyska*vyska)


# Vytvor promennou kategorie a prirad ji hodnoy pomoci podminek
if bmi <= 18.5:
    vyhodnoceni = 'Podvýživa'
elif bmi <= 25:
    vyhodnoceni = 'Zdrava vaha'
elif bmi <= 30:
    vyhodnoceni = 'Mirna nadvaha'
elif bmi <= 40:
    vyhodnoceni = 'Obezita'
else:
    vyhodnoceni = 'Tezka obezita'



# Vytiskni odpoved s vysledkem
print(jmeno + ' Tvoje bmi je', str(bmi) + ' coz je ', vyhodnoceni)
input('hulahula')