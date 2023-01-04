SERVICE_FEE_PERCENT = 2
REDUCTION_VALUE = 0.5

#serviceCharges calculation
def calculate_service_charge (balance, fare) :
    serviceCharge = fare - balance
    serviceCharge = serviceCharge*SERVICE_FEE_PERCENT
    return int(serviceCharge/100)

#Fare Reduction for Return Journey 
def reduce_fare(fare) :
    return int(fare * REDUCTION_VALUE)


class MetroCardPassenger :
    def __init__(self, passengerID, passengerBalance, returnJourney = False):
        self.passengerID = passengerID
        self.passengerBalance = passengerBalance
        self.returnJourney = returnJourney
        
    def get_passenger_id (self) :
        return self.passengerID
    def is_passenger_id_same(self, passengerID) :
        return (self.get_passenger_id() == passengerID)
 

    def is_return_journey(self) :
        return self.returnJourney
    def update_return_journey_status(self, updatedReturnJourney) :
        self.returnJourney = updatedReturnJourney


    def get_passenger_balance (self) :
        return int(self.passengerBalance)
    def update_passenger_balance(self, updatedBalance) :
        self.passengerBalance = int(updatedBalance)


    #Passenger Has Enough balance to travel, hence deducting Fare
    def deduct_passenger_balance(self, fare, balance, collectionSummary) :
        updatedBalance = balance - fare
        self.update_passenger_balance(updatedBalance)
        collectionSummary.add_to_collection(fare)

    #Passenger does not have Enough balance to travel, hence deducting Fare and applying Service charges
    def deduct_service_charge_and_passenger_balance(self, fare, balance, collectionSummary) :
        serviceChargeFee = calculate_service_charge(balance, fare)
        updatedBalance = 0
        self.update_passenger_balance(updatedBalance)
        collectionSummary.add_to_collection(fare+serviceChargeFee)
        
    #checking if Passenger Having Enough balance to travel
    def check_balance_and_deduct(self, fare , collectionSummary) :
        if self.get_passenger_balance() >= fare :
            self.deduct_passenger_balance(fare, self.get_passenger_balance(), collectionSummary)
        else :
            self.deduct_service_charge_and_passenger_balance(fare, self.get_passenger_balance(), collectionSummary)

    #Passenger is Doing Return Journey, hence Reduced fare will be deducted
    def deduct_for_return_journey(self, reducedTravelfare, collectionSummary):
        self.check_balance_and_deduct(reducedTravelfare, collectionSummary)
        collectionSummary.add_to_discount(reducedTravelfare)

    #Passenger is Doing OneWay Journey, hence Actual fare will be deducted
    def deduct_for_one_way_journey(self, actualTravelFare, collectionSummary) :
        self.check_balance_and_deduct(actualTravelFare, collectionSummary)

    def deduct_travel_charges(self, travelFare, collectionSummary) :   
        #if passenger doing OneWay Journey
        if not self.is_return_journey() :
            self.deduct_for_one_way_journey(travelFare, collectionSummary)
            self.update_return_journey_status(True)
        #if passenger doing Return Journey        
        else :
            self.deduct_for_return_journey(reduce_fare(travelFare), collectionSummary)
            self.update_return_journey_status(False)
