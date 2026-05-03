# Umag tenisz szervezés

Az umagi nyaralás sava-borsa a teniszverseny, ami évről évre fejlődik a résztvevőkkel együtt.
Már tavaly is eszünkbe jutott, hogy hogyan lehetne még jobbá tenni, de az idő hiányában a hagyományos, ad-hoc jelleggel kialakult módszerekhez nyúlt vissza a szervezés annak minden előnyével és hátrányával együtt.

Ezért annak érdekében, hogy idén is sikerüljön megugrani a már eddig is magasra emelt lécet elkészítettük ezt a dokumentumot, hogy kikérhessük a közösség véleményét a verseny lebonyolításáról a párok összeállításától a győztes hirdetéséig.
A folyamat széleskörűbb egyeztetése átláthatóbbá teszi a rendszert, kiemel rejtett igényeket, amik eddig nem kaptak érvényt, ezáltal igazságosabbá, izgalmasabbá és élvezetesebbé teszi a versenyt.

Azzal az alap feltevéssel élünk, hogy körülbelül 5-6 napon keresztül három pályán egy délelőtti és egy délutáni két órás sávban zajlanak a hivatalos meccsek, ez összessen 30-36 meccset jelent, azaz minden párosra teljesítménytől függően 5-7-et. A továbbiakban a fő kérdések mentén felvázoljuk a lehetőségeket és azok életszerű kombinációt, majd egy szavazással lehet véleményt és igényt nyílvánítani.

## Párok összeállítása

Az egész verseny kardinális kérdése és megalapozója, hogy ki-kivel van párban, ezért fontos, hogy a lehető legtöbbet hozzuk ki a lehetőségeinkből. Adottság, hogy a társaság nagyon színes és hatalmas skálán mozog a tenisz képességek terén, ezért különös kihívás olyan rendszert alkotni, ami igazságos, átlátható és izgalmas, jó párosításokat eredményez.

### A.) Legyenek fix párok?

A1 - Igen.)

Előnyök:
- A verseny egyik fő eleme a csapatszellem és az csapatösszhang, ami így kap teret igazán. Az összeszokás az egyik fő fejlődési pontja egy párosnak és a tenisz páros a szinglivel ellentétben nem egyéni sport
- Komolyabban vehető és nagyobb a súlya egy-egy meccsnek

Hátrányok:
- A párosítások véglegesek, ezért egy rosszul, vagy túl jól sikerült párosítás rányomja a bélyegét az egész versenyre

A2 - Nem.)

Előnyök:
- A párok ideiglenesek, ezért sok emberrel "ki lehet próbálni" az együtt játszást
- Egy túl erős vagy túl gyenge párosítás nem jár súlyos következményekkel

Hátrányok:
- Egyéni verseny lenne, ezért nem alakulna ki meccseken átívelő összetartás egy csapaton belül

### B.) Mi alapján legyenek a párok összerakva?

B1 - Areiosz Pagosz, a vének tanácsa

Eddig ez volt az alkalmazott módszer. Néhány kiválasztott végtelen jószándékkal önkényesen meghatározott egy ordinális sorrendet és igyekezett hasonló erejű játékosokat összepárosítani, figyelembe venni, hogy ki kivel és kivel nem szeretne együtt lenni.
A döntéshez felhasználta az összes szubjektív megérzést ami létezik és összehasonlításokat végzett ezek alapján, amíg kialakult a legkevesebb elégedetlenséget kiváltó felállás.
Ennek a módszernek az előnye az, hogy bizonyítottan működik, viszont 10 páros összeállításánál a (2n)!/(2^n*n!) képlet alapján 20!/(2^10*10!), azaz 654'729'075 lehetséges párosítás létezik, 24 embernél 316'234'143'225.
Ezáltal különös kihívás levezetni a párosítással elégedetlen versenyzőknek, hogy a több százmillió vagy esetleg milliárd lehetőség közül miért pont erre esett a választás és miért nem egy másikra, illetve valószínűtlen, hogy a legjobb megoldás került kiválasztásra.

B2 - Sorsolás

B2a - Egykalapos sorsolás

Igazságos módszer, viszont az így keletkező párok a legkisebb valószínűséggel lesznek kiegyenlítettek.
Két gyengébb játékos nem biztos, hogy annyira élvezné a versenyt együtt, de ha a két legerősebb összekerül lehet nekik is hiányozna a kihívás.

B2b - Kétkalapos sorsolás (vegyes)

