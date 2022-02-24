import extract_msg
import argparse
from pathlib import Path
from dateutil.parser import parse

ap = argparse.ArgumentParser()
ap.add_argument('dir', help='dir containing grab')
ap.add_argument('--budget', help='monthly budget', default=160.00, type=float)
args = ap.parse_args()

grab_dir = Path(args.dir)

total_spent = 0

spend_list = []
for grabfile in grab_dir.glob("*.msg"):
    msg = extract_msg.Message(grabfile)
    if "@grab.com" in msg.sender and "Your Grab E-Receipt" in msg.subject:
        rest = msg.body.split('Picked up on')[-1]
        date_str = rest.split('\n')[0].strip()
        dt = parse(date_str, fuzzy=True)
        price = rest.split('Total Paid')[-1].split('\n')[0]
        price = float(price.strip())
        total_spent += price
        spend_list.append((dt, price))

for date, pri in sorted(spend_list):
    print(f"\u2022 ${pri:0.2f} on {date.date()}")


balance = args.budget - total_spent
print()
print('-'*80)
print(f"Budget: ${args.budget:0.2f}")
print(f"Total spent: ${total_spent:0.2f}")
print(f"Total left: ${balance:0.2f}")
