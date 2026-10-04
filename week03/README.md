## Week 03

**AI Tool Used:** Gemini

**Prompt Used:** "I wrote a python ticket office program using while loops and if/elif statements,
but I am getting indentation errors and want to handle invalid inputs without crashing. Can you help me fix my syntax?"

**What did you change?** 
I fixed the `IndentationError` in my loops and corrected the operator from `=+` to `+=` to properly calculate the total revenue.
I also added `continue` statements to catch invalid inputs and restart the loop without breaking the program.

**Tests:**
1. *Input:* Age 65 (Boundary age), Weekday. *Result:* Senior discount (50%) applied successfully.
2. *Input:* Age -5 (Invalid age). *Result:* Program printed "Invalid age" and restarted the loop asking for the name again.
3. *Input:* Age 20, Student "yes", Weekend. *Result:* Student discount (30%) applied to the base price of 250 TRY.

**Why does the order of the rules matter?** 
Python checks `if/elif` statements from top to bottom and stops at the first `True` condition.
If the "Student" rule came before the "Child" rule, a 10-year-old student would wrongly receive the 30% student discount instead of the 40% child discount they deserve.
