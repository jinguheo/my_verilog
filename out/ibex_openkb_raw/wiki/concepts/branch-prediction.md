---
sources: [summaries/instruction_fetch.md]
brief: Static branch prediction is an experimental feature that attempts to improve performance by predicting branch outcomes based on offset signs.
---

# Branch Prediction

Branch prediction is a feature available in Ibex that can be configured to use static prediction to improve performance during instruction fetching.

## Mechanism and Goal

When enabled (by setting the ``BranchPrediction`` parameter to 1), the predictor attempts to predict the outcome of a branch based on its offset.

*   **Prediction Rule:** The predictor assumes that any branch with a negative offset is taken, and any branch with a positive offset is not taken.
*   **Benefit:** If the prediction is successful, it can remove a stall cycle from a taken branch, thereby improving overall performance.

## Mis-prediction Penalty

While branch prediction offers performance gains, it carries a penalty if the prediction is wrong:

*   A mis-predict penalty exists if a branch is wrongly predicted to be taken.
*   This penalty is at least one cycle, or at least two cycles if the instructions following the branch are uncompressed and not aligned.

## Status

This feature is currently marked as *EXPERIMENTAL*, and its full effects are not yet fully documented.

Refer to [[summaries/instruction_fetch]] for details on how the Instruction Fetch stage handles instruction flow and prediction.