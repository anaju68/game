# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Viuva Negra")
define b = Character("capitainamerica")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene avenger


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show viuva

    # These display lines of dialogue.

    e "Você acabou de criar um jogo RENPY."

    hide viuva
    show capitao   

    b "alguma coisa"

    # This ends the game.

    return