A versenyzőket egy erős és még erősebb csoportba osztályozzuk, önbevallás/csoportos szavazás/önkény alapján és a páros úgy jön létre, hogy mindkét csapatból kiválasztunk egy-egy résztvevőt.
Az így létrejövő párosok kiegyenlítettebbek, de szintén valószínűtlen az optimális megoldás feltéve ha cél, hogy minél kiegyenlítettebb legyen a verseny.

B2c - Kétkalapos sorsolás (kalapon belül)

A versenyzőket az előző módon kétfelé osztjuk, viszont a párosok úgy születnek, hogy a kalapon belül választunk párt, így létrejön egy erős csoport az első kalapból és egy még erősebb a másodikból. Így a csoporton belül kiegyenlített párosítások vannak és izgalmas meccsek lesznek, két csoport segítségével könnyebb a csoporton belüli különbségeket minimalizálni mint egy csoporton belül.

B3 - Adat alapú párosítás

Az Areiosz Pagosz módszerből kiemelnénk a felhalmozott bölcsességet és felhatalmaznánk a közösséget, közösen mérjék fel az erőviszonyokat.
Így a lehető legtöbb helyről érkezik információ, azok, akik egymással gyakran játszanak viszonylag reális képet tudnak adni a másik játékosról és össze tudják őket hasonlítani. És  minél nagyobb a részvétel, annál pontosabb képet kapunk. Az értékelések nyilvánosak, de az értékelő személye rejtett (szervezők számára ismert) és kompenzálunk az ellen, hogy senki ne szenvedjen hátrányos megkülönböztetést saját magától így egy viszonylag transzparens képet kapunk a mezőnyről a párok összeállításához.
Ezt követően egy programmal optimális megoldást keresünk arra a problémára, hogy minél kisebb legyen a csoporton (vagy két csoporton) belüli erőkülönbség.

B3a - Közösségi ordinális sorrendállítás

Legegyszerűbb módszer, mindenki felállít egy sorrendet az általa ismert játékosokról (magát leszámítva) és ezeket összesítjük.
Ez a módszer nem ad képet arról, hogy két hely között is lehet akkora erőkülönbség mint 4-5 között, akik viszonylag hasonló szinten vannak.

B3b - Közösségi sorrendállítás Élő pontrendszerrel

Azokat a játékosokat hasonlíttatjuk össze egy programmal, akiket a szavazó ismer (Ki nyerne? Aladár vagy Béla - döntetlen megengedett).
Így kialakul egy árnyaltabb rendszer rejtett Élő pontokkal (mindenkinek kérés szerint eláruljuk a sajátját), így nem csak egy egyszerű sorrend áll fel, de az erőkülönbségeket is viszonylag jól méri ezáltal pontosabb eredményt kapunk.

