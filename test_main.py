from main import resultat

def tests_fn():
    assert resultat(132, "+", 314) == 446
    assert resultat(132, "+", 14) == 146
    assert resultat(12, "*", 3) == 36
    assert resultat(10, "*", 20) == 200
    assert resultat(42, "-", 22) == 20
    assert resultat(33, "-", 11) == 22
    assert resultat(66, "/", 6) == 11
    assert resultat(64, "/", 2) == 32