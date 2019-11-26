#!/usr/bin/env python
# coding: utf-8

# In[24]:


class FnB:
    def __init__(self,address, area, revenue, staffnum):
        self.address  = address
        self.area     = area
        self.revenue  = revenue
        self.staffnum = staffnum
    def info(self):
        print("Address: ", self.address, "Area: ", self.area, "Revenue: ", self.revenue, "Number of staff: ", self.staffnum)
        

class DeliveryFnB(FnB):
    def __init__(self,address, area, revenue, staffnum, delivery_channel):
        FnB.__init__(self,address, area, revenue, staffnum)
        self.delivery_channel=delivery_channel
    def info(self):
        FnB.info(self)
        print("Delivery channel: ", self.delivery_channel)
    
    
    


# In[7]:


# Initial FnB class and DeliveryFnB class

Timhortons_Kelowna = FnB("145 Ponto road", 145, 135000, 10)
Timhortons_Kelowna.info()


# In[ ]:


# Initial DeliveryFnB class


# In[25]:


NumberOneKFC = DeliveryFnB("129 King street", 25, 85000, 3,"UberEat")
NumberOneKFC.info()

