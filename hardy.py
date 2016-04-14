#Created by Ishan Kamat

import time
punc = (',', ';', ':', '?')

markers = []

hardy = input("Hardy-Weinberg Question: ")
start = time.time()
print("\nProcessing...")
def number_detection(word):
    if '%' in word:
        word = "0." + word.replace('%', "")
    try:
        float(word)
        return True
    except:
        return False

def remove_punctuation(word):
    for p in punc:
        if p in word:
            word = word.replace(p, "")
    if word[-1] == '.':
        word = word[:-1]
    return word

wordMap = {}
words = []
ind = 0
time.sleep(0.1) #if we sleep here then it 
#looks like something cool is happening
print("Analyzing...")
for bword in hardy.split():
    bword = bword.lower()
    if bword[-1] == '.':
        markers.append(ind)
    word = remove_punctuation(bword)
    words.append(word)
    time.sleep(0.01)
    wordMap[word] = number_detection(word)

    ind += 1

popl = 0
varP = 0
varQ = 0

pSqr = 0
qSqr = 0
pq_2 = 0

#dear whoever is reading my code,
#sorry for all of the weird stuff
#i was kinda tired
#sincerely, ishan

def nondescript_function_name():
    return [varP, varQ, pSqr, qSqr, pq_2]

oldVars = nondescript_function_name()

ind = 0
marker = 0
print("Comprehending...")
for word in words:
    time.sleep(0.02)
    if wordMap[word]:
        if '%' in word:
            newWord = word.replace('%', "")
            word = "0." + ("0" * (2 - len(newWord))) + newWord
        lowerLimit = marker
        
        uppperLimit = 0
        for mrker in markers:
            if ind < mrker:
                uppperLimit = mrker + 1
        if uppperLimit == 0:
            uppperLimit = len(words)

        curIndex = lowerLimit

        for wordn in words[lowerLimit:uppperLimit]:
            if wordn == "dominant":
                dom = True
            elif wordn == "recessive":
                dom = False
            if wordn == "gene":
                #expects gene frequencies in decimal or percentages
                if dom:
                    varP = float(word)
                elif not dom:
                    varQ = float(word)
                marker = curIndex + 1
                break
            elif wordn == "trait" or wordn == "phenotype":
                #can use amount of population (integer) or percentage for this
                #also will take a decimal
                if float(word) > 1:
                    word = str(float(word) / popl)
                if dom:
                    pSqr = float(word)
                elif not dom:
                    qSqr = float(word)
                marker = curIndex + 1
                break
            if (wordn == "population" or wordn == "sample") and "of" == words[curIndex+1]:
                popl = float(word)
                marker = curIndex + 2
                break
            curIndex += 1


    ind += 1



cantEven = "I wasn't able to determine "
askUser = ". Do you know this? "

if popl == 0:
    print("\nUnable to comprehend the question. Asking user for data...\n")
    try:
        popl = float(remove_punctuation(input(cantEven + "the population" + askUser)))
    except:
        while popl == 0:
            try:
                response = input("Can you give me an integer or something? (If not, say no): ").lower()
                popl = float(remove_punctuation(response))
            except:
                if response == "no":
                    print("Assuming population of 1000...")
                    popl = 1000.0
                else:
                    continue

#this next part is really awful but im lazy so it stays

haveData = False
for varVal in nondescript_function_name():
    if varVal != 0:
        haveData = True
if not haveData:
    try: 
        response = input(cantEven + "p" + askUser + " (If not, leave blank): ").lower()
        varP = float(remove_punctuation(response))
    except:
        pass
    if varP == 0:
        try:
            response = input(cantEven + "q" + askUser + " (If not, leave blank): ").lower()
            varQ = float(remove_punctuation(response))
        except:
            pass
        if varQ == 0:
            try:
                response = input(cantEven + "p^2" + askUser + " (If not, leave blank): ").lower()
                pSqr = float(remove_punctuation(response))
            except:
                pass
            if pSqr == 0:
                try:
                    response = input(cantEven + "q^2" + askUser + " (If not, leave blank): ").lower()
                    qSqr = float(remove_punctuation(response))
                except:
                    pass
                if qSqr == 0:
                    print("\nSUPER FATAL ERROR! Unable to comprehend and user has not provided adequate data!\n")
                    #definitely super fatal

print("Calculating...")

if popl:
    curVars = nondescript_function_name()
    while curVars != oldVars:
        time.sleep(0.05)
        if varP:
            varQ = float(100 - varP * 100) / 100.0
        if varQ:
            varP = float(100 - varQ * 100) / 100.0
        if pSqr:
            varP = pSqr ** 0.5
        else:
            pSqr = varP ** 2
        if qSqr:
            varQ = qSqr ** 0.5
        else:
            qSqr = varQ ** 2
        if not pq_2:
            pq_2 = varP * varQ * 2

        oldVars = curVars
        curVars = nondescript_function_name()

print("Done!\n")

time.sleep(0.25)

print("I've determined that...")

def roundf(number):
    try:
        return float(str(number)[:4])
    except IndexError:
        return number

print("the population is " + str(popl))
print("p is " + str(roundf(varP)))
print("q is " + str(roundf(varQ)))
print("p^2 is " + str(roundf(pSqr)) + " (" + str(roundf(popl * pSqr)) + " individuals)")
print("q^2 is " + str(roundf(qSqr)) + " (" + str(roundf(popl * qSqr)) + " individuals)")
print("2pq is " + str(roundf(pq_2)) + " (" + str(roundf(popl * pq_2)) + " individuals)")

print("\nNote: Answers may be off by a small amount for reasons.")
print("\nFinished in " + str(time.time() - start)[:5] + " seconds")
print("If something isn't working then email me and I might be able to fix it.")
