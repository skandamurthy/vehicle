from vehile import Vehicle
class Car(Vehicle):
	ac = False
	steering_wheel = True
	seat_belt = True
	audio_player=True
	def __init__(self,ac,steering_wheel,seat_belt,audio_player,no_of_wheels,speed,weight,milage,colour):
		self.ac =ac
		self.steering_wheel =steering_wheel
		self.seat_belt = seat_belt
		self.audio_player=audio_player
		Vehicle.__init__(self,no_of_wheels,speed,weight,milage,colour)

	def drift(self):
		print("Car's Drifting")

	def deploy_airbags(self):
		print("Car's met with an Accident")
		
		
		
