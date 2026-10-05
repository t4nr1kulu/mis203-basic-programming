### Lab 03: Order Approval Policy

**What did you change after testing?**
During my initial tests, I used Turkish inputs ("evet/hayır") for the membership question, which caused the discount condition (`member == "yes"`) to fail.
I changed all string checks and input prompts to English to ensure the logical `and` operator works correctly for the 10% discount rule.

**Boundary Tests (Stretch Task):**

| Order Amount | Stock | Quantity | Member | Expected Result |
| 500 TRY | 50 | 2 | yes | Order approved with a 10% discount! Final price: 450.0 TRY (Discount Boundary) |
| 499 TRY | 50 | 2 | yes | Order approved. Final price: 499.0 TRY (Below Discount Boundary) |
| 100 TRY | 10 | 0 | no | Invalid quantity. Order rejected. (Zero Quantity Boundary) |
