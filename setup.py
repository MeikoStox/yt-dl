import os
import pafy
	
print("""
      _____        ___                    _                 _           
/\_/\/__   \      /   \_____      ___ __ | | __ _  ___   __| | ___ _ __ 
\_ _/  / /\/____ / /\ / _ \ \ /\ / / '_ \| |/ _` |/ _ \ / _` |/ _ \ '__|
 / \  / / |_____/ /_// (_) \ V  V /| | | | | (_| | (_) | (_| |  __/ |   
 \_/  \/       /___,' \___/ \_/\_/ |_| |_|_|\__,_|\___/ \__,_|\___|_|   

""")


path = os.path.dirname(pafy.__file__)


print( """
[+] FILE backend_youtube_dl.py TROVATO SULLA PATH: """ + path + """
""")

with open( path+"/backend_youtube_dl.py" ) as fin:
	lines = fin.readlines()

with open( "./patch/backend_youtube_dl.py" ) as fin:
	lines_patch = fin.readlines()


print( """
[+] FILE backend_youtube_dl.py LETTO CON SUCCESSO
""")


with open ( "backup.py", "w" ) as fout:
	for line in lines:
		fout.write(line) 

print( """
[+] COPIA DI BACKUP CREATA

[+] PATCHO IL FILE backend_youtube_dl.py
""")

with open ( path+"/backend_youtube_dl.py" , "w" ) as fout:
	for line in lines_patch:
		fout.write(line) 

print("""
[+] PATCH INSTALLATA CON SUCCESSO
""")

