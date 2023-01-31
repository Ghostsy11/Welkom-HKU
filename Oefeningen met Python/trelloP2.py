
benzine_kosten_per_liter =  1.54
verzekering_per_maand   = int(input("hoe veel betaal je per maand verzekering? : "))
liter_per_kilometer = 0.2
km_per_maand = int(input("hoeveel Kilometer rijd je per maand? : "))
maandkosten = ((km_per_maand * liter_per_kilometer) * benzine_kosten_per_liter) + verzekering_per_maand
bereken_maandkosten = maandkosten
print(bereken_maandkosten)