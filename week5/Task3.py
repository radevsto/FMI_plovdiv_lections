import re

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis tempus suscipit. Mauris efficitur interdum turpis, vitae varius nunc fringilla non. Vestibulum malesuada fringilla tellus vel iaculis. In vehicula gravida fermentum. Vivamus ultrices lacinia pretium. Mauris orci lectus, lacinia at placerat ut, aliquam at quam. Donec condimentum feugiat arcu, ut consectetur tortor ornare id. Vivamus et arcu nunc. Morbi viverra quam id libero rutrum elementum. Integer nibh eros, varius eu euismod ac, accumsan congue mauris. Integer eu mattis dui. Pellentesque volutpat vehicula ultrices."
words = re.split(r'(;|,|\.|\s)\s*', string)

result = {
    "two": set(),
    "three": set()
}
for word in words:
    if len(word) == 2:
        result["two"].add(word)
    elif len(word) == 3:
        result["three"].add(word)

print(result)

two_count = {"two": len(result["two"]) * 2}
three_count = {"three": len(result["three"]) * 3}
print(two_count)
print(three_count)