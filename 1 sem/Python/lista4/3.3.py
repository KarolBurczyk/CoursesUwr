def usun_w_nawiasach(s):
    k=1
    for i in range(len(s)):
        if s[i]=='(':
            k=0
        elif s[i]==')':
            k=1
        elif k==1:
            print(s[i], end="")
    print()

usun_w_nawiasach("Ala ma kota (perskiego)!")
usun_w_nawiasach("Ala (ma kota) (perskiego)!")
usun_w_nawiasach("(Ala ma kota perskiego)!")