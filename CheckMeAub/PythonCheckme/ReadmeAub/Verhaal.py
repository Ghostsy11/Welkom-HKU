from pygame import mixer
import time
import os
Score = 0

mixer.init()
mixer.music.load('Halloyou2.mp3')
mixer.music.play()


def ask():
    while True:
        antwoord = 0
        inp = int(input("kiest u nummer 1 of 2 : \n"))
        if inp in [1, 2]:
            antwoord = inp
            break
    return antwoord


while True:
    print("Mijn naam is Abdulrhaman en Ik kom uit Syrië. Ik ga u meenemen naar de reisroute die ik heb genomen toen ik 14 jaar oud was bijna 15.\n Ik woon op dat moment in Nederland en Ik heb veel meegemaakt onderweg, maar vandaag gaat u weten wat ik allemaal heb gedaan, totdat ik hier vandaag in Nederland ben.\n U krijgt verschillende opties iedere optie stuurt u naar andere route of andere einde als u goed doet eindigt u in Nederland waar ik vandaag ben. Anders bent u bij de verkeerde route.\n U mag opnieuw doen als u wil. Wanneer u een ander einde krijgt dat betekent als ik deze beslissingen had genomen,ik woon op dat moment daar.\n Er zijn ook twee opties die kunt kiezen voordat,u gaat starten.\n U mag hulpverteller krijgen bij optie 1 dat geeft of je op de juiste route bent of niet. Anders mag u gewoon beginnen zonder hulpverteller bij optie 2, bij optie 2 verdient u punten\n hoe meer punten u verdient wijst u of u goed deed of niet.\n U kunt niet herkennen waar bevindt u zich. Alleen kunt u weten waar u bent en of u goed hebt gedaan of niet bij een het einde.")
    print("Let op: op verschillende opties kunt u punten maken bij andere niet er wordt door gegeven bij iedere optie waar u punten kunt krijgen.")
    print("Als u 3 punten hebt, u hebt helaas niet goed er over nagedacht.")
    print("Als u boven 6 punten hebt u was halve weg, maar kan veel beter. ")
    print("Als u 9 punten hebt u bent echt goed gekozen  ")
    print("Ik wens u heel veel succes ")
    antwoord_1 = input(
        "Als u met hulp optie wil tijpt u AUB ja anders nee \n:")
    os.system("cls")
    if antwoord_1 == "ja":
        print("U heeft gekoezen met een hulp ik wens u succes")
        print("In 2010 begint het situatie in Syrië slecht te worden door de lang bezettende dictator Assad, in 2011 begint het volk te protesteren om het land beter te worden.")
        print("Op dat moment krijgen de Syrische volk antwoord met kogels terug en toen ontstaan oorlog.\n Dag na dag de situatie wordt alleen maar erger totdat, u kunt niet meer leven in het land.\n Op dat moment ik was 14 bijna 15.\n Ik besloot om mijn toekomst ergens anders te bouwen, omdat ik zeker weet dat ik geen meer toekomst in Syrië zou hebben.\n Ik game sinds zeven jaar oud was. Misschien zou u zegen ben je gek wat heeft een gamen te maken met je eigen route naar Europa.\n Ik had veel vrienden uit Egypte en veel veel andere verschillenden nationaliteiten, Ik was sociaal en ik vond internet echt vet. Hoe ik met mensen kan communiceren.\n Vrienden maken en hun leren kennen. Tot dat 2011 mijn leven was school en gamen. En dan toen ik 14 jaar en half was de naam van het leven bestaat niet in Syrië. Dus ik heb beslissing genomen om te reizen naar Europa.\n Hoe, wat en wanneer ik weet niet. Op dat tijd ik speel een game heet Combat arms en ik heb iemand ontmoet die heet Zakarje. We hadden een goede klik met elkaar.\n Ik heb hem goed leren kennen aardig man en we hebben altijd gezellig tijd samen als we gamen.\n Hij woont in Turkije in Istanbul.\n Het Idea kwam en ik heb hem gevraagd letterlijk zo: Zakarje HET SITUATIE IN Syrië SUPER SLECHT, IK HEB GEEN TOEKMOST HIER EN IK WIL RIZEN NAAR TURKIJE, MAAR IK WEET NIEMAAND DAAR.\n IK WILDE MIJN WOORD AF MAKEN OF HIJ MIJ KAN HELPEN EN HIJ ZEI MAAK GEEN ZORGEN KOM NAAR MIJ TOE JE SLAAPT BIJ WAAR IK WERK. IK GA JE OOK HELPEN OM EEN WERK TE VINDEN.\n Ik zei tegen hem ik ga geld sparen en we gaan afspreken waar en wanneer.\n Dus we hebben afgesproken als ik alles klaar heb.\n Ik ga hem bespreken, zeker ik heb een goede klik, ik ken hem alleen via een game en ik weet niet hoe hij eruit zit.\n Ik ging direct geld sparen paspoort aangevraagd.\n Ik bleef tussen de tijd in contact met hem.")
        print(".1 Ik ben wel gek geweest en ik reisde naar Turkije naar iemand die nooit heb ontmoet?")
        print(".2 Nee ik ben in Syrië gebleven, omdat het te gevaarlijk was?")
        Stukje1keuzes = ask()
        os.system("cls")
        if Stukje1keuzes == 2:
            print(
                "U keuze was niet zo goed maar u bent nog steeds op juiste route let op voor volgende keer")
            print("Ja klopt het is te gevaarlijk zo een iemand te vertrouwen 100 procent met 3-4 maanden kennis tijd.\n Ook als ik in Syrië bleef. De situatie wordt alleen erger toen. Dus ik verwacht niet dat ik langer daar zou kunnen blijven.\n Omdat ik ook geen optie heb om naar andere landen te gaan bijv.: Saoedi-Arabië of Egypte.\n Ik reisde wel naar Turkije, maar dan niet naar Zakarje.\n Ergens in Turkije met wie of waar ik weet niet.")
        elif Stukje1keuzes == 1:
            print("Dat was goed optie")
            print("                __/___         ")
            print("          _____/______|        ")
            print("  _______/_____\_______\_____  ")
            print("  \              < < <       | ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Ik ben wel gek geweest en ik ben naar Turkije geweest,\n want ik had geen toekomst in Syrië in andere word Ik kan doodgaan of later moet ik mensen neerschieten wanneer ik dienstplicht heb bij het leger.\n Mensen neerschieten lijk mij geen optie ze zouden ook mij nemen niemand zou kunnen weet waar ik ben.\n In iedere moment is geen veiligheid alleen gevaarlijk. Dus ik heb niks te verlezen sowieso.\n Ik en Zakarje hebben we afgesproken in Istanbul,\n maar mij geld is te klein dus ik moest met schip reizen.\n Dus ik ben in nacht vertrokken van Syrië naar Turkije Mersin.\n Ik zie iedereen met zijn familie behalve ik vanwege mijn familie hadden geen geld om weg te gaan.\n Ik was bang, want het zou kunnen Zakarje dat hij niet komt of niet verschijnt.\n Ik heb hem alleen via spel gekend, telefoon en een foto de kennis tijd was 3-4 maanden dat was het.\n Mijn hartslag was zeker 100, maar ik zeg altijd tegen mijzelf spierballen diep adamhalen je bent een man je moet nooit bang zijn, omdat god is met altijd.\n Ik weet dat ik heb met Zakarje afgesproken. In mij hart ik twijfel, maar toch naar daar heen, omdat ik reken niet op hem ik reken op god ik weet zeker god zou mij nooit in straten laten.\n  6 uur ochtend ik ben in Turkije Mersin, andere taal die ik niks van begrijp. Ik zeg tegen de chauffeur Istanbul? En hij zei ja Istanbul ik heb hem geld gegeven en ik ben met bus naar daar heen.\n 19:00 ik ben in Istanbul busstation en ik zit Zakarje te wachten.\n Zakarje hield zijn woorden en verschijnt. Het is wonderbaar ik weet niet hoe moet ik het beschrijven. Het is gewoon supermooi gevoel eerste glimlach sinds lange tijd.\n")
            print("ik reisde naar Turkije. Ik heb werk gezocht en ik heb een werk gevonden. Ik was toen 14 en 9 maanden. Helaas ik had geen gelukkig,\n want het was kersttijden en in kerst er zin niet zo veel werk in Turkije. Als ik geen werk heb, ik heb ook geen geld om te eten.\n Ik hoorde van mensen dat het zou lang duren totdat het werk weer terugkomt naar de normaal situatie dus veel werk.\n Ik had op dit moment twee opties en ik heb geld voor een ticket terug naar Syrië of blijf ik en geef ik kans.\n Ik zie wat gebeurt zonder werk! Dat zou lang duren tot wachttijd met 1-4 maanden.")
            print(
                " .1 Ik ben wel terug naar Syrië geweest, omdat ik geen geld heb straks om te eten?")
            print(
                " .2 Ik ben wel in Turkije gebleven, omdat ik beter kans kan maken in Syrië?")
            Stukje4keuzes = ask()
            os.system("cls")
            if Stukje4keuzes == 1 or 2:
                print("U bent op juiste weg!")
                print("In iedere geval bij het gewone dagen ik eet avond gekoot eieren s avonds tijdens het werk ik eet een boterhaam van werkeigenaar dat waren mijn dagelijks eten bij de normaal situatie.\n Als ik in Turkije bleef had ik het gevaar genomen. Waarschijnlijk ik had het overleeft, maar dan ik eet alleen eieren, omdat het goedkoopst is.\n Ik heb ieder dag eieren gegeten, want ik moest geld sparen voor spoed situatie of als iets anders gebeurt bijv.: familie behoeften.\n")
                print("Ik moest wel terug Syrië , want er was geen specifiek datum wanneer kan ik weer werken. Mijn geld zijn te klein om zo een gevaar te nemen.")
                time.sleep(3)
                print("Dus ik ben naar Syrië teruggegaan, omdat het resultaat niet duidelijk was.\n Ook als ik het overleeft in Turkije. Er geen zekerheid wanneer het werk begint.\n Januari 2015 Ik reisde terug naar Syrië in hoop dat het land beter dan wat het was toen ik weggegaan.\n Helaas het was niet zoals ik gehopte het was precies andersom erger geworden. Ik dacht het wordt alleen maar slachter dus ik moet nieuw plan.\n")
                print("Wat was mijn plan? ")
                print(".1 Ik reisde terug naar Turkije? ")
                print(".2 nee ik bleef in Syrië? ")
            Stukje5keuzes = ask()
            os.system("cls")
            if Stukje5keuzes == 2:
                print("dat was echt geen goede optie")
                print("Helaas als ik in Syrië bleef had ik geen kans om ergens buiten Syrië te gaan. De toekomst is superonduidelijk.\n Het gevaar overal waar je gaan je bent met onveilig gevoel daar. Als ik niet gepakt door het leger in mijn 17 zou ik in mijn 18 zeker bij het leger zijn.\n Ik word gestuurd naar plekken waar oorlog gebieden is en ik schiet andere Syrisch of mensen die aan het te protesten zijn.\n Als ik het word niet goed geluisterd en deed. Of hij schieten mij in hoofd of moet ik mensen dood maken.\n Dat gebeurt echt voor een vrienden van mij en nu zijn ze niet meer levende. Omdat ze andere keuze had gemaakt.\n")
                print("Doorloppende eind")
                quit
            elif Stukje5keuzes == 1:
                print(
                    "U bent op juiste route keep it up, maar let op voor volgende opties")
                print("Tussen de tijd in Syrië ")
                print("Ja klopt ik moet terug naar Turkije ook als ik eet elke dag eieren maak niet uit tenminste ik kan het licht zien in nacht.\n Het was zo erg dat Syrië geen elektriciteit soms hele dag soms 3 dagen niet. Ik ging werken geld sparen en ik had toen nog steeds contact met de werkweigeraar.\n Ik vroeg of het werk beter is en of ik een plek daar heb. Dat gesprek was maart 2015 in Syrië. Het geluk was met mij deze keer en hij antwoorde ja dit keer ik heb je echt nodig je kan ook bij het werk slapen niet bij Zakarje,\n want mijn vorige werk is gevonden door Zakarje. Ik heb mijn werkgever besproken dat ik moet extra geld sparen en ik wil naar Europa gaan.\n Zodat hij weet het is onmogelijk dat ik geen werk heb. Hij ging akkoord dat ik zeker een werk zou hebben.\n Gelijk geld gespaard ticket gekocht ik ging naar Turkije met een werk die op mij wacht.Ik ben ik Turkije en ik ben bij mij werk.\n Ik werk 12-16 uur elke dag afhankelijk hoe druk het werk is, maar ik mag niet stoppen totdat het werk af.\n Ieder dag is anders dan die andere soms max 16 uren moet ik werken soms 12, maar nooit minder dan 12 uur per dag.\n Ik had geen keuzes hier alleen mond dicht en door werken, want ik heb het werk echt nodig anders zit ik in problemen. Mijn doel is dat ik naar Europa gaan in een of andere marineer,\n omdat in mijn hart ik weet mijn familie hebben hulp nodig vooral mijn moeder ik kan haar niet zo achterlaten mijn gedachten zijn met haar altijd.\n Ik hoorde geruchten dat de grenzen van Europa dicht zou gaan straks. Ik was bang dat naar daar heen niet zo ver zou komen anders kan ik mijn familie totaal niet helpen.\n Dat kost duizenden geld zo een 5000$ en ik heb alleen 300$ van dat had ik gespaard.\n")
                print(".1 Ik probeerde wel naar Europa te gaan. ")
                print(".2 Ik bleef in Turkije, omdat ik heb geen geld.")
                Stukje7keuzes = ask()
                os.system("cls")
                if Stukje7keuzes == 2:
                    print("dat was echt geen goede optie")
                    print("Als ik dat had gezegd nee ik bleef in Turkije en groei daar met tijd met een onbekende toekomst.\n Ik zou op dat moment geen man zijn. In mij cultuur we leren als je naar vechtveld gaat je gaat voor 100 procent je mag en je moet winnen optie verloren is voor lafaards optie verloren moet niet bekend zijn in ons woordenboek.\n Omdat ik dacht te gevaarlijk was om met maffia om te gaan, had ik een laste optie om te winnen achter gelaten vanwege dat ik bang was.\n Dat betekent toen ik beslist om van Syrië naar Europa te gaan had ik dit vechtveld gekozen en ik moet winnen als ik niet win betekent dat ik geen man ben en ik zou niet tevreden zijn over mijzelf omdat ik bang en lafaards was.\n Doodlopende einde Onbekende toekomst\n")
                    quit
                elif Stukje7keuzes == 1:
                    print(" goed gedaan keep going ")
                    print("Ja inderdaad ik probeerde om naar Europa te gaan, alleen ik moet wat bedenken hoe en wat.\n Hoe! De enige marineer was via de boot in zee anders of vliegtuig maar dat kost zo een 6000$. Een boot kost 2000$.\n Ik heb 300$. Ik hoorde dat iemand die de boot vaart in zee hij hoeft niks te betalen, omdat als hij of zij gepakt wordt naar gevangenis gestuurd, maar ja ik heb geen geld.\n Dus Ik ben wel gek geweest en ik werd de person die mensen gaan varen naar overkant van Turkije naar Griekenland!\n")
                    time.sleep(3)
                    print("Misschien zou u zeggen dat ik totaal gek ben. Ja ik ben er ook. Ik heb 300$ terwijl ik werk 16 uur per dag ongeveer.\n Ik heb alleen 300$ gespaard. Als ik wil wachten, totdat ik 2000$ heb grenzen zijn dicht. Dat lijk mij verschrikkelijk leven in Turkije.\n Ik had het gevaar genomen weer met veel sterke gevoel dat ik kan het. Ik kan 40 mensen varen naar de overkant.\n Ik ben via via in contact geweest met een maffia en met hen afgesproken over de boot dat ik gaan varen voor kosten 0$ ze zouden niet zo makkelijk mij laten,\n maar ze zagen in mijn ogen dat ik nodig had om naar Europa te gaan. Ze ging akkoord na dat ze beetje over mij gehoord.\n Tijd plek afgesproken. Istanbul Aksry plein: op tijd met de man afgesproken ik word gehaald door iemand met wachtwoord.\n Klopt het wachtwoord ik loop mij, want er zijn meerder maffia's daar ik moet bij de juiste groep horen. Ik liep met man hij was aardig en hij kocht voor mij reddingsvest.\n Ik kon op die tijd niet zwemmen maar toch doen geen andere optie.\n Hij bracht mij naar wacht plek totdat groep klaar is. Alles goed hij zegt hızlı bir şekilde betekent snel we gaan.\n  12 uur nacht 3 auto's een auto met gewapende mannen en andere 2 auto's is waar gewone mensen zijn. 5 uur ochtend waar de zon begint te schijnen de gewapende auto kwijt,\n omdat ik denk het was gevaarlijk is in dag te rijden zo met wapens.\n Dus we bleven 2 auto's een auto had de boot die met andere mensen en ons. Opeens 2 politieauto achter ons volgen!")
                    print("Wat denk je dat het gebeurt ")
                    print("  /|_||_\`.__ ")
                    print("  (   _    _ _\ ")
                    print(" =`-(_)--(_)-' ")
                    print(".1 politie heeft ons gepakt! ")
                    print(".2 de andere auto gepakt!")
                    Stukje9keuzes = ask()
                    if Stukje9keuzes == 1 or 2:
                        os.system("cls")
                        print(
                            "U bent nog steeds op de juiste weg maak geen zorgen, op passen bij de volgende opties")
                        print("Ja dat zou kunnen gebeuren, maar dan we zijn alleen mensen we hebben niks verkeerd gedaan.\n ze zouden ons vrij sturen na paar dagen van gevangenis vrij. Waarschijnlijk we gaan het weer kans geven en proberen.\n Gelukkig zijn we niet gepakt door de Turks politie de man was bang dat hij wordt gepakt zijn hele leven in gevangenis zou zitten.\n Dus hij ging met hoog snelheid de berg snijden om hoog door de bergen. Hij is ontsnappen en kwijt.\n Nu moet we varen met mensen ik heb geen boot. Ik moet niet te laat zijn, omdat grenzen zou dicht gaan straks.  Helaas de andere auto met boot is gepakt.\n Ik word gebeld informatie door gegeven wat aan hand is. Ze zei een andere boot zou morgen komen. We hebben geen eten niks. We kunnen zien de overkant kan Griekenland eilanden.\n Het lijk dat dichtbij in oog te zien. Het regent en koud wij frezen. Dus we moest mannen dicht bij elkaar slapen en vrouwen dicht bij elkaar.\n Ik was in midden tussen 2. Ik werd echt pakje kaas de mannen waren echt groet en ik ben klein, maar regen komt niet op mijn dan op ze.\n We zijn in middel van bergen wel nog keer gebeld we hebben geen eten en kinderen zit te huilen. Informatie doorgegeven eten gebracht. We hebben gegeten en geslapen.\n Ik kond echt niet slapen 2 mannen om mij heen, maar ik heb het overleeft. Volgende dag 5 uur ochtend we krijgen informatie door iemand boot is hier we moeten de boot ophalen.\n  We waren 10 mannen 5 mannen moeten de boot optellen op onze schouders 5 voor de motor van boot. Ik deed mee met boot maar het was te zwaar ze beschouwd mij als man ik moest doen.\n Ik was niet zo sterk zoals ze denken maar ik help wat ik kan. Die waren echt best zwaar het kostte ons 2 uur totdat we boven in berg zijn en nu moeten we naar beneden.\n Mensen zijn bang sommige huilen, en de gil van kinderen. Ik realiseerde het echt moment kwam om met hen te rijden.\n Ik was super dood bang, want als iets gebeurt iemand doodgaan dat is door mij. Mij hartslag is best hoog. Ik roep god help mij en bescherm ons.\n Op eens ik hoor twee mensen zitten te word wisselen wie wil het boot varen. Ik dacht dat ik gaan varen, toen dat hoorde dat. Ik zat stil niks gezegd boot in acteer dat ik dom was.\n Ik wil niet varen laat de groet mannen varen, ik wil niet niemand doodgaan als ik iets verkeerd heb gedaan.\n Ik wil niet schuldig zijn, ik vind het fijn als iets gebeurt en ben ik dood. Omdat het kans is te groot dat boot zinkt, maar als ik achter mij kijk geen light als ik doodgaan ben ik bij mij god tenminste.\n Voordat we varen ontdekken we dat de boot heeft kleine gat, ik twijfelde heel veel om te gaan.\n We denken dat gebeurt door dat zwaar was en het is geraakt per ongeluk. We gokkende we zouden het maken naar overkant, dat is gewoon een klein gat geen gevaar.\n")
                        print(".1 Ben ik toch met gatende boot geweest! ")
                        print(
                            ".2 Of ik stoppend buiten, vanwege dat te gevaarlijk was kans dat ik zinkt groot.")
                        Stukje10keuzes = ask()
                        os.system("cls")
                        if Stukje10keuzes == 2:
                            print("was geen goede optie ")
                            print("Het kans zo groot dat ik doodgaat met een gatende boot te gaan, Ik denk dat ik mij kans had gemist naar Europa en ik bleef in Turkije.\n Dat zou geen goede beslissing geweest en ik woon waarschijnlijk in Turkije met een onbekende toekmost. Doodlopende einde Onbekende toekomst...\n")
                            quit
                        elif Stukje10keuzes == 1:
                            print("                                   \ ")
                            print("                                    \   O,")
                            print(
                                "                         \___________\/ )_________/")
                            print(
                                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print(
                                "perfect keep it up maar let op op de volgende opties")
                            print("Ik stap de boot in en in mijn hart roep ik god bescherm ons.We zijn de zee in, over andere half uur we zien andere boot met turk vlag.\n We weten dat het politie van turk was. Polities zeggen stop nu, nu stoppen maar de man die vaart luister niet.\n Ze gingen ons vechten probeert ons te zinken, om ons te stoppen terug naar Turkije gaan, maar niemand wil dat. We beschermende de boot met onze handen bijna iedereen had een wond geraakt door het vechten van politie.\n De politie was te boss dat ze ons niet kunnen stoppen. Hij probeerde heel dicht bij te komen en de motor te zinken. Iemand heeft de politieman gepakt naar ons boot en hij heeft hem geslagen en groeide hem in zee.\n Politie was bezig met de hun vriend die in zee is, ze moet hem redden. Tussen dat we hadden een tijd om door te varen, helaas de politie kwam weer om ons te stoppen.\n Dit keer ze vallen ons met hun boot en de man die in zee gegooid is terug met korte broek ook. Ze maken afstand tussen ons en hun dan varen met hoog snelheid richting ons weer,\n zodat ons kunnen zieken of dachten dat we gaan stoppen. Na drie keer proberen vierde keer was het heftigste hun boot stond boven ons boot. We zijn half onderwater half boven het water.\n Ik was hartelijke bang op dat moment. Ik zei in mijn hart fuck Europa en de zee ik wil niet dood, ik was gewoon te bang na dat allemaal gebeurt.\n")
                            print(
                                ".1 denkt u dat we hebben de grenzen overgestoken! ")
                            print(".2 of we zijn gepakt!  ")
                            Stukje11keuzes = ask()
                            os.system("cls")
                            if Stukje11keuzes == 2:
                                print(" was geen goede optie ")
                                print(
                                    "Ik denk had mij kans gemist naar Europa en ik bleef in Turkije! Doodlopende einde Onbekende toekomst.")
                                quit
                            elif Stukje11keuzes == 1:
                                print(
                                    "je kan het, blijf de goede opties pakken, maar op letten!!!!!!!")
                                print("   _________  ")
                                print("  |   ...   | ")
                                print("  |  :   :  | ")
                                print("  |__`...'__| ")
                                print("  Europe ")
                                print("Het klinkt misschien dat we worden gepakt, maar gelukkig niet. Ik had wat gek gedaan en sprong ik naar de politie, nog voordat ik in de politieboot zou zitten pakt mij iemand trekt mij terug naar boot.\n Hij zegt kut jonge spierballen we zijn der bijna. Ik was gewoon te bang ik wil terug, maar ja dat gaf mij motivatie.\n Iedereen zeg push de boot, iedere keer probeert de politie ons aan te vallen pushen we hen terug totdat we zitten in grenzen die niet hoort bij Turkije en Griekenland.\n Boot is bijna vul van water, maar gelukkig niet beschadigt. We gooiden alle onze spullen, zodat we licht worden en niet zinken.\n Na half uur van de hele ellende we hebben de grens overgestoken naar Griekenland en we worden gebracht naar een van Grieks haven bij een eiland door het Griekse leger.\n1 Vandaar moet ik snel legaal papier maken en weg van eiland zo snel mogelijk.\n De reden is voor ik moet de Griekse grens oversteken ook, zodat ik naar Duitsland kan gaan, omdat mijn broer is daar al.\n Op diezelfde dag gelijk naar politie papier gemaakt. Ik ben nu legaal papier mee, ik verwacht dat ik mag reizen nu gewoon fijn, maar vanwege dat ik onder 18 jaar was ik mag niet alleen reizen.\n Ik hoorde van mensen politie zou mij houden voor veiligheid van mij. Ik schrok toen ik dat hoorde, want ik moet zo snel mogelijk weg van eiland anders zit ik vast.\n Toen ik het legaal papier heb ben ik weg van politiebureau. Gelijk naar haven ik vroeg waar dit schip gaat heen, ik hoor het is bedoel voor vluchtelingen alleen ik moet ticket kopen.\n Ik heb ticket gekocht, maar de politie checkt of iedereen legaal is. Ja ik ben toch legaal, omdat ik onder 18 jaar ben ik mag alleen niet reizen.\n")
                                print(".1 Ik ben stiekem het schip in geweest.")
                                print(
                                    ".2 Ik was bang dat politie mij pakt en ik wil graag geen problemen hebben, zodat geen slecht effect op mij papier zou hebben in toekomst.")
                                Stukje12keuzes = ask()
                                os.system("cls")
                                if Stukje12keuzes == 2:
                                    print("U was halve weg jammer")
                                    print("Als ik dat had gedaan, ik ben er waarschijnlijk vast gezeten in die eiland met onduidelijk toekomst. Het zou kunnen dat ik na 6 maanden wordt gestuurd naar plek waar onder 18 mensen zou zijn of nog langer moet zetten in eiland.\n Zou kunnen, totdat ik 18 ben daarna mag ik weg of beslissingen nemen dan waarschijnlijk bouw ik mijn toekomst in Griekenland.Doodlopende einde onbekende toekomst...\n")
                                    time.sleep(3)
                                    print(
                                        "Ik denk had mij kans gemist naar Europa en ik bleef in Turkije! Doodlopende einde Onbekende toekomst... ")
                                    quit
                                elif Stukje12keuzes == 1:
                                    print("U bent havle weg keep it upp!!!!")
                                    print("        _    _")
                                    print("     __|_|__|_|__")
                                    print("   _|____________|__")
                                    print("  |o o o o o o o o /")
                                    print("~'`~'`~'`~'`~'`~'`~'`~")
                                    print("Ik nam het gevaar weer en ik ben het schip ingestapt in drukke moment, ik heb wel een ticket.\n Ik reis nu illegaal, maar ja ik wil ook niet vast in eiland zitten met een onduidelijk toekomst. Het schip gaat richting Thessaloniki.\n Het gevoel dat ik heb op dat moment onbeschrijfelijk. Ik was super blij. Na 12 uur reizen ik ben eindelijk in Thessaloniki we werden opgehaald door militeer bus naar een kamp.\n We kregen sleep zaken om te slapen en het kamp vul van tenten. Het kamp was leeg En we sliepen tot het volgende dag.\n 12 uur ochtend ongeveer komt hoog Grieks generaal en hij legt alles uit hoe de situatie bij de grens is, want hij wist al dat meeste mensen gaan dit weg nemen.\n Hij zei grenzen zijn dicht en de situatie niet totaal niet goed. Alstublieft luister en ga niet naar daar u zou niks profeteren.\n Wacht tot organisatie hier zijn om u te helpen en zo snel mogelijk naar beter toekomst gaan.\n")
                                    print(
                                        ".1 Ik heb wel naar generaal geluisterd  ")
                                    print(".2 Nee ik heb niet geluisterd ")
                                    Stukje13keuzes = ask()
                                    mixer.music.load('ha.mp3')
                                    mixer.music.play()
                                    os.system("cls")
                                    print(
                                        "dat was niet goede optie maar je verdient een kans keep it up en let op voor volgende opties!!!!u bent er bijna daar om te winnen")
                                    if Stukje13keuzes == 2:
                                        os.system("cls")
                                        print("Als ik niet naar de generaal heb geluisterd en wel naar grens geweest had ik groot fout gedaan.\n Ik ben naar de grenzen van Macedonië geweest die waren dicht. De situatie was super slecht.\n Ik heb nog maar 100$ over, vanwege ik moest eten en tickets van bussen kopen. Dus ik heb niks geprofeteerd en mijn geld kwijt, zoals de generaal hebt gezegd\n")
                                        time.sleep(3)
                                        print("Indeed ik heb dit keer het advies van generaal geluisterd en ik bleef in kamp. Na wacht tijd van drie maanden.\n Komt het UN en begint mensen te helpen. Ik werd geholpen door hen, maar het sleutel is wachten.")
                                        print("                        __,--'\ ")
                                        print(
                                            "                    __,--'    :. \. ")
                                        print(
                                            "               _,--'              \`. ")
                                        print(
                                            "              /|\       `          \ `. ")
                                        print(
                                            "             / | \        `:        \  `/ ")
                                        print(
                                            "            / '|  \        `:.       \ ")
                                        print(
                                            "           / , |   \                  \ ")
                                        print(
                                            "          /    |:   \              `:. \ ")
                                        print(
                                            "         /| '  |     \ :.           _,-'`. ")
                                        print(
                                            "       \' |,  / \   ` \ `:.     _,-'_|    `/ ")
                                        print(
                                            "          '._;   \ .   \   `_,-'_,-' ")
                                        print(
                                            "        \'    `- .\_   |\,-'_,-' ")
                                        print("                    `--|_,`' ")
                                        print("                            `/ ")
                                    elif Stukje13keuzes == 1:
                                        print(
                                            "Dat was verstandige opties je doet echt goed! maar altijd op letten u bent er bijna daar om te winnen.")
                                        print("Indeed ik heb dit keer het advies van generaal geluisterd en ik bleef in kamp. Na wacht tijd van drie maanden. Komt het UN en begint mensen te helpen.\n Ik werd geholpen door hen, maar het sleutel is wachten. ")
                                        time.sleep(3)
                                        print(
                                            "                                       __ ")
                                        print(
                                            "                                    _.-~  ) ")
                                        print(
                                            "                         _..--~~~~,'   ,-/     _ ")
                                        print(
                                            "                      .-'. . . .'   ,-','    ,' ) ")
                                        print(
                                            "                   ,'. . . _   ,--~,-'__..-'  ,' ")
                                        print(
                                            "                   ,'. . .  (@)' ---~~~~      ,' ")
                                        print(
                                            "                  /. . . . '~~             ,-' ")
                                        print(
                                            "                 /. . . . .             ,-' ")
                                        print(
                                            "                ; . . . .  - .        ,' ")
                                        print(
                                            "               : . . . .       _     / ")
                                        print(
                                            "              . . . . .          `-.: ")
                                        print(
                                            "             . . . ./  - .          ) ")
                                        print(
                                            "            .  . . |  _____..---.._/ ____  _ ")
                                        print(
                                            "      ~---~~~~----~~~~             ~~ ")
                                        print("Nadat de UN kwam, ik moet alleen maar wachten, totdat ze terug zijn met informatie over Duitsland Ze zei tegen mij dat ze zouden afsprak maken bij Duitse consulaat om naar daar heen te gaan wonen bij mijn broer.\n Het kamp was mooi het was dicht bij de zee ik ga elke dag zwemmen, rennen en spelen met vrienden. Na 6 maanden van het aankwam van kamp, moesten we verhuizen van deze kamp naar andere door de overheid.\n We gingen naar andere plek die was niet mooi en er is geen zee.\n Ik was echt verdrietig dat ik weg moest ik vind de zee vet om elke dag te zwemmen.\n Ik leerde zwemmen zelf daar ik maakt nieuw vrienden ik ging omheen de kamp ontdekken.\n Het was soort van een avontuur voor mij, omdat ik toen ik had niks te doen behalve wachten totdat UN komt. Na wacht tijd van drie maanden.\n UN bezoekt de nieuw kamp weer ik moest toen naar Duitse consulaat. Toen ik daar was bleek dat ik werd twee keer uitgenodigd naar afspraak.\n Ze denken dat ik naar daar heen niet geweest. Ik was zo boos en huilde ik daar.\n Niemand had iets gezegd dat ik een afspraak had dus De Duitse consulaat had mijn bestand gesloten en gingen vandoor dat ik niet mag naar Duitsland.\n Wachttijd 1 jaar geen resultaat en ik mag nu niet naar Duitsland. Ik ben naar UN weer geweest en ik zeg tegen hen dat zijn fout hadden gedaan en ze weten het heel goed.\n Ze besluiten om mij van dit kamp naar beter kamp te verhuizen.\n Ik ben naar daar heen geweest en moest ik daar wonen om een beter dienst te krijgen. Na 4 maanden weer moet ik verhuizen naar huis voor mensen die onder 18 zijn.\n Ik ben verhuizend, omdat ik heel graag weggaan wil en starten met mij toekomst te bouwen.\n")
                                        print("in de tussen tijd Athena")
                                        time.sleep(3)
                                        print("Ik had niet verwacht dat ik, zolang zou vastzitten in Griekenland. Het is al nu meer dan een jaar geweest en ik mag niet werken, ik kan niet naar school en er zijn geen activiteiten waarvan veel kun je leren.\n Zeker tussen de tijd heb ik veel vrienden gemaakt vooral om tijd kwijt te krijgen, maar ook sommige willen mij graag helpen dat zijn Griekse leraar, Engels lerares, Mohammed en Lin.\n Deze personen ze hebben unieke eigenschappen in mijn karakter geïmplementeerd dat ga ik allemaal vertellen. Deze eigenschappen heb ik ook gebruiken om andere mensen te helpen.\n Eerste ga ik over deze geweldig mensen hebben. Lin was een meisje die 9 jaar oud was, ze komt uit Syrië.\n Ze spreekt wel Arabisch maar niet zo goed, ze spreekt wel heel goed Engelse. Ze voelt in kamp heel saai soms heeft ze echt niks te doen.\n Ik ken haar familie en de hele kamp kent mij heel goed ze voelen zich comfortabel bij mij.\n Heel veel kinderen vinden spelen met mij leuk en meestal als niet met vrienden ben zekere ik ben met kinderen bezig die zijn van 7- 12 jaar oud.\n Ik vond het leuk ook om met hen te spelen en probeer ik hen dag mooier te maken, omdat in kamp er was niet zo veel te doen.\n Ze voelen zich saai, tenminste wat had ik kunnen doen, kan ik hun dag beetje mooi maken. Lin was bijzonder meisje ze besteed extra tijd met mij elke dag meer dan andere kinderen 3 uur extra's.\n Ze wil mij heel graag dat ik Engels spreek en vond ze dat belangrijk. Iedere dag leert mij meer dan 20 worden.\n I vond dat supergoed eigenlijk, omdat ik Engels nodig had om meer te kunnen bewegen in het land of in Europa.\n Ze verbetert haar Arabisch ook met mij en we maken mooi tijd van. Lin was bij het allerlei eerste kamp toen ik naar Griekenland aankwam, we verhuizend naar andere kamp samen ook met alle mensen die samen kwamen.\n Daarna moest ik verhuizen naar een huis bedoel voor jongeren die onder 18 zijn.  Vanaf dat moment ik weet niks over Lin en mij andere vrienden behalve 3 jongeren.\n Nadat ik meer dan een jaar in kampen gezeten en mijn kans verloren om naar Duitsland te gaan. Verhuizende ik naar een huis dat bedoel voor mensen onder 18.\n Daar zijn er regels en ik moet daaraan houden. Als ik niet aan de regels houd word ik besproken of moet ik een straf doen. Dat leek mij heel kinderachtig.\n Ik mag 3 keer eten per dag, ik moet naar Griekse school die ik niks van begrijp, omdat ik geen Grieks weet, er zijn activiteiten\n bijv.: Engels, Griekse taal, ICT  vaardigheden. Om 11 uur iedereen moet in zijn bed en slapen. We hebben 2 volwassen die in nacht blijven om ons te controleren.\n Ik ben gewoon niet gewend om dat allemaal te doen. Ik vond het te moeilijk. Ik ben gewoon gewend om wat ik wil doen. Ik had geen keuzes en ik heb aan de regels gehouden.\n Ik was blij dat ik Engels kreeg Grieks taallessen. Ik vond Grieks taal niet zo belangrijk om te leren,\n omdat ik weet na tijdje ga ik naar andere land daar bouw ik mijn toekomst. De Engels, Griekse docenten waren superaardig, ze motiveerde mij heel erg goed om hard te studeren,\n maar de Griekse docent leerde mij altijd de bewustheid hoe ik met leven omgaan en slim zijn, omdat op die tijd hij wist dat we geen Griekse willen leren.\n Toch hij heeft wat anders geleerd hoe we een beter leven kan krijgen. Mohammed woonde ook met mij in het huis en hij was aardig jonge hij helpt mij ook met Engels te spreken, zodat ik taal kan beter spreken.\n Hij corrigeert altijd om perfect Engels te spreken.  Mohammed was aardig met iedereen ook maken we altijd gezellig tijd. Ik vond het huis prima, maar niet blij van de regels.\n We zetten met 21 jongeren, iedereen heeft zijn bed en spullen. Ik ga dagelijks naar school ik ga naar fitness gym, Parkour gym, echt dat mogen naar gym gaan was mijn ding.\n Paar maanden alles is goed, totdat ik moest weg van huis doordat ik iemand had geslagen zijn neus kapot maakte.\n Ik speel normaal speel met de andere jongens soort van gevecht sport UCF zeker zonder de controllers ons te zien anders stoppen ze ons.\n Soms kreeg ik blue plekken soms ze krijgen blue plekken. We vonden vechten gezellig en amusement sport. Dat jonge die had ik geslagen hij was irritant hij doet niet mee aan het spel en hij zit ons te mokken.\n Dus ja hij kreeg wat van mij, toen grote chaos gebeurt, hij werd te bang en rende buiten het huis in nacht door mij. Ik vond dat erg dat ik zijn neus kapot maakte, maar ja hij had niet moeten mij pesten.\n  Iedereen wist als je zoiets gebeurt moet je weg van huis daarom niemand luistert naar hem. Controllers kwamen ze haalde mij naar kamer en ze begonnen mij te bespreken schreeuwen.\n Hij ging niet goed met mij om dus ik schreeuwde terug ik zeg je geluid om laag anders gebeurt iets die niet leuk vindt.\n Hij belde de politie en politie kwam mij opgehaald.\n Die jongens waren meer fit dan mij denk geen kans om te rennen politiemannen zitten er vet uit met zijn uniform.\n Ik ging met hen mee en ik zag mooi politievrouw en ik hoopte dat ik door haar word besproken. Ze zit echt er leuk uit,\n maar ja helaas niet. Ik was 6 uur bezig met een hoofdagent te bespreken waarom had ik hem geslagen en leg uit dat mag niet anders moet ik naar gevangenis.\n Uiteindelijk hij laat mij weg. Ik ging naar huis met een van controllers. Alle de medewerkers van het huis waren daar en ik word in public besproken.\n Ze willen mij of ik weggaan of straf doen op eens komt de jonge die had ik geslagen en zegt stuur hem Aub niet weg hij is mijn broer.\n Hij raakt mij gevoelens eerlijk zeggen en Ik voelde toen echt verdrietig. Ik bedoel niet, omdat ik weg moest of straf gaan doen als ik wil blijven.\n Omdat ik had dat niet moeten doen. Ze stuur de jonge weg en ze gingen mij door bespreken met een onaardig accent, terwijl hij heeft mij vergeven en alles is goed ze vinden het niet klaar is.\n Of moet ik weg of straf voeren en dan pas mag ik blijven.\n")
                                        print("Wat denkt u dat ik had gedaan? ")
                                        print(
                                            ".1 Ik ging weg met mijn spullen en laatste 60$ die ik heb ")
                                        print(
                                            ".2 ik heb de straf gedaan ik bleef ik in het huis. ")
                                        Stukje18keuzes = ask()
                                        os.system("cls")
                                    if Stukje18keuzes == 2:
                                        print("dat was bijna goed optie jammer")
                                        print(
                                            "Als ik de straf had gedaan, Ik zou nog 3 maanden wachten en ik zei geen licht dus ik had waarschijnlijk besloten om mijn toekomst in Griekenland te bouwen.\n Onbekend Einde  ")
                                        time.sleep(3)
                                        quit
                                    elif Stukje18keuzes == 1:
                                        print("Dat was goede optie")
                                        print(
                                            " .-------------------------------------------------------------.")
                                        print(
                                            "'------..-------------..----------..----------..----------..--.|")
                                        print(
                                            "|       \\            ||          ||          ||          ||  ||")
                                        print(
                                            "|        \\           ||          ||          ||          ||  ||")
                                        print(
                                            "|    ..   ||  _    _  ||    _   _ || _    _   ||    _    _||  ||")
                                        print(
                                            "|    ||   || //   //  ||   //  // ||//   //   ||   //   //|| /||")
                                        print(
                                            "|_.-----------------------------------------------------------||")
                                        print(
                                            " | |      |       |       |       |    |         |      ||==|  |")
                                        print(
                                            " | |      |  _-_  |       |       |    |  .-.    |      ||==| C|")
                                        print(
                                            " | |  __  |.'.-.' |   _   |   _   |    |.'.-.'.  |  __  |  __==")
                                        print(
                                            " |'-------- |( )|'----------------------'|( )|'----------|")
                                        print("Juist ging ik weg van het huis, omdat ze praten tegen mij nog steeds onaardig. Ja dus in mij hoofd en voor mij gevoel ik vond het niet goed dus ik zeg fuck jullie ik wil mij spullen en ik wil weg.\n Ze schrokkend van mij reactie en ze zeggen ok. Dat was het laatste woord dat heb ik op dit huis gehoor. Ik heb mij spullen en ik ging naar Acropolis.\n Ik woonde toen in Athene. Ik had geen idee waar moet ik heen en ik ga niet terug sorry zeggen. Dus ik ben een nacht in Acropolis geslapen, omdat ik wist niet waar moet ik heen op dat moment.\n Het was leuk trouwens geen regels niks beetje koud in nacht maar ik voel mij vrij. Volgende dag 6 uur ochtend ik heb gegeten en ik belde een vriend van mij dat ik moet bij hem komen wonen,\n ik legde uit wat was in hand. Hij zegt maak geen zorgen, zijn naam was Ibrahim. We ontmoeten in eerste kamp we hadden vroeger ons belovend dat we vrienden zou zijn tot einde van de aarde.\n Ik wist dat ik kan op hem rekenen. Ik reisde met bus van Athene naar Chalcis een stad die drie kwartier ver weg de naam van kamp is Ritsonna.\n Ik arriveerde naar het kamp het kamp was erger dan alle andere kampen waar ik geweest ben. Dat was mij keuze, ik vind het fijn.\n Ik registert in de ik kamp en ik moest weer in plek in kamp waar jongeren onder 18 zijn.\n Ik vond het prima, omdat ik ging naar daar heen en ik zag dat ze minder string zijn echt super lief mensen. Ik hoorde bij het rode kruis. Echt heel aardig mensen.\n Ik moet gewoon wachten, totdat ik iets hoor van organisatie over mij toekomst.\n")
                                        print(" Tussen de tijd in Ritsonna: ")
                                        print(
                                            "___________   _______________________________________^__")
                                        print(
                                            " ___   ___ |||  ___   ___   ___    ___ ___  |   __  ,----\ ")
                                        print(
                                            "|   | |   |||| |   | |   | |   |  |   |   | |  |  | |_____\ ")
                                        print(
                                            "|___| |___|||| |___| |___| |___|  | O | O | |  |  |        \ ")
                                        print(
                                            "           |||                    |___|___| |  |__|         )")
                                        print(
                                            "___________|||______________________________|______________/")
                                        print(
                                            "           |||                                        /--------")
                                        print(
                                            "-----------'''---------------------------------------'")
                                        print("Gebleven tijd andere half jaar in Griekenland. Na een anderhalf jaar ik heb zeker veel geleerd van het leven ik zag situatie,\n ik hoorde verhalen, ik had een klein meisje die ik veel van haar houd haar leven verloren door iemand die dronken was in ongeluk auto.\n Hij was dronken en ging door rijden meisje was kwijt. Dat was de grootste schok voor mijn in Griekenland en het verdrietigste moment van mij leven op dat moment.\n Ik ging terug naar Thessaloniki om haar andere twee zusje te bezoeken en haar moeder. Ik deed wat ik kon, bleef tot haar begrafenis en probeerde haar zusjes en de moeder te kalmeren.\n Toen moest ik terug naar Chalcis ik mag niet veel tijd besteden buiten de kamp knuffel aan iedereen gegeven en Ik ging terug naar kamp.\n Zeker door dit gebeurtenis er is altijd kleine gat in mijn haar voor dat meid die was 5-6 jaar oud en haar leven verloren vanwege iemand dronken is voor niks. Ik ben terug in kamp.\n Ik heb eindelijk niet zo veel te doen. Elke dag zelfde routen.  Ik ging zeker zelf leren met Engels taal door.\n  Spelen met kienden van kamp zoals altijd en vrienden maken om tijd kwijt te raken. Ik vond het niet genoeg, ik wilde wat andere stepjes doen. Ik ging naar rode kuise en andere organisatie violenteren om hen te helpen.\n Ik ging naar gesprek en ik had het gesprek. Ik mag hun helpen. Ik werd een leraar assistent ik vertaal voor andere volwassen leraren in Arabisch die willen graag Engels leren, Ik had meer dan 20 kind die ik zelf geef Engels les voor, Andere activiteiten film kijken met kinderen en soms moet ik mee met rode kruis naar ziekenhuis om te vertalen.\n Het is nu al 4 maanden in Ritsonna kamp en ik begin hoop te verloren na bijna 2 jaar wachttijd in Griekenland.\n Ik ging naar mensen die zijn verantwoordelijk over mij en Ik vroeg hun dat ik heel graag wil naar Turkije of begin ik hier mij leven te bouwen. Toevallig er was een advocaat die ons helpen en het was haar functie zorgen dat we beter toekomst krijgen.\n Ze hoorde mij gesprek dat ik depperset ben en niet blij. Ze wilden mij graag helpen om te rijzen naar andere land met beter toekomst. Ze vertelt mij.\n Ik beloven je als je wacht, totdat ik terug ben ik zou goede nieuws hebben. Ik vroeg ongeveer hoeveel maanden moet ik wachten ongeveer ze zei drie maanden.\n")
                                        print("Wat denkt u? ")
                                        print(".1 Ik heb wel gewacht!  ")
                                        print(
                                            ".2 of ik vertrouw de advocaat niet! En ik wil nog steeds graag naar Turkije of wonen in Griekenland!")
                                        Stukje19keuzes = ask()
                                        os.system("cls")
                                        if Stukje19keuzes == 2:
                                            print(
                                                "dat was bijna goed optie jammer")
                                            print("als ik toch de advocaat had niet vertrouwde, Ik woon in Griekenland op dat moment, omdat Elena was een van mijn favoriete mensen.\n Ze zei je mag niet terug van naar Turkije ik wil je heel graag adopteren, ik houd ook van haar heel veel dus als ik niks had gehoord had.\n Ik woon nu in Griekenland met Elena.  Einde")
                                            time.sleep(3)
                                            print("onbekende eind")
                                            quit
                                        elif Stukje19keuzes == 1:
                                            print(
                                                "U bent een fenomenaal u hebt gewonnen.")
                                            print("3 maanden zijn geen kwaad, nadat alle geduid. Wel juist gewacht. De mevrouw hield haar woord ze is terug met een beter nieuws.\n Ze zegt je wordt gebeld dan moet je naar Athene, Athene consulaat daar hoor het nieuws. Ik ben gebeld naar paar dagen. Ik ben naar Athene geweest om het nieuws te horen.\n Het was het mooiste moment van mij leven, ik werd verwelkomde in koninkrijk van der Nederland om te gaan wonen.  Ik heb mijn handtekking op Ja gezet terwijl ik aan het huilen was.\n Ik woon op dat moment in Nederland met blij leven.\n")
                                            time.sleep(3)
                                            print("        ______")
                                            print("            _\ _~-\___")
                                            print("    =  = ==(____AA____D")
                                            print(
                                                "                \_____\___________________,-~~~~~~~`-.._")
                                            print(
                                                "                /     o O o o o o O O o o o o o o O o  |\_")
                                            print(
                                                "               `~-.__        ___..----..                  )")
                                            print(
                                                "                      `---~~\___________/------------`````")
                                            print(
                                                "                      =  ===(_________D")
                                            print(
                                                "Blij Einde Ik woon in Nederland")
                                            print(
                                                "   _    _.--.____.--._          ")
                                            print(
                                                " \\\:;:;:;:;:;;:;::;:;:;:\          ")
                                            print(
                                                "  \\\:;:;:;:;:;;:;:;:;:;:;\         ")
                                            print(
                                                "   \\\:;::;:;:;:;:;::;:;:;:\        ")
                                            print(
                                                "    \\\:;:;:;:;:;;:;::;:;:;:\       ")
                                            print(
                                                "     \\\:;::;:;:;:;:;::;:;:;:\      ")
                                            print(
                                                "      \\\;;:;:_:--:_:_:--:_;:;\     ")
                                            print(
                                                "       \\\_.-"             "-._\    ")
                                            print(
                                                "        \\                          ")
                                            print(
                                                "         \\ Nederland yesss         ")
                                            print(
                                                "          \\                        ")
                                            print(
                                                "           \\                       ")
                                            print(
                                                "            \\                      ")
                                            print(
                                                "             \\                     ")
                                            ask1 = input(
                                                "Wilt u nog een keer spelen? ja of nee : \n")
                                            if ask1 == "nee":
                                                print("Helaas niet:")
                                                quit

    elif antwoord_1 == "nee":
        print(" u had gekozen om zonder hulp te gaan veel succes")
        print("bij de goede opties kunt u punten verdienen let goed op.")
        print("In 2010 begint het situatie in Syrië slecht te worden door de lang bezettende dictator Assad, in 2011 begint het volk te protesteren om het land beter te worden.\n Op dat moment krijgen de Syrische volk antwoord met kogels terug en toen ontstaan oorlog.\n Dag na dag de situatie wordt alleen maar erger totdat, u kunt niet meer leven in het land.\n Op dat moment ik was 14 bijna 15.\n Ik besloot om mijn toekomst ergens anders te bouwen, omdat ik zeker weet dat ik geen meer toekomst in Syrië zou hebben.\n Ik game sinds zeven jaar oud was. Misschien zou u zegen ben je gek wat heeft een gamen te maken met je eigen route naar Europa.\n Ik had veel vrienden uit Egypte en veel veel andere verschillenden nationaliteiten, Ik was sociaal en ik vond internet echt vet. Hoe ik met mensen kan communiceren.\n Vrienden maken en hun leren kennen. Tot dat 2011 mijn leven was school en gamen. En dan toen ik 14 jaar en half was de naam van het leven bestaat niet in Syrië. Dus ik heb beslissing genomen om te reizen naar Europa.\n Hoe, wat en wanneer ik weet niet. Op dat tijd ik speel een game heet Combat arms en ik heb iemand ontmoet die heet Zakarje. We hadden een goede klik met elkaar.\n Ik heb hem goed leren kennen aardig man en we hebben altijd gezellig tijd samen als we gamen.\n Hij woont in Turkije in Istanbul.\n Het Idea kwam en ik heb hem gevraagd letterlijk zo: Zakarje HET SITUATIE IN Syrië SUPER SLECHT, IK HEB GEEN TOEKMOST HIER EN IK WIL RIZEN NAAR TURKIJE, MAAR IK WEET NIEMAAND DAAR.\n IK WILDE MIJN WOORD AF MAKEN OF HIJ MIJ KAN HELPEN EN HIJ ZEI MAAK GEEN ZORGEN KOM NAAR MIJ TOE JE SLAAPT BIJ WAAR IK WERK. IK GA JE OOK HELPEN OM EEN WERK TE VINDEN.\n Ik zei tegen hem ik ga geld sparen en we gaan afspreken waar en wanneer.\n Dus we hebben afgesproken als ik alles klaar heb.\n Ik ga hem bespreken, zeker ik heb een goede klik, ik ken hem alleen via een game en ik weet niet hoe hij eruit zit.\n Ik ging direct geld sparen paspoort aangevraagd.\n Ik bleef tussen de tijd in contact met hem.")
        print("Kiest u een nummer Aub! ")
        print("In deze opties kunt u punten verdienen")
        print(".1 Ik ben wel gek geweest en ik reisde naar Turkije naar iemand die nooit heb ontmoet? ")
        print(".2 Nee ik ben in Syrië gebleven, omdat het te gevaarlijk was?")
        Stukje1keuzes = ask()
        os.system("cls")
        if Stukje1keuzes == 2:
            print("Ja klopt het is te gevaarlijk zo een iemand te vertrouwen 100 procent met 3-4 maanden kennis tijd.\n Ook als ik in Syrië bleef. De situatie wordt alleen erger toen. Dus ik verwacht niet dat ik langer daar zou kunnen blijven.\n Omdat ik ook geen optie heb om naar andere landen te gaan bijv.: Saoedi-Arabië of Egypte.\n Ik reisde wel naar Turkije, maar dan niet naar Zakarje.\n Ergens in Turkije met wie of waar ik weet niet.")
            time.sleep(3)
            print("In iedere geval ik reisde naar Turkije. Ik heb werk gezocht en ik heb een werk gevonden.\n Ik was toen 14 en 9 maanden. Helaas ik had geen gelukkig, want het was kersttijden en in kerst er zin niet zo veel werk in Turkije.\n Als ik geen werk heb, ik heb ook geen geld om te eten. Ik hoorde van mensen dat het zou lang duren totdat het werk weer terugkomt naar de normaal situatie dus veel werk. Ik had op dit moment twee opties en ik heb geld voor een ticket terug naar Syrië of blijf ik en geef ik kans.\n Ik zie wat gebeurt zonder werk! Dat zou lang duren tot wachttijd met 1-4 maanden.\n")
        elif Stukje1keuzes == 1:
            Score += 1
            print("                __/___         ")
            print("          _____/______|        ")
            print("  _______/_____\_______\_____  ")
            print("  \              < < <       | ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Ik ben wel gek geweest en ik ben naar Turkije geweest,\n want ik had geen toekomst in Syrië in andere word Ik kan doodgaan of later moet ik mensen neerschieten wanneer ik dienstplicht heb bij het leger.\n Mensen neerschieten lijk mij geen optie ze zouden ook mij nemen niemand zou kunnen weet waar ik ben.\n In iedere moment is geen veiligheid alleen gevaarlijk. Dus ik heb niks te verlezen sowieso.\n Ik en Zakarje hebben we afgesproken in Istanbul,\n maar mij geld is te klein dus ik moest met schip reizen.\n Dus ik ben in nacht vertrokken van Syrië naar Turkije Mersin.\n Ik zie iedereen met zijn familie behalve ik vanwege mijn familie hadden geen geld om weg te gaan.\n Ik was bang, want het zou kunnen Zakarje dat hij niet komt of niet verschijnt.\n Ik heb hem alleen via spel gekend, telefoon en een foto de kennis tijd was 3-4 maanden dat was het.\n Mijn hartslag was zeker 100, maar ik zeg altijd tegen mijzelf spierballen diep adamhalen je bent een man je moet nooit bang zijn, omdat god is met altijd.\n Ik weet dat ik heb met Zakarje afgesproken. In mij hart ik twijfel, maar toch naar daar heen, omdat ik reken niet op hem ik reken op god ik weet zeker god zou mij nooit in straten laten.\n  6 uur ochtend ik ben in Turkije Mersin, andere taal die ik niks van begrijp. Ik zeg tegen de chauffeur Istanbul? En hij zei ja Istanbul ik heb hem geld gegeven en ik ben met bus naar daar heen.\n 19:00 ik ben in Istanbul busstation en ik zit Zakarje te wachten.\n Zakarje hield zijn woorden en verschijnt. Het is wonderbaar ik weet niet hoe moet ik het beschrijven. Het is gewoon supermooi gevoel eerste glimlach sinds lange tijd.\n")
            print("In iedere geval ik reisde naar Turkije. Ik heb werk gezocht en ik heb een werk gevonden.\n Ik was toen 14 en 9 maanden.\n Helaas ik had geen gelukkig, want het was kersttijden en in kerst er zin niet zo veel werk in Turkije.\n Als ik geen werk heb, ik heb ook geen geld om te eten.\n Ik hoorde van mensen dat het zou lang duren totdat het werk weer terugkomt naar de normaal situatie dus veel werk.\n Ik had op dit moment twee opties en ik heb geld voor een ticket terug naar Syrië of blijf ik en geef ik kans.\n Ik zie wat gebeurt zonder werk! Dat zou lang duren tot wachttijd met 1-4 maanden.\n")
            print("u kunt hier geen punten maken gok de goede optie")
            print(
                ".1 Ik ben wel terug naar Syrië geweest, omdat ik geen geld heb straks om te eten? ")
            print(
                ".2 Ik ben wel in Turkije gebleven, omdat ik beter kans kan maken in Syrië?")
        Stukje4keuzes = ask()
        os.system("cls")
        if Stukje4keuzes == 1 or 2:
            print("In iedere geval bij het gewone dagen ik eet avond gekoot eieren s avonds tijdens het werk ik eet een boterhaam van werkeigenaar dat waren mijn dagelijks eten bij de normaal situatie.\n Als ik in Turkije bleef had ik het gevaar genomen. Waarschijnlijk ik had het overleeft, maar dan ik eet alleen eieren, omdat het goedkoopst is.\n Ik heb ieder dag eieren gegeten, want ik moest geld sparen voor spoed situatie of als iets anders gebeurt bijv.: familie behoeften.\n")
            time.sleep(3)
            print("Ik moest wel terug Syrië , want er was geen specifiek datum wanneer kan ik weer werken. Mijn geld zijn te klein om zo een gevaar te nemen.")
            print("Dus ik ben naar Syrië teruggegaan, omdat het resultaat niet duidelijk was.\n Ook als ik het overleeft in Turkije. Er geen zekerheid wanneer het werk begint.\n Januari 2015 Ik reisde terug naar Syrië in hoop dat het land beter dan wat het was toen ik weggegaan. Helaas het was niet zoals ik gehopte het was precies andersom erger geworden.\n Ik dacht het wordt alleen maar slachter dus ik moet nieuw plan.")
            print("Wat was mijn plan? ")
            print(".1 Ik reisde terug naar Turkije? ")
            print(".2 nee ik bleef in Syrië? ")
            print("In deze opties kunt u punten verdienen")
            Stukje5keuzes = ask()
            os.system("cls")
            if Stukje5keuzes == 2:
                print("Helaas als ik in Syrië bleef had ik geen kans om ergens buiten Syrië te gaan.\n De toekomst is superonduidelijk. Het gevaar overal waar je gaan je bent met onveilig gevoel daar.\n Als ik niet gepakt door het leger in mijn 17 zou ik in mijn 18 zeker bij het leger zijn.\n Ik word gestuurd naar plekken waar oorlog gebieden is en ik schiet andere Syrisch of mensen die aan het te protesten zijn.\n Als ik het word niet goed geluisterd en deed. Of hij schieten mij in hoofd of moet ik mensen dood maken.\n Dat gebeurt echt voor een vrienden van mij en nu zijn ze niet meer levende. Omdat ze andere keuze had gemaakt.\n")
                print("Doorloppende eind")
                print(" jij hebt zowel punten: " + str(Score))
                quit
            elif Stukje5keuzes == 1:
                Score += 1
                time.sleep(3)
                print("Tussen de tijd in Syrië")
                print("Ja klopt ik moet terug naar Turkije ook als ik eet elke dag eieren maak niet uit tenminste ik kan het licht zien in nacht.\n Het was zo erg dat Syrië geen elektriciteit soms hele dag soms 3 dagen niet.\n Ik ging werken geld sparen en ik had toen nog steeds contact met de werkweigeraar.\n Ik vroeg of het werk beter is en of ik een plek daar heb. Dat gesprek was maart 2015 in Syrië.\n Het geluk was met mij deze keer en hij antwoorde ja dit keer ik heb je echt nodig je kan ook bij het werk slapen niet bij Zakarje,\n want mijn vorige werk is gevonden door Zakarje. Ik heb mijn werkgever besproken dat ik moet extra geld sparen en ik wil naar Europa gaan.\n Zodat hij weet het is onmogelijk dat ik geen werk heb. Hij ging akkoord dat ik zeker een werk zou hebben.\n Gelijk geld gespaard ticket gekocht ik ging naar Turkije met een werk die op mij wacht.Ik ben ik Turkije en ik ben bij mij werk.\n Ik werk 12-16 uur elke dag afhankelijk hoe druk het werk is, maar ik mag niet stoppen totdat het werk af.\n Ieder dag is anders dan die andere soms max 16 uren moet ik werken soms 12, maar nooit minder dan 12 uur per dag.\n Ik had geen keuzes hier alleen mond dicht en door werken, want ik heb het werk echt nodig anders zit ik in problemen.\n Mijn doel is dat ik naar Europa gaan in een of andere marineer, omdat in mijn hart ik weet mijn familie hebben hulp nodig vooral mijn moeder ik kan haar niet zo achterlaten mijn gedachten zijn met haar altijd.\n Ik hoorde geruchten dat de grenzen van Europa dicht zou gaan straks. Ik was bang dat naar daar heen niet zo ver zou komen anders kan ik mijn familie totaal niet helpen.\n Dat kost duizenden geld zo een 5000$ en ik heb alleen 300$ van dat had ik gespaard.\n")
                print("bij de goede optie kunt u punten verdienen ")
                print(".1 Ik probeerde wel naar Europa te gaan.")
                print(".2 Ik bleef in Turkije, omdat ik heb geen geld.")
                Stukje7keuzes = ask()
                os.system("cls")
                if Stukje7keuzes == 2:
                    print("Als ik dat had gezegd nee ik bleef in Turkije en groei daar met tijd met een onbekende toekomst.\n Ik zou op dat moment geen man zijn.\n In mij cultuur we leren als je naar vechtveld gaat je gaat voor 100 procent je mag en je moet winnen optie verloren is voor lafaards optie verloren moet niet bekend zijn in ons woordenboek.\n Omdat ik dacht te gevaarlijk was om met maffia om te gaan, had ik een laste optie om te winnen achter gelaten vanwege dat ik bang was.\n Dat betekent toen ik beslist om van Syrië naar Europa te gaan had ik dit vechtveld gekozen en ik moet winnen als ik niet win betekent dat ik geen man ben en ik zou niet tevreden zijn over mijzelf omdat ik bang en lafaards was.\n Doodlopende einde Onbekende toekomst")
                    print(" jij hebt zowel punten: " + str(Score))
                    quit
                elif Stukje7keuzes == 1:
                    Score += 1
                    print("Ja inderdaad ik probeerde om naar Europa te gaan, alleen ik moet wat bedenken hoe en wat.\n Hoe! De enige marineer was via de boot in zee anders of vliegtuig maar dat kost zo een 6000$.\n Een boot kost 2000$. Ik heb 300$. Ik hoorde dat iemand die de boot vaart in zee hij hoeft niks te betalen, omdat als hij of zij gepakt wordt naar gevangenis gestuurd, maar ja ik heb geen geld.\n Dus Ik ben wel gek geweest en ik werd de person die mensen gaan varen naar overkant van Turkije naar Griekenland! ")
                    time.sleep(3)
                    print("u kunt hier geen punten maken gok de goede optie")
                    time.sleep(3)
                    print("Misschien zou u zeggen dat ik totaal gek ben. Ja ik ben er ook. Ik heb 300$ terwijl ik werk 16 uur per dag ongeveer.\n Ik heb alleen 300$ gespaard. Als ik wil wachten, totdat ik 2000$ heb grenzen zijn dicht. Dat lijk mij verschrikkelijk leven in Turkije.\n Ik had het gevaar genomen weer met veel sterke gevoel dat ik kan het. Ik kan 40 mensen varen naar de overkant.\n Ik ben via via in contact geweest met een maffia en met hen afgesproken over de boot dat ik gaan varen voor kosten 0$ ze zouden niet zo makkelijk mij laten,\n maar ze zagen in mijn ogen dat ik nodig had om naar Europa te gaan. Ze ging akkoord na dat ze beetje over mij gehoord.\n Tijd plek afgesproken. Istanbul Aksry plein: op tijd met de man afgesproken ik word gehaald door iemand met wachtwoord.\n Klopt het wachtwoord ik loop mij, want er zijn meerder maffia's daar ik moet bij de juiste groep horen. Ik liep met man hij was aardig en hij kocht voor mij reddingsvest.\n Ik kon op die tijd niet zwemmen maar toch doen geen andere optie.\n Hij bracht mij naar wacht plek totdat groep klaar is. Alles goed hij zegt hızlı bir şekilde betekent snel we gaan.\n  12 uur nacht 3 auto's een auto met gewapende mannen en andere 2 auto's is waar gewone mensen zijn. 5 uur ochtend waar de zon begint te schijnen de gewapende auto kwijt,\n omdat ik denk het was gevaarlijk is in dag te rijden zo met wapens.\n Dus we bleven 2 auto's een auto had de boot die met andere mensen en ons. Opeens 2 politieauto achter ons volgen!")
                    print("Wat denk je dat het gebeurt?")
                    print("  /|_||_\`.__ ")
                    print("  (   _    _ _\ ")
                    print(" =`-(_)--(_)-' ")
                    print(".1 politie heeft ons gepakt!")
                    print(".2 de andere auto gepakt! ")
                    Stukje9keuzes = ask()
                    os.system("cls")
                    if Stukje9keuzes == 1 or 2:
                        print("bij de goede optie kunt u punten verdienen ")
                        print("Ja dat zou gebeuren dat we gepakt zijn, maar dan we zijn alleen mensen we hebben niks ze stuur ons vrij na paar dagen van gevangenis.\n Waarschijnlijk we gaan het weer kans geven en proberen.")
                        time.sleep(3)
                        print("Gelukkig zijn we niet gepakt door de Turks politie de man was bang dat hij wordt gepakt zijn hele leven in gevangenis zou zitten.\n Dus hij ging met hoog snelheid de berg snijden om hoog door de bergen.\n Hij is ontsnappen en kwijt. Nu moet we varen met mensen ik heb geen boot.\n Ik moet niet te laat zijn, omdat grenzen zou dicht gaan straks.\n Helaas de andere auto met boot is gepakt. Ik word gebeld informatie door gegeven wat aan hand is.\n Ze zei een andere boot zou morgen komen. We hebben geen eten niks. We kunnen zien de overkant kan Griekenland eilanden.\n Het lijk dat dichtbij in oog te zien. Het regent en koud wij frezen. Dus we moest mannen dicht bij elkaar slapen en vrouwen dicht bij elkaar.\n Ik was in midden tussen 2. Ik werd echt pakje kaas de mannen waren echt groet en ik ben klein, maar regen komt niet op mijn dan op ze.\n We zijn in middel van bergen wel nog keer gebeld we hebben geen eten en kinderen zit te huilen.\n Informatie doorgegeven eten gebracht. We hebben gegeten en geslapen. Ik kond echt niet slapen 2 mannen om mij heen, maar ik heb het overleeft.\n Volgende dag 5 uur ochtend we krijgen informatie door iemand boot is hier we moeten de boot ophalen.\n We waren 10 mannen 5 mannen moeten de boot optellen op onze schouders 5 voor de motor van boot. Ik deed mee met boot maar het was te zwaar ze beschouwd mij als man ik moest doen.\n Ik was niet zo sterk zoals ze denken maar ik help wat ik kan. Die waren echt best zwaar het kostte ons 2 uur totdat we boven in berg zijn en nu moeten we naar beneden.\n Mensen zijn bang sommige huilen, en de gil van kinderen. Ik realiseerde het echt moment kwam om met hen te rijden.\n Ik was super dood bang, want als iets gebeurt iemand doodgaan dat is door mij. Mij hartslag is best hoog.\n Ik roep god help mij en bescherm ons. Op eens ik hoor twee mensen zitten te word wisselen wie wil het boot varen.\n Ik dacht dat ik gaan varen, toen dat hoorde dat. Ik zat stil niks gezegd boot in acteer dat ik dom was.\n Ik wil niet varen laat de groet mannen varen, ik wil niet niemand doodgaan als ik iets verkeerd heb gedaan.\n Ik wil niet schuldig zijn, ik vind het fijn als iets gebeurt en ben ik dood. Omdat het kans is te groot dat boot zinkt, maar als ik achter mij kijk geen light als ik doodgaan ben ik bij mij god tenminste.\n Voordat we varen ontdekken we dat de boot heeft kleine gat, ik twijfelde heel veel om te gaan.\n We denken dat gebeurt door dat zwaar was en het is geraakt per ongeluk. We gokkende we zouden het maken naar overkant, dat is gewoon een klein gat geen gevaar.\n")
                        print(".1 Ben ik toch met gatende boot geweest!")
                        print(
                            ".2 Of ik stoppend buiten, vanwege dat te gevaarlijk was kans dat ik zinkt groot.")
                        Stukje10keuzes = ask()
                        os.system("cls")
                        if Stukje10keuzes == 2:
                            print("Het kans zo groot dat ik doodgaat met een gatende boot te gaan, Ik denk dat ik mij kans had gemist naar Europa en ik bleef in Turkije.\n Dat zou geen goede beslissing geweest en ik woon waarschijnlijk in Turkije met een onbekende toekmost.\n Doodlopende einde Onbekende toekomst...")
                            print(" jij hebt zowel punten: " + str(Score))
                            quit
                        elif Stukje10keuzes == 1:
                            Score += 1
                            print("bij de goede optie kunt u punten verdienen ")
                            print("                                   \ ")
                            print("                                    \   O,")
                            print(
                                "                         \___________\/ )_________/")
                            print(
                                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            time.sleep(3)
                            print("Ik stap de boot in en in mijn hart roep ik god bescherm ons.We zijn de zee in, over andere half uur we zien andere boot met turk vlag.\n We weten dat het politie van turk was. Polities zeggen stop nu, nu stoppen maar de man die vaart luister niet.\n Ze gingen ons vechten probeert ons te zinken, om ons te stoppen terug naar Turkije gaan, maar niemand wil dat. We beschermende de boot met onze handen bijna iedereen had een wond geraakt door het vechten van politie.\n De politie was te boss dat ze ons niet kunnen stoppen. Hij probeerde heel dicht bij te komen en de motor te zinken. Iemand heeft de politieman gepakt naar ons boot en hij heeft hem geslagen en groeide hem in zee.\n Politie was bezig met de hun vriend die in zee is, ze moet hem redden. Tussen dat we hadden een tijd om door te varen, helaas de politie kwam weer om ons te stoppen.\n Dit keer ze vallen ons met hun boot en de man die in zee gegooid is terug met korte broek ook. Ze maken afstand tussen ons en hun dan varen met hoog snelheid richting ons weer,\n zodat ons kunnen zieken of dachten dat we gaan stoppen. Na drie keer proberen vierde keer was het heftigste hun boot stond boven ons boot. We zijn half onderwater half boven het water.\n Ik was hartelijke bang op dat moment. Ik zei in mijn hart fuck Europa en de zee ik wil niet dood, ik was gewoon te bang na dat allemaal gebeurt.\n")
                            print(
                                ".1 denkt u dat we hebben de grenzen overgestoken!")
                            print(".2 of we zijn gepakt!")
                            Stukje11keuzes = ask()
                            os.system("cls")
                            if Stukje11keuzes == 2:
                                print(
                                    "Ik denk had mij kans gemist naar Europa en ik bleef in Turkije! Doodlopende einde Onbekende toekomst...")
                                print(" jij hebt zowel punten: " + str(Score))
                                quit
                            elif Stukje11keuzes == 1:
                                Score += 1
                                print("   _________  ")
                                print("  |   ...   | ")
                                print("  |  :   :  | ")
                                print("  |__`...'__| ")
                                print("bij de goede optie kunt u punten verdienen ")
                                time.sleep(3)
                                print("Het klinkt misschien dat we worden gepakt, maar gelukkig niet.\n Ik had wat gek gedaan en sprong ik naar de politie, nog voordat ik in de politieboot zou zitten pakt mij iemand trekt mij terug naar boot.\n Hij zegt kut jonge spierballen we zijn der bijna.\n Ik was gewoon te bang ik wil terug, maar ja dat gaf mij motivatie. Iedereen zeg push de boot,\n iedere keer probeert de politie ons aan te vallen pushen we hen terug totdat we zitten in grenzen die niet hoort bij Turkije en Griekenland.\n Boot is bijna vul van water, maar gelukkig niet beschadigt.\n We gooiden alle onze spullen, zodat we licht worden en niet zinken.\n Na half uur van de hele ellende we hebben de grens overgestoken naar Griekenland en we worden gebracht naar een van Grieks haven bij een eiland door het Griekse leger.\n Vandaar moet ik snel legaal papier maken en weg van eiland zo snel mogelijk.\n De reden is voor ik moet de Griekse grens oversteken ook, zodat ik naar Duitsland kan gaan, omdat mijn broer is daar al.\n Op diezelfde dag gelijk naar politie papier gemaakt.\n Ik ben nu legaal papier mee, ik verwacht dat ik mag reizen nu gewoon fijn, maar vanwege dat ik onder 18 jaar was ik mag niet alleen reizen.\n Ik hoorde van mensen politie zou mij houden voor veiligheid van mij.\n Ik schrok toen ik dat hoorde, want ik moet zo snel mogelijk weg van eiland anders zit ik vast.\n Toen ik het legaal papier heb ben ik weg van politiebureau.\n Gelijk naar haven ik vroeg waar dit schip gaat heen, ik hoor het is bedoel voor vluchtelingen alleen ik moet ticket kopen.\n Ik heb ticket gekocht, maar de politie checkt of iedereen legaal is.\n Ja ik ben toch legaal, omdat ik onder 18 jaar ben ik mag alleen niet reizen.\n Dus wat heb ik gedaan?\n")
                                print(".1 Ik ben stiekem het schip in geweest.")
                                print(
                                    ".2 Ik was bang dat politie mij pakt en ik wil graag geen problemen hebben, zodat geen slecht effect op mij papier zou hebben in toekomst.")
                            Stukje12keuzes = ask()
                            os.system("cls")
                            if Stukje12keuzes == 2:
                                print("Als ik dat had gedaan, ik ben er waarschijnlijk vast gezeten in die eiland met onduidelijk toekomst.\n Het zou kunnen dat ik na 6 maanden wordt gestuurd naar plek waar onder 18 mensen zou zijn of nog langer moet zetten in eiland.\n Zou kunnen, totdat ik 18 ben daarna mag ik weg of beslissingen nemen dan waarschijnlijk bouw ik mijn toekomst in Griekenland.\n Doodlopende einde onbekende toekomst...")
                                time.sleep(3)
                                print(" jij hebt zowel punten: " + str(Score))
                                quit
                            elif Stukje12keuzes == 1:
                                Score += 1
                                print("        _    _")
                                print("     __|_|__|_|__")
                                print("   _|____________|__")
                                print("  |o o o o o o o o /")
                                print("~'`~'`~'`~'`~'`~'`~'`~")
                                print("bij de goede optie kunt u punten verdienen ")
                                time.sleep(3)
                                print("Ik nam het gevaar weer en ik ben het schip ingestapt in drukke moment, ik heb wel een ticket.\n Ik reis nu illegaal, maar ja ik wil ook niet vast in eiland zitten met een onduidelijk toekomst.\n Het schip gaat richting Thessaloniki. Het gevoel dat ik heb op dat moment onbeschrijfelijk. Ik was super blij.\n Na 12 uur reizen ik ben eindelijk in Thessaloniki we werden opgehaald door militeer bus naar een kamp. We kregen sleep zaken om te slapen en het kamp vul van tenten. Het kamp was leeg En we sliepen tot het volgende dag.\n 12 uur ochtend ongeveer komt hoog Grieks generaal en hij legt alles uit hoe de situatie bij de grens is, want hij wist al dat meeste mensen gaan dit weg nemen.\n Hij zei grenzen zijn dicht en de situatie niet totaal niet goed. Alstublieft luister en ga niet naar daar u zou niks profeteren.\n Wacht tot organisatie hier zijn om u te helpen en zo snel mogelijk naar beter toekomst gaan.\n")
                                print(".1 Ik heb wel naar generaal geluisterd")
                                print(".2 Nee ik heb niet geluisterd ")
                                Stukje13keuzes = ask()
                                mixer.music.load('ha.mp3')
                                mixer.music.play()
                                os.system("cls")
                                if Stukje13keuzes == 2:
                                    print("Als ik niet naar de generaal heb geluisterd en wel naar grens geweest had ik groot fout gedaan.\n Ik ben naar de grenzen van Macedonië geweest die waren dicht.\n De situatie super slecht. Ik heb nog maar 100$ over, vanwege ik moest eten en tickets van bussen kopen.\n Dus ik heb niks geprofeteerd en mijn geld kwijt, zoals de generaal hebt gezegd.")
                                    print("Indeed ik heb dit keer het advies van generaal geluisterd en ik bleef in kamp. Na wacht tijd van drie maanden. Komt het UN en begint mensen te helpen. Ik werd geholpen door hen, maar het sleutel is wachten. ")
                                    print("                        __,--'\ ")
                                    print("                    __,--'    :. \. ")
                                    print(
                                        "               _,--'              \`. ")
                                    print(
                                        "              /|\       `          \ `. ")
                                    print(
                                        "             / | \        `:        \  `/ ")
                                    print(
                                        "            / '|  \        `:.       \ ")
                                    print(
                                        "           / , |   \                  \ ")
                                    print(
                                        "          /    |:   \              `:. \ ")
                                    print(
                                        "         /| '  |     \ :.           _,-'`. ")
                                    print(
                                        "       \' |,  / \   ` \ `:.     _,-'_|    `/ ")
                                    print("          '._;   \ .   \   `_,-'_,-' ")
                                    print("        \'    `- .\_   |\,-'_,-' ")
                                    print("                    `--|_,`' ")
                                    print("                            `/ ")
                                    time.sleep(3)
                                    print("Indeed ik heb dit keer het advies van generaal geluisterd en ik bleef in kamp. Na wacht tijd van drie maanden.\n Komt het UN en begint mensen te helpen. Ik werd geholpen door hen, maar het sleutel is wachten.\n")
                                elif Stukje13keuzes == 1:
                                    Score += 1
                                    print(
                                        "                                       __ ")
                                    print(
                                        "                                    _.-~  ) ")
                                    print(
                                        "                         _..--~~~~,'   ,-/     _ ")
                                    print(
                                        "                      .-'. . . .'   ,-','    ,' ) ")
                                    print(
                                        "                   ,'. . . _   ,--~,-'__..-'  ,' ")
                                    print(
                                        "                   ,'. . .  (@)' ---~~~~      ,' ")
                                    print(
                                        "                  /. . . . '~~             ,-' ")
                                    print(
                                        "                 /. . . . .             ,-' ")
                                    print(
                                        "                ; . . . .  - .        ,' ")
                                    print(
                                        "               : . . . .       _     / ")
                                    print(
                                        "              . . . . .          `-.: ")
                                    print(
                                        "             . . . ./  - .          ) ")
                                    print(
                                        "            .  . . |  _____..---.._/ ____ Seal _ ")
                                    print(
                                        "      ~---~~~~----~~~~             ~~ ")
                                    print("Indeed ik heb dit keer het advies van generaal geluisterd en ik bleef in kamp. Na wacht tijd van drie maanden.\n Komt het UN en begint mensen te helpen. Ik werd geholpen door hen, maar het sleutel is wachten.\n")
                                    time.sleep(3)
                                    print("Nadat de UN kwam, ik moet alleen maar wachten, totdat ze terug zijn met informatie over Duitsland Ze zei tegen mij dat ze zouden afsprak maken bij Duitse consulaat om naar daar heen te gaan wonen bij mijn broer.\n Het kamp was mooi het was dicht bij de zee ik ga elke dag zwemmen, rennen en spelen met vrienden. Na 6 maanden van het aankwam van kamp, moesten we verhuizen van deze kamp naar andere door de overheid.\n We gingen naar andere plek die was niet mooi en er is geen zee.\n Ik was echt verdrietig dat ik weg moest ik vind de zee vet om elke dag te zwemmen.\n Ik leerde zwemmen zelf daar ik maakt nieuw vrienden ik ging omheen de kamp ontdekken.\n Het was soort van een avontuur voor mij, omdat ik toen ik had niks te doen behalve wachten totdat UN komt. Na wacht tijd van drie maanden.\n UN bezoekt de nieuw kamp weer ik moest toen naar Duitse consulaat. Toen ik daar was bleek dat ik werd twee keer uitgenodigd naar afspraak.\n Ze denken dat ik naar daar heen niet geweest. Ik was zo boos en huilde ik daar.\n Niemand had iets gezegd dat ik een afspraak had dus De Duitse consulaat had mijn bestand gesloten en gingen vandoor dat ik niet mag naar Duitsland.\n Wachttijd 1 jaar geen resultaat en ik mag nu niet naar Duitsland. Ik ben naar UN weer geweest en ik zeg tegen hen dat zijn fout hadden gedaan en ze weten het heel goed.\n Ze besluiten om mij van dit kamp naar beter kamp te verhuizen.\n Ik ben naar daar heen geweest en moest ik daar wonen om een beter dienst te krijgen. Na 4 maanden weer moet ik verhuizen naar huis voor mensen die onder 18 zijn.\n Ik ben verhuizend, omdat ik heel graag weggaan wil en starten met mij toekomst te bouwen.\n")
                                    print("in de tussen tijd Athena")
                                    print(
                                        "Wat denk u dat ik heb gedaan tussen de wacht tijden?")
                                    time.sleep(3)
                                    print(
                                        "bij de goede optie kunt u punten verdienen ")
                                    time.sleep(3)
                                    print("in de tussen tijd Athena.")
                                    print("k had niet verwacht dat ik, zolang zou vastzitten in Griekenland. Het is al nu meer dan een jaar geweest en ik mag niet werken, ik kan niet naar school en er zijn geen activiteiten waarvan veel kun je leren.\n Zeker tussen de tijd heb ik veel vrienden gemaakt vooral om tijd kwijt te krijgen, maar ook sommige willen mij graag helpen dat zijn Griekse leraar, Engels lerares, Mohammed en Lin.\n Deze personen ze hebben unieke eigenschappen in mijn karakter geïmplementeerd dat ga ik allemaal vertellen. Deze eigenschappen heb ik ook gebruiken om andere mensen te helpen.\n Eerste ga ik over deze geweldig mensen hebben. Lin was een meisje die 9 jaar oud was, ze komt uit Syrië.\n Ze spreekt wel Arabisch maar niet zo goed, ze spreekt wel heel goed Engelse. Ze voelt in kamp heel saai soms heeft ze echt niks te doen.\n Ik ken haar familie en de hele kamp kent mij heel goed ze voelen zich comfortabel bij mij.\n Heel veel kinderen vinden spelen met mij leuk en meestal als niet met vrienden ben zekere ik ben met kinderen bezig die zijn van 7- 12 jaar oud.\n Ik vond het leuk ook om met hen te spelen en probeer ik hen dag mooier te maken, omdat in kamp er was niet zo veel te doen.\n Ze voelen zich saai, tenminste wat had ik kunnen doen, kan ik hun dag beetje mooi maken. Lin was bijzonder meisje ze besteed extra tijd met mij elke dag meer dan andere kinderen 3 uur extra's.\n Ze wil mij heel graag dat ik Engels spreek en vond ze dat belangrijk. Iedere dag leert mij meer dan 20 worden.\n I vond dat supergoed eigenlijk, omdat ik Engels nodig had om meer te kunnen bewegen in het land of in Europa.\n Ze verbetert haar Arabisch ook met mij en we maken mooi tijd van. Lin was bij het allerlei eerste kamp toen ik naar Griekenland aankwam, we verhuizend naar andere kamp samen ook met alle mensen die samen kwamen.\n Daarna moest ik verhuizen naar een huis bedoel voor jongeren die onder 18 zijn.  Vanaf dat moment ik weet niks over Lin en mij andere vrienden behalve 3 jongeren.\n Nadat ik meer dan een jaar in kampen gezeten en mijn kans verloren om naar Duitsland te gaan. Verhuizende ik naar een huis dat bedoel voor mensen onder 18.\n Daar zijn er regels en ik moet daaraan houden. Als ik niet aan de regels houd word ik besproken of moet ik een straf doen. Dat leek mij heel kinderachtig.\n Ik mag 3 keer eten per dag, ik moet naar Griekse school die ik niks van begrijp, omdat ik geen Grieks weet, er zijn activiteiten\n bijv.: Engels, Griekse taal, ICT  vaardigheden. Om 11 uur iedereen moet in zijn bed en slapen. We hebben 2 volwassen die in nacht blijven om ons te controleren.\n Ik ben gewoon niet gewend om dat allemaal te doen. Ik vond het te moeilijk. Ik ben gewoon gewend om wat ik wil doen. Ik had geen keuzes en ik heb aan de regels gehouden.\n Ik was blij dat ik Engels kreeg Grieks taallessen. Ik vond Grieks taal niet zo belangrijk om te leren,\n omdat ik weet na tijdje ga ik naar andere land daar bouw ik mijn toekomst. De Engels, Griekse docenten waren superaardig, ze motiveerde mij heel erg goed om hard te studeren,\n maar de Griekse docent leerde mij altijd de bewustheid hoe ik met leven omgaan en slim zijn, omdat op die tijd hij wist dat we geen Griekse willen leren.\n Toch hij heeft wat anders geleerd hoe we een beter leven kan krijgen. Mohammed woonde ook met mij in het huis en hij was aardig jonge hij helpt mij ook met Engels te spreken, zodat ik taal kan beter spreken.\n Hij corrigeert altijd om perfect Engels te spreken.  Mohammed was aardig met iedereen ook maken we altijd gezellig tijd. Ik vond het huis prima, maar niet blij van de regels.\n We zetten met 21 jongeren, iedereen heeft zijn bed en spullen. Ik ga dagelijks naar school ik ga naar fitness gym, Parkour gym, echt dat mogen naar gym gaan was mijn ding.\n Paar maanden alles is goed, totdat ik moest weg van huis doordat ik iemand had geslagen zijn neus kapot maakte.\n Ik speel normaal speel met de andere jongens soort van gevecht sport UCF zeker zonder de controllers ons te zien anders stoppen ze ons.\n Soms kreeg ik blue plekken soms ze krijgen blue plekken. We vonden vechten gezellig en amusement sport. Dat jonge die had ik geslagen hij was irritant hij doet niet mee aan het spel en hij zit ons te mokken.\n Dus ja hij kreeg wat van mij, toen grote chaos gebeurt, hij werd te bang en rende buiten het huis in nacht door mij. Ik vond dat erg dat ik zijn neus kapot maakte, maar ja hij had niet moeten mij pesten.\n  Iedereen wist als je zoiets gebeurt moet je weg van huis daarom niemand luistert naar hem. Controllers kwamen ze haalde mij naar kamer en ze begonnen mij te bespreken schreeuwen.\n Hij ging niet goed met mij om dus ik schreeuwde terug ik zeg je geluid om laag anders gebeurt iets die niet leuk vindt.\n Hij belde de politie en politie kwam mij opgehaald.\n Die jongens waren meer fit dan mij denk geen kans om te rennen politiemannen zitten er vet uit met zijn uniform.\n Ik ging met hen mee en ik zag mooi politievrouw en ik hoopte dat ik door haar word besproken. Ze zit echt er leuk uit,\n maar ja helaas niet. Ik was 6 uur bezig met een hoofdagent te bespreken waarom had ik hem geslagen en leg uit dat mag niet anders moet ik naar gevangenis.\n Uiteindelijk hij laat mij weg. Ik ging naar huis met een van controllers. Alle de medewerkers van het huis waren daar en ik word in public besproken.\n Ze willen mij of ik weggaan of straf doen op eens komt de jonge die had ik geslagen en zegt stuur hem Aub niet weg hij is mijn broer.\n Hij raakt mij gevoelens eerlijk zeggen en Ik voelde toen echt verdrietig. Ik bedoel niet, omdat ik weg moest of straf gaan doen als ik wil blijven.\n Omdat ik had dat niet moeten doen. Ze stuur de jonge weg en ze gingen mij door bespreken met een onaardig accent, terwijl hij heeft mij vergeven en alles is goed ze vinden het niet klaar is.\n Of moet ik weg of straf voeren en dan pas mag ik blijven.\n")
                                    print("Wat denkt u dat ik had gedaan?")
                                    print(
                                        ".1 Ik ging weg met mijn spullen en laatste 60$ die ik heb")
                                    print(
                                        ".2 ik heb de straf gedaan ik bleef ik in het huis.")
                                    Stukje18keuzes = ask()
                                    os.system("cls")
                                    if Stukje18keuzes == 2:
                                        time.sleep(3)
                                        print(
                                            "Als ik de straf had gedaan, Ik zou nog 3 maanden wachten en ik zei geen licht dus ik had waarschijnlijk besloten om mijn toekomst in Griekenland te bouwen. Onbekend Einde")
                                        print(
                                            " jij hebt zowel punten: " + str(Score))
                                        quit
                                    elif Stukje18keuzes == 1:
                                        Score += 1
                                        print(
                                            " .-------------------------------------------------------------.")
                                        print(
                                            "'------..-------------..----------..----------..----------..--.|")
                                        print(
                                            "|       \\            ||          ||          ||          ||  ||")
                                        print(
                                            "|        \\           ||          ||          ||          ||  ||")
                                        print(
                                            "|    ..   ||  _    _  ||    _   _ || _    _   ||    _    _||  ||")
                                        print(
                                            "|    ||   || //   //  ||   //  // ||//   //   ||   //   //|| /||")
                                        print(
                                            "|_.-----------------------------------------------------------||")
                                        print(
                                            " | |      |       |       |       |    |         |      ||==|  |")
                                        print(
                                            " | |      |  _-_  |       |       |    |  .-.    |      ||==| C|")
                                        print(
                                            " | |  __  |.'.-.' |   _   |   _   |    |.'.-.'.  |  __  |  __==")
                                        print(
                                            " |'-------- |( )|'----------------------'|( )|'----------|")
                                        print(
                                            "bij de goede optie kunt u punten verdienen ")
                                        time.sleep(3)
                                        print("Juist ging ik weg van het huis, omdat ze praten tegen mij nog steeds onaardig.\n Ja dus in mij hoofd en voor mij gevoel ik vond het niet goed dus ik zeg fuck jullie ik wil mij spullen en ik wil weg. Ze schrokkend van mij reactie en ze zeggen ok.\n Dat was het laatste woord dat heb ik op dit huis gehoor. Ik heb mij spullen en ik ging naar Acropolis.\n Ik woonde toen in Athene.\n Ik had geen idee waar moet ik heen en ik ga niet terug sorry zeggen. Dus ik ben een nacht in Acropolis geslapen, omdat ik wist niet waar moet ik heen op dat moment.\n Het was leuk trouwens geen regels niks beetje koud in nacht maar ik voel mij vrij.\n Volgende dag 6 uur ochtend ik heb gegeten en ik belde een vriend van mij dat ik moet bij hem komen wonen, ik legde uit wat was in hand.\n Hij zegt maak geen zorgen, zijn naam was Ibrahim. We ontmoeten in eerste kamp we hadden vroeger ons belovend dat we vrienden zou zijn tot einde van de aarde.\n Ik wist dat ik kan op hem rekenen. Ik reisde van Athene naar Chalcis een stad die drie kwartier ver weg de naam van kamp is Ritsonna.\n Ik arriveerde naar het kamp het kamp was erger dan alle andere kampen waar ik geweest ben. Dat was mij keuze, ik vind het fijn.\n Ik registert in de ik kamp en ik moest weer in plek in kamp waar jongeren onder 18 zijn. Ik vond het prima, omdat ik ging naar daar heen en ik zag dat ze minder string zijn echt super lief mensen.\n Ik hoorde bij het rode kruis. Echt heel aardig mensen. Ik moet gewoon wachten, totdat ik iets hoor van organisatie over mij toekomst.\n")
                                        print("Tussen de tijd in Ritsonna:")
                                        print(
                                            "___________   _______________________________________^__")
                                        print(
                                            " ___   ___ |||  ___   ___   ___    ___ ___  |   __  ,----\ ")
                                        print(
                                            "|   | |   |||| |   | |   | |   |  |   |   | |  |  | |_____\ ")
                                        print(
                                            "|___| |___|||| |___| |___| |___|  | O | O | |  |  |        \ ")
                                        print(
                                            "           |||                    |___|___| |  |__|         )")
                                        print(
                                            "___________|||______________________________|______________/")
                                        print(
                                            "           |||                                        /--------")
                                        print(
                                            "-----------'''---------------------------------------'")
                                        print("Gebleven tijd andere half jaar in Griekenland. Na een anderhalf jaar ik heb zeker veel geleerd van het leven ik zag situatie,\n ik hoorde verhalen, ik had een klein meisje die ik veel van haar houd haar leven verloren door iemand die dronken was in ongeluk auto.\n Hij was dronken en ging door rijden meisje was kwijt. Dat was de grootste schok voor mijn in Griekenland en het verdrietigste moment van mij leven op dat moment.\n Ik ging terug naar Thessaloniki om haar andere twee zusje te bezoeken en haar moeder. Ik deed wat ik kon, bleef tot haar begrafenis en probeerde haar zusjes en de moeder te kalmeren.\n Toen moest ik terug naar Chalcis ik mag niet veel tijd besteden buiten de kamp knuffel aan iedereen gegeven en Ik ging terug naar kamp.\n Zeker door dit gebeurtenis er is altijd kleine gat in mijn haar voor dat meid die was 5-6 jaar oud en haar leven verloren vanwege iemand dronken is voor niks. Ik ben terug in kamp.\n Ik heb eindelijk niet zo veel te doen. Elke dag zelfde routen.  Ik ging zeker zelf leren met Engels taal door.\n  Spelen met kienden van kamp zoals altijd en vrienden maken om tijd kwijt te raken. Ik vond het niet genoeg, ik wilde wat andere stepjes doen. Ik ging naar rode kuise en andere organisatie violenteren om hen te helpen.\n Ik ging naar gesprek en ik had het gesprek. Ik mag hun helpen. Ik werd een leraar assistent ik vertaal voor andere volwassen leraren in Arabisch die willen graag Engels leren, Ik had meer dan 20 kind die ik zelf geef Engels les voor, Andere activiteiten film kijken met kinderen en soms moet ik mee met rode kruis naar ziekenhuis om te vertalen.\n Het is nu al 4 maanden in Ritsonna kamp en ik begin hoop te verloren na bijna 2 jaar wachttijd in Griekenland.\n Ik ging naar mensen die zijn verantwoordelijk over mij en Ik vroeg hun dat ik heel graag wil naar Turkije of begin ik hier mij leven te bouwen. Toevallig er was een advocaat die ons helpen en het was haar functie zorgen dat we beter toekomst krijgen.\n Ze hoorde mij gesprek dat ik depperset ben en niet blij. Ze wilden mij graag helpen om te rijzen naar andere land met beter toekomst. Ze vertelt mij.\n Ik beloven je als je wacht, totdat ik terug ben ik zou goede nieuws hebben. Ik vroeg ongeveer hoeveel maanden moet ik wachten ongeveer ze zei drie maanden.\n")
                                        print("Wat denkt u?")
                                        print(".1 Ik heb wel gewacht!")
                                        print(
                                            ".2 of ik vertrouw de advocaat niet! En ik wil nog steeds graag naar Turkije of wonen in Griekenland!")
                                        Stukje19keuzes = ask()
                                        os.system("cls")
                                        if Stukje19keuzes == 2:
                                            print("Als ik toch de advocaat had niet vertrouwde, Ik woon in Griekenland op dat moment, omdat Elena was een van mijn favoriete mensen.\n Ze zei je mag niet terug van naar Turkije ik wil je heel graag adopteren, ik houd ook van haar heel veel dus als ik niks had gehoord had.\n Ik woon nu in Griekenland met Elena.  Einde")
                                            time.sleep(3)
                                            print(
                                                " jij hebt zowel punten: " + str(Score))
                                            quit
                                        elif Stukje19keuzes == 1:
                                            Score += 1
                                            print("3 maanden zijn geen kwaad, nadat alle geduid.\n Wel juist gewacht. De mevrouw hield haar woord ze is terug met een beter nieuws.\n Ze zegt je wordt gebeld dan moet je naar Athene, Athene consulaat daar hoor het nieuws. Ik ben gebeld naar paar dagen.\n Ik ben naar Athene geweest om het nieuws te horen. Het was het mooiste moment van mij leven, ik werd verwelkomde in koninkrijk van der Nederland om te gaan wonen.\n Ik heb mijn handtekking op Ja gezet terwijl ik aan het huilen was. Ik woon op dat moment in Nederland met blij leven.\n")
                                            time.sleep(3)
                                            print("        ______")
                                            print("            _\ _~-\___")
                                            print("    =  = ==(____AA____D")
                                            print(
                                                "                \_____\___________________,-~~~~~~~`-.._")
                                            print(
                                                "                /     o O o o o o O O o o o o o o O o  |\_")
                                            print(
                                                "               `~-.__        ___..----..                  )")
                                            print(
                                                "                      `---~~\___________/------------`````")
                                            print(
                                                "                      =  ===(_________D")
                                            print(
                                                "Blij Einde Ik woon in Nederland")
                                            print(
                                                "   _    _.--.____.--._          ")
                                            print(
                                                " \\\:;:;:;:;:;;:;::;:;:;:\          ")
                                            print(
                                                "  \\\:;:;:;:;:;;:;:;:;:;:;\         ")
                                            print(
                                                "   \\\:;::;:;:;:;:;::;:;:;:\        ")
                                            print(
                                                "    \\\:;:;:;:;:;;:;::;:;:;:\       ")
                                            print(
                                                "     \\\:;::;:;:;:;:;::;:;:;:\      ")
                                            print(
                                                "      \\\;;:;:_:--:_:_:--:_;:;\     ")
                                            print(
                                                "       \\\_.-"             "-._\    ")
                                            print(
                                                "        \\                          ")
                                            print(
                                                "         \\ Nederland yesss         ")
                                            print(
                                                "          \\                        ")
                                            print(
                                                "           \\                       ")
                                            print(
                                                "            \\                      ")
                                            print(
                                                "             \\                     ")
                                            print(
                                                " jij hebt zowel punten: " + str(Score))
                                            ask1 = input(
                                                "Wilt u nog een keer spelen? ja of nee : \n")
                                            if ask1 == "nee":
                                                print("Helaas niet:(")
                                                break
