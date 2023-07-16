from colorama import Fore

coloured_wrong_answer = Fore.YELLOW + 'Dies ist keine gültige Eingabe!' + Fore.RESET
coloured_north = Fore.BLUE + 'Norden' + Fore.RESET
coloured_south = Fore.BLUE + 'Süden' + Fore.RESET
coloured_east = Fore.BLUE + 'Osten' + Fore.RESET
coloured_west = Fore.BLUE + 'Westen' + Fore.RESET
coloured_look_around = Fore.BLUE + 'Umschauen' + Fore.RESET
coloured_arun = Fore.BLUE + 'Arun' + Fore.RESET


class Kambodscha:

    current_chapter = ''
    talked_to_arun = False
    visited_stonehill = False

    def __init__(self, player_name: str):
        self.player_name = player_name

    def __str__(self):
        return self.current_chapter

    def stonehill(self):
        self.current_chapter = 'Stonehill'
        print()
        print(Fore.LIGHTGREEN_EX + '-----Stonehill-----' + Fore.RESET)
        print('Du fliegst mit einem Flieger nach Kambodscha. Von dort wirst du mit einem Boot nach Stonehill gebracht.\n'
              'Stonehill ist ein kleines Dorf, welches am Dschungel von Kambodscha liegt.\n'
              'Es hat nur noch wenige Einwohner, da es nicht sehr viele menschen gibt, welche so abgeschieden von der Civilisation leben möchten\n'
              'Als du dort an kommst und durch das Dorf gehst fällt dir auf, dass bei ein paar Hütten die Fenster zugenagelt wurden.\n'
              '') if not self.visited_stonehill else None
        print('Was willst du tun?')
        choice = input('> ')
        self.visited_stonehill = True
        match choice:
            case 'Norden':
                print('Im Norden endet das Dorf und der Dschungel beginnt. Willst du dort hin gehen? Ja oder Nein')
                choice = input('> ')
                if choice == 'Ja':
                    print('"Ich bin bereit in den Dschungel zu gehen."\n')
                    Kambodscha.crossing1(self)
                else:
                    print('"Ich gehe zurück ins Dorf."')
                    Kambodscha.stonehill(self)
            case 'Süden':
                print('Im Süden des Dorfes ist der Pier, an welchem du abgesetzt wurdest. Als du ausgestiegen bist, hast du dich bereits\n'
                      'umgesehen und nichts auffälliges entdeckt.')
                input('> ')
                Kambodscha.stonehill(self)
            case 'Osten':
                print('Im Osten ist ein Berg. Die Häuser des Dorfes gehen bis kurz vor eine Felswand, welche unmöglich erklommen werden kann.\n'
                      'So wie es aussieht, sollte dort ein Weg nach oben errichtet werden, welcher jedoch nicht fertig gestellt wurde.\n'
                      'An der Felswand hängt ein Zettel.\n'
                      '"Vorsicht vor herabfallenden Steinen!"\n'
                      '"Der Bau des Weges auf den Berg wurde noch nicht beendet."')
                input('> ')
                Kambodscha.stonehill(self)
            case 'Westen':
                print('Im Westen des Dorfes sind drei sehr alte Häuser, welche vermutlich jederzeit zusammenbrechen könnten.\n'
                      '"Ich sollte auf keinen Fall dort hinein gehen."\n'
                      'Sonst scheint es, dort nichts zu geben.')
                input('> ')
                Kambodscha.stonehill(self)
            case 'Umschauen':
                if not self.talked_to_arun:
                    print('Du entdeckst ein Kind, welches von einer Schaukel auf der Terrasse des Hauses,\n'
                          'dass dir am nächsten ist, sitzt und dich anschaut.\n'
                          f'Als du dich dem Haus näherst, steht das Kind auf. Willst du mit dem Kind im {coloured_west} ist?')
                    choice = input('> ')
                    if choice == 'Westen':
                        print()
                        print('Du gehst näher an das Kind heran.')
                        print(f'[{self.player_name}] "Hallo."\n'
                              f'[{coloured_arun}] "Hallo. Ich heiße Arun. Was wollt ihr hier\n'
                              f'[{self.player_name}] "Ich bin auf der Suche nach etwas.\n'
                              f'[{coloured_arun}] "Ich auch."\n'
                              f'[{self.player_name}] "Wonach suchst du denn?"\n'
                              f'[{coloured_arun}] "An der Küste ist vor kurzem ein FLoß gegen die Küste geprallt und kaputt gegangen."\n'
                              f'[{coloured_arun}] "Kurz vorher habe ich es beobachtet und ein Glänzendes Objekt gesehen. Das suche ich,"\n'
                              f'[{coloured_arun}] "doch meine Eltern erlauben mir nicht, an die Küste zu gehen und nachzuschauen,"\n'
                              f'[{coloured_arun}] "da dort eine große Krabbe ist, welche sehr aggressive seien soll."\n'
                              f'[{coloured_arun}] "Wonach Suchen sie denn?"\n'
                              f'[{self.player_name}] "Ich suche nach einem Amulett. Ein paar Eingeborenen sollen wissen, wo es ist."\n'
                              f'[{coloured_arun}] "Sie sollten sich von ihnen fern halten."\n'
                              f'Kaum hatte Arun den Satz ausgesprochen, rannte ehr zurück ins Haus und verschloss die Tür.\n'
                              f'"Habe ich was falsches gesagt?"')
                        self.talked_to_arun = True
                        input('> ')
                        Kambodscha.stonehill(self)
                    else:
                        print()
                        print("Ich will erst mal noch nicht mit ihm reden.")
                        Kambodscha.stonehill(self)
                else:
                    print('\n"Arun ist im Haus verschwunden. Ich sollte nicht noch einmal versuchen, mit ihm zu reden."')
                    Kambodscha.stonehill(self)
            case _:
                print('falsch')
                Kambodscha.stonehill(self)

    def crossing1(self):
        self.current_chapter = 'crossing1'
        print(f'Eine Kreuzung. Dort vorne steht ein Wegweiser:\n{coloured_north} = Dschungel\n{coloured_south} = Stonehill\n{coloured_west} = Küste\n'
              f'"Was soll ich tun?')
        choice = input('> ')
        match choice:
            case 'Norden':
                print('"Ich gehe tiefer in den Dschungel hinein."')
                Kambodscha.crossing2(self)
            case 'Süden':
                print('"Ich gehe zurück ins Dorf."')
                Kambodscha.stonehill(self)
            case 'Osten':
                print('Im Osten ist der Dschungel zu dicht, um ihn zu durchqueren.')
                Kambodscha.crossing1(self)
            case 'Westen':
                print(f'"Ich versuche mal mein Glück im {coloured_west}."')
                Kambodscha.coast(self)
            case 'Umschauen':
                print('Es ist nur dichter Dschungel und Stonehill zu sehen.')
                Kambodscha.crossing1(self)

    def crossing2(self):
        self.current_chapter = 'crossing2'
        print(f'"Hier ist nur dichter Dschungel. In der Ferne sehe ich ein paar Häuser von Stonehill, welche im {coloured_south} sind."')
        choice = input('> ')
        match choice:
            case 'Norden':
                print('"Am besten gehe ich in den Norden."')
                Kambodscha.crossing3(self)
            case 'Süden':
                print('"Ich gehe näher zu den Häusern von Stonehill."')
                Kambodscha.crossing1(self)
            case 'Osten':
                print('"Dort ist extrem dichter Dschungel. Ich glaube, dass ich dort nicht hindurch komme."')
                Kambodscha.crossing2(self)
            case 'Westen':
                print('')
            case 'Umschauen':
                print(f'"Ich sehe nur dichten Dschungel und in der Ferne Stonehill. Im {coloured_north} und {coloured_west} sieht der Dschungel"\n'
                      f'"Durchquerbar aus. Vielleicht sollte ich es dort versuchen."')
                Kambodscha.crossing2(self)

    def crossing3(self):
        self.current_chapter = 'crossing3'
        print(f'"Schon wieder nur dichter Dschungel. Irgendwo muss es doch etwas geben, was mir weiter hilft."')
        choice = input('> ')
        match choice:
            case 'Norden':
                print(f'"Im {coloured_north} gibt es keinen Weg, durch welchen ich den Dschungel weiter durchqueren könnte."')
                Kambodscha.crossing3(self)
            case 'Süden':
                print('"Ich gehe nach Süden"')
                Kambodscha.crossing2(self)
            case 'Osten':
                print('')
            case 'Westen':
                print(f'')
            case 'Umschauen':
                print(f'"Hier gibt es wieder nur Dschungel. Wobei ich im {coloured_east} etwas durch die Bäume zu sehen.\n'
                      f'Ich kann nicht genau erkennen, was es ist."')
                Kambodscha.crossing3(self)

    def coast(self):
        self.current_chapter = 'coast'
