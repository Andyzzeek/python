def upravJmeno(upravene_jmeno):
    noveJmeno = upravene_jmeno.upper()
    noveJmeno2 = upravene_jmeno.lower()
    return noveJmeno, noveJmeno2
jmeno = input(str("jmeno:"))
print(  upravJmeno(jmeno)  )