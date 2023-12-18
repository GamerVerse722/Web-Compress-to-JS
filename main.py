from bs4 import BeautifulSoup
import htmlmin
from compress import compression

with open("output.html") as f:
    code = f.read()

minifyed = htmlmin.minify(compression(), remove_comments=True, remove_empty_space=True)

add_style = '''button, #MySelectMenu {
    margin-left: 2px;
    margin-right: 2px;
}'''

soup = BeautifulSoup(minifyed, 'html.parser')

style_tag = soup.new_tag('style')
style_tag.string = add_style

soup.head.append(style_tag)

minifyed = str(soup)

compressed_content = minifyed.replace('"', '\\"')
remainder = ""

length = len(compressed_content.split('\n'))
for index, line in enumerate(compressed_content.splitlines()):
    _ = line.replace('"', '\"')
    if _ == '':
        continue
    if index+1 == length:
        remainder += f"\"{_}\""
    else:
        remainder += f"\"{_}\", "

js_string = f'''function codeRunner() {{
    title_Name = document.title;
    const html = [{remainder}];
    for (var x of html) {{
        document.writeln(x);
    }}
    document.title = title_Name;
    document.close();
}}'''

f = open("string.js", "w")
f.write(js_string)
f.close()
