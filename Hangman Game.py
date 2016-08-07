import random
words = ["vantilatör", "adaptör", "kalem", "fare", "telefon", "kulaklık" ]
pictures = [
    "\n\n\n\n\n",
    "\n\n\n\n ---",
    "\n\n | \n | \n | \n---",
    "\n______\n | \n | \n | \n---",
    "\n______\n |  0 \n | -|-\n | / \\ \n---"
]
def oyunhazirlik():
    global selected_word, faults, visibles, visible
    faults = 0
    visibles = 0
    selected_word = random.choice(words)
    visible = ["[-]"] * len(selected_word)
def oyundongu():
    global selected_word, faults, visibles, visible
    while True:
        print(pictures[faults])
        print("".join(visible))
        print("Lives = " + str(5 - faults))
        inputstring = input("Bir Harf Giriniz: ")
        inputletter = inputstring[0].lower()
        if (inputletter in selected_word ) and ("["+ inputletter+ "]" not in visible):
            for index, h in enumerate(selected_word):
                if h == inputletter:
                    visible[index] = "["+h+"]"
                    visibles += 1
        elif len(inputstring) > 0 and "["+ inputletter+ "]" not in visible:
            faults += 1
        if visibles == len(selected_word):
            print ("kazandınız")
            break
        elif faults == 5 :
            print ("kaybettiniz")
            break

oyunhazirlik()
oyundongu()
