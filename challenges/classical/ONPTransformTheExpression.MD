# ONP - Transform the Expression
<p align="center"> #stack </p>
Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation). Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ). Operands: only letters: a,b,...,z. Assume that there is only one RPN form (no expressions like a*b*c).

## Input

- t [the number of expressions <= 100]
- expression [length <= 400]
- [other expressions]
- Text grouped in [ ] does not appear in the input file.

## Output

The expressions in RPN form, one per line.
Example

### Input:
```shell
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))
```

### Output:
```shell
abc*+
ab+zx+*
at+bac++cd+^*
 Submit solution!
```
