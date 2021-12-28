#!/usr/bin/env python

    # Malware DB - the most awesome free malware database on the air
    # Copyright (C) 2014, Yuval Nativ, Lahad Ludar, 5Fingers

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sys
import os
import random

class init:

    def init(self):
        # Global Variables
        version = "1.0"
        appname = "Pestilence"
        codename = "Err"
        authors = "Err0r_HB"
        maintainers = "HackBoyz Team"
        github_add = "https://www.github.com/Err0r-ICA/Pestilence"
        licensev = "GPL v3.0"
        fulllicense = appname + " Copyright (C) 2021 " + authors + "\n"
        fulllicense += "This program comes with ABSOLUTELY NO WARRANTY; for details type '" + \
            sys.argv[0] + " -w'.\n"
        fulllicense += "This is free software, and you are welcome to redistribute it."

        usage = '\nUsage: ' + sys.argv[0] + \
            ' -s search_query -t trojan -p vb\n\n'
        usage += 'The search engine can search by regular search or using specified arguments:\n\nOPTIONS:\n   -h  --help\t\tShow this message\n   -t  --type\t\tMalware type, can be virus/trojan/botnet/spyware/ransomeware.\n   -p  --language\tProgramming language, can be c/cpp/vb/asm/bin/java.\n   -u  --update\t\tUpdate malware index. Rebuilds main CSV file. \n   -s  --search\t\tSearch query for name or anything. \n   -v  --version\tPrint the version information.\n   -w\t\t\tPrint GNU license.\n'

        conf_folder = 'conf'
        eula_file = conf_folder + '/eula_run.conf'
        maldb_ver_file = conf_folder + '/db.ver'
        giturl = 'https://github.com/Err0r-ICA/Pestilence/blob/master'


##########################################################
class Completer:
    def __init__(self, commands):
        self.commands = commands
        self.prefix = None

    def complete(self, prefix, index):
        if prefix != self.prefix:
            self.matchingCommand = [w for w in self.commands if w.startswith(prefix)
                ]
            self.prefix = prefix
        try:
            return self.matchingCommand[index]
        except IndexError:
            return None
################################################################


