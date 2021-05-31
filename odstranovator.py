texticek = '''V noci na sobotu napadla skupinka mladíků v Praze na Rašínově nábřeží tři muže.
 Podle poškozených kvůli tomu, že dva z nich se drželi za ruce. Policie případ vyšetřuje.
  Její mluvčí Jan Rybanský odmítl komentovat, zda k útoku na muže došlo kvůli jejich sexuální orientaci.'''
l = [',', '.', ':', ';']
for znak in l:
    texticek = texticek.replace(znak, '-kokot-')
print(texticek)