# Armstrong numbers
Implementation of the Armstrong numbers (https://en.wikipedia.org/wiki/Narcissistic_number) search algorithm on Python.

The number S consists of M digits, for example, S = 370 and M (number of digits) = 3.
It is necessary to implement the logic of the method, which must be among natural numbers less than N (int64) to find all numbers,
satisfying the following criterion:
the number S is equal to the sum of its digits raised to the power of M. The program must return all such numbers in ascending order.

Example of the number:
370 = 3 * 3 * 3 + 7 * 7 * 7 + 0 * 0 * 0
8208 = 8 * 8 * 8 * 8 + 2 * 2 * 2 * 2 + 0 * 0 * 0 * 0 + 8 * 8 * 8 * 8
The execution time must not be more than 10 seconds.

### Run the program:
```
python ArmstrongNumbers.py
```

#### Output:
```
1. 1
2. 2
3. 3
4. 4
5. 5
6. 6
7. 7
8. 8
9. 9
10. 153
11. 370
12. 371
13. 407
14. 1634
15. 8208
16. 9474
17. 54748
18. 92727
19. 93084
20. 548834
21. 1741725
22. 4210818
23. 9800817
24. 9926315
25. 24678050
26. 24678051
27. 88593477
28. 146511208
29. 472335975
30. 534494836
31. 912985153

Execution time: 1.076 seconds
```

The full list of the numbers is here: http://mathworld.wolfram.com/NarcissisticNumber.html
