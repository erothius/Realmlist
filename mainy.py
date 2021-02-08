import os


realmlists = {
    "warmane": "logon.warmane.com",
    "whitemane": "logon.whitemane.gg",

}


def edit(realmlist):
    f = open(r"E:\WoW_-_WotLK\data\enUS\realmlist.wtf", "w+")
    f.write("set realmlist " + realmlist)
    f.close()


def userinput():
    default = realmlists["warmane"]
    quest = input(f"Default {default} = Enter \n")

    if quest == "":
        realmlist = realmlists["warmane"]
    else:
        realmlist = realmlists["whitemane"]

    edit(realmlist)


def runexe():
    os.system(r"E:\WoW_-_WotLK\Wow.exe")


def main():
    userinput()
    runexe()


if __name__ == "__main__":
    main()
