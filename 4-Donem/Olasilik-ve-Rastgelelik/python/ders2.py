import random
"""
olaslık ölçüsü
1. Negatif olmama : olasılık ölçüsü 0 ile 1 arasında bir değer alır
2. Normalizasyon : olasılık ölçüsünün tüm kümeler için toplamı 1 olmalıdır
3. Toplamsallık: iki olay birbirinden ayrıksa P(AuB) = P(A) + P(B)
"""

#olasılığın temle özellikleri 1
#A olayı evrensel kümenin bir alt kümesi ise
#Ac A kümesinin tersidir
P_A = random.uniform(0,1)
#=>
P_A_C = 1 - P_A
print("P(Ac) = ", P_A_C, "P(A) = ", P_A)

#olasılığın temel özellikleri 2
# Eğer A olayı B kümesinin bir alt kümesi ise, P(A) =< P(A)
# P(B) = P( A u (Ac n B) )= P(A) + P(Ac n B) >= P(A)

#olasılığın temel özellikleri 3
# P(AuB) = P(A) + P(B) - P(A n B)
#ikiden fazla olan olaylara da genişletilebilir
# P(AuBuC) = P(A) + P(B) + P(C) - P(A n B) - P(A n C) - P(B n C) + P(A n B n C)
def Ufor_n_action(list_of_action):
    string = ""
    for i in range(len(list_of_action)):
        
        string += ("P(%s)" % (list_of_action[i]) )
        if i < len(list_of_action) - 1:
            string += "+"
        else :
            string += "-"
    for i in range(len(list_of_action)):
        for j in range(len(list_of_action)):
            if i != j and i < j:
                string += ("P(%s n %s)" % (list_of_action[i], list_of_action[j]))
                if i < len(list_of_action) - 1:
                    string += "-"
                else :
                    string += "+"
    string+= "P("
    for i in range(len(list_of_action)):
        if i < len(list_of_action) - 1:
            string += list_of_action[i] + " n "
        else :
            string += list_of_action[i] + ")"
    
    return string
print(Ufor_n_action(["A","B","C"])) 

# olayların birleşim sınırı
# P(A U B) = P(A) - P(B) - P(A n B)

#örnek 1
def communication_error_finder( error,filesize):
    
    
    pass