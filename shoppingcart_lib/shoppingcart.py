class Cart:
    def __init__(self) -> None:
        self.__data = {}

    def tambahProduk(self, kodeProduk, kuantitas):
        if kodeProduk in self.__data.keys():
            self.__data[kodeProduk] += kuantitas
        else:
            self.__data[kodeProduk] = kuantitas
    
    def hapusProduk(self, kodeProduk):
        if kodeProduk in self.__data.keys():
            self.__data.pop(kodeProduk)

    def getCart(self):
        if bool(self.__data):
            return self.__data

    def tampilkanCart(self):
        if bool(self.__data):
            for key, val in self.__data.items():
                print(key+" ("+str(val)+")")
