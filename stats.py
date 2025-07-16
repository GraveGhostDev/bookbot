def count_words(text):
    return len(text.split())


def count_character(text):
    myDict = {}
    for character in text:
        letter = character.lower()
        if letter in myDict:
           myDict[letter] +=1
        else:
            myDict[letter] = 1
    return myDict


def sort_by_count(item):
    return item[1]


def sorting(myDict):
    new_list = list(myDict.items()) 
    new_list.sort(reverse=True, key=sort_by_count)
    return new_list

    
