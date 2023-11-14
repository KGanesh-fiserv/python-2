from dataclasses import dataclass

@dataclass(frozen=False, order=True)
class Invoice:
    def __init__(self, a:str):
        lst = a.split(", ")
        self.invoice_id = lst[0].strip()
        self.user_id = lst[1].strip()
        self.amount = lst[2].strip()
        self.paid = lst[3].strip()
    
    def __repr__(self):
        return f"Invoice(invoice_id='{self.invoice_id}', user_id='{self.user_id}', amount='{self.amount}', paid='{self.paid}')"