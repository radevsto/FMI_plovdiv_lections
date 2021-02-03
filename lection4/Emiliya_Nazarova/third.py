string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices.'

dict = {}

for word in string.split():
    if word[-1] == '.' or word[-1] == ',':
        key = len(word) - 1
        if key not in dict:
            dict[key] = []

        dict[key].append(word[:-1])

    else:
        key = len(word)
        if key not in dict:
            dict[key] = []

        dict[key].append(word)

for key in dict:
    print(key)
    count = len(dict[key]) * key
    print(f"the count is {count}")
