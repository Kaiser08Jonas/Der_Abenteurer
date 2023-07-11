from colorama import Fore, Style
from Kapitel_1_Der_verlorene_Tempel.Einführung import Introduction as Kapitel_1_Introduction

colored_wrong_answer = Fore.YELLOW + 'Dies ist keine gültige Eingabe!' + Style.RESET_ALL

player_name = ''


# Kapitelauswahl
def main():
    global player_name
    print('Dies ist ein Text basiertes Spiel.\n'
          'Als erstes gib doch bitte deinen Namen ein.')
    name = input('> ')
    name = Fore.CYAN + name + Style.RESET_ALL
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
    print(Fore.GREEN + '-----Kapitelauswahl-----' + Style.RESET_ALL + '\n'
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
                kapitel = Kapitel_1_Introduction(player_name=player_name)
                kapitel.introduction()
    else:
        print(colored_wrong_answer)
        print()
        chapter_selection()


if __name__ == '__main__':
    main()
