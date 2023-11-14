class TaxMan:
    def __init__(self, lst, tax_percent:str):
        self.lst = lst
        self.tax_percent = 1 + float(tax_percent.split("%")[0])/100
        self.total = 0
        
    def calc_total(self):
        self.total = round(sum(list(map(lambda x: x["price"], self.lst))) * self.tax_percent, 2)
        
    def get_total(self):
        return self.total