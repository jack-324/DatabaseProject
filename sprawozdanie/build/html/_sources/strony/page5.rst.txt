=========================
System praw dostępu
=========================

    System praw dostępu można rozszerzyć poprzez zastosowanie dodatkowych zabezpieczeń i mechanizmów

------------------------------------------------------------
Kontrola uprawnień użytkowników
------------------------------------------------------------

    Oprócz podziału na role, można szczegółowo kontrolować uprawnienia użytkowników do poszczególnych danych i funkcji systemu. Można określić, które konkretne operacje są dozwolone dla poszczególnych użytkowników lub grup.

------------------------------------------------------------
Autoryzacja dwuskładnikowa (2FA)
------------------------------------------------------------ 

    Wprowadzenie autoryzacji dwuskładnikowej dodaje dodatkową warstwę zabezpieczeń. Oprócz hasła, użytkownik musi potwierdzić swoją tożsamość za pomocą drugiego czynnika, na przykład kodu wysłanego na telefon komórkowy lub skanu odcisku palca.

------------------------------------------------------------
Monitorowanie i rejestracja aktywności użytkowników
------------------------------------------------------------

    System powinien być wyposażony w mechanizmy monitorujące i rejestrujące aktywność użytkowników. Dzienniki zdarzeń (logi) mogą być wykorzystywane do audytu, identyfikacji podejrzanej aktywności lub śladów naruszeń.

------------------------------------------------------------
Kontrola czasu dostępu
------------------------------------------------------------

    Można zastosować ograniczenia czasowe dotyczące dostępu do danych. Na przykład, niektórzy użytkownicy mogą mieć dostęp tylko w określonym czasie lub dniu tygodnia, a poza tym czasem są ograniczeni.

------------------------------------------------------------
Audytowanie i raportowanie
------------------------------------------------------------

 W celu zapewnienia przejrzystości i odpowiedzialności, warto rozważyć implementację funkcji audytowania i generowania raportów. Dzięki temu można śledzić, kto, kiedy i jak korzysta z danych oraz monitorować zgodność z politykami bezpieczeństwa.

------------------------------------------------------------
Użycie certyfikatów SSL/TLS
------------------------------------------------------------ 

    Jeśli dane są przesyłane przez sieć, należy skonfigurować zabezpieczone połączenie za pomocą certyfikatów SSL/TLS. Szyfrowanie danych w transporcie zapewnia poufność i integralność komunikacji.

------------------------------------------------------------
Ograniczenia geograficzne 
------------------------------------------------------------

    W niektórych przypadkach istnieje potrzeba kontrolowania dostępu do danych na podstawie lokalizacji geograficznej. Można zastosować mechanizmy, które sprawdzają, czy użytkownik ma dostęp tylko z określonych obszarów geograficznych.

------------------------------------------------------------
Monitorowanie zmian uprawnień
------------------------------------------------------------

    Warto monitorować i kontrolować zmiany w uprawnieniach użytkowników. Administracja systemu powinna posiadać odpowiednie mechanizmy, które śledzą i raportują o zmianach uprawnień w celu wykrywania potencjalnych działań nieautoryzowanych lub błędów.

------------------------------------------------------------
Wdrażanie polityk hasłowych
------------------------------------------------------------

    Opracowanie i egzekwowanie silnych polityk dotyczących haseł jest ważne. Wymuszanie silnych haseł, okresowe zmiany haseł i ograniczenia w liczbie nieudanych prób logowania mogą pomóc w zwiększeniu bezpieczeństwa systemu.
