from random import choice
import math, pyperclip
#text="""Letter frequency is simply the amount of times letters of the alphabet appear on average in written language. Letter frequency analysis dates back to the Arab mathematician Al-Kindi (c. 801–873 AD), who formally developed the method to break ciphers. Letter frequency analysis gained importance in Europe with the development of movable type in 1450 AD, where one must estimate the amount of type required for each letterform. Linguists use letter frequency analysis as a rudimentary technique for language identification, where it's particularly effective as an indication of whether an unknown writing system is alphabetic, syllabic, or ideographic. The use of letter frequencies and frequency analysis plays a fundamental role in cryptograms and several word puzzle games, including Hangman, Scrabble and the television game show Wheel of Fortune. One of the earliest descriptions in classical literature of applying the knowledge of English letter frequency to solving a cryptogram is found in Edgar Allan Poe's famous story The Gold-Bug, where the method is successfully applied to decipher a message instructing on the whereabouts of a treasure hidden by Captain Kidd.[1] Letter frequencies also have a strong effect on the design of some keyboard layouts. The most frequent letters are on the bottom row of the Blickensderfer typewriter, and the home row of the Dvorak keyboard layout. The frequency of letters in text has been studied for use in cryptanalysis, and frequency analysis in particular, dating back to the Iraqi mathematician Al-Kindi (c. 801–873 AD), who formally developed the method (the ciphers breakable by this technique go back at least to the Caesar cipher invented by Julius Caesar, so this method could have been explored in classical times). Letter frequency analysis gained additional importance in Europe with the development of movable type in 1450 AD, where one must estimate the amount of type required for each letterform, as evidenced by the variations in letter compartment size in typographer's type cases.No exact letter frequency distribution underlies a given language, since all writers write slightly differently. However, most languages have a characteristic distribution which is strongly apparent in longer texts. Even language changes as extreme as from old English to modern English (regarded as mutually unintelligible) show strong trends in related letter frequencies: over a small sample of Biblical passages, from most frequent to least frequent, enaid sorhm tgþlwu æcfy ðbpxz of old English compares to eotha sinrd luymw fgcbp kvjqxz of modern English, with the most extreme differences concerning letterforms not shared.[2]Linotype machines for the English language assumed the letter order, from most to least common, to be etaoin shrdlu cmfwyp vbgkjq xz based on the experience and custom of manual compositors. The equivalent for the French language was elaoin sdrétu cmfhyp vbgwqj xz.Arranging the alphabet in Morse into groups of letters that require equal amounts of time to transmit, and then sorting these groups in increasing order, yields e it san hurdm wgvlfbk opxcz jyq.[a] Letter frequency was used by other telegraph systems, such as the Murray Code.Similar ideas are used in modern data-compression techniques such as Huffman coding.Letter frequencies, like word frequencies, tend to vary, both by writer and by subject. One cannot write an essay about x-rays without using frequent Xs, and the essay will have an idiosyncratic letter frequency if the essay is about the use of x-rays to treat zebras in Qatar. Different authors have habits which can be reflected in their use of letters. Hemingway's writing style, for example, is visibly different from Faulkner's. Letter, bigram, trigram, word frequencies, word length, and sentence length can be calculated for specific authors, and used to prove or disprove authorship of texts, even for authors whose styles are not so divergent.Accurate average letter frequencies can only be gleaned by analyzing a large amount of representative text. With the availability of modern computing and collections of large text corpora, such calculations are easily made. Examples can be drawn from a variety of sources (press reporting, religious texts, scientific texts and general fiction) and there are differences especially for general fiction with the position of 'h' and 'i', with 'h' becoming more common.Herbert S. Zim, in his classic introductory cryptography text "Codes and Secret Writing", gives the English letter frequency sequence as "ETAON RISHD LFCMU GYPWB VKJXZQ", the most common letter pairs as "TH HE AN RE ER IN ON AT ND ST ES EN OF TE ED OR TI HI AS TO", and the most common doubled letters as "LL EE SS OO TT FF RR NN PP CC".[3] Also, to note that different dialects of a language will also affect a letter's frequency. For example, an author in the United States would produce something in which the letter 'z' is more common than an author in the United Kingdom writing on the same topic: words like "analyze", "apologize", and "recognize" contain the letter in American English, whereas the same words are spelled "analyse", "apologise", and "recognise" in British English. This would highly affect the frequency of the letter 'z' as it is a rarely used letter by British speakers in the English language.[4]The "top twelve" letters constitute about 80% of the total usage. The "top eight" letters constitute about 65% of the total usage. Letter frequency as a function of rank can be fitted well by several rank functions, with the two-parameter Cocho/Beta rank function being the best.[5] Another rank function with no adjustable free parameter also fits the letter frequency distribution reasonably well[6] (the same function has been used to fit the amino acid frequency in protein sequences.[7]) A spy using the VIC cipher or some other cipher based on a straddling checkerboard typically uses a mnemonic such as "a sin to err" (dropping the second "r")[8][9] or "at one sir"[10] to remember the top eight characters. """
#text="please excuse my dear aunt sally"
text=pyperclip.paste()
print("text: "+text)

letters=r'abcdefghijklmnopqrstuvwxyz'
code={}

#generate my OTP
for letter in letters:
    while True:
        value=choice(letters)
        if value not in code.values():
            code[letter]=value
            break

#for key, value in code.items():
    #print(f"{key}:{value}")

#using OTP, encode the text
encoded_text=''
for letter in text.lower():
    if letter in code:
        encoded_text+=code[letter]
    else:
        encoded_text+=letter

print("encoded_text: "+encoded_text)


#generate frequency of characters from encoded text
freqs={}


for letter in encoded_text.lower():
    if letter in freqs:
        freqs[letter]+=1
    else:
        freqs[letter]=1

my_freqs=[]
for key, value in sorted(freqs.items(), key=lambda item: item[1], reverse=True):
    #print(f"{key}:{value}")
    if key in letters:
        my_freqs.append(key)

#Compare with a true frequency of letters
true_freqs=list('ETAOINSRHDLUCMFYWGPBVKXQJZ'.lower())

print("my freqs:  ",my_freqs)
print("true freqs:",true_freqs)

#Check the similarities of the frequency
score=0
for i in range(len(my_freqs)):
    if my_freqs[i]==code[true_freqs[i]]:
        score+=1

print(f"Similarity: {score}/26 ({math.ceil((score/26)*100)}%)")
    
    
#use the frequency to decode the encoded text
decoded_text=''
for letter in encoded_text:
    if letter in my_freqs:
        decoded_text+=true_freqs[my_freqs.index(letter)]
    else:
        decoded_text+=letter

print("decoded_text: "+decoded_text)

#Check accuracy of output
correct_letters=[]
score=0
for i in range(len(decoded_text)):
    if decoded_text[i]==text[i]:
        if text[i] not in correct_letters and text[i] in letters:
            correct_letters.append(text[i])
        score+=1
        
print(f"Accuracy: {score}/{len(decoded_text)} ({math.ceil((score/len(decoded_text))*100)}%)")
print(f"Correct Letters: {correct_letters}")


        
