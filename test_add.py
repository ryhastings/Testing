import pytest

@pytest.mark.parametrize('a,b,expected',[
							(2,3,5),
							(3,7,10),
							(-2,5,3),
							(.1,.2,.3)])

def test_add(a,b,expected):
	from mycode import add
	return add(a,b)
	expected = 5
	assert result == pytest.approx(expected)