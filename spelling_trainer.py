from gtts import gTTS
import playsound
import getpass
# State the purpose of the program
print("This is a spelling test program that you can use to learn how to spell words that you find tricky.")

# Ask the user to input 10 tricky words to spell
tricky_words = []
while (len(tricky_words) < 5):
    word = getpass.getpass("Please correctly enter a word: ")
    word = word.lower()
    if (word not in tricky_words):
        tricky_words.append(word)
    else:
        print("You have already added that word. Please add a different word.")

    
# Ask the user to spell each word
print("Let the spelling test begin!")

score = 0
counter = 1
def play_sound(file_name):
    playsound.playsound(file_name)
    
for word in tricky_words:
    language = "en"
    myobj = gTTS(text = word, lang = language, slow = True)
    filename = "word" + str(counter) + ".mp3"
    myobj.save(filename)
    play_sound(filename)
    spelling = input("Spell: ")
    # Check if each spelling is correct
    if (spelling.lower() == word):
        score = score + 1
    counter = counter + 1

# Add up the final score and present it
print("Your final score is", score)
