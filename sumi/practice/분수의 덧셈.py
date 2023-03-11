from fractions import Fraction

# Fraction : 기약분수를 만드는 모듈
# 첫번째 인자에 분자, 두번째 인자에 분모
def solution(numer1, denom1, numer2, denom2):
    answer = []
    bottom = denom1 * denom2
    top = numer1 * denom2 + numer2 * denom1

    res = Fraction(top, bottom)
    # numerator 는 분자 denominator는 분모이다.
    return [res.numerator, res.denominator]
