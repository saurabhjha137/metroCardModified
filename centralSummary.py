class CentralSummary :

    def initialize_central_collections(self, centalCollectionAmount = 0, centralDiscount = 0) :    
        self.centalCollectionAmount = centalCollectionAmount
        self.centalDiscount = centralDiscount

    def initialize_central_passenger_count(self,adults = 0,kids = 0,seniorCitezens = 0) :
        self.centralAdultCount = adults
        self.centralSeniorCitizenCount = seniorCitezens
        self.centralKidCount = kids

    def __init__(self) :
        self.initialize_central_collections()
        self.initialize_central_passenger_count()

    def add_to_collection(self, passengerFare) :
        self.centalCollectionAmount += passengerFare
    
    def add_to_discount(self, discountAmount) :
        self.centalDiscount += discountAmount
    
    def increment_central_kid_count(self) :
        self.centralKidCount += 1
    def increment_central_adult_count(self) :
        self.centralAdultCount += 1
    def increment_central_seniorcitizen_count(self) :
        self.centralSeniorCitizenCount +=1

    def central_summary_print (self) :
        print('TOTAL_COLLECTION CENTRAL ' + str(self.centalCollectionAmount) + ' ' + str(self.centalDiscount))
        print('PASSENGER_TYPE_SUMMARY')
        if self.centralAdultCount > 0 :
            print('ADULT ' + str(self.centralAdultCount))
        if self.centralKidCount > 0 :
            print('KID ' + str(self.centralKidCount))
        if self.centralSeniorCitizenCount > 0 :
            print('SENIOR_CITIZEN ' + str(self.centralSeniorCitizenCount))



    