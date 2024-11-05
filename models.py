from database import connect_db


class SeasonalFlavor:
    # models for managing seasonal flavour offerings in the chocolate house
    @staticmethod
    def add_flavor(name, availability):
        ## Add a new seasonal flavour to the seasonal_flavour table
        # Args: 
        # name (str) : The name of the flavour (ex:  "pumpkin spice")
        # availability (str): The season or avialbilty status
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO seasonal_slavprs (flavor_name, avilability) VALUES ( ?, ?)", (name, availability))
        conn.comite()
        conn.close()
class IngredientInventory:

    @staticmethod
    def add_ingredient(name, quantity):
       # Args:
       #     name (str): The name of the ingredient (e.g., "Cocoa Powder").
        #    quantity (int): The quantity available (e.g., 100).
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", (name, quantity))
        conn.commit()
        conn.close()


class CustomerSuggestion:
    @staticmethod
    def add_suggestion(name, suggestion, allergy):

        # Args:
        #   name (str): Customer's name providing the suggestion.
        #    suggestion (str): The suggested flavor (e.g., "Mint Chocolate").
        #    allergy (str): Allergy concerns noted by the customer (e.g., "None" or "Peanuts").

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customer_suggestion (customer_name, slavor_suggestion, allergy_consern) VALUES (?, ?, ?)", (*name, suggestion, allergy))
        conn.commit()
        conn.close()