class vars:
    version = "1.0'"
    appname = "Pestilence"
    authors = "Err0r_HB"
    maintainers = [ "Err0r_HB", "" ]
    github_add = "https://www.github.com/Err0r-ICA/Pestilence"
    licensev = "GPL v3.0"

    ############ DEBUGGING ###############
    #### SET TO ZERO BEFORE COMMIT #######

        # DEBUG_LEVEL 0 = NO DEBUGGING
        # DEBUG_LEVEL 1 = DEBUG DOWNLOADS
        # DEBUG_LEVEL 2 = DEBUG SQL QUERIES

    DEBUG_LEVEL = 0

    fulllicense = appname + " Copyright (C) 2021 " + authors + "\n"
    fulllicense += "This program comes with ABSOLUTELY NO WARRANTY; for details type '" + \
        sys.argv[0] + " -w'.\n"
    fulllicense += "This is free software, and you are welcome to redistribute it."

    usage = '\nUsage: ' + sys.argv[0] + ' -s search_query -t trojan -p vb\n\n'
    usage += 'The search engine can search by regular search or using specified arguments:\n\nOPTIONS:\n   -h  --help\t\tShow this message\n   -t  --type\t\tMalware type, can be virus/trojan/botnet/spyware/ransomeware.\n   -p  --language\tProgramming language, can be c/cpp/vb/asm/bin/java.\n   -u  --update\t\tUpdate malware index. Rebuilds main CSV file. \n   -s  --search\t\tSearch query for name or anything. \n   -v  --version\tPrint the version information.\n   -w\t\t\tPrint GNU license.\n'

    # :todo: add filter usage

    opts = [
        ("type", ("Virus", "Worm", "Ransomware", "Botnet", "Apt", "Rootkit", "Trojan", "ExploitKit", "Dropper")),
        ("architecture", ("x86", "x64", "arm", "web")),
        ("platform", ("win32", "win64", "android", "ios", "mac", "*nix32", "*nix64", "symbian")),
        ("language", ("c", "cpp", "asm", "bin", "java", "apk", "vb", "php"))]

    conf_folder = 'conf'
    eula_file = conf_folder + '/eula_run.conf'
    maldb_ver_file = conf_folder + '/db.ver'
    db_path = conf_folder + "/maldb.db"
    giturl_dl = 'https://github.com/ytisf/theZoo/raw/master/'
    giturl = 'https://github.com/Err0r-ICA/Pestilence/'

    with open(maldb_ver_file, 'r') as f:
        db_ver = f.read()

    # ASCII Art is a must...
    screen = random.randrange(1, 6)

    if screen is 1:
        maldb_banner = "\n"
        maldb_banner += "\033[38;5;196m        sMMs              oMMy      \n"
        maldb_banner += "        :ooooo/        /ooooo:      \n"
        maldb_banner += "        ```+MMd````````hMMo```      \n"
        maldb_banner += "        oNNNMMMNNNNNNNNMMMNNNs      \n"
        maldb_banner += "     /oodMMdooyMMMMMMMMyoodMMdoo/   \t\033[38;5;053mPestilence \033[38;5;015m" + version + "\n"
        maldb_banner += "\033[38;5;196m  `..dMMMMMy. :MMMMMMMM/  sMMMMMm..`\t \033[38;5;055mDB ver. \033[38;5;015m" + db_ver + "\n"
        maldb_banner += "\033[38;5;196m  dmmMMMMMMNmmNMMMMMMMMNmmNMMMMMMmmm\n"
        maldb_banner += "\033[38;5;196m  NMMyoodMMMMMMMMMMMMMMMMMMMMdoosMMM\t\033[38;5;015m" + giturl + "\n"
        maldb_banner += "\033[38;5;196m  NMM-  sMMMNNNNNNNNNNNNNNNMMy  .MMM\n"
        maldb_banner += "  NMM-  sMMy``````````````sMMy  .MMM\n"
        maldb_banner += "  ooo.  :ooooooo+    +ooooooo/  `ooo\n"
        maldb_banner += "           /MMMMN    mMMMM+         \n"
        maldb_banner += "                                 \033[38;5;118mAuthors: \033[38;5;015m" + authors + "\n"
        maldb_banner += "                                 \033[38;5;154mMaintained by: \033[38;5;015m" + ', '.join(maintainers) + "\n"
        maldb_banner += "                                 \033[38;5;215mGithub: \033[38;5;015m" + giturl + "\n"
        maldb_banner += "                                 \033[38;5;221mInstagram: \033[38;5;015m@termux_hacking\n\n"

    elif screen is 2:
        maldb_banner = "           ____.----. \n"
        maldb_banner += " ____.----'          \ \n"
        maldb_banner += "  \                    \ \tPestilence " + version + "\n"
        maldb_banner += "    \          ____.----'`--.__ \t" + giturl + "\n"
        maldb_banner += "     \___.----'          |     `--.____\n"
        maldb_banner += "    /`-._                |       __.-' \ \n"
        maldb_banner += "   /     `-._            ___.---'       \ \n"
        maldb_banner += "  /          `-.____.---'                \ \n"
        maldb_banner += " '_         /   |   \            __.--'--'\n"
        maldb_banner += "   `-._    /    |    \     __.--'     |\n"
        maldb_banner += "     | `-./     |     \_.-'           |\n"
        maldb_banner += "     |          |                     |\n"
        maldb_banner += "     |          |      Free Malwares  |\n"
        maldb_banner += "     |          |          & Hugs     |\n"
        maldb_banner += "_____|          |        *Err0r_HB*   |______\n"
        maldb_banner += "     `-.        |  /\              _.-'\n"
        maldb_banner += "        `-.     |  || UP    __..--'\n"
        maldb_banner += "           `-.  |      __.-'\n"
        maldb_banner += "              `-|__.--'\n"

    elif screen is 3:
        maldb_banner = "\033[38;5;202m ____    ___  _____ ______  ____  _        ___  ____     __    ___ \n"
        maldb_banner += "\033[38;5;202m|    \  /  _]/ ___/|      Tl    j| T      /  _]|    \   /  ]  /  _]\n"
        maldb_banner += "\033[38;5;202m|  o  )/  [_(   \_ |      | |  T | |     /  [_ |  _  Y /  /  /  [_ \n"
        maldb_banner += "\033[38;5;202m|   _/Y    _]\__  Tl_j  l_j |  | | l___ Y    _]|  |  |/  /  Y    _]\n"
        maldb_banner += "\033[38;5;202m|  |  |   [_ /  \ |  |  |   |  | |     T|   [_ |  |  /   \_ |   [_ \n"
        maldb_banner += "\033[38;5;202m|  |  |     T\    |  |  |   j  l |     ||     T|  |  \     ||     T\n"
        maldb_banner += "\033[38;5;202ml__j  l_____j \___j  l__j  |____jl_____jl_____jl__j__j\____jl_____j\n\n"
        maldb_banner += "\033[38;5;049m                      Version: \033[38;5;015m" + version + "\n"
        maldb_banner += "\033[38;5;118m                      DB_version: \033[38;5;015m" + db_ver + "\n"
        maldb_banner += "\033[38;5;154m                      Built by: \033[38;5;015m" + authors + "\n"
        maldb_banner += "\033[38;5;215m                      Maintained by: \033[38;5;015m" + ', '.join(maintainers) + "\n"
        maldb_banner += "\033[38;5;221m                      Github: \033[38;5;015m" + giturl + "\n"
        maldb_banner += "\033[38;5;197m                      Instagram: \033[38;5;015m@termux_hacking\n\n"

    elif screen is 4:
        maldb_banner = "\n"
        maldb_banner += "\033[38;5;152m.       ..       .\n"
        maldb_banner += "|\      ||      /|\n"
        maldb_banner += "| \     ||     / |\n"
        maldb_banner += "|  \    ||    /  |\n"
        maldb_banner += "|  :\___JL___/   |\n"
        maldb_banner += "|  :|##XLJ: :|   |\n"
        maldb_banner += "'\ :|###||: X|  /'\n"
        maldb_banner += "  \:|###||:X#| /\n"
        maldb_banner += "   |==========|\n"
        maldb_banner += "    |###XXX;;|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##Xn:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##Xn:: :|\n"
        maldb_banner += "    |##XX:: n|\n"
        maldb_banner += "    |##XX:: U|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##Xn:: :|\n"
        maldb_banner += "    |##XU:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: n|\n"
        maldb_banner += "    |##XX:: U|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##XX:: :|\n"
        maldb_banner += "    |##Xn:: :|\n"
        maldb_banner += "    |##XU:: :|\n"
        maldb_banner += "\033[38;5;152m    |##Xn:: :|\t\033[38;5;048mPestilence \033[38;5;015m" + version + "\n"
        maldb_banner += "\033[38;5;152m    |##XU:: :|\t\033[38;5;118mDB_Version  \033[38;5;015m" + db_ver + "\n"
        maldb_banner += "\033[38;5;152m    |##XX:: :|\t\033[38;5;154mAuthors: \033[38;5;015m" + authors + "\n"
        maldb_banner += "\033[38;5;152m    |##XX:: :|\t\033[38;5;215mMaintained by: \033[38;5;015m" + ', '.join(maintainers) + "\n"
        maldb_banner += "\033[38;5;152m    |##XX:: :|\t\033[38;5;221mGithub: \033[38;5;015m" + giturl + "\n"
        maldb_banner += "\033[38;5;152m    |##,_,: :|\t\033[38;5;197mInstagram:\033[38;5;015m @termux_hacking\n"
        maldb_banner += "\033[38;5;152m    |./ T \.:|\n"
        maldb_banner += "    || o|o |:|\n"
        maldb_banner += "    ||  |  |:|\n"
        maldb_banner += "  .============.\n"
        maldb_banner += " .==============.\n"
        maldb_banner += ".================.\n\n"

    elif screen is 5:
        maldb_banner = "\n"
        maldb_banner += "\033[38;5;036m_______________________________________\n"
        maldb_banner += "|\ ___________________________________ /|\n"
        maldb_banner += "| | _                               _ | |\n"
        maldb_banner += "| |(+)        _           _        (+)| |\n"
        maldb_banner += "| | ~      _--/           \--_      ~ | |\n"
        maldb_banner += "| |       /  /             \  \       | |\n"
        maldb_banner += "| |      /  |               |  \      | |\n"
        maldb_banner += "| |     /   |               |   \     | |\n"
        maldb_banner += "| |     |   |    _______    |   |     | |\n"
        maldb_banner += "| |     |   |    \     /    |   |     | |\n"
        maldb_banner += "| |     \    \_   |   |   _/    /     | |\n"
        maldb_banner += "| |      \     -__|   |__-     /      | |\n"
        maldb_banner += "| |       \_                 _/       | |\n"
        maldb_banner += "| |         --__         __--         | |\n"
        maldb_banner += "| |             --|   |--             | |\n"
        maldb_banner += "| |               |   |               | |\n"
        maldb_banner += "| |                | |                | |\n"
        maldb_banner += "| |                 |                 | |\n"
        maldb_banner += "| |                                   | |\n"
        maldb_banner += "| |      \033[38;5;037m  P E S T I L E N C E \033[38;5;036m       | |\n"
        maldb_banner += "| |  \033[38;5;037m I S   G O O D   F O R   Y O U \033[38;5;036m  | |\n"
        maldb_banner += "| | _           \033[38;5;037m  %s \033[38;5;036m               | |\n\033[38;5;015m" % version
        maldb_banner += "\033[38;5;036m| |(+)                             (+)| |\n"
        maldb_banner += "| | ~                               ~ | |\n"
        maldb_banner += "|/ ----------------------------------- \|\n"
        maldb_banner += "---------------------------------------\n"
        maldb_banner += "\t\033[38;5;048mMaintained by:\033[38;5;015m %s\n" % ', '.join(maintainers)
        maldb_banner += "\t\033[38;5;118mGitURL:\033[38;5;015m %s\n" % giturl
        maldb_banner += "\t\033[38;5;154mAuthors:\033[38;5;015m %s\n" % authors
        maldb_banner += "\t\033[38;5;215mInstagram:\033[38;5;015m @termux_hacking\n"
