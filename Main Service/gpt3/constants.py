prompt = """Assign Type using Text

Text: FW: EK setzen. Bitte die Bestellungen schließen.
-----
EK setzen

Einkaufsbeleg
9704291204
9704444700
9704492525
9704452285
9704579750
9704336331
9704781386
9704407509
9704406420
9704407509
9704406420


Liebe Frau $PERSON ,
könnten Sie bitte für diese Belege EK setzen lassen?
Vielen Dank!
Renate Kaspar



With best

Category: [elk, erk]
###
Text: Endrechnungskennzeichen. Bitte in folgenden Bestellungen das #Endrechnungskennzeichen setzen.

9704530974
9704679737

Vielen Dank!
Category:
###
Text: RE: Ticket 392353: WE kann nicht gebucht werden - PO 9703814574 9703375074. Könnt ihr bitte die Anforderung übernehmen?

Vielen Dank!


Wichtiger Hinweis zur Zentralisierung des operativen Einkaufsprozesses:
Zentraler Kontakt für Freitextbestellungen:
* $PERSON ( $PERSON

$PERSON Kontakt für Katalogbestellungen:
*
$Email


Ich wünsche Ihnen einen schönen Tag!
-----
Ticket 392353: WE kann nicht gebucht werden - PO 9703814574 9703375074

$PERSON ,
hiermit übergeben wir Ihnen die unten angeführte Supportanfrage mit der Nr. 392353 zur Bearbeitung, da es sich um eine Einkaufsthematik handelt.
Bitte entfernt das Endlieferkennzeichen in den og PO´s da $PERSON gebucht werden muss und gebt uns nach Erledigung innerhalb von zwei Werktagen unbedingt eine Rückmeldung.
Wichtiger Hinweis zur Zentralisierung des Einkaufsprozesses:
1 zentralisierte Kontakt-Email:
$Email
1 zentralisierte $PERSON : $PERSON : Mo-Fr, 08.00-17.00
Für Fragen steht Ihnen unser Team gerne zur Verfügung.
Category: [elk, erk]
"""

text_prompt = """

        WG: Endliefer- und Endrechnungskennzeichen - PV2050. hier nochmal unverschlüsselt…
        -----
        Endliefer- und Endrechnungskennzeichen - PV2050


        bitte bei folgenden Bestellungen ein Endliefer- und Endrechnungskennzeichen setzen.

        9704187851 Pos. 1 und 2 (Endrechnungskennzeichen)

        9704612454 Pos. 1 und 2 (Endrechnungskennzeichen)

        9704114442 Pos. 1 und 2 (Endrechnungs- und Endlieferkennzeichen)

        9703784941 Pos. 1 und 2 (Endrechnungs- und Endlieferkennzeichen)

        9704187708 Pos. 1 und 2 (Endrechnungskennzeichen)

        9704613098 Pos. 1 und 2 (Endrechnungskennzeichen)

        9704242380 Pos. 1 (Endrechnungskennzeichen)

        9704634083 Pos. 1 und 2 (Endrechnungskennzeichen)

        9704187710 Pos. 1 und 2 (Endrechnungskennzeichen)

        9704616065 Pos. 1 und 2 (Endrechnungskennzeichen)"""
