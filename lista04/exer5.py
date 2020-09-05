#Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das 
#letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar 
#maiúsculas para minúsculas e de remover antes os caracteres especiais.

import re

txt = """The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.""".lower()

txt = txt.replace('.', '')
txt = txt.replace(',', '')
stxt = txt.split()
palavras = []
y = []

for x in stxt:
    z = re.search(r"\w+[python]\w+", x)
    if z:
        palavras.append(z.group())

for x in palavras:
    if len(x) > 4:
        y.append(x)

print(y)
print(len(y))