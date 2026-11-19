# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
#.       DANIEL BROWN
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Games Project
# Date: 22 October 2026
#
import random
import time

def game_loop():
    game_selection = input('''
    What game would you like to play?
        Hangman (1): A word guessing game where you guess letters. You win by getting the whole word and lose by guessing
        6 invalid letters.
        Blackjack (2): A card game where your goal is to obtain an additive card value as close to 21 as possible without
        passing it. Your hand value will be displayed after every action.
        Trivia (3): A fast paced, knowledge based game of the mind. Who knows the most? Test your knowledge with a competitive
        multiple choice quiz
        
    You can get back to this menu at any time by using the input 'exit'
    Enter your selection (1/2/3):  ''')
    if game_selection == "1":
        words = ["python", "engineering", "computer", "soccer", "college", "programming", "hangman", "university"]

        word = random.choice(words)

        guessed_letters = []

        incorrect_guesses = 6

        print("Welcome to Hangman!")
        print("Guess the word one letter at a time.")

        while incorrect_guesses > 0:

            display_word = ""

            for letter in word:
                if letter in guessed_letters:
                    display_word += letter + " "
                else:
                    display_word += "_ "

            print("\nWord:", display_word)
            print("Incorrect guesses remaining:", incorrect_guesses)

            if "_" not in display_word:
                print("\nCongratulations! You won!")
                break

            guess = input("Guess a letter: ").lower()

            if guess == "exit":
                game_loop()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter one letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue

            guessed_letters.append(guess)

            if guess in word:
                print("Correct guess!")
            else:
                print("Incorrect guess!")
                incorrect_guesses -= 1

        else:
            print("\nYou lost!")
            print("The word was:", word)

    elif game_selection == "2":
        # Deck Setup
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10,
                  'King': 10, 'Ace': 11}


        # DECK class
        class Deck:
            def __init__(self):
                self.cards = []
                for rank in ranks:
                    for suit in suits:
                        self.cards.append((rank, suit))

                random.shuffle(self.cards)  # Shuffles the deck

            def deal_card(self):  # Deals a card from the deck
                if self.cards:
                    return self.cards.pop()
                else:
                    return None


        # Player class
        class Player:
            def __init__(self, name):
                self.name = name
                self.hand = []
                self.score = 0

            def score_hand(self):
                self.score = 0
                aces = 0
                for card in self.hand:
                    rank, suit = card
                    self.score += values[rank]
                    if rank == 'Ace':
                        aces += 1
                while self.score > 21 and aces > 0:
                    self.score -= 10
                    aces -= 1

            def hand_show(self):
                hand_string = ', '.join([f"{rank} of {suit}" for rank, suit in self.hand])
                print(f"{self.name}'s hand: {hand_string} | Score: {self.score}")


        # The actual game of Black Jack
        def blackJack():
            print("Welcome to Black Jack!")
            deck = Deck()

            # Get the name and number of players
            num_players = (input("Enter the number of players (1-4): "))
            while num_players not in ['1', '2', '3', '4']:
                if num_players == "exit":
                    game_loop()
                print("Please enter a valid number of players (1-4).")
                num_players = (input("Enter the number of players (1-4): "))
            num_players = int(num_players)
            players = []
            for i in range(num_players):
                player_name = input(f"What is the name of player #{i + 1}? ")
                if player_name == "exit":
                    game_loop()
                players.append(Player(player_name))
            dealer = Player("Dealer")

            # Initial deal
            for player in players + [dealer]:
                player.hand.append(deck.deal_card())
                player.hand.append(deck.deal_card())
                player.score_hand()

            # Player Turns
            for player in players:
                while True:
                    if player.score > 21:
                        break
                    player.hand_show()
                    action = input(f"{player.name}, do you want to hit or stand? (h/s): ").lower()
                    if action == "exit":
                        game_loop()
                    if action == 'h':
                        new_card = deck.deal_card()
                        player.hand.append(new_card)
                        player.score_hand()
                        print(f"{player.name} hits and receives {new_card[0]} of {new_card[1]}.")
                        if player.score > 21:
                            print(f"{player.name} busts with a score of {player.score}!")
                    elif action == 's':
                        print(f"{player.name} stands with a score of {player.score}.")
                        break
                    else:
                        print("Invalid input. Please enter 'h' to hit or 's' to stand.")

            # Dealer's Turn
            print("\nDealer's turn:")
            dealer.hand_show()
            while dealer.score < 17:
                print("Dealer hits.")
                dealer.hand.append(deck.deal_card())
                dealer.score_hand()
                dealer.hand_show()
            if dealer.score > 21:
                print("Dealer busts!")

            # Determine Winners
            print("\nFinal Results:")
            for player in players:
                if player.score > 21:
                    print(f"{player.name} busts and loses.")
                elif dealer.score > 21 or player.score > dealer.score:
                    print(f"{player.name} wins!")
                elif player.score < dealer.score:
                    print(f"{player.name} loses.")
                else:
                    print(f"{player.name} ties with the dealer.")


        # Runs the game
        blackJack()
    elif game_selection == "3":
        import time
        movies_easy = {
            "Who played Jack in Titanic?": ["1) Brad Pitt", "2) Leonardo DiCaprio", "3) Tom Cruise", "4) Matt Damon",
                                            "2) Leonardo DiCaprio"],
            "What is Dorothys dogs name in The Wizard of Oz?": ["1) Toto", "2) Tattoo", "3) Buddy", "4) Rex",
                                                                "1) Toto"],
            "Which animated film features a snowman named Olaf?": ["1) Moana", "2) Tangled", "3) Frozen", "4) Brave",
                                                                   "3) Frozen"],
            "What kind of fish is Nemo?": ["1) Goldfish", "2) Clownfish", "3) Angelfish", "4) Pufferfish",
                                           "2) Clownfish"],
            "Who is the cowboy toy in Toy Story?": ["1) Buzz", "2) Slinky", "3) Rex", "4) Woody", "4) Woody"],
            "What is the name of Harry Potters school?": ["1) Beauxbatons", "2) Hogwarts", "3) Texas A&M",
                                                          "4) Ilvermorny", "2) Hogwarts"],
            "Which superhero is known as the Dark Knight?": ["1) Superman", "2) Spider-Man", "3) Batman", "4) Iron Man",
                                                             "3) Batman"],
            "Who is Simbas father in The Lion King?": ["1) Scar", "2) Mufasa", "3) Zazu", "4) Rafiki", "2) Mufasa"],
            "What is the kingdom in Frozen called?": ["1) Arendelle", "2) Corona", "3) Genovia", "4) DunBroch",
                                                      "1) Arendelle"],
            "Which film features the line “Ill be back”?": ["1) Predator", "2) Rocky", "3) The Terminator",
                                                            "4) Die Hard", "3) The Terminator"],
            "Who directed Jaws?": ["1) George Lucas", "2) Steven Spielberg", "3) Martin Scorsese", "4) James Cameron",
                                   "2) Steven Spielberg"],
            "What color is Shrek?": ["1) Blue", "2) Purple", "3) Green", "4) Orange", "3) Green"],
            "Which actor plays Iron Man in the Marvel films?": ["1) Chris Evans", "2) Mark Ruffalo",
                                                                "3) Robert Downey Jr.", "4) Chris Hemsworth",
                                                                "3) Robert Downey Jr."],
            "What is Indiana Jones profession?": ["1) Archaeologist", "2) Pilot", "3) Journalist", "4) Detective",
                                                  "1) Archaeologist"],
            "What is Kevins surname in Home Alone?": ["1) McFly", "2) McCallister", "3) McAllister", "4) McKenzie",
                                                      "2) McCallister"],
            "Which 1997 film is set aboard the RMS Titanic?": ["1) Pearl Harbor", "2) Titanic", "3) The Perfect Storm",
                                                               "4) Cast Away", "2) Titanic"],
            "What is the clownfish fathers name in Finding Nemo?": ["1) Bruce", "2) Marlin", "3) Gill", "4) Bloat",
                                                                    "2) Marlin"],
            "Which Disney princess loses a glass slipper?": ["1) Aurora", "2) Belle", "3) Cinderella", "4) Ariel",
                                                             "3) Cinderella"],
            "Who is Luke Skywalkers father?": ["1) Obi-Wan Kenobi", "2) Han Solo", "3) Darth Vader",
                                               "4) Emperor Palpatine", "3) Darth Vader"],
            "Which pill does Neo take in The Matrix?": ["1) Blue", "2) Red", "3) Green", "4) White", "2) Red"],
        }
        movies_medium = {
            "What was Disneys first feature-length animated film?": ["1) Pinocchio", "2) Fantasia",
                                                                     "3) Snow White and the Seven Dwarfs", "4) Dumbo",
                                                                     "3) Snow White and the Seven Dwarfs"],
            "Who directed Pulp Fiction?": ["1) Quentin Tarantino", "2) Spike Lee", "3) Oliver Stone",
                                           "4) David Fincher", "1) Quentin Tarantino"],
            "What is the hotel in The Shining called?": ["1) The Bates Motel", "2) The Overlook Hotel",
                                                         "3) The Stanley Hotel", "4) The Grand Budapest",
                                                         "2) The Overlook Hotel"],
            "Who played Hannibal Lecter in The Silence of the Lambs?": ["1) Brian Cox", "2) Anthony Hopkins",
                                                                        "3) Ian McKellen", "4) Jeremy Irons",
                                                                        "2) Anthony Hopkins"],
            "What speed must the DeLorean reach to time travel in Back to the Future?": ["1) 77 mph", "2) 88 mph",
                                                                                         "3) 98 mph", "4) 108 mph",
                                                                                         "2) 88 mph"],
            "Which film won the first Academy Award for Best Picture?": ["1) Wings", "2) Metropolis", "3) Sunrise",
                                                                         "4) The Jazz Singer", "1) Wings"],
            "Who composed the score for The Good, the Bad and the Ugly?": ["1) Nino Rota", "2) Ennio Morricone",
                                                                           "3) John Williams", "4) Bernard Herrmann",
                                                                           "2) Ennio Morricone"],
            "What is the fictional African nation in Black Panther called?": ["1) Zamunda", "2) Genovia", "3) Wakanda",
                                                                              "4) Sokovia", "3) Wakanda"],
            "What is the name of Ricks café in Casablanca?": ["1) Café de Paris", "2) Ricks Café Américain",
                                                              "3) Blue Parrot", "4) Café Casablanca",
                                                              "2) Ricks Café Américain"],
            "Who played Clarice Starling in The Silence of the Lambs?": ["1) Sigourney Weaver", "2) Jodie Foster",
                                                                         "3) Glenn Close", "4) Meryl Streep",
                                                                         "2) Jodie Foster"],
            "What is the subtitle of the second Star Wars film released?": ["1) Return of the Jedi",
                                                                            "2) The Phantom Menace",
                                                                            "3) The Empire Strikes Back",
                                                                            "4) Attack of the Clones",
                                                                            "3) The Empire Strikes Back"],
            "Who directed Spirited Away?": ["1) Satoshi Kon", "2) Isao Takahata", "3) Hayao Miyazaki",
                                            "4) Makoto Shinkai", "3) Hayao Miyazaki"],
            "Who played the Joker in The Dark Knight?": ["1) Joaquin Phoenix", "2) Jack Nicholson", "3) Heath Ledger",
                                                         "4) Jared Leto", "3) Heath Ledger"],
            "What is the name of the ship in Alien?": ["1) Sulaco", "2) Nostromo", "3) Prometheus", "4) Discovery One",
                                                       "2) Nostromo"],
            "Which 1994 film features Andy Dufresne?": ["1) Forrest Gump", "2) The Shawshank Redemption",
                                                        "3) Pulp Fiction", "4) The Green Mile",
                                                        "2) The Shawshank Redemption"],
            "Which dinosaur do visitors first see in Jurassic Park?": ["1) Velociraptor", "2) Brachiosaurus",
                                                                       "3) Tyrannosaurus rex", "4) Triceratops",
                                                                       "2) Brachiosaurus"],
            "Who played the title character in Edward Scissorhands?": ["1) Johnny Depp", "2) Tom Cruise",
                                                                       "3) Christian Slater", "4) Leonardo DiCaprio",
                                                                       "1) Johnny Depp"],
            "Which film features the Navi language?": ["1) Dune", "2) Avatar", "3) The Fifth Element", "4) Stargate",
                                                       "2) Avatar"],
            "What is the newspaper in Citizen Kane called?": ["1) The Chronicle", "2) The Inquirer", "3) The Gazette",
                                                              "4) The Examiner", "2) The Inquirer"],
            "Who directed Seven Samurai?": ["1) Yasujirō Ozu", "2) Akira Kurosawa", "3) Kenji Mizoguchi",
                                            "4) Masaki Kobayashi", "2) Akira Kurosawa"],
        }
        movies_hard = {
            "Who was the cinematographer for Citizen Kane?": ["1) Gregg Toland", "2) James Wong Howe",
                                                              "3) Robert Krasker", "4) Freddie Young",
                                                              "1) Gregg Toland"],
            "Which film was the first non-English-language winner of the Academy Award for Best Picture?": ["1) Roma",
                                                                                                            "2) Crouching Tiger, Hidden Dragon",
                                                                                                            "3) Parasite",
                                                                                                            "4) Life Is Beautiful",
                                                                                                            "3) Parasite"],
            "What is the prison planet in The Chronicles of Riddick called?": ["1) Crematoria", "2) Furya", "3) Helion",
                                                                               "4) M6-117", "1) Crematoria"],
            "Who directed the 1927 science-fiction film Metropolis?": ["1) F. W. Murnau", "2) Fritz Lang",
                                                                       "3) Sergei Eisenstein", "4) G. W. Pabst",
                                                                       "2) Fritz Lang"],
            "Which city is the setting of The Third Man?": ["1) Prague", "2) Vienna", "3) Berlin", "4) Budapest",
                                                            "2) Vienna"],
            "Who voiced HAL 9000 in 2001: A Space Odyssey?": ["1) Keir Dullea", "2) Douglas Rain",
                                                              "3) William Sylvester", "4) Arthur C. Clarke",
                                                              "2) Douglas Rain"],
            "What was the first film to win the Academy Award for Best Animated Feature?": ["1) Monsters, Inc.",
                                                                                            "2) Shrek",
                                                                                            "3) Spirited Away",
                                                                                            "4) Jimmy Neutron: Boy Genius",
                                                                                            "2) Shrek"],
            "Who composed the score for Vertigo?": ["1) Max Steiner", "2) Bernard Herrmann", "3) Miklós Rózsa",
                                                    "4) Franz Waxman", "2) Bernard Herrmann"],
            "What is Popeye Doyles first name in The French Connection?": ["1) Eddie", "2) Jimmy", "3) Frank",
                                                                           "4) Buddy", "2) Jimmy"],
            "Which film marked Orson Welles directorial debut?": ["1) The Magnificent Ambersons", "2) Touch of Evil",
                                                                  "3) Citizen Kane", "4) The Stranger",
                                                                  "3) Citizen Kane"],
            "Who played Antonio Salieri in Amadeus?": ["1) Tom Hulce", "2) F. Murray Abraham", "3) Roy Dotrice",
                                                       "4) Ian Holm", "2) F. Murray Abraham"],
            "Who directed The Passion of Joan of Arc?": ["1) Carl Theodor Dreyer", "2) Abel Gance", "3) Jean Renoir",
                                                         "4) Robert Bresson", "1) Carl Theodor Dreyer"],
            "Who played T. E. Lawrence in Lawrence of Arabia?": ["1) Alec Guinness", "2) Peter OToole",
                                                                 "3) Omar Sharif", "4) Richard Harris",
                                                                 "2) Peter OToole"],
            "What is the protagonists name in Bicycle Thieves?": ["1) Bruno Ricci", "2) Antonio Ricci",
                                                                  "3) Enzo Staiola", "4) Umberto D.",
                                                                  "2) Antonio Ricci"],
            "Which 1947 film noir features the character Jeff Bailey?": ["1) Out of the Past", "2) The Big Sleep",
                                                                         "3) The Killers", "4) Dark Passage",
                                                                         "1) Out of the Past"],
            "Who edited Raging Bull?": ["1) Dede Allen", "2) Thelma Schoonmaker", "3) Verna Fields",
                                        "4) Anne V. Coates", "2) Thelma Schoonmaker"],
            "Which film won the Palme dOr at the 1994 Cannes Film Festival?": ["1) Three Colors: Red",
                                                                               "2) Pulp Fiction", "3) The Piano",
                                                                               "4) Farewell My Concubine",
                                                                               "2) Pulp Fiction"],
            "What instrument features prominently in Harry Limes theme in The Third Man?": ["1) Mandolin", "2) Zither",
                                                                                            "3) Balalaika",
                                                                                            "4) Accordion",
                                                                                            "2) Zither"],
            "Which director made The 400 Blows?": ["1) Jean-Luc Godard", "2) François Truffaut", "3) Claude Chabrol",
                                                   "4) Éric Rohmer", "2) François Truffaut"],
            "Who directed The Rules of the Game?": ["1) Marcel Carné", "2) Jean Renoir", "3) René Clair",
                                                    "4) Julien Duvivier", "2) Jean Renoir"],
        }

        music_easy = {
            "Which singer is known as the King of Pop?": ["1) Prince", "2) Michael Jackson", "3) Elvis Presley",
                                                          "4) Bruno Mars", "2) Michael Jackson"],
            "Which band recorded “Hey Jude”?": ["1) The Rolling Stones", "2) The Beatles", "3) The Who", "4) The Kinks",
                                                "2) The Beatles"],
            "How many keys does a standard piano have?": ["1) 76", "2) 82", "3) 88", "4) 96", "3) 88"],
            "Who sang “Like a Virgin”?": ["1) Cyndi Lauper", "2) Madonna", "3) Cher", "4) Tina Turner", "2) Madonna"],
            "Which singer released the album 1989?": ["1) Katy Perry", "2) Taylor Swift", "3) Miley Cyrus",
                                                      "4) Ariana Grande", "2) Taylor Swift"],
            "What band featured Freddie Mercury as its lead singer?": ["1) Queen", "2) Kiss", "3) The Police",
                                                                       "4) Genesis", "1) Queen"],
            "Which Jamaican musician is closely associated with reggae and “One Love”?": ["1) Peter Tosh",
                                                                                          "2) Bob Marley",
                                                                                          "3) Jimmy Cliff", "4) Shaggy",
                                                                                          "2) Bob Marley"],
            "Who sang “Rolling in the Deep”?": ["1) Adele", "2) Amy Winehouse", "3) Duffy", "4) Leona Lewis",
                                                "1) Adele"],
            "Which band released “Bohemian Rhapsody”?": ["1) Queen", "2) Led Zeppelin", "3) Pink Floyd", "4) The Doors",
                                                         "1) Queen"],
            "What instrument is central to a drum kit?": ["1) Drums", "2) Harp", "3) Oboe", "4) Banjo", "1) Drums"],
            "What is U2s lead singers stage name?": ["1) Bono", "2) Sting", "3) Edge", "4) Seal", "1) Bono"],
            "Who recorded the song and album “Purple Rain”?": ["1) David Bowie", "2) Prince", "3) Lionel Richie",
                                                               "4) George Michael", "2) Prince"],
            "What is the highest standard female singing voice?": ["1) Alto", "2) Tenor", "3) Soprano", "4) Baritone",
                                                                   "3) Soprano"],
            "Which band recorded “Smells Like Teen Spirit”?": ["1) Pearl Jam", "2) Nirvana", "3) Soundgarden",
                                                               "4) Green Day", "2) Nirvana"],
            "Who sang “Jolene”?": ["1) Tammy Wynette", "2) Dolly Parton", "3) Loretta Lynn", "4) Reba McEntire",
                                   "2) Dolly Parton"],
            "Who composed The Four Seasons?": ["1) Antonio Vivaldi", "2) Johann Sebastian Bach",
                                               "3) George Frideric Handel", "4) Joseph Haydn", "1) Antonio Vivaldi"],
            "What instrument does Yo-Yo Ma play?": ["1) Violin", "2) Cello", "3) Viola", "4) Double bass", "2) Cello"],
            "Who released “Single Ladies (Put a Ring on It)”?": ["1) Rihanna", "2) Beyoncé", "3) Alicia Keys",
                                                                 "4) Shakira", "2) Beyoncé"],
            "What is the name of the Beatles drummer?": ["1) Charlie Watts", "2) Ringo Starr", "3) Keith Moon",
                                                         "4) Phil Collins", "2) Ringo Starr"],
            "Which genre is Louis Armstrong most associated with?": ["1) Jazz", "2) Punk", "3) Disco", "4) Reggae",
                                                                     "1) Jazz"],
        }
        music_medium = {
            "What was David Bowies birth name?": ["1) David Jones", "2) Robert Jones", "3) David Robert Smith",
                                                  "4) David Bowie Jones", "1) David Jones"],
            "Which band released The Dark Side of the Moon?": ["1) The Beatles", "2) Pink Floyd", "3) The Who",
                                                               "4) Yes", "2) Pink Floyd"],
            "Who composed the opera The Magic Flute?": ["1) Mozart", "2) Verdi", "3) Puccini", "4) Wagner",
                                                        "1) Mozart"],
            "Which bands debut album was Please Please Me?": ["1) The Rolling Stones", "2) The Beatles", "3) The Kinks",
                                                              "4) The Hollies", "2) The Beatles"],
            "What was the first music video shown on MTV?": ["1) “Billie Jean”", "2) “Video Killed the Radio Star”",
                                                             "3) “Take on Me”", "4) “You Better Run”",
                                                             "2) “Video Killed the Radio Star”"],
            "Who composed the music for West Side Story?": ["1) Stephen Sondheim", "2) Leonard Bernstein",
                                                            "3) Richard Rodgers", "4) Andrew Lloyd Webber",
                                                            "2) Leonard Bernstein"],
            "Which pair were Fleetwood Mac lead vocalists on Rumours?": ["1) Stevie Nicks and Christine McVie",
                                                                         "2) Debbie Harry and Patti Smith",
                                                                         "3) Ann Wilson and Nancy Wilson",
                                                                         "4) Karen Carpenter and Olivia Newton-John",
                                                                         "1) Stevie Nicks and Christine McVie"],
            "What is the relative minor of C major?": ["1) D minor", "2) A minor", "3) E minor", "4) G minor",
                                                       "2) A minor"],
            "Who released the album Blue in 1971?": ["1) Carole King", "2) Joni Mitchell", "3) Joan Baez",
                                                     "4) Carly Simon", "2) Joni Mitchell"],
            "Which Beatle played bass?": ["1) George Harrison", "2) John Lennon", "3) Paul McCartney", "4) Ringo Starr",
                                          "3) Paul McCartney"],
            "Who composed The Rite of Spring?": ["1) Claude Debussy", "2) Igor Stravinsky", "3) Maurice Ravel",
                                                 "4) Sergei Rachmaninoff", "2) Igor Stravinsky"],
            "What is Gordon Sumners stage name?": ["1) Sting", "2) Seal", "3) Bono", "4) Moby", "1) Sting"],
            "Which band recorded London Calling?": ["1) The Clash", "2) The Jam", "3) The Specials", "4) Sex Pistols",
                                                    "1) The Clash"],
            "Who was Genesis original lead singer?": ["1) Phil Collins", "2) Peter Gabriel", "3) Tony Banks",
                                                      "4) Steve Hackett", "2) Peter Gabriel"],
            "Which saxophonist recorded A Love Supreme?": ["1) Charlie Parker", "2) John Coltrane", "3) Sonny Rollins",
                                                           "4) Stan Getz", "2) John Coltrane"],
            "What was the 1969 music festival held at Bethel, New York, called?": ["1) Monterey Pop", "2) Woodstock",
                                                                                   "3) Isle of Wight Festival",
                                                                                   "4) Altamont", "2) Woodstock"],
            "Who composed the score for Psycho?": ["1) Bernard Herrmann", "2) Elmer Bernstein", "3) Henry Mancini",
                                                   "4) Miklós Rózsa", "1) Bernard Herrmann"],
            "Who released the album Jagged Little Pill?": ["1) Sheryl Crow", "2) Alanis Morissette",
                                                           "3) Sarah McLachlan", "4) Tori Amos",
                                                           "2) Alanis Morissette"],
            "What vocal effect is prominent in Chers “Believe”?": ["1) Vocoder", "2) Auto-Tune", "3) Talk box",
                                                                   "4) Looping", "2) Auto-Tune"],
            "Who composed the Goldberg Variations?": ["1) Ludwig van Beethoven", "2) Johann Sebastian Bach",
                                                      "3) Franz Schubert", "4) Frédéric Chopin",
                                                      "2) Johann Sebastian Bach"],
        }
        music_hard = {
            "Which Beatles album was recorded entirely on four-track equipment?": ["1) Please Please Me",
                                                                                   "2) Rubber Soul", "3) Abbey Road",
                                                                                   "4) Let It Be", "2) Rubber Soul"],
            "Who was the first woman inducted into the Rock and Roll Hall of Fame?": ["1) Janis Joplin",
                                                                                      "2) Aretha Franklin",
                                                                                      "3) Tina Turner", "4) Etta James",
                                                                                      "2) Aretha Franklin"],
            "Who composed the opera Wozzeck?": ["1) Alban Berg", "2) Anton Webern", "3) Arnold Schoenberg",
                                                "4) Kurt Weill", "1) Alban Berg"],
            "What is the standard tuning of a four-string bass, lowest to highest?": ["1) A-D-G-C", "2) E-A-D-G",
                                                                                      "3) D-G-B-E", "4) C-G-D-A",
                                                                                      "2) E-A-D-G"],
            "Which Miles Davis album was released in 1959 and became a landmark jazz recording?": ["1) Bitches Brew",
                                                                                                   "2) Kind of Blue",
                                                                                                   "3) Sketches of Spain",
                                                                                                   "4) Birth of the Cool",
                                                                                                   "2) Kind of Blue"],
            "Who was the principal producer of Marvin Gayes Whats Going On?": ["1) Norman Whitfield", "2) Marvin Gaye",
                                                                               "3) Smokey Robinson", "4) Berry Gordy",
                                                                               "2) Marvin Gaye"],
            "Which composer developed the twelve-tone method?": ["1) Arnold Schoenberg", "2) Pierre Boulez",
                                                                 "3) Philip Glass", "4) John Cage",
                                                                 "1) Arnold Schoenberg"],
            "What was the first rap song to reach number one on the Billboard Hot 100?": ["1) “Rappers Delight”",
                                                                                          "2) “Ice Ice Baby”",
                                                                                          "3) “U Cant Touch This”",
                                                                                          "4) “Baby Got Back”",
                                                                                          "2) “Ice Ice Baby”"],
            "Who wrote the lyrics for most of the musical Company?": ["1) Ira Gershwin", "2) Stephen Sondheim",
                                                                      "3) Oscar Hammerstein II", "4) Tim Rice",
                                                                      "2) Stephen Sondheim"],
            "Which instrument did Charlie Parker play?": ["1) Tenor saxophone", "2) Alto saxophone", "3) Trumpet",
                                                          "4) Clarinet", "2) Alto saxophone"],
            "Who was The Whos original drummer?": ["1) Keith Moon", "2) Ginger Baker", "3) John Bonham",
                                                   "4) Mitch Mitchell", "1) Keith Moon"],
            "Which record label did Berry Gordy found in Detroit?": ["1) Stax", "2) Motown", "3) Atlantic", "4) Chess",
                                                                     "2) Motown"],
            "How is the first movement of Beethovens Moonlight Sonata marked?": ["1) Allegro con brio",
                                                                                 "2) Adagio sostenuto",
                                                                                 "3) Presto agitato",
                                                                                 "4) Largo e mesto",
                                                                                 "2) Adagio sostenuto"],
            "Who composed the opera The Nose?": ["1) Sergei Prokofiev", "2) Dmitri Shostakovich",
                                                 "3) Modest Mussorgsky", "4) Pyotr Ilyich Tchaikovsky",
                                                 "2) Dmitri Shostakovich"],
            "Who produced The Beatles Abbey Road?": ["1) George Martin", "2) Phil Spector", "3) Brian Epstein",
                                                     "4) Geoff Emerick", "1) George Martin"],
            "What is the scale made up of six whole tones per octave called?": ["1) Chromatic scale",
                                                                                "2) Whole-tone scale",
                                                                                "3) Pentatonic scale",
                                                                                "4) Diminished scale",
                                                                                "2) Whole-tone scale"],
            "Who released the 1968 album Astral Weeks?": ["1) Van Morrison", "2) Tim Buckley", "3) Donovan",
                                                          "4) Nick Drake", "1) Van Morrison"],
            "Who wrote the jazz standard “Take the A Train”?": ["1) Duke Ellington", "2) Billy Strayhorn",
                                                                "3) Count Basie", "4) Thelonious Monk",
                                                                "2) Billy Strayhorn"],
            "Which electronic instrument was invented by Leon Theremin?": ["1) Ondes Martenot", "2) Theremin",
                                                                           "3) Moog synthesizer", "4) Telharmonium",
                                                                           "2) Theremin"],
            "Who composed the opera Einstein on the Beach?": ["1) Steve Reich", "2) Philip Glass", "3) Terry Riley",
                                                              "4) John Adams", "2) Philip Glass"],
        }

        tamu_easy = {
            "What do the letters A&M stand for in Texas A&M?": ["1) Arts and Music", "2) Agriculture and Manufacturing",
                                                                "3) Agricultural and Mechanical",
                                                                "4) Academy and Military",
                                                                "3) Agricultural and Mechanical"],
            "What is Texas A&Ms mascot called?": ["1) Reville", "2) Reveille", "3) Revelle", "4) Revolution",
                                                  "2) Reveille"],
            "What is the nickname of Texas A&Ms athletic teams?": ["1) Longhorns", "2) Aggies", "3) Red Raiders",
                                                                   "4) Bears", "2) Aggies"],
            "What city is Texas A&Ms main campus in?": ["1) Austin", "2) College Station", "3) Waco", "4) Houston",
                                                        "2) College Station"],
            "What are Texas A&M students and former students traditionally called?": ["1) Aggies", "2) Cadets",
                                                                                      "3) Mustangs", "4) Farmers",
                                                                                      "1) Aggies"],
            "What does Texas A&M call its student supporters at football games?": ["1) The 10th Man", "2) The 12th Man",
                                                                                   "3) The Corps", "4) The Yell Squad",
                                                                                   "2) The 12th Man"],
            "What is Texas A&Ms primary school color?": ["1) Burnt orange", "2) Maroon", "3) Navy blue", "4) Crimson",
                                                         "2) Maroon"],
            "What is Texas A&Ms marching band called?": ["1) The Longhorn Band", "2) The Fightin Texas Aggie Band",
                                                         "3) The 12th Man Band", "4) The Aggie Orchestra",
                                                         "2) The Fightin Texas Aggie Band"],
            "In which athletic conference does Texas A&M compete?": ["1) Big Ten", "2) Big 12", "3) SEC", "4) ACC",
                                                                     "3) SEC"],
            "What is Texas A&Ms football stadium called?": ["1) Darrell K Royal Stadium", "2) Kyle Field",
                                                            "3) Jones AT&T Stadium", "4) Rice Stadium",
                                                            "2) Kyle Field"],
            "What is the name of Texas A&Ms football yell practice?": ["1) Yell Night", "2) Midnight Yell",
                                                                       "3) Aggie Rally", "4) Maroon Midnight",
                                                                       "2) Midnight Yell"],
            "What is the name of Texas A&Ms yearbook?": ["1) The Battalion", "2) The Aggieland", "3) The Maroon",
                                                         "4) The Reveille", "2) The Aggieland"],
            "What is the name of Texas A&Ms student newspaper?": ["1) The Aggieland", "2) The Battalion",
                                                                  "3) The Eagle", "4) The Collegian",
                                                                  "2) The Battalion"],
            "Which animal is Reveille?": ["1) Horse", "2) Dog", "3) Eagle", "4) Cat", "2) Dog"],
            "What traditional greeting is often heard at Texas A&M?": ["1) Hook em", "2) Howdy", "3) Gig em",
                                                                       "4) Roll Tide", "2) Howdy"],
            "Which phrase is paired with a thumb-and-finger hand sign at Texas A&M?": ["1) Gig em", "2) Whoop em",
                                                                                       "3) Go Maroon", "4) Saw em off",
                                                                                       "1) Gig em"],
            "What is the name of Texas A&Ms live mascot?": ["1) Reveille", "2) Bevo", "3) Smokey", "4) Uga",
                                                            "1) Reveille"],
            "What is the name of Texas A&Ms student section tradition known for standing during football games?": [
                "1) The 12th Man", "2) The Corps Block", "3) The Maroon Wall", "4) The Yell Section",
                "1) The 12th Man"],
            "What is the name of Texas A&Ms annual student-built bonfire tradition?": ["1) Aggie Bonfire",
                                                                                       "2) Maroon Flame",
                                                                                       "3) Midnight Fire",
                                                                                       "4) Century Bonfire",
                                                                                       "1) Aggie Bonfire"],
            "What is the nickname of Texas A&Ms womens basketball team?": ["1) Lady Longhorns", "2) Aggies",
                                                                           "3) Cowgirls", "4) Maroon Stars",
                                                                           "2) Aggies"],
        }
        tamu_medium = {
            "In what year was Texas A&M founded?": ["1) 1865", '2) 1876', '3) 1889', '4) 1901', '2) 1876'],
            "What was Texas A&M originally called?": ['1) Texas Agricultural College',
                                                      '2) Agricultural and Mechanical College of Texas',
                                                      '3) Texas State University', '4) Texas Military Institute',
                                                      '2) Agricultural and Mechanical College of Texas'],
            "What was the Texas A&Ms football team originally nicknamed?": ['1) The Farmers', '2) The Rangers',
                                                                            '3) The Maroons', '4) The Cadets',
                                                                            '1) The Farmers'],
            "What is the abbreviation for Texas A&Ms Memorial Student Center?": ['1) TAMC', '2) MSC', '3) MSA',
                                                                                 '4) AMSC', '2) MSC'],
            "What does the Aggie Ring represent to graduates?": ['1) Being in a frat', '2) Having tons of money',
                                                                 '3) Connection to the Aggie community',
                                                                 '4) Academic success',
                                                                 '3) Connection to the Aggie community'],
            "In what year did Texas A&M join the Southeastern Conference?": ["1) 2008", "2) 2010", "3) 2012", "4) 2014",
                                                                             "3) 2012"],
            "Which former Texas A&M president is the namesake of Rudder Tower?": ["1) Robert Gates",
                                                                                  "2) James Earl Rudder",
                                                                                  "3) Lawrence Sullivan Ross",
                                                                                  "4) William Bizzell",
                                                                                  "2) James Earl Rudder"],
            "What is the name of the universitys main library?": ["1) Evans Library", "2) Rudder Library",
                                                                  "3) Bonfire Library", "4) Aggie Library",
                                                                  "1) Evans Library"],
            "What is the title of Texas A&Ms alma mater?": ["1) The Aggie Song", "2) The Spirit of Aggieland",
                                                            "3) Maroon Forever", "4) The Farmers Hymn",
                                                            "2) The Spirit of Aggieland"],
            "During Aggie roll call, what do “Here” and “There” help remember?": ["1) Former coaches",
                                                                                  "2) Absent Aggies", "3) Past mascots",
                                                                                  "4) Military battles",
                                                                                  "2) Absent Aggies"],
            "What is Texas A&Ms engineering school called?": ["1) College of Engineering",
                                                              "2) School of Applied Science", "3) School of Technology",
                                                              "4) Institute of Engineering Studies",
                                                              "1) College of Engineering"],
            "What is the name of Texas A&Ms campus in Galveston?": ["1) Texas A&M Coastal Campus",
                                                                    "2) Texas A&M University at Galveston",
                                                                    "3) Galveston Maritime College",
                                                                    "4) Texas Maritime University",
                                                                    "2) Texas A&M University at Galveston"],
            "What are the student leaders who lead Texas A&M yells called?": ["1) Yell Leaders", "2) Aggie Captains",
                                                                              "3) Spirit Guides", "4) Corps Sergeants",
                                                                              "1) Yell Leaders"],
            "What is Texas A&Ms student recreation facility commonly called?": ["1) Student Recreation Center",
                                                                                "2) Aggie Athletic Hall",
                                                                                "3) Rudder Gymnasium",
                                                                                "4) Maroon Fieldhouse",
                                                                                "1) Student Recreation Center"],
            "What does an Aggie “Whoop!” commonly express?": ["1) Disapproval", "2) Enthusiasm or approval",
                                                              "3) A request to sit down", "4) The end of a game",
                                                              "2) Enthusiasm or approval"],
            "What was the original purpose of Texas A&M as a land grant institution?": [
                "1) Agricultural and mechanical education", "2) Teacher training only", "3) Law and government studies",
                "4) Fine arts education", "1) Agricultural and mechanical education"],
            "How many stripes are on the boots of a Texas A&M senior cadet?": ["1) One", "2) Two", "3) Three",
                                                                               "4) Four", "3) Three"],
            "What is a central purpose of Texas A&Ms Corps of Cadets?": ["1) Leadership development",
                                                                         "2) Agricultural research only",
                                                                         "3) Athletic recruitment", "4) Campus tours",
                                                                         "1) Leadership development"],
            "What is the name of Texas A&Ms College Station newspaper?": ["1) The Battalion", "2) The Eagle",
                                                                          "3) The Daily Aggie",
                                                                          "4) The College Station Times",
                                                                          "1) The Battalion"],
            "What does the “M” in Texas A&M stand for?": ["1) Military", "2) Manufacturing", "3) Mechanical",
                                                          "4) Medicine", "3) Mechanical"],
        }
        tamu_hard = {
            "In what year did women first enroll as full-time students at Texas A&M?": ["1) 1956", "2) 1963", "3) 1967",
                                                                                        "4) 1972", "2) 1963"],
            "In what year did Texas A&M officially become a university?": ["1) 1948", "2) 1959", "3) 1963", "4) 1971",
                                                                           "3) 1963"],
            "In what year was the first Aggie Ring designed?": ["1) 1876", "2) 1889", "3) 1909", "4) 1921", "2) 1889"],
            "In what year did the first Aggie Bonfire burn?": ["1) 1896", "2) 1909", "3) 1917", "4) 1923", "2) 1909"],
            "In what year did the Aggie Bonfire collapse occur?": ["1) 1989", "2) 1995", "3) 1999", "4) 2001",
                                                                   "3) 1999"],
            "How many people died in the 1999 Bonfire collapse?": ["1) 8", "2) 10", "3) 12", "4) 14", "3) 12"],
            "What is the name of the campus memorial dedicated to those who died in the Bonfire collapse?": [
                "1) Aggie Memorial", "2) Bonfire Memorial", "3) Spirit Plaza", "4) Rudder Memorial",
                "2) Bonfire Memorial"],
            "In what year was the Bonfire Memorial dedicated?": ["1) 2001", "2) 2004", "3) 2006", "4) 2009", "2) 2004"],
            "What are the three pillars of the Bonfire Memorial called?": ["1) Honor, Courage, Commitment",
                                                                           "2) Tradition, Spirit, Unity",
                                                                           "3) Past, Present, Future",
                                                                           "4) Service, Sacrifice, Strength",
                                                                           "2) Tradition, Spirit, Unity"],
            "What is the Latin motto on Texas A&Ms seal?": ["1) E pluribus unum", "2) Disciplina Praesidium Civitatis",
                                                            "3) Veritas et Lux", "4) Ad astra per aspera",
                                                            "2) Disciplina Praesidium Civitatis"],
            "What does Disciplina Praesidium Civitatis mean?": ["1) Knowledge is power",
                                                                "2) Education is the safeguard of the state",
                                                                "3) Service above self",
                                                                "4) Through hardship to the stars",
                                                                "2) Education is the safeguard of the state"],
            "Who was the first Black student admitted to Texas A&M?": ["1) John Warren", "2) George Washington Carver",
                                                                       "3) Charles Whitman", "4) James Byrd",
                                                                       "1) John Warren"],
            "In what year did John Warren enroll at Texas A&M?": ["1) 1959", "2) 1961", "3) 1964", "4) 1967",
                                                                  "3) 1964"],
            "In what year did Texas A&M win its first football national championship?": ["1) 1919", "2) 1927",
                                                                                         "3) 1939", "4) 1947",
                                                                                         "3) 1939"],
            "Which Texas A&M alumnus became a NASA flight director during the Apollo era?": ["1) Gene Kranz",
                                                                                             "2) Chris Kraft",
                                                                                             "3) Gene Cernan",
                                                                                             "4) John Young",
                                                                                             "1) Gene Kranz"],
            "Who was president of Texas A&M during the 1999 Bonfire collapse?": ["1) Robert Gates", "2) Ray Bowen",
                                                                                 "3) James Earl Rudder",
                                                                                 "4) Elsa Murano", "2) Ray Bowen"],
            "Which former Texas A&M president led the U.S. Army Rangers during the D-Day invasion?": [
                "1) Lawrence Sullivan Ross", "2) James Earl Rudder", "3) William Bizzell", "4) Robert Gates",
                "2) James Earl Rudder"],
            "What is the name of Texas A&Ms academic and research campus in Qatar?": [
                "1) Texas A&M University at Qatar", "2) Aggie Gulf Institute", "3) Qatar Agricultural College",
                "4) Doha Engineering University", "1) Texas A&M University at Qatar"],
            "What was Texas A&Ms original name when it opened in 1876?": ["1) Texas A&M University",
                                                                          "2) Agricultural and Mechanical College of Texas",
                                                                          "3) Texas State Agricultural School",
                                                                          "4) College of Texas",
                                                                          "2) Agricultural and Mechanical College of Texas"],
            "In what year did Texas A&M join the Southwest Conference?": ["1) 1896", "2) 1915", "3) 1917", "4) 1925",
                                                                          "3) 1917"],
        }

        categories = {
            '1': movies_easy,
            '2': movies_medium,
            '3': movies_hard,
            '4': music_easy,
            '5': music_medium,
            '6': music_hard,
            '7': tamu_easy,
            '8': tamu_medium,
            '9': tamu_hard
        }

        print('Trivia selected! Choose from the following catagories: ')
        catagory = input(
            '1) Movies: Easy \n2) Movies: Medium \n3) Movies: Hard \n4) Music: Easy \n5) Music: Medium \n6) Music: Hard \n7) TAMU: Easy \n8) TAMU: Medium \n9) TAMU: Hard \n10) Random \nEnter the number associated with the catagory: ').strip()
        while catagory not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            if catagory == "exit":
                game_loop()
            catagory = input('Invalid input. Please enter a number between 1 and 10: ').strip()
        if catagory == '10':
            catagory = random.choice(list(categories.keys()))
        qset = categories.get(catagory)
        time.sleep(1)
        qnum = input('How many questions would you like to answer? (1-10): ')
        while qnum not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            if qnum == "exit":
                game_loop()
            qnum = input('Invalid input. Please enter a number between 1 and 10: ').strip()
        time.sleep(1)
        num_correct = 0
        num_wrong = 0
        for i in range(int(qnum)):
            q = random.choice(list(qset))
            print(f'Question {i + 1}:')
            time.sleep(1)
            print(q)
            time.sleep(1)
            print(*qset[q][0:4], sep='\n')
            answer = input('Enter answer as a number (1-4): ')
            while answer not in ['1', '2', '3', '4']:
                if answer == "exit":
                    game_loop()
                answer = input('Invalid input. Please enter a number between 1 and 4: ').strip()
            if (qset[q][int(answer) - 1]) == (qset[q][4]):
                print('CORRECT!')
                num_correct += 1
            else:
                print(f"WRONG! The correct answer is: {(qset[q][4])}")
                num_wrong += 1
            qset.pop(q)
            if i < int(qnum) - 1:
                print('Finding another question...')
                time.sleep(1)

        print(f"You got {num_correct} correct and {num_wrong} wrong!")
    elif game_selection == "exit":
        game_loop()
    else:
        print("Invalid game selection. Please try again")
        game_loop()
    while True:
        play_again = input("Do you want to play another game? (y/n): ").lower()
        if play_again == "y" or play_again == "n":
            break
        elif play_again == "exit":
            game_loop()
        else:
            print("Invalid input. Please try again.")
    if play_again == "y":
        print("Let's play again!")
        game_loop()

game_loop()
