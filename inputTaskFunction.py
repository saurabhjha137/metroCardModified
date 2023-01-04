from metroPassengersCopy import MetroCardPassenger

class InputTask :

    def __init__(self):
        self.passengers = []

    #iterating over List of Passenger to find passenger
    def find_passenger(self, passengerID):
        for passenger in self.passengers :
            if (passenger.is_passenger_id_same(passengerID)) :
                return passenger
        return False        

    #if Input is Balance
    def balance_input_actions (self, inputString) :
        passengerID = inputString.split()[1]
        passengerBalance = inputString.split()[2]
        newPassenger = MetroCardPassenger(passengerID, passengerBalance)
        self.passengers.append(newPassenger)

    #if Input is CheckIn
    def checkIn_input_actions (self, inputString, collectionSummary) :
        
        passengerID = inputString.split()[1]
        passengerType = inputString.split()[2]
        travellingSource = inputString.split()[3]
        #iterating over List of Passenger to Deduct Balance and AddCollection
        passenger = self.find_passenger(passengerID)

        if passenger :
            collectionSummary.calculate_travel_charges(passenger, passengerType, travellingSource)
        else :
            print('No Such Passenger Exists')