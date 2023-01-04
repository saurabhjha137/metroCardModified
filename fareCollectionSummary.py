from centralSummary import CentralSummary 
from airportSummary import AirportSummary

ADULT_FARE = 200
SENIOR_CITIZEN_FARE = 100
KID_FARE = 50

def get_fare_for_passenger_type(passengerType):
    match passengerType :
        case "ADULT" :
            return ADULT_FARE
        case 'SENIOR_CITIZEN' :
            return SENIOR_CITIZEN_FARE
        case 'KID' :
            return KID_FARE

def is_travelling_source_airport(travellingSource) :
    return (travellingSource == "AIRPORT")
       
class FareCollection(CentralSummary, AirportSummary) :
   
    def __init__(self) :
        self.airportCollection = AirportSummary()
        self.centralCollection = CentralSummary()
        
    def update_airport_passenger_count(self, passengerType, airportCollection):
        match passengerType :
            case "ADULT" :
                airportCollection.increment_airport_adult_count()
            case 'SENIOR_CITIZEN' :
                airportCollection.increment_airport_seniorcitizen_count()
            case 'KID' :
                airportCollection.increment_airport_kid_count()


    def update_central_passenger_count(self, passengerType, centralCollection):
        match passengerType :
            case "ADULT" :
                centralCollection.increment_central_adult_count()
            case 'SENIOR_CITIZEN' :
                centralCollection.increment_central_seniorcitizen_count()
            case 'KID' :
                centralCollection.increment_central_kid_count()

    def calculate_travel_charges(self, passenger, passengerType, travellingSource) :

        travelFare = get_fare_for_passenger_type(passengerType)
        if is_travelling_source_airport(travellingSource) :
            self.update_airport_passenger_count(passengerType, self.airportCollection)
            passenger.deduct_travel_charges(travelFare, self.airportCollection)
        else :
            self.update_central_passenger_count(passengerType, self.centralCollection)
            passenger.deduct_travel_charges(travelFare, self.centralCollection)

    def print_summary(self) :
        self.centralCollection.central_summary_print()
        self.airportCollection.airport_summary_print()
        
