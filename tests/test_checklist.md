# Task 5 – Test Record

| Test | Input | Expected result | Actual result |
|---|---|---|---|
| Normal run | data/sample_sales.csv | KPIs, two charts, table and download appear | PASS |

| Failure 1 | wrong_columns.csv |The file could not be processed: Required column(s) missing: Product, Category, Sales, Quantity. Use the exact column names shown in the sample CSV | PASS |

| Failure 2 | empty.csv | The file could not be processed: The uploaded CSV has no data rows. Please upload a file containing sales records.| PASS |

| Failure 3 | invalid_values.csv | File processed. 10 valid row(s) are ready.
2 row(s) were excluded because one or more values were missing or invalid. | PASS |

Tested by: Daniel Asham Isaac
Date: 2026-11-25
Notes / issues found: None
