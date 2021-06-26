Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> E={0,1,2,3,4}
>>> N={2,4,5,6,8}
>>> E.union(N)
{0, 1, 2, 3, 4, 5, 6, 8}
>>> E.difference(N)
{0, 1, 3}
>>> E.intersection(N)
{2, 4}
>>> E.symmetric_difference(N)
{0, 1, 3, 5, 6, 8}
>>> 