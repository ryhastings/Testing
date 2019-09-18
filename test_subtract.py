import pytest

@pytest.mark.parametrize('a,b,expected',[
							(2,3,-1),
							(3,7,-4),
							(-2,5,-7),
							(5,5,0),
							(6,6,0)])

def test_subtract(a,b,expected):
	from subtract import subtract
	return subtract(a,b)
	assert result == expected