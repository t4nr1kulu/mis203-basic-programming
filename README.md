# mis203-basic-programming
MIS203 - Basic Programming Course Assignments
Şükrü Taha Tanrıkulu
2404109030
Management Information Systems
MIS203 - Basic Programming

**Week01:**

**AI Tool Used:** Gemini

**Prompt Used:** "Can you help me write a simple Python program that asks the user for their name, department, age, and career goal, and then prints a short student profile?"

**What did you change?** 
I modified the print statements to use f-strings to ensure the output format perfectly matches the requested "--- Student Profile ---" template. I also updated the input variables to make the code easier to read.



**Week02:**
**AI Tool Used**: Gemini

**Prompt Used**: I am working on my Python grading assignment. Instead of giving me the direct code, can you explain the logic behind 'while True' loops and 'if-elif' statements? I want to understand why and how we use them to control the flow of the program.

**What did you change?**:I used the AI mostly to understand the logic of loops, conditions, and indentation. After understanding the concepts, I wrote the actual code, variables, and math calculations myself. I also added my own Turkish comments to explain what each line does so I can remember the logic later.

**What does break do in your program?**: In my program, the `break` command stops the infinite `while True` loop when the user types "e", which allows the program to stop asking for inputs and move on to calculating the average.

**Week03:**
**AI Tool Used**: Gemini

**Prompt Used**: "I wrote a python ticket office program using while loops and if/elif statements, but I am getting indentation errors and want to handle invalid inputs without crashing. Can you help me fix my syntax?"

**What did you change?** I fixed the IndentationError in my loops and corrected the operator from =+ to += to properly calculate the total revenue. I also added continue statements to catch invalid inputs and restart the loop without breaking the program.

**Tests**:

Input: Age 65 (Boundary age), Weekday. Result: Senior discount (50%) applied successfully.
Input: Age -5 (Invalid age). Result: Program printed "Invalid age" and restarted the loop asking for the name again.
Input: Age 20, Student "yes", Weekend. Result: Student discount (30%) applied to the base price of 250 TRY.
Why does the order of the rules matter? Python checks if/elif statements from top to bottom and stops at the first True condition. If the "Student" rule came before the "Child" rule, a 10-year-old student would wrongly receive the 30% student discount instead of the 40% child discount they deserve.


# Week 04: Surprise Me - Pong Game

## 1. Description
A two-player interactive Pong game demonstrating `while` loops, `if/else` conditions, and functions. Uses two external libraries: `turtle` (for graphics and keyboard controls) and `random` (for ball trajectory).

## 2. How to Play
Run the script to open the game window.
- **Player 1 (Left Paddle):** Use `W` (Up) and `S` (Down).
- **Player 2 (Right Paddle):** Use `Up Arrow` and `Down Arrow`.
- **Goal:** Deflect the ball. The game ends if the ball passes your paddle.
- **Result:** The winner ("Player 1 wins!" or "Player 2 wins!") is printed in the terminal/console behind the game window.

## 3. Test Cases

| Test Case | Condition | Expected Output | Actual Output | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| **Wall Bounce** | Ball Y > 190 or < -190 | Reverses Y direction | Bounces off top/bottom | Pass ✅ |
| **Paddle Hit** | Ball hits X = 290 or -290 | Reverses X, speed +0.1 | Bounces back, gets faster | Pass ✅ |
| **Game Over** | Ball X > 300 or < -300 | Loop breaks, prints winner | Prints "Player X wins!" | Pass ✅ |

## 4. Note & AI Usage
**AI Usage:** I used AI as an assistant to review my code, translate my original Turkish `print` outputs into proper English (e.g., "Player 1 wins!"), and format this README file. The core game logic and loop were written by me.