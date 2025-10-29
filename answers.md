# CMPS 2200 Recitation 06
## Answers

**Name:** GitHub Copilot


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** Work T(n) = T(n-1) + T(n-2) + O(1). Solution T(n) = Theta(phi^n), so exponential.

- **3)** Span S(n) = max{S(n-1), S(n-2)} + O(1) = S(n-1) + O(1). Solution S(n) = Theta(n).

- **4)** counts[i] equals F_{n-i+1} and so closely follows Fibonacci numbers; the combined call counts form the fibonacci sequence, and sum(counts) = 2*F_{n+1} - 1 (which is just the total calls in tree).

- **6)** Each i is computed at most once (due to memoization), so there are O(n) calls; work Theta(n), span Theta(n).

- **8)** Each F_i is read O(1) times per subsequent step, so total work Theta(n). Span Theta(n) if sequential loop, and since parallel prefix not applicable here, span remains Theta(n).
