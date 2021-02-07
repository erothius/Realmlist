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
    print("Default realmlist is : " + default)
    quest = input(
        "Do you want to use the default realmlist ? If so, press Enter \n")

    if quest == "":
        realmlist = realmlists["warmane"]
        edit(realmlist)
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
