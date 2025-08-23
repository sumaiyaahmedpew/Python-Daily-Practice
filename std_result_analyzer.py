# problem_23  Student Result Analyzer

import numpy as np

def subject_result(marks):
    print("\n Subject wise Result:")
    print("Average per subject:", np.mean(marks, axis=0))
    print("Highest per subject:", np.max(marks, axis=0))
    print("Lowest per subject:", np.min(marks, axis=0))

def student_result(marks, names=None):
    print("\n Students Result:")
    totals = np.sum(marks, axis=1)
    avgs = np.mean(marks, axis=1)
    for i, (t, a) in enumerate(zip(totals, avgs)):
        label = names[i] if names else f"Student {i+1}"
        print(f"{label} -> Total: {t}, Average: {a:.2f}")
    topper = np.argmax(totals)
    print(f"Topper: {names[topper] if names else 'Student ' + str(topper+1)}")

# Example Run
marks = np.array([[80, 90, 75],
                  [60, 70, 85],
                  [95, 88, 100]])

names = ["Alice", "Bob", "Charlie"]

subject_result(marks)
student_result(marks, names)

