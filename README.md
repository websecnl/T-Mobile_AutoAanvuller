# T-Mobile_AutoAanvuller
Automatisch Aanvuller van T-Mobile Onbeperkt MB's , zodra data onder 300MB komt voegt hij gratis 1GB toe.

# Instructie
vervang alle waardes met 'XXXXXX' in de .py bestand met uw waardes.
- Cookie Waardes
- Token Waarde
- Uw telefoon nummer
- Klant nummer
- ID nummer

om dit te vinden moet de request onderschept worden van de T-Mobile App, dit kan u doen door middel van BlueStacks verkeer te onderscheppen met Burp Suite en op BlueStacks de Burp Certificaat te installeren middels de app 'Root Certificate Manager', de BlueStacks omgeving moet wel geroot zijn dus dit moet ook gebeuren.
Vervolgends dient u ProxyCap te installeren en de burp proxy in te stellen in ProxyCap met rules voor programmas Bluestacks.exe , HD-Agent.exe en HD-Player.exe op port 443 en 80.
Daarna installeert u de T-Mobile app op BlueStacks, logd u in met uw mobiele nummer en onderschept u de verzoek (request) om 1GB toe te voegen (hiervoor moet u op de Top Up knop klikken in de T-Mobile app). als Burp Suite de request onderschept dan zult u daarin vrijwel alle waardes vinden dat u nodig heeft om dit script te laten werken.
