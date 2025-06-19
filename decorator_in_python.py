def mazak(fun):
    def mazak():
        print("Hello Masti karte hein")
        fun()
        print("Hello masti ho gyi")
    return mazak
@mazak
def printing():
    print("Narsingh is king")

printing()
