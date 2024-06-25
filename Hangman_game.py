from random import choice
print("Welcome to Hangman\nThe computer will randomly choose a aword and you will try to guess what the word is"
      "\nGood Luck! Have fun playing")
animals_easy = ["elephant", "giraffe", "dinosaur", "shark", "zebra", "monkey", "panda", 'lion', 'tiger', 'fox', 'cow',
                'sheep','horse','cat','fish','dog','wolf','ant','donkey','chicken','gorilla','bear','cheetah','whale',
                'bat','camel','cobra','eagle','goat','mouse','rabbit','snake','spider','tiger','turtle','owl','parrot']
animals_hard = ["koala","Jaguar","leopard","rhino","platypus","kangaroo","moose","python","axolotl","pangolin","blobfish"
    ,"orangutan","armadillo","cockroach","beluga","muskellunge",'crocodile','hippopotamus','baboon','badger','beaver','clam'
                ,'cougar','coyote','crow','deer','duck','ferret','frog','goose','hawk','lizard','llama','mole','mule',
                'newt','otter','pigeon','ram','rat','raven','salmon','seal','skunk','sloth','stork','swan','toad',
                'trout','turkey','weasel','wombat']
hangman = ['       O       ',
           '+------|       ',
           '|    -----     ',
           '|   /  |  \    ',
           '|      |       ',
           '|    -----     ',
           '===  |   |     ']
play_again = 'y'
while play_again.lower() == ('y' or 'yes' or 'ye'):
    game_level = input("please choose between:\n(1) Easy\n(2) Hard\n")
    if game_level == 1 or (1):
        animal = choice(animals_easy)
    elif game_level == 2 or (2):
        animal = choice(animals_hard)
    else:
        print("Invalid Error!!Try again.")
    solution = "*" * len(animal)
    tries = 1
    wrong = True
    MAX_TRIES = 7
    art = ""
    for i in range(tries):
        art += hangman[i] + "\n"
    print(art)
    while wrong and tries <= MAX_TRIES:
        print(solution)
        word = input("Guess a letter in the word or enter the full word: ").strip().lower()
        gotone = False
        if word not in solution:
            for i in range(len(animal)):
                for char in word:
                    if char == animal[i]:
                        solution = solution[:i] + char + solution[i + 1:]
                        gotone = True
                        print(f"You input {char}, Great! That letter exists in the word!\n")
        if not gotone:
            tries += 1
            art = ""
            print("Sorry, that letter is not part of the word\n")
            for i in range(tries):
                art += hangman[i] + "\n"
            if tries <= 7:
                print(art)
        if solution.find("*") == -1:
            wrong = False
    if not wrong:
        print(f'Great Job! You guessed the word correctly!\nIt is in fact "{animal}"', "You won!", sep='\n')
    else:
        print("Sorry, that was not the word we were looking for\n")
        print(art + hangman[-1], f'It was "{animal}"', "You lost", sep='\n')
    play_again = input("Do you want to play again? (y/n): ")
print("End Game.\nHope you had fun playing the game. See you next time")
