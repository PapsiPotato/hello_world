def line(length,inputStr):
    if inputStr!="":
        print(inputStr[:1]*length)
    else:
        print("*"*length)

def box_of_hashes(rows):
    while rows > 0:
        line(10,"#")
        rows -= 1

def square_of_hashes(rows):
    rowsTmp=rows
    while rows>0:
        line(rowsTmp,"#")
        rows -= 1

def square(length,input):
    rowsTmp=length
    while length>0:
        line(rowsTmp,input[:1])
        length -= 1


def triangle(rows):
    tempCount=1
    while rows>0:
        line(tempCount,'#')
        rows -= 1
        tempCount +=1

def triangle_shape(rows,character):
    tempCount=1
    while rows>0:
        line(tempCount,character[:1])
        rows -= 1
        tempCount +=1


def rectangle_shape(rows,height,character):
    while height> 0:
        line(rows,character[:1])
        height -= 1


def shape(a,b,c,d):
    triangle_shape(a,b)
    rectangle_shape(a,c,d)

    

def spruce(height):
    width=(height*2)-1
    x=1
    y=height
    while y>0:
        print(" "*(height-x),"*"*(((x-1)*2)+1))
        x+=1
        y-=1
    print(" "*(height-1),"*")
    print("a spruce!")

def greatest_number(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

def same_chars(string, char1,char2):
    if char1>len(string) or char2>len(string):
        return False
    if string[char1]==string[char2]:
        return True
    else:
        return False


def first_word(sentence):
    return sentence.split()[0]

def second_word(sentence):
    return sentence.split()[1]

def last_word(sentence):
    return sentence.split()[(len(sentence.split()))-1]



# list_exercise=[]
# listEntries=int(input("How many items:"))
# for x in range(listEntries):
#     inputStr=input(f"Item {x+1}:")
#     list_exercise.append(inputStr)
# print(list_exercise)

# inputEntry=""
# listTest=[]
# while inputEntry!='x':
#     print(f"The list is now {listTest}")
#     action=input("a(d)d, r(e)move, or e(x)it:")
#     if action=="d":
#         listTest.append(len(listTest)+1)
#     elif action=="r":
#         if len(listTest)>0:
#             listTest.pop(len(listTest)-1)
#     elif action=="x":
#         print("Bye!")
#         break

    
def length(my_list : list):
    return len(my_list)

def mean(my_list : list):
    number =sum(my_list)/len(my_list)
    return number

def range_of_list(my_list : list):
    number = max(my_list)-min(my_list)
    return number

# listEntry=[]
# while True:
#     inputStr=int(input("New integer: "))
#     if inputStr==0:
#         print('Bye!')
#         break
#     listEntry.append(inputStr)
#     print(f'The list now: {listEntry}')
#     print(f'The list now in order: {sorted(listEntry)}')
#     print(f'List length: {length(listEntry)}')
#     print(f'Mean of the list: {mean(listEntry)}')
#     print(f'Range of the list: {range_of_list(listEntry)}')
    
while True:
    inputStr=input("Which editor are you using?")
    if inputStr.upper()=="NOTEPAD":
        print("Awful!")
    elif inputStr.upper()=="WORD":
        print("Awful!")
    elif inputStr.upper()=="VISUAL STUDIO CODE":
        print("Awesome - great choice!")
        break
    else:
        print("Not good")
