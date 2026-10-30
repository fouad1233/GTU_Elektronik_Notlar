#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:49:07 2022

@author: fuad
"""


import datetime
 
class Person:
    
    def __init__(self, name, lastname):
        #print("Person initializing.")
        #self.name = name
        self.set_name(name)
        self.lastname = lastname.capitalize()
        
    def set_birthday(self, day, month, year):
        self.bday = datetime.date(year, month, day)
        
    def get_age(self):
        tdays = (datetime.date.today() - self.bday).days
        years = tdays//365
        tdays -= int(years *365.25)
        months = tdays//30
        days = tdays - months*30
        return 'Şimdiye kadar tam olarak ' +str(years)+ ' yıl,' +str(months)+' ay,' +  str(days)+' gün yaşadınız.'          
        
    def set_name(self, name):
        import string
        s = string.ascii_letters
        
        if not isinstance(name, str):
            raise TypeError("String bekliyoruz")
        
        for c in name:
            if c not in s:
                raise ValueError("turkce karakter olmasin")
            
        self.name = name.capitalize()
    
        
    def say(self, cumle):
        print(self.name, "diyor ki: ", cumle)
    
    def adini_soyle(self):
        self.say("Benim adim " + self.name + " " + self.lastname)

    def __str__(self):
        return self.name + " " + self.lastname

   
    def __lt__(self, other):
        #if self.lastname < other.lastname:
        #    return True
        #else:
        #    return False
        print("Comparing", self, other)
        #return self.get_age() < other.get_age()
        return self.lastname < other.lastname
    


    
    
    
    
    
    
    
    
    
    
    
