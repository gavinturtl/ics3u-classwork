
def test_make_abba():
    assert make_abba('Hi', 'Bye') == "HiByeByeHi"
    assert make_abba('Yo', 'Alice') == "YoAliceAliceYo'"
    assert make_abba('What', 'Up') == 'WhatUpUpWhat'
    assert make_abba('aaa', 'bbb') == 'aaabbbbbbaaa'
    assert make_abba('x', 'y') == 'xyyx'
    assert make_abba('x', '') == 'xx'
    assert make_abba('', 'y') == 'yy'
    assert make_abba('Bo', 'Ya') == 'BoYaYaBo'
    assert make_abba('Ya', 'Ya') == 'YaYaYaYa'

def test_make_tags():
    assert make_tags('i', 'Yay') == '<i>Yay</i>'
    assert make_tags('i', 'Hello') == '<i>Hello</i>'
    assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'
    assert make_tags('address', 'here') == '<address>here</address>'
    assert make_tags('body', 'Heart') == '<body>Heart</body>'
    assert make_tags('i', 'i') == '<i>i</i>'
    assert make_tags('i', '') == '<i></i>'

def test_common_end():
    assert common_end([1, 2, 3], [7, 3]) == True
    assert common_end([1, 2, 3], [7, 3, 2]) == False
    assert common_end([1, 2, 3], [1, 3]) == True
    assert common_end([1, 2, 3], [1]) == True
    assert common_end([1, 2, 3], [2]) == False

def test_parrot_trouble():
    assert parrot_trouble(True, 6) == True
    assert parrot_trouble(True, 7) == False
    assert parrot_trouble(False, 6) == False
    assert parrot_trouble(True, 21) == True
    assert parrot_trouble(False, 21) == False
    assert parrot_trouble(False, 20) == False
    assert parrot_trouble(True, 23) == True
    assert parrot_trouble(False, 23) == False
    assert parrot_trouble(True, 20) == False
    assert parrot_trouble(False, 12) == False

def test_squirrel_play():
    assert squirrel_play(70, False) == True
    assert squirrel_play(95, False) == False
    assert squirrel_play(95, True) == True
    assert squirrel_play(90, False) == True
    assert squirrel_play(90, True) == True
    assert squirrel_play(50, False) == False
    assert squirrel_play(50, True) == False
    assert squirrel_play(100, False) == False
    assert squirrel_play(100, True) == True	
    assert squirrel_play(105, True) == False
    assert squirrel_play(59, False) == False
    assert squirrel_play(59, True) == False
    assert squirrel_play(60, False) == True
