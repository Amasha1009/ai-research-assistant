# AI Research Assistant - Test Cases

## Test Case 1

Feature:
Upload PDF

Input:
Valid research paper PDF

Expected Result:
Paper uploads successfully and preview is displayed.

Status:
Pass


---

## Test Case 2

Feature:
Empty Question

Input:
Click Apply without entering a question

Expected Result:
Display:
"Please enter a question."

Status:
Pass


---

## Test Case 3

Feature:
Research Question

Input:
"What is the objective of this paper?"

Expected Result:
System answers using uploaded paper.

Status:
Pass


---

## Test Case 4

Feature:
Summary

Input:
"Summarize this paper"

Expected Result:
Objective
Methodology
Key Findings
Conclusion

Status:
Pass


---

## Test Case 5

Feature:
Comparison

Input:
Compare Paper 1 and Paper 2

Expected Result:
Shows similarities and differences.

Status:
Pass


---

## Test Case 6

Feature:
Comparison without Paper 2

Input:
Compare papers

Expected Result:
Display warning asking user to upload Paper 2.

Status:
Pass


---

## Test Case 7

Feature:
Clear Button

Input:
Click Clear

Expected Result:
Question and answer are cleared.

Status:
Pass


---

## Test Case 8

Feature:
Reflection

Input:
Ask any research question

Expected Result:
Final answer is improved by Reflection Agent.

Status:
Pass


---

## Test Case 9

Feature:
API Error

Input:
Disable API

Expected Result:
Friendly error message appears.

Status:
Pass