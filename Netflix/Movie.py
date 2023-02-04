class Movie:
    
    def __innit__(self):
        self.__title=""
        self.__director=""
        self.__length=0
        self.__genre=""
        self.__year=0
    
    def set_title(self,t):
        self.__title=t
    
    def set_director(self,name):
        self.__director=name
    
    def set_length(self,mins):
        self.__length=mins
        
    def set_genre(self,genre):
        self.__genre=genre
    
    def set_year(self,year):
        self.__year=year
    
    def get_title(self):
        return self.__title
    
    def get_director(self):
        return self.__director
    
    def get_length(self):
        return self.__length
    
    def get_genre(self):
        return self.__genre

    def get_year(self):
            return self.__year
    
    def get_movieinfo(self):
        return self.__title+","+self.__director+","+str(self.__length)+","+self.__genre+","+str(self.__year)

    def get_info(self):
        return (self.__title,self.__director,str(self.__length),self.__genre,str(self.__year))
