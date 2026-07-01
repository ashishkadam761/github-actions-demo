from calculater import add

def test_add_positiuve_number():
    assert add(2,3)==5
    
def test_add_large_number():
    assert add(100,200)==300
    
def  test_add_zero():
    assert add(0,0)==0        