import keyboard
from click import clear


FIRST_CHAPTER_PHRASES = ["'TAB' in a single copy! Don't click!", "Get your hands off me!", "You can break me!", "That's enough!", "That's it! Stop!"]
FIRST_QUEST_PHRASES = ["I ran away. Find me (poke the keys)", "How? And so?"]
SECOND_CHAPTER_PHRASES = ["I'm tired of you! Stop it!", "Aren't you tired of it yourself?", "Will that be enough?", "You're wasting your time!", "I see that you are not giving up. Well done!", "NO!!!"]
SECOND_QUEST_PHRASES = ["NO!!!", "NO!!!", "NO!!!", "Is it broken?"]
THIRD_CHAPTER_PHRASES = ["HA-HA-HA!", "What???", "How did you fix it?", "It doesn't matter though.", "Stop it!", "Would it please you if you were pressed all the time?", "ALL THE TIME!", "Don't you understand?", "This game has no end!"]
THIRD_QUEST_PHRASE = "I won't talk to you until you type my name."
FINISH_PHRASES = ["You did it!", "But how?", "You handled everything!", "Yes! Well down!", "...", ".....", ".......", "This", "This is", "This is the", "This is the end!", "Thanks for playing!", "Press 'Tab' to exit."]


def about():
    clear()
    print("This game was created by George Salt at the 23rd of April. To start the game restart the project.")


def first_quest(phrases):
    print(phrases[0])
    keyboard.wait("g")
    clear()
    print(phrases[1])
    keyboard.wait("m")
    clear()


def second_quest(phrases):
    for phrase in phrases:
        print(phrase)
        keyboard.wait("Tab")
        clear()


def third_quest(phrase):
    print(phrase)
    keyboard.wait("t")
    keyboard.wait("a")
    keyboard.wait("b")
    clear()


def first_chapter(phrases):
    for phrase in phrases:
        print(phrase)
        keyboard.wait("Tab")
        clear()


def second_chapter(phrases):
    for phrase in phrases:
        print(phrase)
        keyboard.wait("Tab")
        clear()


def third_chapter(phrases):
    for phrase in phrases:
        print(phrase)
        keyboard.wait("Tab")
        clear()


def finish(phrases):
    for phrase in phrases:
        print(phrase)
        keyboard.wait("Tab")
        clear()


def main_game():
    clear()
    first_chapter(FIRST_CHAPTER_PHRASES)
    first_quest(FIRST_QUEST_PHRASES)
    second_chapter(SECOND_CHAPTER_PHRASES)
    second_quest(SECOND_QUEST_PHRASES)
    third_chapter(THIRD_CHAPTER_PHRASES)
    third_quest(THIRD_QUEST_PHRASE)
    finish(FINISH_PHRASES)


if __name__ == "__main__":
    keyboard.add_hotkey("Ctrl + h", about)
    main_game()
