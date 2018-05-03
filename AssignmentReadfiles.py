import os
import Arcade as arcade


def getNums():
    f = open("nums.txt", "r")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = int(lines[i])

    return lines


def getD_txt():
    f = open("d.txt", "r")
    words = f.read()
    f.close()
    words = words.split()
    return words


def average(lines):
    sum = 0.0
    for i in range(len(lines)):
        sum += lines[i]
    print(sum / len(lines))


def mostFrequent(lines):
    mf = 0
    for i in range(max(lines)):
        if lines.count(i) > lines.count(mf):
            mf = i
    print(mf)


def uniqueLetters(words):
    word = []
    for i in range(len(words)):
        if len(words[i]) == 7:
            word.append(words[i])

    unique = []
    for i in range(len(word)):
        un = True
        for j in range(len(word[i])):
            if word[i].count(word[i][j]) > 1:
                un = False
        if un:
            unique.append(word[i])

    return len(unique), unique[9]


def avoid():
    f = open("avoid.txt", "r")
    avoid = f.read()
    f.close()
    avoid = avoid.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'

    for i in letters:
        print(i, ":", avoid.count(i))
    count = 0
    for i in avoid:
        if i in vowels:
            count += 1
    print("vowels:", count)


def strip(word):
    newWord = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in word:
        if i in letters:
            newWord += i
    return newWord


def spellCheck():
    f = open("d.txt", "r")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = lines[i][:-2]
        lines[i] = lines[i].lower()
    f = open("NYTimes.txt", "r")
    times = f.read()
    f.close()
    times = times.lower()
    times = times.split()
    spell = 0
    for i in times:
        newWord = strip(i)
        if newWord in lines:
            spell += 1


def writeFile():
    dirList = os.listdir("./")  # makes a list of all the files in directory
    boo = True
    while boo:
        filename = raw_input("What is the name of the file?\n")
        if filename in dirList:
            x = raw_input("This file already exists, overwrite?\n")
            x = x.lower()
            if x[0] == "y":
                boo = False
        else:
            boo = False

    f = open(filename, "w")
    num = ["first", "second", "third", "fourth", "fifth"]
    for i in range(5):
        quest = "The " + num[i] + " line of the file:\n"
        ln = raw_input(quest)
        f.write(ln + "\n")
    f.close


def readFile():
    filename = raw_input("What is the name of the file?\n")
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    for i in lines:
        i = i[:-2]
    print(lines)


def topTenList():
    scores = {}
    f = open("scoreSheet", "r")
    lns = f.readlines()
    if len(lns) > 0:
        for i in lns:
            i = i.split("\t")
            name = i[1]
            scores[name] = int(i[0][1:])
    f.close

    money = arcade.play()

    name = raw_input("What is your name\n")
    scores[name] = money


    names = []
    srcs = []
    for key, value in sorted(scores.iteritems(), key=lambda (k, v): (v, k)):
        names.append(key)
        srcs.append(value)

    names = names[::-1]
    srcs = srcs[::-1]

    f = open("scoreSheet", "w")
    if len(srcs) < 10:
        for i in range(len(srcs)):
            ln = "$" + str(srcs[i]) + "\t" + str(names[i])
            if '\n' in ln:
                f.write(str(ln))
            else:
                f.write(str(ln)+'\n')
    else:
        for i in range(10):
            ln = "$" + str(srcs[i]) + "\t" + str(names[i])
            if '\n' in ln:
                f.write(str(ln))
            else:
                f.write(str(ln)+'\n')
    f.close

    ans = raw_input("Would you like to see the top ten list?")
    if ans[0].lower() == "y":
        print "\nSCORE\tPLAYER\n"
        if len(srcs)<10:
            for i in range(len(srcs)):
                print "$" + str(srcs[i]) + "\t" + str(names[i].rstrip())
        else:
            for i in range(10):
                print "$" + str(srcs[i]) + "\t" + str(names[i].rstrip())

def main():
    lines = getNums()
    words = getD_txt()
    print("\n0- done")
    print("1- average")
    print("2- most frequent")
    print("3- words")
    print("4- a Void")
    print("5- spell check")
    print("6- write a file")
    print("7- read a file")
    print("8- top ten list")

    assign = raw_input("Which Assignment would you like to see?\n")
    while not assign.isdigit():
        assign = raw_input("Which Assignment would you like to see?\n")
    assign = int(assign)

    options = [1, 2, 3, 4, 5, 6, 7, 8]

    if assign in options:
        if assign == 1:
            average(lines)
            main()
        if assign == 2:
            mostFrequent(lines)
            main()
        if assign == 3:
            amount, tenth = uniqueLetters(words)
            print("There are", amount, "unique-lettered words in the file.")
            print("The tenth one is", tenth+".")
            main()
        if assign == 4:
            avoid()
        if assign == 5:
            spellCheck()
        if assign == 6:
            writeFile()
        if assign == 7:
            readFile()
        if assign == 8:
            topTenList()
        main()
    elif assign == 0:
        pass
    else:
        main()


main()
