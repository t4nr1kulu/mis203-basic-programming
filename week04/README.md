Lab 04: Savings Goal Planner

Testing Notes

Test run: I tested the boundary case mentioned in the requirements: Starting balance 0, deposit 10, rate 0, goal 10000. The program successfully simulated the process, correctly stopped after exactly 60 months, and printed the "Goal not reached" message with a final balance of 600.00.

Change made after testing: Initially, the table columns were unaligned and floating numbers had too many decimal places. After testing, I changed the print statement to use Python's formatted strings (f-strings) with :<15 for spacing and :.2f to lock the currency outputs to exactly two decimal places, making the table much easier to read.