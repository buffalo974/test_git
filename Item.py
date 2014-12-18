# v 0.1  __18/12/2014___
# buffalo
# brouillon et essai github




# ============================================================================   *** CLASSE MERE ***  =======================================================

class Item():

	    def __init__(self, description=''):
		self.description = description
		self.typeItem = None # ===> Vivres = aliment / boisson ; arme ; protection ; ecritures ;  materiel craftable ; artefact
		# courte lame par défaut
		
		self.poid = 1
		self.place = 1
		self.usure = 0  # armes émoussées, armures cabossées, aliments avariés...
		
		
    def get_description(self):
        return description

# ============================================================================____MANGER ET BOIRE_____=======================================================		
		
class Vivres(Item):

    def __init__(self, description=''):
		self.description = description
		self.typeVivres = mangeable # par defaut :risque de pourrir, compact  ; buvable = necessite recipient,peu compacte,lourd.
		
		self.SatieteBonus = 1 # par defaut 
		self.HydratationBonus = 1 # par defaut : la pasteque rehydrate un peu , le jambon assoife.
		self.UsureCoeff = 1 # par defaut ; les viandes auront un fort coefficient d'usure, mais sont tres rassasiantes. Les aliments salés se conservent mais donnent soif.
		
		
		
		

    def get_description(self):
        return description		

class Mangeable(Vivres):

    def __init__(self, description=''):
		self.description = description
		
		
		

    def get_description(self):
        return description			

class Buveable(Vivres):

    def __init__(self, description=''):
		self.description = description
		
		
		

    def get_description(self):
        return description		
		
# ===============================================================================____ SE BATTRE ____=================================================================================





class Arme(Item):

    def __init__(self, description=''):
		self.description = description
		self.typeArme = courte_lame
		
		# courte lame par défaut ; longue lame ; rapiere ;  lance ; javelot ; arc ; arbalete ; fouet ; fumigene ; hache ; marteau ; fleau
		self.degat = 1
		self.portee = 1
		
		self.conso_mana = 0
		self.conso_ammo = 0
	

    def get_description(self):
        return description



		
class Protection(Item):

	def __init__(self, description=''):
		self.description = description
		self.typeProtection = maille
		# courte lame par défaut ; maille , plaque , ecailles,mythril
		self.anatomie = thorax # par defaut ; 
		# liste_equip_slot = ['tete','cou','main_D','main_G','poignet_D','poignet_G','carquoi','thorax','rachis','abdomen','jambe_D','jambe_G','pied_D','pied_G']
		self.absorption = 1 # par defaut



	def get_description(self):
		return description	


# ===============================================================================____ LE SAVOIR ET LA MAGIE ____===================================================================

# frequence_ecritures = dict(list(frequence_livre.items()) + list(frequence_grimoire.items()) + list(frequence_parchemin.items()))

A FAIRE______en cours

class Ecriture(Item):

	    def __init__(self, description=''):
		self.description = description
		
		
		
    def get_description(self):
        return description
