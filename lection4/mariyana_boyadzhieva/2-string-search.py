import re

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. " \
       "Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla " \
       "tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, " \
       "lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. " \
       "Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, " \
       "varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."

found_words = []

for word in re.split(r'[,.\s]\s*', text):
    if word.endswith("o") or word.endswith("t"):
        found_words.append(word)

print(f"Words ending with 'o' or 't': {found_words}")
