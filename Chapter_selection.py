from colorama import Fore
import os
from Kapitel_1_Der_verlorene_Tempel.Einführung import Introduction as Kapitel_1_Introduction
from Kapitel_1_Der_verlorene_Tempel.Kambodscha import Kambodscha as Kapitel_1_Kambodscha

coloured_wrong_answer = Fore.YELLOW + 'Dies ist keine gültige Eingabe!' + Fore.RESET
coloured_north = Fore.BLUE + 'Norden' + Fore.RESET
coloured_south = Fore.BLUE + 'Süden' + Fore.RESET
coloured_east = Fore.BLUE + 'Osten' + Fore.RESET
coloured_west = Fore.BLUE + 'Westen' + Fore.RESET
coloured_look_around = Fore.BLUE + 'Umschauen' + Fore.RESET

player_name = ''


# Kapitelauswahl
def main():
    global player_name
    print(Fore.RED + '-----Der Abenteurer-----' + Fore.RESET + '\n'
          'Dies ist ein Text basiertes Spiel.\n'
          f'\nUm dich im Spiel zu bewegen, kannst du die Himmelsrichtungen verwenden.\n'
          f'Einfach {coloured_north}, {coloured_south}, {coloured_east} oder {coloured_west} eingeben.\n'
          f'Du kannst dich auch mit {coloured_look_around} nach versteckten sachen umsehen.\n'
          'Als erstes gib doch bitte deinen Namen ein.')
    name = input('> ')
    name = Fore.CYAN + name + Fore.RESET
    player_name = name
    print(f'Dein name lautet {name}.\n')
    explanation()


def explanation():
    print('Bevor das Spiel beginnt, solltest du erfahren, wer du bist.\n'
          'Du bist ein furchtloser Abenteurer. Bereits zahlreiche Abenteuer hast du hinter dir und sehr viele\n'
          'Artefakte hast du aufgetrieben. Es gibt einige Forscher, welche sich immer an dich wenden,\n'
          'wenn sie irgend wo ein Abenteuer vermuten.\n'
          'Aber als erstes kannst du dein nächstes Abenteuer in der Kapitelauswahl wählen, indem du eine beliebige Taste ein gibst.')
    input('> ')
    chapter_selection()


def chapter_selection():
    chapter = {
        1: 'Der verlorene Tempel'
    }
    print()
    print(Fore.GREEN + '-----Kapitelauswahl-----' + Fore.RESET + '\n'
          'Bitte die Zahl eines der folgenden Kapitel eingeben, um ein Kapitel auszuwählen:')
    print()
    for number, titel in chapter.items():
        print(f'{number}: {titel}')
    selected_chapter = int(input('> '))

    if selected_chapter in chapter:
        print(f'Du hast Kapitel {selected_chapter}: {chapter[selected_chapter]} ausgewählt')
        match selected_chapter:
            case 1:
                print()
                print('Hast du dieses Kapitel schon einmal angefangen zu spielen? Ja oder Nein')
                play_again = input('> ')
                match play_again:
                    case 'Ja':
                        print()
                        print('Bitte wähle das letzte Kapitel aus, von welchem aus du weiter spielen möchtest.')
                        chapter_1 = {
                            1: 'Kambodscha'
                        }
                        for number, titel in chapter_1.items():
                            print(f'{number}: {titel}')
                        selected_chapter = int(input('> '))
                        if selected_chapter in chapter_1:
                            match selected_chapter:
                                case 1:
                                    print('Dann kannst du das Spiel in Kambodscha fortsetzen.')
                                    path = os.path.join(os.path.dirname(__file__), 'Kapitel_1_Der_verlorene_Tempel')
                                    os.startfile(path)
                                    kapitel = Kapitel_1_Kambodscha(player_name=player_name)
                                    kapitel.stonehill()
                        else:
                            print(coloured_wrong_answer)
                            print()
                            chapter_selection()

                    case 'Nein':
                        print()
                        print('Dann kannst du dieses Kapitel mit einer beliebigen Eingabe starten:')
                        input('> ')
                        print()
                        kapitel = Kapitel_1_Introduction(player_name=player_name)
                        kapitel.introduction()
                    case _:
                        print(coloured_wrong_answer)
                        print()
                        chapter_selection()
            case _:
                print(coloured_wrong_answer)
                print()
                chapter_selection()

    else:
        print(coloured_wrong_answer)
        print()
        chapter_selection()


if __name__ == '__main__':
    main()
