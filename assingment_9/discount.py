class Discount:
    def __init__(self,op,dp):
        self.original_price=op
        self.discount_percentage=dp
        self.discount_amount = op*(dp/100)
        DA = self.discount_amount

        self.final_price= op - DA

    def display(self):
        print("the final price after discount is  ",self.final_price)

answer_obj = Discount(op = 300 , dp = 20)
answer_obj.display()


