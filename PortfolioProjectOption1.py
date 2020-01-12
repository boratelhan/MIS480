class Automobile:

	# constructor of the class
	def __init__(self,make,model,color,year,mileage):
		self.make = make
		self.model = model
		self.color = color
		self.year = (int)(year)
		self.mileage = (int)(mileage)

	# setters of the class
	def setMake(self,make):
		self.make = make

	def setModel(self,model):
		self.model = model

	def setColor(self,color):
		self.color = color

	def setYear(self,year):
		self.year = year

	def setMileage(self,mileage):
		self.mileage = mileage

	# getters of the class
	def getMake(self):
		return self.make

	def getModel(self):
		return self.model

	def getColor(self):
		return self.color

	def getYear(self):
		return self.year

	def getMileage(self):
		return self.mileage

# vehicle inventory is the list of automobiles
vehicleInventory=[]

def addVehicle():
	#Enter the automobile details:
	print('Enter automobile details:')
	make = input('Enter make: ') 
	model = input('Enter model: ')
	color = input('Enter color: ')
	year = (int)(input('Enter year: '))
	mileage = (int)(input('Enter mileage: '))
	# create object of Automobile class
	vehicle = Automobile(make,model,color,year,mileage)

	# append the vehicle to the end of the vehicle inventory
	vehicleInventory.append(vehicle)

def removeVehicle():
	# here remove the vehicle for this enter details
	print('Enter index of vehicle to remove')
	idx = (int)(input('Enter index of vehicle to remove: '))
	
	if idx < len(vehicleInventory):
		# remove that attribute from the vehicle inventory list
		vehicleInventory.pop(idx)
	else:
		print('Invalid index')

def updateVehicle():
	# update vehicle attributes using idx
	idx = (int)(input('Enter idx of the vehicle to update: '))
	if idx >= len(vehicleInventory):
		print('Invalid index')
	else:
		vehicleInventory[idx].setMake(input('Enter make: ')) 
		vehicleInventory[idx].setModel(input('Enter model: '))
		vehicleInventory[idx].setColor(input('Enter color: '))
		vehicleInventory[idx].setYear((int)(input('Enter year: ')))
		vehicleInventory[idx].setMileage((int)(input('Enter mileage: ')))	

def saveData():
	#open the file to write 
	f = open('vehicleInventory.txt', 'w')
	for x in vehicleInventory:
		make = 'Make: '+x.getMake()
		f.write(str(make))
		model = ' Model: '+x.getModel()
		f.write(str(model))
		color = ' Color: '+x.getColor()
		f.write(str(color))
		year = ' Year: '+(str)(x.getYear())
		f.write(str(year))
		mileage = ' Mileage: '+(str)(x.getMileage())
		f.write(str(mileage))
		f.write(str('\n'))

	# close the file
	f.close()

# function to print the inventory items
def printInventory():
	print('Vehicles in the inventory are: ')
	for x in vehicleInventory:
		make = 'Make: '+x.getMake()
		model = 'Model: '+x.getModel()
		color = 'Color: '+x.getColor()
		year = 'Year: '+(str)(x.getYear())
		mileage = 'Mileage: '+(str)(x.getMileage())
		print(make),
		print(model),
		print(color),
		print(year),
		print(mileage),
		print('')

def main():
	while 1:
		print('\tMenu')
		print('1.Add a vehicle')
		print('2.Remove a vehicle')
		print('3.Update Vehicle Attributes')
		print('4.Write Vehicle inventory to file and exit')
		option = (int)(input('Enter your choice: '))

		if option == 1:
			addVehicle()
			printInventory()

		elif option == 2:
			removeVehicle()
			printInventory()

		elif option == 3:
			updateVehicle()
			printInventory()

		elif option == 4:
			saveData()
			exit()


# call main function
if __name__=="__main__":
	main()
