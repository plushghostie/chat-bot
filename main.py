import random
welcome = input("Say hello!: ")
greeting = random.choice(["Hello!", "Hi there!", "Hey!", "wassup!", "Hi!", "Hiya!", "Pleased to meet you!", "It's nice to meet you!", "It's a pleasure to meet you."])
print(greeting)
color = input("Whats your favorite color!: ")
colorselect = random.choice(["oh I love that color!!", "I hate that color, ew..", "wow thats a lovely color, big fan!", "woah thats my favorite too!", "oh ig thats cool color..", "thats actually one my most top favorite colors ever!"])
print(colorselect)
sport = input("Enter your favorite sport: ")
sport = random.choice(["Thats great sport! I play it too!", "That sport is kinda boring..", "Maybe we should play some time?", "Maybe you should teach me some time!", "That sport is so fun, bit hard at times though!", "ehh I dont really like that sport but you do you!!"])
print(sport)
book = input("Please enter your favorite book: ")
book = random.choice(["That's a classic!", "I've read mixed reviews about it, but good read!", "Oh, that's one of my favorites too!", "That's a bold choice! Yet great one!", "I haven't heard of it, I should check out some time!", "Ah, a fellow fan! Nice meet someone with good taste", "That's a book that's been on my shelf for ages. Maybe I should take a read!", "That book isnt something I personally like, but Im happy you found intrest in it!"])
print(book)
movie = input("Please enter your favorite movie: ")
movie = random.choice(["You have impeccable taste in movies! Your selections are always so captivating.", "I admire how diverse and interesting your movie choices are. It shows a real appreciation for cinema!", "You always seem to pick the most thought-provoking films. It's inspiring to see your passion for storytelling", "Your taste in movies is truly unique and refreshing. You have a knack for finding hidden gems.", "I love discussing movies with you because you always introduce me to new favorites. Your taste is top-notch.", "Your movie recommendations never disappoint. It's clear you have a keen eye for quality cinema!!", "Your taste in movies is about as exciting as watching paint dry. Do you ever choose anything with substance?", "You seriously think that's a classic? Please, spare me your pedestrian taste in cinema.", "Your movie choices are so predictable. It's like you only watch whatever's trending on Netflix. Can't you appreciate something with a bit more depth?"])
print(movie)
game = input("Please enter your favorite game: ")
game = random.choice(["You have excellent taste in games! Your selections always showcase a perfect blend of innovation and entertainment!", "I really admire your gaming choices. It's clear you have a deep appreciation for immersive storytelling!!", "Your gaming library is so diverse and intriguing. You have a knack for finding hidden gems that offer unique experiences.", "I always enjoy hearing your recommendations because your taste in games is top-notch. You know how to pick titles that leave a lasting impression!", "You have such a refined palate when it comes to games. It's obvious you value quality and craftsmanship in your gaming experiences", "I've seen better narratives in mobile games. How can you waste your time on such shallow experiences?", "Your gaming choices are so basic. It's like you only play whatever's popular, without any regard for quality."])
print(game)
print("· · ────── ·❀· ────── · ·")
print("Im feeling bit bored, lets play minigame! guess the number!")
print("I am thinking of a number between 1 and 10... Can you guess what is?")
secret_number = random.randint(1, 10)
num_guesses = 0
while True:
    guess = int(input("Enter your guess: "))  
    num_guesses += 1
    if guess == secret_number:
        print("Congratulations! You've guessed the number in", num_guesses, "guesses!")
        bye = input("Well, I guess its time say are goodbye's! :) Bye!!: ")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")