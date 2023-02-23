
def ParseAndModify(abrDB, testSlangsDict):
    f_write = open("DemoOutput.txt", "w")

    with open('DemoInput.txt','r') as f:
        for line in f:
            for word in line.split():
                if word in abrDB:
                    #print(abrDB[word])
                    newWord = '[' + abrDB[word] + ' ]'
                    line = line.replace(word,newWord)
                if word.swapcase() in abrDB:
                    #print(abrDB[word.swapcase()])
                    newWord = '[' + abrDB[word.swapcase()] + ' ]'
                    line = line.replace(word,newWord)

                if word in testSlangsDict:
                    #print(abrDB[word])
                    newWord = '[' + testSlangsDict[word] + ' ]'
                    line = line.replace(word,newWord)
                if word.swapcase() in testSlangsDict:
                    #print(abrDB[word.swapcase()])
                    newWord = '[' + testSlangsDict[word.swapcase()] + ' ]'
                    line = line.replace(word,newWord)

            f_write.write(line)
            #print(line)

    f_write.close()