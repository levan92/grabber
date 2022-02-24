# GRABBER

Helps to collate cost of grab rides

## Usage

1. Drag e-receipts emails from outlook into File Explorer
2.  `python3 run.py <filepath of folder containing .msg e-receipts>

## Example 

```bash
python3 run.py ~/Documents/admin/transport/grab/receipts
```

Output:
• $16.30 on 24 February 2022
• $22.30 on 23 February 2022
• $24.30 on 18 February 2022
• $28.30 on 14 February 2022
• $21.30 on 17 February 2022
• $22.30 on 16 February 2022

--------------------------------------------------------------------------------
Budget: $160.00
Total spent: $134.80
Total left: $25.20