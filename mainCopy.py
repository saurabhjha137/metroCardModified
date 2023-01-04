import sys
from inputTaskFunction import InputTask
from fareCollectionSummary import FareCollection

if __name__ == '__main__':
    
    inputTask = InputTask()
    fareCollection = FareCollection()

    file = open('sampleIOfile2.txt', 'r+')
    # file = open(sys.argv[1], 'r+')
    
    for inputString in file.readlines():
        
        action = inputString.split()[0]
        match action :
            case "BALANCE" :
                inputTask.balance_input_actions(inputString)
            case "CHECK_IN":
                inputTask.checkIn_input_actions(inputString, fareCollection)
            case "PRINT_SUMMARY":
                fareCollection.print_summary()
            case _:
                break

    file.close()