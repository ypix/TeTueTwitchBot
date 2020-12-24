import sys

sys.path.append('../')
from tetuebot import configParser


# liste_badwords = config.get("keywords", "badwords").split(",")
# 
# liste = ["böse1", ...]

def main():
    #read_successful, cfg = configParser.get_configuration("bot")
    print(dir(configParser))
    
if __name__ == "__main__":
    main()
