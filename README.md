# GRABBER

Helps to collate cost of grab rides

## Usage

1. Drag e-receipts emails from Outlook into a folder in File Explorer
2.  `python3 run.py <filepath of folder containing e-receipts emails (*.msg)>

## Example 

```bash
python3 run.py ~/Documents/admin/transport/grab/receipts
```

```
Output:
• $28.30 on 2022-02-14
• $22.30 on 2022-02-16
• $21.30 on 2022-02-17
• $24.30 on 2022-02-18
• $22.30 on 2022-02-23
• $16.30 on 2022-02-24

--------------------------------------------------------------------------------
Budget: $160.00
Total spent: $134.80
Total left: $25.20
```
