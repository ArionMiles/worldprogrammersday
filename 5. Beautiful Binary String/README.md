# Beautiful Binary String

## Problem
Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring `"010"`.

In one step, Alice can change a 0 to a 1 or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

For example, if Alice's string is `b = 010` she can change any one element and have a beautiful string.

### Function Description

Complete the _beautifulBinaryString_ function in the editor below. It should return an integer representing the minimum moves required.

beautifulBinaryString has the following parameter(s):

 - _b_: a string of binary digits

## Input Format
The first line contains an integer `n`, the length of binary string.
The second line contains a single binary string `b`.

## Constraints
- 1<= n <= 100
- b[i] ∈ {0, 1}

## Output Format
Print the minimum number of steps needed to make the string beautiful.

## Sample Input 0
```
7
0101010
```

## Sample Output 0
```
2
```

## Explanation 0
Because we were able to make the string beautiful by changing 2 characters (`b[2]` and `b[5]`), we print 2.

## Sample Input 1
```
5
01100
```

## Sample Output 1
```
0
```

## Explanation 1
The substring `"010"` does not occur in `b`, so the string is already beautiful and we print 0.