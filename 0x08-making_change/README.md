
# 0x08-making_change

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#0x08-making_change)

# Coin Change Problem

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#coin-change-problem)

## Problem Description

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#problem-description)

The goal of this project is to determine the fewest number of coins needed to meet a given amount (`total`) using a set of coin denominations (`coins`). If it is not possible to make the exact  `total`, the function returns  `-1`.

This problem is commonly referred to as the  **coin change problem**, and it is an example of an optimization problem, where the objective is to minimize the number of coins used to make the total.

## Code Explanation

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#code-explanation)

The code contains the function  `makeChange(coins, total)`, which calculates the minimum number of coins required to make up the  `total`.

### Function Definition

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#function-definition)

def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given amount."""

### Parameters:

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#parameters)

-   `coins`: A list of coin denominations available (e.g.,  `[1, 2, 5]`).
-   `total`: The target amount to be made using the coins.

### Return:

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#return)

-   Returns the minimum number of coins needed to make the total.
-   Returns  `-1`  if it is not possible to make the exact total with the available coins.

### Function Logic:

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#function-logic)

1.  **Base Case**:
    
    -   If  `total`  is less than or equal to 0, return  `0`  because no coins are needed.
2.  **Sort Coins**:
    
    -   The  `coins`  list is sorted in descending order. This helps prioritize using the largest coin denominations first, minimizing the number of coins.
3.  **Greedy Approach**:
    
    -   The code uses a greedy approach, where it attempts to subtract the largest possible coin denomination from the total as many times as possible.
4.  **Adjustment if Solution Fails**:
    
    -   If the current set of coins fails to produce the exact total, the largest coin is removed, and the process is repeated.
5.  **Return Results**:
    
    -   The function returns the number of coins used if the total can be made, or  `-1`  if no valid solution exists.

## Examples

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#examples)

### Example 1:

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#example-1)

coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3

In this case, the fewest number of coins required to make a total of 11 is  `3`  (5 + 5 + 1).

### Example 2:

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#example-2)

coins = [2]
total = 3
print(makeChange(coins, total))  # Output: -1

Here, it is impossible to make the total  `3`  using only coin denomination  `2`, so the function returns  `-1`.

## Edge Cases

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#edge-cases)

1.  **Negative or Zero Total**:
    
    -   If the total is less than or equal to  `0`, the function immediately returns  `0`.
2.  **Unsolvable Case**:
    
    -   If it is not possible to reach the  `total`  using any combination of coins, the function returns  `-1`.
3.  **Empty Coin List**:
    
    -   If the list of coins is empty, the function will return  `-1`, as there are no coins to make any total.

## When if FAILS

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#when-if-fails)

there are scenarios where the current implementation of the makeChange function could fail due to its greedy approach. The greedy algorithm works by selecting the largest coin denomination first, which may not always lead to an optimal solution.

Here’s an example scenario where the code could fail:

###Scenario Example: Consider the following case:

Coins available: [1, 3, 4] Total to make: 6

###Greedy Approach:

The greedy algorithm will attempt to use the largest coin first:

1.  The largest coin is 4, so it subtracts 4 from 6, leaving 2 (6 - 4 = 2).
2.  Now, it tries to make 2, but the largest coin that is less than or equal to 2 is 1, so it subtracts two 1 coins.
3.  The solution becomes 4 + 1 + 1 = 6, using 3 coins.

###Optimal Solution: However, the optimal solution is to use two 3 coins:

3 + 3 = 6, which uses only 2 coins. The greedy approach in this case doesn't find the optimal solution because it chooses the largest coin first, which leads to a suboptimal result.

## General Limitation:

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#general-limitation)

The greedy algorithm works well when the coin denominations are multiples of each other (e.g., [1, 2, 4, 8]). But when the coin denominations don't follow such a pattern, there are cases where the greedy approach will not find the fewest coins.

## How to Fix:

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#how-to-fix)

To guarantee the correct result for all cases, you can implement dynamic programming or use a breadth-first search (BFS) approach, which ensures you always find the optimal solution. These methods would explore all possible ways to make the total and return the fewest coins needed.

## How to Use

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#how-to-use)

1.  **Input**:
    
    -   Provide a list of available coin denominations and a target total.
2.  **Output**:
    
    -   The function returns the minimum number of coins needed to make the target total, or  `-1`  if it is not possible.

### Sample Usage

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#sample-usage)

coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(f"The fewest number of coins to make {total} is: {result}")

## Time Complexity

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#time-complexity)

The function sorts the list of coins in descending order and uses a greedy approach to subtract the largest coin possible at each step.

-   **Sorting**  the coins takes  `O(n log n)`  time, where  `n`  is the number of coins.
-   The  **while loop**  and inner  **for loop**  may iterate over the coins multiple times, leading to a time complexity of  `O(n * m)`, where  `n`  is the number of coins, and  `m`  is the target total.

Thus, the overall time complexity is  **O(n log n + n * m)**.

## Conclusion

[](https://github.com/alaahamed1/alx-interview/blob/main/0x08-making_change/README.md#conclusion)

The  `makeChange`  function provides a simple and efficient way to determine the minimum number of coins needed for a given total using a greedy algorithm. However, in cases where the greedy approach fails, the function adjusts by removing the largest coin and trying again. This code provides a good solution for many common cases of the coin change problem.

----------

Feel free to reach out for any questions or improvements regarding this implementation.
