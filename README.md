# Crypto Solvers
This is a command line tool I developed to help solve common cryptology problems. This tool is different from other online calculators becasue it prints
out all intermediate steps of the problem. This output for all of my programs is given in LaTex format. This program was designed to assist me in 
my MATH 5284 class at the university of Minnesota. 

## Usage
Launch the `crypto-solver.py` file to launch the command line interface. From there it will explain how to do various actions.

## Problems it can solve

`[GCD]` = Extended Euclidean Algorithm, given two numbers `a` and `b` it will solve the following equation: `au+bv = gcd(a, b)`.
<br>
`[Fast Powering]` = Fast powering algorithm. Given three numbers `g`, `x`, and `p` it will perform a fast powering algorithm to square potentially really large numbers effecitnaly. `g^x(mod p)`.
<br>
`[Is Prime]` = A brute force prime checking algorithm. Given an input `p` will check if `p` is divisbile by every integar `0 < n < sqrt(p)`.
<br>
`[CRT]` = Chinese remainder theorem. Given a list of congruence systems will solve the system. 
<br>
`[SHANKS]` = Shank's Giant step Baby step algorithm. Will perform shank's algorithm to solve the discrete log problem for primes.
<br>
`[POHLIG]` = Pohlig-Hellman algorithm to solve discrete log problem for non primes. 
<br>
`[MILLER-RABIN]` = Miller rabin test. Given a number and a witness will check if that witness is indeed a miller rabin witness.
