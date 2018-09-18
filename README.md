# RTR105
## Datormacības kursa elektroniskā klade ##  

   **2. nodarbības Linux komandas** 
   
* Ctrl+Alt+t - *termināla izsaukšana*   
* Ctrl+Shift+t - *atvērt terminalā jaunu lapu* 
* Tab(x2) - *visas komandas*    
* Ctrl+l - *attīrīt ekrānu*  
* uname - *informācija par OS*  
* man "komanda" - *komandas apraksts*  
* komanda -atslēga(uname -a) - *pilna informācija par OS* 
* echo $0 - *Shell valodas versija*  
* whoami - *lietotāja vārds*  
* who - *kādi lietotāji atrodas blakus*  
* Ctrl+Alt+F1 - *pieslēguma veidi (**F7** - grafisks interfeiss)*  
* pwd - *lietotaja atrašanas vieta(directory)*   
* ls - *objektu saraksts*  
* ls -l - *detalizēta informācija*   
* ls -la - *visu objektu saraksts*  
* history - *apskatīt komandu vēsturi*  
* history > history_date.txt - *saglabāt komandu vēsturi failā ar nosaukumu history_date*    

**3. nodarbības Linux komandas**

* cd Music - pārvietoties mapē *Music*  
* cd . - pārvietoties uz tekošo direktoriju (solis uz vietas)  
* cd .. - pārvietoties uz vienu līmēni augstāk (solis atpakaļ)  
* / - saknes apgabala direktorija (root) piemērs:cd /  
* cd /home/user/ - apgabals, uz kuru gribu doties  
* cd ~ relatīvais mājas apgabals  
* cd+Enter - ātri pārvietoties uz mājas apgabalu  
* mkdir ManaMape - izveidot mapi ar nosaukumu *ManaMape*  
* rmdir ManaMape - dzēst mapi ar nosaukumu *ManaMape*  
* rm -r - dzēst mapi ar visām apakšmapēm  
* echo "Teksts" - attēlot tekstu: "Teksts"  
* echo -e "Teksts\nTeksts\nTeksts" - \n pārvieto kursoru uz nakamo rindu   
* echo "Teksts" > fails1.txt - ievietot tekstu "Teksts" failā ar nosaukumu fails1.txt  
                             - ja tāda faila nebija, tas tiks izveidots  
                             - ja bija, tad fails tikd pārrakstīts  
* cat fails1.txt - apskatīt failu  
* more fails1.txt - apskatīt failu  
* less fails1.txt - apskatīt failu  
* echo "Papildus teksts" >> fails1.txt - papildināt failu ar tekstu   
* nano fails1.txt - atvērt failu teksta redaktorā. Saglabāt ar Crtl+X  
* chmod **540** fails1.txt - mainīt tiesības failam  
                  rwx rwx rwx  
                  101 100 000  
               **5**  \   **4**     **0**  
* echo "Teksts" > ../fails1.txt - ieraksīt tekstu failā, kas atrodas vienu direktoriju augstāk  
* cp fails1.txt fails101.txt - kopēt failu "fails1.txt" failā "fails101.txt"  
* mv \*1*.txt Music/ - pārvietot visus failus, kuri nosaukumā satur "1" uz mapi Music/  
* ls Music/ - pārādīt objektus, kas atrodas mape Music/  
* rm Music/fails101.txt - dzēst failu no mapes Music/  
* rm fails*.txt - dzēst visus failus, kuriem nosaukums sākas ar burtiem "fails..."  



