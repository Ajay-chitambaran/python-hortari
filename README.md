# python-hortari
python_workshop31/10/2018
psychometric test-Ajay @ newpsycho.py
Q-1012 -Holes in a Number @hole.py
Q1013-modifyprice @alex.py
Q1014-@pangrams.py
----------------------psychometry--------------------------------------
Psychometric testing is designed to find job-relevant information about
an applicant that the traditional interview process would not uncover. It
typically includes a combination of online aptitude and personality tests
that measure cognitive ability and personality traits.

A company has psychometric scores for n candidates, and it will only
extend job offers to candidates with scores in the inclusive range given
by [lowerLimit, upperLimit]. Given the list of scores and a sequence of
score ranges, determine how many candidates the company will extend
offers to for each range of scores. For example, if the scores are scores
= [1,2,2,3,4] and the limits are 2 and 4, there are 4 candidates, i.e. those
with scores [2,2,3,4] that match the conditions.

*Input Format*
The first line contains an integer, n, that denotes the number of
elements in scores.
Each line j of the n subsequent lines (where 0 ≤ j < n) contains an
integer that describes scores[j].
The next line contains an integer, q, that denotes the number of
elements in lowerLimits.
Each line i of the q subsequent lines (where 0 ≤ i < q) contains an
integer that describes lowerLimits[i].
The next line contains an integer, q, that denotes the number of
elements in lowerLimits.
Each line i of the q subsequent lines (where 0 ≤ i < q) contains an
integer that describes upperLimits[i].

*Sample Input*

```5
1
3
5
6
8
1
2
1
6```

*Sample Output*

```3```
----------------------------------------------------------------------------------

*Q-1012 -> Holes in a Number* @hole.py

You are designing a poster which prints out numbers with a unique style
applied to each of them. The styling is based on the number of closed
paths or holes present in a given number.

The number of holes that each of the digits from 0 to 9 have are equal to
the number of closed paths in the digit. Their values are:
1, 2, 3, 5, and 7 = 0 holes.
0, 4, 6, and 9 = 1 hole.
8 = 2 holes.

Given a number, you must determine the sum of the number of holes for
all of its digits. For example, the number 819 has 3 holes.

*Input Format*
There is one line of text containing a single integer num, the value to
process.

*Sample Input*
```630```

*Sample Output*
```2```
----------------------------------------------------------------------------
1013-modifyprice @alex.py

Michael is a shop owner who keeps a list of the name and sale price for each item in the store's inventory. At each sale, his employees record the name and sale price of each item sold. Michael suspects his manager, Alex, of embezzling money by modifying the sale price of some of the items. Write a program that finds the number of times Alex recorded an incorrect sale price.

*Function Description*

Write the function 'verifyItems'. The function must return an integer denoting the number of sale prices incorrectly recorded by Alex.

*verifyItems has the following parameter(s):*
origItems[origItems[0],...origItems[n-1]]: an array of n strings, where
each origItems[i] is the name of an item in inventory
origPrices[origPrices[0],...origPrices[n-1]]: an array of n floating point
numbers, where each origPrices[i] is the price of origItems[i]
items[items[0],...items[m-1]]: an array of m strings containing the
name of each item[j] sold by Alex
prices[prices[0],...prices[m-1]]: An array of floating-point numbers,
where each prices[j] contains the sale price recorded by Alex for items[j].

*Input Format*
The first line contains an integer n, denoting the size of the origItems
array.
The next n lines each contain an element origItems[i].
The next line contains an integer n, denoting the size of the origPrices
array.
The next n lines each contain an element origPrices[i].
The next line contains an integer m, denoting the size of the items
array.
The next m lines each contain an element items[j].
The next line contains an integer, m, the size of the prices array.
The next m lines each contain an element prices[j].

*Sample Input*
```4
rice
sugar
wheat
cheese
4
16.89
56.92
20.89
345.99
2
rice
cheese
2
18.99
400.89
*Sample Output*
 2 
 -------------------------------------------------------
Q1014-pangrams
A pangram is a word or sentence that contains every letter of the alphabet. For example: the quick brown fox jumps over the lazy dog. Nicole wants to improve her typing speed for programming contests, and she thinks that practicing typing pangrams is the best way to do it.
Given a list of strings made of lowercase letters in the range ascii[a-z], determine whether or not they are pangrams.

*Function Description*
Complete the function isPangram in the editor below. The function must return a string where each position represents the results of your test. Use a '1' to represent true, '0' for false.

is Pangram has the following parameter(s)
: strings[strings[0],...strings[n-1]]: an array of strings to test

*Input Format*
Input from stdin will be processed as follows and passed to the function.
The first line contains an integer n, the size of the array strings.
The next n lines each contain an element strings[i] where 0 ≤ i < n.

*Sample Input*
```4
we promptly judged antique ivory buckles for the
next prize
we promptly judged antique ivory buckles for the
prizes
the quick brown fox jumps over the lazy dog
the quick brown fox jump over the lazy dog```

*Sample Output*
```1010```

*Explanation*
```strings[0] = we promptly judged antique ivory
buckles for the next prize = True
strings[1] = we promptly judged antique ivory
buckles for the prizes = False
strings[2] = the quick brown fox jumps over the
lazy dog = True
strings[3] = the quick brown fox jump over the
lazy dog = False```
Only strings[0] and strings[2] are pangrams.
