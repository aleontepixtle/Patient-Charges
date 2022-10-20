class Patient():

    def __init__(self, name, address, City, State, Zip, phone, EMcontact, EMphone):
        self.name = name
        self.address = address
        self.City = City
        self.State = State
        self.Zip = Zip
        self.phone = phone
        self.Emcontact = EMcontact
        self.Emphone = EMphone
        
    def getPatient(self):
        print('Patient \n----------------------\nName:    ', self.name,
              '\nAddress: ', self.address,'\n\t ', self.City,', ', 
              self.State, ' ', self.Zip,'\n', sep='')           
    #print("Patient Class successful.")
    def setPatient(self):
        import random as r
        PatientList = [
            'Marvin Jerrard Eloísa',
            'Kaydence Nadia Charla',
            'Lyle Clare Isiah',
            'Jo-Anne Romaine Marilynn',
            'Corina Juan Marjory',
            'Merilyn Linsay Lovell',
            'Seraphina Jazlyn Stacey',
            'Graysen Dina Derrick',
            'Izabelle Elnora Milly',
            'Mike Mavis Gaynor',
            'Rowley Nyree Sharmaine',
            'Harvey Nita Leandra',
            'Melesina Max Hamilton',
            'Marita Pepita Olegario',
            'Maggie Roz Edna']
        
        self.name = PatientList[r.randint(0,len(PatientList)-1)]
        return self.name

class Procedure():
    
    def __init__(self, ProcedureName, ProcedureDate, ProcedureDoc, ProcedureCost):
        self.ProcedureName = ProcedureName
        self.ProcedureDate = ProcedureDate
        self.ProcedureDoc = ProcedureDoc
        self.ProcedureCost = ProcedureCost
        
    def getProcedure(self, Procedure1, Date1, Doc1, Procedure2, Date2, Doc2, Procedure3, Date3, Doc3):
        print(
              'Procedure needed:   ', Procedure1, '\n'
              'Date:                ', Date1, '\n',
              'Practitioner:        ', Doc1, '\n',
              '\nProcedure needed:   ', Procedure2, '\n'
              'Date:                ', Date2, '\n',
              'Practitioner:        ', Doc2, '\n',
              '\nProcedure needed:   ', Procedure3, '\n'
              'Date:                ', Date3, '\n',
              'Practitioner:        ', Doc3, '\n',              
              '\nTotal Base cost for all procedures: ', self.ProcedureCost, '\n',
              '----------------------', sep='')
    
    def setProcedureDoctor(self):
        import random as r
        doctorList = [
            'Dr. Alan Grant',
            'Dr. Joshua Chang',
            'Dr. Melody Garcia',
            'Dr. Ashley Berg',
            'Dr. Ashlynn Ensey',
            'Dr. Jacob Frame',
            'Dr. Mike Hyre',
            'Dr. Shirley Whitrock',
            'Dr. Adele Gessel',
            'Dr. Cheyenne Josilowsky',
            'Dr. Ray Kaauamo',
            'Dr. Remington Reavely',
            'Dr. Sawyer Soares']
        
        self.ProcedureDoc = doctorList[r.randint(0,len(doctorList) -1 )]
        return self.ProcedureDoc
     
    def setProcedureCost(self):
        import random as r  
        ranNum = r.randint(75000, 100000)
        cost = ranNum * 1.07
        formatCost = "${:,.2f}".format(cost)

        self.ProcedureCost = formatCost
        
    def setProcedureDate(self):
        import random as r  
        month, day, year = r.randint(1,12), r.randint(1,30), 2022
        date = str(month) + '/' + str(day) + '/' + str(year)
        return date
