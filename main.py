import htmlmin
from compress import compression

with open("output.html") as f:
    code = f.read()
minifyed = htmlmin.minify(compression(), remove_comments=True, remove_empty_space=True)

compressed_content = minifyed.replace('"', '\\"')
remainder = ""

length = len(compressed_content.split('\n'))
for index, line in enumerate(compressed_content.splitlines()):
    _ = line.replace('"', '\"')
    if index+1 == length:
        remainder += f"\"{_}\\n\""
    else:
        remainder += f"\"{_}\\n\" + \n"

js_string = f'''function codeRunner() {{
    title_Name = document.title;
    var variable = {remainder};
    document.write(variable);
    document.title = title_Name;
    document.close();
}}'''

f = open("string.js", "w")
f.write(js_string)
f.close()
