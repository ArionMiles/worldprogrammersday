# Recursive Digit Sum

## HINT:
[Digital Root of a Number](https://www.hitbullseye.com/Quant/Digital-Root-or-Seed-Number.php)

## Problem
We define super digit of an integer `x` using the following rules:

Given an integer, we need to find the _super digit_ of the integer.

- If `x` has only 1 digit, then its super digit is `x`.
- Otherwise, the super digit of `x` is equal to the super digit of the sum of the digits of `x`.

For example, the super digit of  will be calculated as:
```
	super_digit(9875)   	9+8+7+5 = 29 
	super_digit(29) 	    2 + 9 = 11
	super_digit(11)		    1 + 1 = 2
	super_digit(2)		    = 2  
```

You are given two numbers `n` and `k`. The number `p` is created by concatenating the string `n` `k` times. Continuing the above example where `n = 9875`, assume your value `k = 4`. Your initial `p = 9875 9875 9875 9875` (spaces added for clarity).

```
superDigit(p) = superDigit(9875987598759875)
                  5+7+8+9+5+7+8+9+5+7+8+9+5+7+8+9 = 116
superDigit(p) = superDigit(116)
                  1+1+6 = 8
superDigit(p) = superDigit(8)
```

All of the digits of `p` sum to `116`. The digits of `116` sum to 8. 8 is only one digit, so it's the super digit.

### Function Description
Complete the function _superDigit_ in the editor below. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):

- n: a string representation of an integer
- k: an integer, the times to concatenate `n` to make `p`

## Input Format
The first line contains two space separated integers, `n` and `k`.

## Constraints
- 1<= n <= 10<sup>100000</sup>
- 1<= k <= 10<sup>5</sup>

## Output Format
Return the super digit of `p`, where `p` is created as described above.

## Sample Input 0
```
148 3
```

## Sample Output 0
```
3
```

## Explanation 0
Here `n= 148` and `k = 3`, so `P = 148148148`.

```

super_digit(P) = super_digit(148148148) 
               = super_digit(1+4+8+1+4+8+1+4+8)
               = super_digit(39)
               = super_digit(3+9)
               = super_digit(12)
               = super_digit(1+2)
               = super_digit(3)
               = 3.
```
