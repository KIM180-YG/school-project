# Object oriented programming assignment
class OrderItem:

    def __init__(self, name, prod, unit_price, discount, qty): # initializing the attributes
        self._name = name
        self._prod = prod
        self._unit_price = unit_price
        self._discount = discount
        self._qty = qty
        
  # When write down the disvount it should be 0.** format
  # for example if the discount rate is 20% = 0.20
    def __str__(self):
        return f"| Item name: {self._name}, Product code: {self._prod}, Quantity: {self._qty}, Total price: {self.get_actual_amount()} |"
    # To access the attribute outside of the class I used setter and getter method
    @property
    def prod(self):
        return self._prod
    @prod.setter
    def prod(self, new_prod_value):
        self._prod = new_prod_value
    
    @property
    def unit_price(self):
        return self._unit_price
    
    @unit_price.setter
    def unit_price(self, new_unit_price):
        self._unit_price = new_unit_price
    
    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, new_discount):
        self._discount = new_discount
    
    @property
    def qty(self):
        return self._qty
    
    @qty.setter
    def qty(self, new_qty):
        self._qty = new_qty
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    def get_total_amount(self):                 
        return self._unit_price * self._qty
    
    def get_discount_amount(self):                 # returns how much can I get the amount of dicount
        return self._unit_price * self._qty * self._discount
    
    def get_actual_amount(self):                    # this function returns the actual amount after applying the discount rate
        return self.get_total_amount() - self.get_discount_amount()
    
    def update_item_qty(self, new_qty):              # this function is for updating the quantity for each item
        self._qty = new_qty
        print("Item quantity updated successfully !!!!!")


class CustOrder:

    def __init__(self, ref_no, recipient, address, date_ordered, date_delivered):
        self._ref_no = ref_no
        self._recipient = recipient
        self._address = address
        self._date_ordered = date_ordered
        self._date_delivered = date_delivered
        self.order_list = [] #using the order_list I can easily manage the several orderitems inside the list

    def __str__(self):
        order_items_str = "\n".join(str(item) for item in self.order_list) # not to print the addresses of the objects of OrderItem I wanted to print out as the string method in OrderItem
        return f"++ Code of the order: {self._ref_no}, Name: {self._recipient}, Address: {self._address} ++\n++ Date of Ordered/ Delivery: {self._date_ordered,self._date_delivered} List of the orders: ++ \n{order_items_str}\n **Total amount of this order: {self.get_total()}** "

    @property
    def ref_no(self):
        return self._ref_no
        
    @ref_no.setter
    def ref_no(self, new_ref_value):
        self._ref_no = new_ref_value

    @property
    def recipient(self):
        return self._recipient
    
    @recipient.setter
    def recipient(self, new_recipient_value):
        self._recipient = new_recipient_value

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, new_address):
        self._address = new_address
    
    @property
    def date_ordered(self):
        return self._date_ordered
    
    @date_ordered.setter
    def date_ordered(self, new_date_ordered):
        self._date_ordered = new_date_ordered

    @property
    def date_delivered(self):
        return self._date_delivered
    
    @date_delivered.setter
    def date_delivered(self, new_date_delivered):
        self._date_delivered = new_date_delivered

# each customer has their own order_list
    def add_item(self, new_item):
        for item in self.order_list:
            if item.prod == new_item.prod:
                return False
            
        self.order_list.append(new_item)
        return True
            #append item in the order
    # removing item in the basket by entering the item code 
    def remove_item(self, prod_code):
        for item in self.order_list:
            if item.prod == prod_code:      
                self.order_list.remove(item)
                return True
        return False # if the code wasn't found in the order list return False

    # calculating the total price in the basket(order_list)
    def get_total(self):
        total_price = 0
        for item in self.order_list:
            each_price = OrderItem.get_actual_amount(item)      #using the get_actual_amount function from the OrderItem class
            total_price += each_price
        return total_price

    def update_item_qty(self, prod, new_qty):      # To choose the object inside the order_list I'm using product code to access and then updated the new qty
        for item in self.order_list:
            if item.prod == prod:            # check whether the item is the right one to update or not
                item.update_item_qty(new_qty)
                return True
        return False



def main():
    Kim180 = CustOrder(2003, "Younggun", 652453, "16 April", "18 April")          # Creating CustOrder object
    
    while True:                                       #by using while loop we can add another items if we want
        name = input("Enter the name of the item: ")
        prod = input("Enter the product code: ")
        unit_price = float(input("Enter the unit price: "))
        discount = float(input("Enter the discount rate(ex: 0.10 for 10 %): "))
        qty = int(input("Enter the quantity: "))

        new_item = OrderItem(name, prod, unit_price, discount, qty)

        if Kim180.add_item(new_item):
            print("Item successfully added to your order.")
            
        else:
            print("Item already exists in the order.")

        asking = input("Do you want to add another item?(Yes/No): ")
        if asking.lower() != "yes":
            break
    print("---------------------------------------------------")
    print("These are the items inside your order list")
    for new_items in Kim180.order_list:
        print(new_items)

    while True:
        asking = input("Do you want to remove the item? (Yes/No): ")
        if asking.lower() == "no":
            break     # If you don't want to remove the item by this break you can come out from the loop and move to next one
        remove_prod = input("Enter the product code of the item you want to remove: ")
        removed = Kim180.remove_item(remove_prod)
        if removed:
            print("Item successfully removed from your order !!!!!. ")
        else:
            print("Item code has not found in the order list.")
        
        asking  = input("Do you want to remove another item? (Yes/NO): ")
        if asking.lower() == "no":
            break

    while True:
        asking = input("Do you want to update the item quantity? (Yes/No): ")
        if asking.lower() == "no":
            break
        update = input("Enter the product code / new quantity (code,qty): ")
        prod, new_qty = update.split(",")
        Kim180.update_item_qty(prod, int(new_qty))


    print("-----------------------------------------------")
    print("These are the items inside your order list")
    for new_items in Kim180.order_list:
        print(new_items)
    
    print("------------------------------------------------------------------")
    print(Kim180)

    print("End of main")

main()
