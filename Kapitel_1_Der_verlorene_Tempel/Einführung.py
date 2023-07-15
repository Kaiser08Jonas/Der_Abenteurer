from colorama import Fore
import os
from Kapitel_1_Der_verlorene_Tempel.Kambodscha import Kambodscha as Kapitel_1_Kambodscha

inventory = ['']
cell_phone = Fore.LIGHTCYAN_EX + 'Telefon' + Fore.RESET
pr_goldenbark = Fore.BLUE + 'Goldenbark' + Fore.RESET


class Introduction:

    current_chapter = ''

    def __init__(self, player_name: str):
        self.player_name = player_name

    def __str__(self):
        return self.current_chapter

    def introduction(self):
        self.current_chapter = 'Introduction'
        print(Fore.GREEN + '-----Kapitel 1: Der verlorene Tempel-----' + Fore.RESET)
        print()
        print(Fore.LIGHTGREEN_EX + '-----Einführung-----' + Fore.RESET)
        print(f'Du wachst früh am Morgen durch ein Geräusch auf.\n'
              f'[{cell_phone}] Ring, Ring\n'
              f'[{self.player_name}] "Hallo?"\n'
              f'[{pr_goldenbark}] "Hier ist Professor Goldenbark."\n'
              f'[{self.player_name}] "Hallo Professor. Warum rufen sie mich so früh am Morgen an?"\n'
              f'[{pr_goldenbark}] "Tut mir leid. Ich habe vergessen, dass es bei Ihnen ja erst 5 Uhr ist, aber es ist wichtig."\n'
              f'[{self.player_name}] "Schon gut. Worum geht es?"\n'
              f'[{pr_goldenbark}] "Ich habe von einen Gerücht gehört."\n'
              f'[{self.player_name}] "Sie wecken mich wegen einem Gerücht?"\n'
              f'[{pr_goldenbark}] "Nun, ja. Es geht um einen Verlorenen Tempel. Aber es ist zu wichtig, um es am Telefon zu besprechen"\n'
              f'[{pr_goldenbark}] "Bitte, komm doch zu mir nach Kansas City. Es ist sehr wichtig! Ich zahle auch den Flug."\n'
              f'[{self.player_name}] "Wenn Sie sich so sicher sind, dann komme ich zu Ihnen. Ich nehme den morgigen Flug nach Kansas."\n'
              f'[{pr_goldenbark}] "Super. Dann bis morgen."\n'
              f'[{self.player_name}] "Bis morgen."\n'
              f'[{cell_phone}] Klick\n'
              f'[{self.player_name}] "Ich hoffe, dass es das wert ist."\n'
              f'Bitte beliebige Taste für den nächsten Tag eingeben.')
        input('> ')
        print(f'Du gehst noch etwas ermüdet von der Reise zum Büro von Professor Goldenbark.\n'
              f'[{pr_goldenbark}] "Hallo {self.player_name}"\n'
              f'[{self.player_name}] "Hallo Professor. Was war denn so wichtig, dass ich so schnell her kommen sollte?"\n'
              f'[{pr_goldenbark}] "Komm doch herein."\n'
              f'[{pr_goldenbark}] "Bei diesem Gerücht geht es um einen Verlorenen Tempel. In dem Tempel soll es ein Artefakt geben."\n'
              f'[{self.player_name}] "Was ist das für ein Artefakt?"\n'
              f'[{pr_goldenbark}] "Es ist ein Amulett. Nach diesem Amulett hab ich mein Leben lang gesucht."\n'
              f'[{pr_goldenbark}] "Es gehörte einmal der Königin von Konstantinopel"\n'
              f'[{self.player_name}] "Der Königin von Konstantinopel?"\n'
              f'[{pr_goldenbark}] "JA! Es soll angeblich heilen können. Alten Schriften aus Konstantinopel zufolge, soll es sogar der Königin"\n'
              f'[{pr_goldenbark}] "das Leben gerettet haben, indem es sie von einer Pfeilverletzung geheilt hat."\n'
              f'[{self.player_name}] "Wo soll es sich denn überhaupt befinden?\n'
              f'[{pr_goldenbark}] "Da beginnt es knifflig zu werden. Angeblich hat ein Stamm von Eingeborenen, welche im Dschungel von Kambodscha"\n'
              f'[{pr_goldenbark}] "leben, der Königin das Amulett gestohlen und in einem Ihrer Tempel versteckt. Niemand weis, wo sich der Stamm"\n'
              f'[{pr_goldenbark}] "heute aufhaltet. Sie existieren noch heute, jedoch misstrauen sie jedem, welcher nicht von ihrem Stamm ist."\n'
              f'[{self.player_name}] "Also soll ich herausfinden, wo sich der Stamm befindet, um zu erfahren, wo der Tempel ist oder?"\n'
              f'[{pr_goldenbark}] "Ja. Es gibt jemanden, welcher behauptete zu wissen wo sich der Stamm gerade befindet."\n'
              f'[{pr_goldenbark}] "Ich habe ihn gefunden und er hat mir eine Wegbeschreibung geschrieben und meinte,"\n'
              f'[{pr_goldenbark}] "dass das ihr letzter aufenthaltsort war."')
        path = os.path.join(os.path.dirname(__file__), 'Die Wegbeschreibung.jpg')
        os.startfile(path)
        print(f'[{pr_goldenbark}] "Bitte folge der Wegbeschreibung und finde heraus, wo sich das Artefakt befindet und bringe es zu mir."\n'
              f'[{self.player_name}] "Na gut. Ich mache mich auf die Suche nach dem Artefakt."\n'
              f'[{pr_goldenbark}] "Vielen dank. Natürlich komme ich für alle Kosten auf. Ich hoffe Sie haben erfolg."\n'
              f'[{self.player_name}] "Auf wiedersehen Professor. Ich rufe Sie an, falls ich etwas herausfinde."\n'
              f'[{pr_goldenbark}] "Super. Auf wiedersehen."\n'
              f'Du verlässt das Büro und machst dich auf den Weg zu deinem Hotelzimmer.\n'
              f'Am nächsten Morgen Fliegst du mit dem Flieger nach Kambodscha.')
        input('> ')
        print()
        print(Fore.GREEN + 'Abschnitt 1: Kambodscha' + Fore.RESET)
        kapitel = Kapitel_1_Kambodscha(player_name=self.player_name)
        kapitel.stonehill()
