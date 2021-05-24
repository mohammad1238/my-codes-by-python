
import json
def main():
    words=open("dict.json",'r')
    translator=json.load(words)
    state=input("please select your state(User,Developer): ")
    if state=="User":
        user(translator)
    else:
        developer(translator)
def user(translator):
    while True:
        word_english=input("please enter an english word:('exit to end'):")
        if word_english=="exit":
            break
        if word_english not in translator:
            print("the word not found in dict.")
            break
        print(translator[word_english])
def developer(translator):
    while True:
        word_english=input("enter an english word:('exit to end'):")
        if word_english=='exit':
            break
        word_arabic=input("enter an arabic word: ")
        translator[word_english]=word_arabic
    file=open("dict.json",'w')
    json.dump(translator,file)
main()

