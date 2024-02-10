def flames(name1,name2):
    data = {"A": "ATTRACTION", "F": "FRIEND", "L": "LOVE", "M": "MARRIAGE", "E": "ENEMY", "S": "SISTER"}
    name1 = list(name1.strip().lower())
    name2 = list(name2.strip().lower() )
    for i in list(name1):
        if i in name2:
            name1.remove(i)
            name2.remove(i)
    main = list("FLAMES")
    n = len(name1+name2)
    while len(main)!=1:
        num = n%len(main)-1
        main.pop(num)
        dummy = main[:num:]
        if num == -1:
            continue
        for x in dummy:
            main.remove(x)
            main.append(x)
    return data[main[0]]
from pyscript import document
import pyfiglet
from js import alert

def domytask(event):
    name1 = document.querySelector("#name1").value
    name2 = document.querySelector("#name2").value
    if name1.strip().lower() == name2.strip().lower():
        alert("Both names are same")
        return
    result = flames(name1,name2)
    text = pyfiglet.figlet_format(result,font='digital')
    res = document.querySelector("#p-result")
    res.innerText = text
    document.querySelector("#result").style.display = "block"