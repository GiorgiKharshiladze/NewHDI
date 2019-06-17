class indicator():
    def __init__(self,Type,data, year, weight):
        self.Type= Type
        self.data=data
        self.year=year
        self.weight= weight
    
    def getType(self):
        return self.Type
    
    def getData(self):
        return self.data
    
    def getYear(self):
        return self.year
    
class Dynamic_Indicator():
    def __init__(self, indicator_Name):
        self.indicator_Name= indicator_Name
        self.dict={}

class country():
    def __init__(self, name, yr1=[],yr2=[],yr3=[],yr4=[],yr5=[]):
        self.name=name
        self.yr1=yr1
        self.yr2=yr2
        self.yr3=yr3
        self.yr4=yr4
        self.yr5=yr5
        
"""    def getname(self):
        return self.name
    def setname(self, e):
        self.name=e
    def getyr1(self):
        return self.yr1
    def getyr2(self):
        return self.yr2
    def getyr3(self):
        return self.yr3
    def getyr4(self):
        return self.yr4
    def getyr5(self):
        return self.yr5
    def setyr1(self,x):
        self.yr1=x
    def setyr2(self,x):
        self.yr2=x
    def setyr3(self,x):
        self.yr3=x
    def setyr4(self,x):
        self.yr4=x
    def setyr5(self,x):
        self.yr5=x
    """   
    
lis_data1=[]
lis_data2=[]
lis_data3=[]
lis_data4=[]
lis_data5=[]
lis_data6=[]
lis_country=[]
for k,v in countryDict.items():
    lis_country.append(k)
maxVal= max(lis_data6) + (0.1* max(lis_data6))
        
def normal(ind) :
    
    country_ratio= country("ratio "+ind)
    for i in range(len(lis_country)):
        country_ratio.yr1.append((lis_data6[i]-lis_data5[i])/(maxVal-lis_data5[i]))
        country_ratio.yr2.append((lis_data6[i]-lis_data4[i])/(maxVal-lis_data4[i]))
        country_ratio.yr3.append((lis_data6[i]-lis_data3[i])/(maxVal-lis_data3[i]))
        country_ratio.yr4.append((lis_data6[i]-lis_data2[i])/(maxVal-lis_data2[i]))
        country_ratio.yr5.append((lis_data6[i]-lis_data1[i])/(maxVal-lis_data1[i]))
        
    
    country_index =country("index "+ind)    
    for i in range(len(lis_country)):
        country_index.yr1.append((country_ratio.yr1[i]-min(country_ratio.yr1))/(max(country_ratio.yr1)-min(country_ratio.yr1)))
        country_index.yr2.append((country_ratio.yr2[i]-min(country_ratio.yr1))/(max(country_ratio.yr1)-min(country_ratio.yr1)))
        country_index.yr3.append((country_ratio.yr3[i]-min(country_ratio.yr1))/(max(country_ratio.yr1)-min(country_ratio.yr1)))
        country_index.yr4.append((country_ratio.yr4[i]-min(country_ratio.yr1))/(max(country_ratio.yr1)-min(country_ratio.yr1)))
        country_index.yr5.append((country_ratio.yr5[i]-min(country_ratio.yr1))/(max(country_ratio.yr1)-min(country_ratio.yr1)))
        
    
    for i in range(len(lis_country)):
        name= ind
        name= Dynamic_Indicator(ind)
        name.dict[lis_country[i]]= country_index.yr1[i]*0.50867^1+country_index.yr2[i]*0.50867^2+country_index.yr3[i]*0.50867^3+country_index.yr4[i]*0.50867^4+country_index.yr5[i]*0.50867^5
    

def calculate_DHDI(I1,I2,I3,I4,I5):
    DHDI={}
    normal(I1)
    normal(I2)
    normal(I3)
    normal(I4)
    normal(I5)
    for i in range(len(lis_country)):
        DHDI[lis_country[i]]= I1.dict[i]^(1/5)*I2.dict[i]^(1/5)*I3.dict[i]^(1/5)*I4.dict[i]^(1/5)*I5.dict[i]
        
        
        
        
        
        
        