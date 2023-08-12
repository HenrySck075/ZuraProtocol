class sendhelp(object):
    def __getattribute__(self, name):
        if "__" in name: return super().__getattribute__(name.replace("_sendhelp",""))
        name = name.replace("method_","").replace("event_","").replace("type_","")
        return self.__class__.__name__ + "." + name[0].lower() + name[1:]
