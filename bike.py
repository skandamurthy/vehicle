from vehile import Vehicle

class Bike(Vehicle):
	handle = True
	is_gear =True
	def __init__(self,handle,is_gear):
		self.handle=handle
		self.is_gear=is_gear

	def wheele(self):
		print("The bike has started a wheele on back wheele")

	def stoopie(self):
		print("Stunt done")
