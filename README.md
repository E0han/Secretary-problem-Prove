# Secretary-problem-Prove
Use computer to prove whether the formula n/e works

The secretary problem is a famous problem that uses the optimal stopping theory. The problem has been studied extensively in the fields of applied probability, statistics, and decision theory. It is also known as the marriage problem, the sultan's dowry problem, the fussy suitor problem, the googol game, and the best choice problem.
The basic form of the problem is the following: imagine an administrator who wants to hire the best secretary out of 
**n** rankable applicants for a position. The applicants are interviewed one by one in random order. A decision about each particular applicant is to be made immediately after the interview. Once rejected, an applicant cannot be recalled. During the interview, the administrator can rank the applicant among all applicants interviewed so far, but is unaware of the quality of yet unseen applicants. The question is about the optimal strategy (stopping rule) to maximize the probability of selecting the best applicant. If the decision can be deferred to the end, this can be solved by the simple maximum selection algorithm of tracking the running maximum (and who achieved it), and selecting the overall maximum at the end. The difficulty is that the decision must be made immediately.
The problem has an elegant solution. The optimal stopping rule prescribes always rejecting the first **n/e** applicants after the interview (where e is the base of the natural logarithm) and then stopping at the first applicant who is better than every applicant interviewed so far (or continuing to the last applicant if this never occurs). 


This script use python3 verify how n/e works, you just need to input the total number of applications (or the other stuff) and it will run 100000 times with different arrangements, then generate a .svg document which shows the frequency of each rankable number be choosen. 

The extent library you need to `pip3 install` is pygal
This script is for my essay, Hope it would be helpful
