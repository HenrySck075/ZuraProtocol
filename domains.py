from bs4 import BeautifulSoup as luigi
import requests, re

a = luigi(requests.get("https://chromedevtools.github.io/devtools-protocol/tot/").text,"lxml")
domains = [i.attrs["href"] for i in a.select("aside #domains a")]

initsrc = ""

actualDomains = [i.split("/")[-1] for i in domains]
for name in actualDomains:
    lowname = name.lower()

    s = luigi(requests.get("https://chromedevtools.github.io/devtools-protocol/tot/"+name).text,"lxml")
    n=s.select_one("#header")
    
    tag = ""
    src  = "from . import _ok as base\n\n"
    src += f"class {name}(base.sendhelp):\n"
    for e in n.select("*")[2:]:
        if e.name == "h3":
            src += "\n"
            tag = e.string.replace("s","")
            tag = tag[0].lower()+tag[1:]
            continue
        elif e.name != "div": continue
        else:
            attr = re.search("-(.*)",e.select_one("a").attrs["href"]).group().replace("-","")
            src += "    " + tag + "_" + attr[0].upper() + attr[1:] + ":str" + "\n"
    src += """
    def __init__(self):
        super().__init__()

    """
    src += "\n"
    src += f"domain = {name}()"
    initsrc += "from .{n} import domain as {n2}\n".format(n=lowname,n2=name)
    open(lowname+".py","w").write(src)
open("__init__.py","w").write(initsrc) 
