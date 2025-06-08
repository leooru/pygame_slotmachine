class CreateResults:
    def __init__(self,icon_dict):#constuctor
        #for get_icon_name variables
        self.icon_apple = icon_dict["apple"]
        self.icon_banana = icon_dict["banana"]
        self.icon_book = icon_dict["book"]
        self.icon_cherry = icon_dict["cherry"]
        self.icon_seven = icon_dict["seven"]

        self.icon1_name = ""
        self.icon2_name = ""
        self.icon3_name = ""
        self.icon4_name = ""
        #for amount_combination variables
        self.amount_icon = 1
        self.counter = True
        self.icon1_2 = 0
        self.icon2_3 = 0
        self.icon3_4 = 0

    def amount_combination(self, icon1, icon2, icon3, icon4):
        """This function looks at how many identical icons are next to each other
        e.g. icon1 = apple, icon2 = apple, icon3 = banana, icon4 = book
        output would be 2 because 2 apple are side by side"""

        self.amount_icon = 1
        self.counter = True
        self.icon1_2 = 0
        self.icon2_3 = 0
        self.icon3_4 = 0
        self.icon12 = 0
        self.icon23 = 0
        self.icon34 = 0


        #Überprüfen, ob beide Bilder dieselbe Größe haben für icon1 und icon2
        #icon1 und icon2
        if icon1.get_size() != icon2.get_size():
            self.counter = False # falls etwas nicht passt, dann setzt counter FALSE und der amount_icon geht nicht hoch, somit keine gleiche Bilder nebeneinander

        # Pixelweise vergleichen
        for x in range(icon1.get_width()):
            for y in range(icon1.get_height()):
                if icon1.get_at((x, y)) != icon2.get_at((x, y)):
                    self.counter = False

        if self.counter:
            self.icon12 = 1
            self.amount_icon +=1

        self.counter = True

        #icon2 und icon3
        if icon2.get_size() != icon3.get_size():
            self.counter = False

        # Pixelweise vergleichen
        for x in range(icon2.get_width()):
            for y in range(icon2.get_height()):
                if icon2.get_at((x, y)) != icon3.get_at((x, y)):
                    self.counter = False

        if self.counter:
            self.amount_icon +=1
            self.icon23 = 1

        self.counter = True

        #icon3 und icon4
        if icon3.get_size() != icon4.get_size():
            self.counter = False

        #Pixelweise vergleichen
        for x in range(icon3.get_width()):
            for y in range(icon3.get_height()):
                if icon3.get_at((x, y)) != icon4.get_at((x, y)):
                    self.counter = False

        if self.counter:
            self.amount_icon += 1
            self.icon34 = 1
        return (
            self.amount_icon, # gibt am ende dann die anzahl an icons die nebeneinander liegen aus
            self.icon12,
            self.icon23,
            self.icon34
        )


    def get_icon_name(self, icon1, icon2, icon3, icon4):#finds out which icon has which name
        self.icon1_name = ""
        self.icon2_name = ""
        self.icon3_name = ""
        self.icon4_name = ""

        icon_map = {
            id(self.icon_apple): "apple",
            id(self.icon_banana): "banana",
            id(self.icon_book): "book",
            id(self.icon_cherry): "cherry",
            id(self.icon_seven): "seven"
        }
        return(
            icon_map.get(id(icon1), "unkown"),
            icon_map.get(id(icon2), "unkown"),
            icon_map.get(id(icon3), "unkown"),
            icon_map.get(id(icon4), "unkown")
        )

    def evalutation(self, amount_icon_local, icon12_local, icon23_local, icon34_local, icon1_name_local, icon2_name_local, icon3_name_local, icon4_name_local, wallet_local, entry_local):
        #determines the profit
        gewinn = 0
        match amount_icon_local:
            case 4:
                if icon12_local == 1 and icon23_local == 1 and icon34_local == 1:
                    match icon1_name_local:
                        case "apple":
                            gewinn = entry_local * 100
                            wallet_local += gewinn
                        case "banana":
                            gewinn = entry_local * 100
                            wallet_local += gewinn
                        case "book":
                            gewinn = entry_local * 100
                            wallet_local += gewinn
                        case "cherry":
                            gewinn = entry_local * 100
                            wallet_local += gewinn
                        case "seven":
                            gewinn = entry_local * 100
                            wallet_local += gewinn

            case 3:
                if icon12_local == 1 and icon23_local == 1:
                    match icon2_name_local:
                        case "apple":
                            gewinn = entry_local * 5
                            wallet_local += gewinn
                        case "banana":
                            gewinn = entry_local * 5
                            wallet_local += gewinn
                        case "book":
                            gewinn = entry_local * 15
                            wallet_local += gewinn
                        case "cherry":
                            gewinn = entry_local * 10
                            wallet_local += gewinn
                        case "seven":
                            gewinn = entry_local * 25
                            wallet_local += gewinn

                elif icon23_local == 1 and icon34_local == 1:
                    match icon2_name_local:
                        case "apple":
                            gewinn = entry_local * 5
                            wallet_local += gewinn
                        case "banana":
                            gewinn = entry_local * 5
                            wallet_local += gewinn
                        case "book":
                            gewinn = entry_local * 15
                            wallet_local += gewinn
                        case "cherry":
                            gewinn = entry_local * 10
                            wallet_local += gewinn
                        case "seven":
                            gewinn = entry_local * 25
                            wallet_local += gewinn
            case 2:
                if icon12_local == 1:
                    match icon1_name_local:
                        case "apple":
                            gewinn = entry_local * 2
                            wallet_local += gewinn
                        case "banana":
                            gewinn = entry_local * 2
                            wallet_local += gewinn
                        case "book":
                            gewinn = entry_local * 5
                            wallet_local += gewinn
                        case "cherry":
                            gewinn = entry_local * 3
                            wallet_local += gewinn
                        case "seven":
                            gewinn = entry_local * 7
                            wallet_local += gewinn
                elif icon23_local == 1:
                    match icon2_name_local:
                        case "apple":
                            gewinn = entry_local * 2
                            wallet_local += gewinn
                        case "banana":
                            gewinn = entry_local * 2
                            wallet_local += gewinn
                        case "book":
                            gewinn = entry_local * 5
                            wallet_local += gewinn
                        case "cherry":
                            gewinn = entry_local * 3
                            wallet_local += gewinn
                        case "seven":
                            gewinn = entry_local * 7
                            wallet_local += gewinn
                elif icon34_local == 1:
                    match icon3_name_local:
                        case "apple":
                            gewinn = entry_local * 2
                            wallet_local += gewinn
                        case "banana":
                            gewinn = entry_local * 2
                            wallet_local += gewinn
                        case "book":
                            gewinn = entry_local * 5
                            wallet_local += gewinn
                        case "cherry":
                            gewinn = entry_local * 3
                            wallet_local += gewinn
                        case "seven":
                            gewinn = entry_local * 7
                            wallet_local += gewinn
            case 1:
                gewinn = 0
        return wallet_local, gewinn
