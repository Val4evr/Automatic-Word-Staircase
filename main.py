from requests import get, exceptions
import math

prohibited_characters = [" ", "-", "/"]
prohibited_words = ["abcdefghijklmnopqrstuvwxyz"]

def get_multiple_words(char, n, max=1): 
    """
    This function is the way it is to minimize API calls. 
    It is not possible to enter a query to produce results without the prohibited letters.
    for some reason exclude letters does not work with spaces so they must be filtered out.
    """

    wildcard = "?" * n
    url = f"https://api.datamuse.com/words?sp={char}{wildcard}&max={max}"
    try:
        result = get(url).json()
    except exceptions.ConnectionError:
        print("*"*10)
        print("Cannot connect to API.")
        print("*"*10)
        exit()

    for i in range(len(result)):
        word = result[i]['word']
        if word in prohibited_words:
            continue 
        for l in word:
            if l in prohibited_characters:
                break
        else:
            difficulty = round(math.log(max, 10)) + 1 
            return word, difficulty 

    if max == 1000:
        return False, False

    return get_multiple_words(char, n, max = max*10)

def main():
    print("\n" * 10)
    print("Automatic word staircase solver quickly thrown together by Valeriy Proklov.")
    print("Works using the phenomenal and thankfully free datamuse api.")
    print()

    letter = list(input("Enter your character(/s) with a space delimiter:").strip().lower().split())
    length = input("Enter the number of characters or just press enter for max:")
    if length == "":
        length = 100
    length = int(length)

    for char in letter:
        print("*"*10)

        for n in range(length):

            word, difficulty = get_multiple_words(char, n)

            if word == False:
                print("Longer word not found.")
                break
            print(f"Compute difficulty: {difficulty} Letter:{char} Length:{n+1} Word: {word}")
        print("*"*10)

if __name__ == "__main__":
    main()
