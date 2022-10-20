#name: Andres Leon T
#Date 3.20.2022
#Description: This program creates 3 random patients and displays their unique procedures, practitioners,
# and dates for each and displays them with their respective costs

import Patient as pat   # import classes
import random as rn

def generatePatient(): 
    """Creates patients and initializes attributes"""
    newPatient = pat.Patient('Some name', 'Some address', 'Some City', 'Some State',
                             'Some Zip', 'Some phone', 'Some EMcontact', 'Some EMphone')
    
    patientName1 = newPatient.setPatient()
    patientName2 = newPatient.setPatient()
    patientName3 = newPatient.setPatient()
    
    patientList = [patientName1, patientName2, patientName3] # returns random patient names in list to main()
    return patientList

def generatePatientData(patientName): # uses patient name value 
    
    def getProcedure(): # gets random procedures
        procedureList = [ 
            'Appendectomy', 'Hysterocopy', 'Low back pain surgery',
            'Prostatectomy', 'Epigastric hernia repair', 'Liver biopsy',
            'Mastectomy', 'Paraumbilical hernia repair','Cataract Surgery / Refractive Lens Exchange',
            'Diabetic Retinopathy Surgery / Vitrectomy',
            'Laser Surgery for Glaucoma',
            'Photorefractive Keratectomy',
            'Herniated Disk Surgery',
            'Hip Replacement Surgery',
            'Joint Fusion Surgery',
            'Knee Replacement Surgery',
            'Laminectomy Osteotomy',
            'Rotator Cuff Surgery',
            'Shoulder Replacement',
            'Surgery Spinal Fusion',
            'UCL Reconstruction',
            'Torn PCL Surgery',
            'Vertebroplasty',
            'Kyphoplasty']
        
        randProcedure1 = rn.randint(0, len(procedureList) - 1)
        randProcedure2 = rn.randint(0, len(procedureList) - 1)
        randProcedure3 = rn.randint(0, len(procedureList) - 1)
        return procedureList[randProcedure1], procedureList[randProcedure2], procedureList[randProcedure3] # returns random procedures
     
    def getProcedureCost(): # gets random procedure cost
        newProcedure = pat.Procedure('Some surgery', '01/01/0000', 'Some Doctor', 0)
        return newProcedure.setProcedureCost
    
    
    def getDates(): # returns random procedure dates for each surgery
        newProcedure = pat.Procedure('Some surgery', '01/01/0000', 'Some Doctor', 0)
        date1 = newProcedure.setProcedureDate()
        date2 = newProcedure.setProcedureDate()
        date3 = newProcedure.setProcedureDate()
        return date1, date2, date3
    
    def printProcedure(PatientName, p1, p2, p3, date1, date2, date3, doc1, doc2, doc3): # receives all data and neatly prints to screen
        newProcedure = pat.Procedure('Some surgery', '01/01/0000', 'Some Doctor', 0)
        newPat = pat.Patient(PatientName, '103 Jefferson St', 'Warsaw', 'NC', '28427',
                                '910.252.7789', 'James Brown', '910.442.3356')
        newPat.getPatient()
        newProcedure.setProcedureDate()
        newProcedure.setProcedureCost()    
        newProcedure.getProcedure(p1, date1, doc1, p2, date2, doc2, p3, date3, doc3)
        
    
    def getDoctor(): # gets new doctor from list in Procedure classes
        newProcedure = pat.Procedure('Some surgery', '01/01/0000', 'Some Doctor', 0)
        doc1 = newProcedure.setProcedureDoctor()
        doc2 = newProcedure.setProcedureDoctor()
        doc3 = newProcedure.setProcedureDoctor()
        return doc1, doc2, doc3 # returns 3 random doctors
    
    def main(patientName): # receives individual patient to use in print function
        p1, p2, p3 = getProcedure() # gets 3 procedures
        cost = getProcedureCost() # gets procedure cost
        date1, date2, date3 = getDates()
        doc1, doc2, doc3 = getDoctor() 
        printProcedure(patientName, p1, p2, p3, date1, date2, date3, doc1, doc2, doc3)

    main(patientName)    


def main():
    patientList = generatePatient() # receives patient List to use in loop
    for patient in patientList:
        generatePatientData(patient) # uses individual patient names and sends to function within function
        print('\n')
        
main()