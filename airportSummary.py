class AirportSummary :

    def initialize_airport_collections(self, airportCollectionAmount = 0, airportDiscount = 0) :    
        self.airportCollectionAmount = airportCollectionAmount
        self.airportDiscount = airportDiscount

    def initialize_airport_passenger_count(self,adults = 0,kids = 0,seniorCitezens = 0) :
        self.airportAdultCount = adults
        self.airportSeniorCitizenCount = seniorCitezens
        self.airportKidCount = kids

    def __init__(self) :
        self.initialize_airport_collections()
        self.initialize_airport_passenger_count()


    def add_to_collection(self, passengerFare) :
        self.airportCollectionAmount += passengerFare
    def add_to_discount(self, discountAmount) :
        self.airportDiscount += discountAmount
    
    def increment_airport_kid_count(self) :
        self.airportKidCount += 1
    def increment_airport_adult_count(self) :
        self.airportAdultCount += 1
    def increment_airport_seniorcitizen_count(self) :
        self.airportSeniorCitizenCount +=1


    def airport_summary_print (self) :

        print('TOTAL_COLLECTION AIRPORT '+ str(self.airportCollectionAmount) + ' ' + str(self.airportDiscount))
        print('PASSENGER_TYPE_SUMMARY')
        if self.airportAdultCount > 0 :
            print('ADULT ' + str(self.airportAdultCount))
        if self.airportKidCount > 0 :
            print('KID ' + str(self.airportKidCount))
        if self.airportSeniorCitizenCount > 0 :
            print('SENIOR_CITIZEN ' + str(self.airportSeniorCitizenCount))