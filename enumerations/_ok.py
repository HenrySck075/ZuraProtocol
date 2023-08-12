class sendhelp(object):
    def __getattribute__(self, name):
        if "__" in name: return super().__getattribute__(name.replace("_sendhelp",""))
        a = True
        if "type_" in name: a = False
        name = name.replace("method_","").replace("event_","").replace("type_","")
        return self.__class__.__name__ + "." +(name[0].lower() if a else name[0]) + name[1:]
