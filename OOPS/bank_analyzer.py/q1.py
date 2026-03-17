from csv import DictReader


class TransactionAnilyzer:
    def __init__(self):

        fr=open("/Users/akshay/Desktop/development journey/OOPS/bank_analyzer.py/q1.csv")
        self.transactions=list(DictReader(fr))
        print(len(self.transactions),"records found")
    def debit_transactions(self):
        for t in self.transactions:
            if t.get("type")=="debit":
                print(t)
    def credit_transactions(self):pass
    

analysis=TransactionAnilyzer()
analysis.debit_transactions()

