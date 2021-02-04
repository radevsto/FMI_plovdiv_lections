# 1
even = ""
for num in range(101):
    if (num % 2 == 0):
        if (even == ""):
            even = str(num)
        else:
            even = even + ", " + str(num)
print("Even numbers: " + even)
# ---------------------------------------------------------------------------------
# 2
string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices.'
stringRemoveDot = string.replace(".", "")
stringRemoveDot = stringRemoveDot.replace(",", "")
splitString = stringRemoveDot.split()
otString = ""
for word in splitString:
    if (word.endswith("t") | word.endswith("o")):
        if (otString == ""):
            otString = "" + word
        elif (otString != ""):
            otString = otString + ", " + word
print("Words ending in 'o' and 't': " + otString)
# ---------------------------------------------------------------------------------
# 3
num2words = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',6: 'Six', 7: 'Seven',
    8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
    14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
    19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
    70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 0: 'Zero'
    }


def n2w(n):         # Function to use to convert numbers into words
    if n in num2words:
        return num2words[n]
    else:
        return num2words[n - n % 10] + " " + num2words[n % 10].lower()


newString = splitString
# maxNum=0                                      # Things I used to see more information about
# wordLength=[]                                 # what I'm dealing with
# for word in newString:
#    if(len(word)>maxNum):
#        maxNum=len(word)
#   if len(word) not in wordLength:
#       wordLength.append(len(word))
# print(maxNum)
# wordLength.sort()
# print("List of lengths of words: "+str(wordLength))

dictionary = {}
newString.sort(key=len)

for word in newString:
    dictionary[n2w(len(word))] = [word]         # Add the keys. Forces words to be replaced every time though.
for word in newString:
    dictionary[n2w(len(word))].append(word)     # Append all the words where they should be!
for key in dictionary:
    dictionary[key].pop(0)                      # Remove the first word for each key, as it's a duplicate

print("Dictionary: " + str(dictionary))
# ---------------------------------------------------------------------------------
# 4                                             # I don't know what dictionary comprehension is
for key in dictionary:
    print("Sum of "+key+": "+str(len(dictionary[key])*len(dictionary[key][0])))



