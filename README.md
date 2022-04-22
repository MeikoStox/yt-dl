
# Installazione 

- Installare i requirement, nel caso in cui "pip" sia installato


    pip install -r requirements.txt


> Nel caso in cui il comando non dovesse funzionare bisognerà installare pip (versione 3) per il pc
> > Per macOS provare a guardare <a>https://phoenixnap.com/kb/install-pip-mac</a>

Potrebbero esserci dei bug relativi alla libreria "pafy" che cercherà di accedere a una chiave "dislike"
dei video. Siccome Youtube ha nascosto il numero di non mi piace questa cosa potrebbe causare errore. 

Per risolvere il problema bisogna modificare il file di libreria 

>backend_youtube_dl.py

Che si può trovare alla seguente PATH su sistemi UNIX

> /usr/local/lib/python3.x/dist-packages/pafy/backend_youtube_dl.py

Modificare la riga 54

>self._dislikes = self._ydl_info['dislike_count']

E scriverla così

>self._dislikes = 10

Salvare il file e avremo terminato.

# Lanciare il programma

    python download_music.py

# Inserimento canzoni

Nel caso in cui sia presente un file chiamato "input.txt" il programma lo aprirà e scaricherà le canzoni
presenti su quel file. Esempio file "input.txt":

    OcularNebula Stay Inside Me
    Remmy annegare
    Killer Queen Queen

Nel caso in cui non esista alcun file chiamato "input.txt" il programma chiederà un'elenco di canzoni, inserire
il carattere "-1" per terminare l'inserimento. Esempio di inserimento di seguito:

    -->OcularNebula Stay Inside Me
    -->Remmy annegare
    -->Killer Queen Queen    
    -->-1

I due formati sono equivalenti.

# Selezione modalità

Una volta inserite le canzoni da scaricare, procedere con la selezione della modalità. 

Ne sono disponibili due:
- Modalità Automatica [A]
- Modalità Manuale [M]

Si noti che il programma **non** è case sensitive, di conseguenza le lettere possono essere inserite sia in minuscolo che maiuscolo.

## Modalità Automatica

Nel caso in cui si decida di utilizzare la modalità automatica il programma scaricherà il primo risultato che viene mostrato da youtube
quando si cerca la riga inserita in input.

Nel caso precedente il programma inizierà con la prima riga e cercherà

    OcularNebula Stay Inside Me

E scaricherà il primo risultato che verrà mostrato su youtube cercando "*OcularNebula Stay Inside Me*"

Il file verrà scaricato nella migliore qualità audio disponibile.

## Modalità Manuale

Nel caso in cui si decida di utilizzare la modalità manuale per ogni riga inserita in input, il programma chiederà
quale dei risultati scaricare. Verranno mostrati 5 risultati e per ogni risultato verrà indicata la durata.

Nel caso precedente il programma inizierà con la prima riga e cercherà

    OcularNebula Stay Inside Me

Il risultato che verrà prodotto sarà

>
>[1] Stay Inside Me Durata: 4:08
>
>[2] Stay Inside Me - Geometry Dash Version (10 min) Durata: 10:32
>
>[3] 1 Hour Stay Inside Me - OcularNebula | Koopa 85 Durata: 1:01:56
>
>[4] Geometry Dash - Practice Mode - Stay Inside Me - Soundtrack Durata: 1:46
>
>[5] OcularNebula - Stay Inside Me (8D Audio) Durata: 4:09
>
>[!] Inserire l'id della canzone da scaricare
>

Per decidere quale canzone scaricare basterà inserire il numero fra quadre corrispondente.

## Fine del processo

Una volta che verranno selezionate le varie canzoni il programma le scaricherà automaticamente nella directory
dove è contenuto il file


