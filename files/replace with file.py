word = "Donkey"
with open("files/word.txt","r") as f:
    content=f.read()
new_content=content.replace(word,"######")
with open("files/word.txt","w") as f:
    f.write("THIS FILE IS EDITED BY REPLACE WITH FILE.PY.PY\n")
    f.write(new_content)