**Kitérő:** Mi is az az Élő pont?
Az 1960-as években Élő Árpád találta ki arra a problémára, hogy hogyan állítsanak fel egy rangsort a sakkozók között.
A Ea=1/(1+10^((Rb-Ra)/400), képletben, ahol:
- Ea a várható értéke a mérkőzésnek (0 - biztos vereség, 1 - biztos győzelem, 0,34 - 34%-os győzelem)
- Rb "B" játékos értékelése (Élő pontja)
- Ra "A" játékos értékelése
- 400 egy skálázási döntés, 400 pont különbség azt jelenti, hogy az erősebb játékos 10-ből 9-szer legyőzi a gyengébbet, 200 pont 76% és 0 pont 50%

A mérkőzés kimenetele után módosulnak a pontok:

Ra'=Ra+K*(Sa-Ea), ahol
- Ra' "A" játékos új értékelése
- Ra "A" játékos mérkőzés előtti értékelése
- K az egy faktor ami azt kontrolállja, hogy milyen gyorsan változik az értékelés, nagyobb K-t ismeretlen játékosoknál érdemes használni, hogy gyorsabban beálljon a valósághoz közeli értékelés, kisebbet pedig akkor, amikor már ismert és "be van kalibrálva" így egy rossz meccs nem fogja nagyon lerontani, de sok eredmény így is változtat
- Sa a meccs kimenetele (1-győzelem, 0-vereség, 0,5-döntetlen)

Példával: ...

Azért jó, mert nem kell felállítani egy abszolút mércét és ahhoz mérni mindenkit, mert elég egyszerű összehasonlításokat végezni és a sorrend kialakul magától az erőviszonnyal együtt.
Nem csak a sakkban használják, de szinte az összes sportban, sportfogadásoknál, kompetitív videojátékoknál, társkereső alkalmazásokban, bor értékeléseknél, zene ajánló rendszerekben, szinte mindenhol, ahol nehéz egy abszolút értékelést felállítani, de az összehasonlítás lehetséges.

B3c - Közösségi sorrendállítás képlettel és képesség pontozással



B3d - Közösségi sorrendállítás képlettel és képesség Élő pontrendszerrel

## Verseny lebonyolítása

### X.) Milyen legyen a meccsek lebonyolítása?

X1 - Két csoport, csoportmeccsek, elődöntők, döntő

Ez a megszokott, jól bevált módszer, matematikailag is kedvező, hiszen 10-12 csapat esetén ez két 5-6 fős csoportot jelent, ami 2*(n*(n-1))/2 meccs, ami n=5-nél 20, n=6-nál 30 meccs, ami a verseny lebonyolításához felhasználható kerethez jól igazodik.
Előnye, hogy jól tervezhető, ez szempont lehet ha valaki egy egész napos programot szeretne szervezni a pihenőnapjára (ami előfordulhat).

X2 - Egy nagy csoport

Abban az esetben, ha minden páros minden párossal játszana 10 páros esetén 45, 11 esetén 55, 12 esetén 66 csoportmeccs lenne, ez csak úgy lenne lehetséges, ha egy meccs nem két nyert hagyományos szett lenne, hanem vagy rövidített szettek, vagy egy nyert szett. Ez dupla adminisztrációt, rengeteg cserét, csúszást, kiszámíthatatlanságot jelent, illetve a tenisz hullámvölgyeihez sem annyira jól alkalmazkodik, ezért csak akkor jó választás, ha a mindenki-mindenkivel mérkőzik elv felülírja a felsorolt hátrányokat.

X3 - Svájci

Svájci módszer az 1985-ös Zürich-i sakkversenyből származik, a lényege, hogy körök vannak és minden körben olyan versenyzőket/párokat sorsol össze, akiknek hasonló eredményekkel rendelkeznek.
Az első körben a párosítások véletlenszerűek majd a második körben az első kör győztesei az első kör többi győztesével játszik, a vesztesek a vesztesekkel.
A harmadik körben a 2-0, 1-1 és 0-2 mérlegűek játszanak egymással.
Páratlan szám esetén egy valaki kimarad, ilyenkor plusz fél vagy plusz egy pontot kap, alapelv, hogy az egész verseny alatt ne forduljon elő, hogy egy valaki kétszer is kimaradjon egy körből.
A svájci módszer log2(n) kör alapján tud győztest hirdetni és egy rangsort felállítani, az önszervezés miatt ugyan nem játszik mindenki mindenkivel, viszont egy idő után hasonló erejű párosok mérkőznek, ami jó meccseket eredményez.
12 csapatnál a log2(12)=~3,58 azaz 4 kör alatt már felállna egy sorrend, ez 4*6 meccs, azaz 24.
Ez benne van a keretben és nincs rá ok, hogy miért ne lehetne 5. kört csinálni, az pont 30. (10 csapatnál log2(10)=3,32 tehát szintén 4 kör a minimum, de akár 5-6 is belefér a keretbe 4->20 5->25 6->30 meccs)
A csoportos körmérkőzésekkel szemben viszont ez nem, vagy nehezebben tervezhető, hiszen a párosítások dinamikusan alakulnak.
Egy kör egy napot jelent 2\*3=6 meccs, azaz a másnap párosításai a délutáni meccsek eredményeitől is függnek.

X4 - Americano

Az americano lényege, hogy rövid meccsekről van szó (egy szett, vagy 20 perc) és egy előre meghatározott sorrend szerint cserélődnek a párok és a győzelmeket számolják.
Ezt csináltuk tavaly az első/utolsó nap bemelegítő és levezető kupáján, de a párokat is cserélgettük.

X5 - Mexikói

Ugyanaz, mint az americano, azzal a különbséggel, hogy a meccs párosítások nem egy fix sorrend szerint, hanem svájci módszerrel történnek.

### C.) Legyen egy erősebb és egy gyengébb csoport?
C1 - Igen
C2 - Ne

Főleg akkor releváns, ha a két csoporton belüli csoportmeccsekre, elődöntőkre, döntő-re esett a választás (B1).
Előnye, hogy hasonló képességű párok mérkőznek egymással a csoportmeccseken belül és minden csapatnak van esélye a győzelemre és a dobogóra,
ha az elődöntő és a döntő a két csapat első két-két párosát méri össze. 