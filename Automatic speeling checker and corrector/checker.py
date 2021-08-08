from textblob import TextBlob

with open("text.txt", "r") as f:        # Opening the test file with the intention to read
    text = f.read()                     # Reading the file
    textBlb = TextBlob(text)            # Making our first textblob
    textCorrected = textBlb.correct()   # Correcting the text
    print(textCorrected)