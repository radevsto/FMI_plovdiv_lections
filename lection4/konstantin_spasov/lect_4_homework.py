def even_numbers():

    for i in range(1,101):
        if i % 2 == 0:
            print i

def string_play():
    string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."
    string = string.replace('.','')
    string = string.replace(',', '')
    array = string.split(' ')
    return(array)

def word_play():

    array = string_play()
    for i in array:
        if i[-1:] == 'o':
            print(i)
        elif i[-1:] == 't':
            print(i)

def dict():
    array = string_play()
    sorted_array = sorted(array, key=len)
    dictionary = {}
    for word in sorted_array:
        dictionary.setdefault(len(word), []).append(word)
    count = 0
    for key in dictionary.keys():
        j=0
        for elem in dictionary[key]:
            j+=1
        count = count + (j * int(key))
    for key in dictionary.keys():
        print(str(key) + " - " + str(dictionary[key]))
    print("Number of letters in the string: " + str(count))

def main():
    print("Task number: ")
    option = raw_input("1 - Event Numbers in 1:100 | 2 - words ending in \'o\' and \'t\' | 3 - Dictionary ops: \n")
    print("Selection option is " + option)

    if option == '1':
        even_numbers()
    elif option == '2':
        word_play()
    elif option == '3':
        dict()
    else:
        print ("Unknown selection")
        sys.exit(1)
if __name__ == '__main__':
    main()