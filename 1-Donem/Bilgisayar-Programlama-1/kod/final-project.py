Cairo = "Cairo!!"
Egypt = "Cairo"
Damascus = "Damascus"
Istanbul = "Istanbul" 

name = input("what is your name? ")
print("Nice To meet u, ", name)

Nation = input("Where are u from? ")
print("Ohh First time to see someone from, ", Nation)

Nation = Egypt
fav_city_dict = { "Egypt" : "Cairo", "Lebanon" : "Beyrut" , "UK" :"London"  }


print("So proparly your favorite city is, ", fav_city_dict[Nation])

ask = input("Right? ")

if ask == "Yes":
    print("What a nice city")
    print("Here is your favorite city's sifalar, ")

    def favorite_city_A(name):

        print("Hot weather")
        print("Windy")
        print("My Neighborhood")
    favorite_city_A(Cairo)
            
else:
    ask2 = input("Then What's your favorite city? ")

    if ask2 == Damascus:
        print("Good choice knki my syrian hoomiee")
        print("Here is your favorite city's sifalar, ") 

        def favorite_city_B(Damascus):
   
            print("Warm weather")
            print("Cloudy")
            print("Oldest city in History")
        favorite_city_B(Damascus)
    
    else:
        print("Mmmm, So Istanbul is your favorite ") 
        print("Here is your favorite city's sifalar, ")
    
        def favorite_city_C(Istanbul):    
    
            print("Cold weather")
            print("Rainy")
            print("Very Crowded")
        favorite_city_C(Istanbul)