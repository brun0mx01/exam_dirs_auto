import os

name = str(input("Entre votre nom et prénom: "))

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
stg_path = os.path.join(desktop_path, name)

dossiers = ['Microsoft Word', 'Microsoft Excel', 'Microsoft Power Point', 'MS-DOS']

for doss in dossiers:
    doss_path = os.path.join(stg_path, doss)
    os.makedirs(doss_path, exist_ok=True)

    