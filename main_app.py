def replace_word():

    str = input('Enter a sentence/phrase: ')
    print('\n')
    print('Your Phrase: ', str)
    print('____________________________________________\n')


    word_to_replace = input('Enter the word you want to replace: ')
    print('\n')
    print("The word you would like to replace: ", word_to_replace)
    print('____________________________________________\n')


    word_replacement = input('Enter the new word you want to replace with: ')
    print('\n')
    print("The new word: ", word_replacement)
    print('____________________________________________\n')

    print("Here is the final result!\n")
    print('\n')
    print(str.replace(word_to_replace, word_replacement))



replace_word()