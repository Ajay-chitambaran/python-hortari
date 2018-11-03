# python-hortari
python_workshop31/10/2018
psychometric test @ newpsycho.py
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







