# Implementatie van de 2-3-4 Boom
# Door:			Sibert Aerts
# Tests door:	Othman Nahhas
# Revisie en verdere debugging door: Jonathan Van der Cruysse


class TwoThreeFourNode:
	""" Een Node van een 2-3-4 Boom. """

	def __init__(self, key=None, data=None):
	
		self.d1 = data		# De data items: 1, 2 en 3
		self.d2 = None
		self.d3 = None
	
		self.k1 = key			# De sleutels: 1, 2 en 3
		self.k2 = None
		self.k3 = None
		
		self.c1 = None		# De children: 1, 2, 3 en 4
		self.c2 = None
		self.c3 = None
		self.c4 = None
		
	def size(self):
		""" Geeft terug hoeveel items de node bevat. """
		
		if self.k1 == None:
			return 0
		if self.k2 == None:
			return 1
		if self.k3 == None:
			return 2
		return 3

	def count(self):
		""" Geeft het totale aantal elementen in de boom. """
		
		result = self.size()
		for item in [self.c1, self.c2, self.c3, self.c4]:
			if item != None:
				result += item.count()
		return result

	def rightmost_child(self):
		""" Zoekt het meest rechtse kind van de knop en geeft dat terug. """
		if self.size() < 2:
			return self.c2
		elif self.size() < 3:
			return self.c3
		else:
			return self.c4
		
	def is_leaf(self):
		""" Geeft een boolean terug die aangeeft of de node een blad is. """
		
		if self.c1 == None:
			return True
		return False
	
	def add_item(self, newKey, newData=None):
		""" Dit is een interne functie van het ADT en mag niet gebruikt worden van buitenaf. 
			 Voegt een item toe aan de hand van een sleutel 'newKey', de andere items en children in de node worden gepast opgeschoven. """
		
		if self.size() == 0:
			(self.k1, self.d1) = (newKey, newData)
		elif newKey < self.k1:
			(self.k1, self.k2, self.k3) = (newKey, self.k1, self.k2)
			(self.d1, self.d2, self.d3) = (newData, self.d1, self.d2)
			(self.c3, self.c4) = (self.c2, self.c3)
		elif self.size() == 1 or newKey < self.k2:
			(self.k2, self.k3) = (newKey, self.k2)
			(self.d2, self.d3) = (newData, self.d2)
			self.c4 = self.c3
		else:
			self.k3 = newKey
			self.d3 = newData
		
	def remove_item(self, itemNum):
		""" Dit is een interne functie van het ADT en mag niet gebruikt worden van buitenaf.
			 Verwijdert het 'itemNum'-de item uit de Node en schuift andere items op. Past echter children niet aan. """
		
		if itemNum < 2:
			(self.k1, self.d1) = (self.k2, self.d2)
		if itemNum < 3:
			(self.k2, self.d2) = (self.k3, self.d3)
		(self.k3, self.d3) = (None, None)
		
	def height(self):
		""" Recursieve functie die de hoogte van de deelbom met root 'self' teruggeeft. """
		
		if self.c1 == None:
			return 1
		else:
			return self.c1.height() + 1
			
	def IterateInorder(self):
		""" Itereert in volgorde over alle items in de boom. """

		if self.is_leaf():
			yield self.d1
			if self.size() > 1:
				yield self.d2
				if self.size() > 2:
					yield self.d3
		else:
			yield from self.c1.IterateInorder()
			yield self.d1
			yield from self.c2.IterateInorder()
			if self.size() > 1:
				yield self.d2
				yield from self.c3.IterateInorder()
				if self.size() > 2:
					yield self.d3
					yield from self.c4.IterateInorder()
			
	def __str__(self):
		""" Print de sleutels van de node af, voor debug doeleinden. """
		s = "(" + str(self.k1)
		if self.size() > 1:
			s += " | " + str(self.k2)
			if self.size() > 2:
				s += " | " + str(self.k3)
		s += ")"
		return s
			
class TwoThreeFourTree:
	""" Een 2-3-4 Boom. """
	
	def __init__(self):
		
		self.root = None
	
	def __str__(self):
		""" Geeft een visuele representatie van de keys in de hoogste twee niveaus van de boom, voor debug doeleinden."""
		s = ""
		s += " "*10 + str(self.root) + "\n"
		
		if self.root.is_leaf():
			return s
		elif self.root.size() == 1:
			s+= str(self.root.c1) + " " * 16 + str(self.root.c2)
		elif self.root.size() == 2:
			s+= str(self.root.c1) + " " * 8 + str(self.root.c2) + " " * 8 + str(self.root.c3)
		elif self.root.size() == 3:
			s+= str(self.root.c1) + " " * 5 + str(self.root.c2) + " " * 5 + str(self.root.c3) + " " * 5 + str(self.root.c4)
		return s

	def height(self):
		""" Geeft de hoogte van de boom terug. """
		return self.root.height
	
	def InsertItem(self, key, data=None):
		""" Voeg een nieuw item toe aan de 2-3-4 boom. Dit item wordt opgeslagen aan de hand van 'key' en bevat de data 'data'.
			'data' kan elk type zijn, 'key' moet strikt groter/kleiner zijn dan reeds gebruikte 'key's. """
		
		if self.root == None:
			newNode = TwoThreeFourNode(key, data)
			self.root = newNode
			return
		elif self.root.size() == 3:
			newroot = TwoThreeFourNode()		#Speciaal geval
			newroot.c1 = self.root
			self.root = newroot
			self.Split(newroot, 1)
		
	
		newSpot = self.root
		
		while not newSpot.is_leaf():
		
			if newSpot.size() == 1:
				if key < newSpot.k1:
					if newSpot.c1.size() == 3:
						self.Split(newSpot, 1)
						continue
					else:
						newSpot = newSpot.c1
				else: # Key >= k1
					if newSpot.c2.size() == 3:
						self.Split(newSpot, 2)
						continue
					else:
						newSpot = newSpot.c2
						
			else: # Newspot bevat 2 of 3 elementen
				if key < newSpot.k1:
					if newSpot.c1.size() == 3:
						self.Split(newSpot, 1)
						continue
					else:
						newSpot = newSpot.c1
				elif key < newSpot.k2:
					if newSpot.c2.size() == 3:
						self.Split(newSpot, 2)
						continue
					else:
						newSpot = newSpot.c2
				elif newSpot.size() == 2 or key < newSpot.k3:
					if newSpot.c3.size() == 3:
						self.Split(newSpot, 3)
						continue
					else:
						newSpot = newSpot.c3
				else: # De node bevat 3 elementen (kan enkel nadat een kind reeds gesplit is -> geen splitten meer) en de sleutel is groter dan alle 3 de sleutels
						newSpot = newSpot.c4
		
		# Uit de while loop: newSpot is het blad met minder dan 3 items waarin het item moet worden toegevoegd
		newSpot.add_item(key, data)

		
			
	def Split(self, parent, child):
		""" Interne operatie van het ADT 2-3-4 Boom, mag niet gebruikt worden van buitenaf. 
			 Het aangewezen kind van de gegeven parent wordt gepast gesplitst in 2 2-Nodes, terwijl de parent een 3-Node wordt. """
	
		if child == 1: 		# child == 0 is het speciale geval waarin de root gesplitst wordt, in welk geval de 'parent' een 0-node is
			splitNode = parent.c1
			
			newN1 = TwoThreeFourNode( splitNode.k1, splitNode.d1 )
			(newN1.c1, newN1.c2) = (splitNode.c1, splitNode.c2)
			
			newN2 = TwoThreeFourNode( splitNode.k3, splitNode.d3 )
			(newN2.c1, newN2.c2) = (splitNode.c3, splitNode.c4)
			
			parent.add_item(splitNode.k2, splitNode.d2)
			(parent.c1, parent.c2) = (newN1, newN2)
			
			del(splitNode)
		
		elif child == 2:
			splitNode = parent.c2
			
			newN1 = TwoThreeFourNode( splitNode.k1, splitNode.d1 )
			(newN1.c1, newN1.c2) = (splitNode.c1, splitNode.c2)
			
			newN2 = TwoThreeFourNode( splitNode.k3, splitNode.d3 )
			(newN2.c1, newN2.c2) = (splitNode.c3, splitNode.c4)
			
			parent.add_item(splitNode.k2, splitNode.d2)
			(parent.c2, parent.c3) = (newN1, newN2)
			
			del(splitNode)
			
		elif child == 3:
			splitNode = parent.c3
			
			newN1 = TwoThreeFourNode( splitNode.k1, splitNode.d1 )
			(newN1.c1, newN1.c2) = (splitNode.c1, splitNode.c2)
			
			newN2 = TwoThreeFourNode( splitNode.k3, splitNode.d3 )
			(newN2.c1, newN2.c2) = (splitNode.c3, splitNode.c4)
			
			parent.add_item(splitNode.k2, splitNode.d2)
			(parent.c3, parent.c4) = (newN1, newN2)
			
			del(splitNode)
			
	def Inorder(self, node=None):
		""" Print alle sleutels en items in de boom in volgorde af. """
	
		if node == None:
			node = self.root
		
		if node.is_leaf():
			print(str(node.k1) + " " + str(node.d1))
			if node.size() >1 :
				print(str(node.k2) + " " + str(node.d2))
				if node.size() > 2:
					print(str(node.k3) + " " + str(node.d3))
		else:
			self.Inorder(node.c1)
			print(str(node.k1) + " " + str(node.d1))
			self.Inorder(node.c2)
			if node.size() > 1:
				print(str(node.k2) + " " + str(node.d2))
				self.Inorder(node.c3)
				if node.size() > 2:
					print(str(node.k3) + " " + str(node.d3))
					self.Inorder(node.c4)
	
	
	
	def RemoveItem(self, key):
		""" Verwijdert het item met zoeksleutel 'key' uit de boom, geeft een boolean terug naargelang het item gevonden is of niet. """
	
		searchNode = self.root

		if searchNode == None:
			return False
		
		if searchNode.is_leaf() and searchNode.size() == 1:
			if searchNode.k1 == key:
				self.root = None
				return True
			return False
		
		swapped = False
			
		while not searchNode.is_leaf():
			
			if not swapped:
			# Check of de key in de huidige node zit
				if key == searchNode.k1:
					(searchNode, swapped) = self.swapInorder(searchNode, 1)
					continue
				elif searchNode.size() > 1 and key == searchNode.k2:
					(searchNode, swapped) = self.swapInorder(searchNode, 2)
					continue
				elif searchNode.size() > 2 and key == searchNode.k3:
					(searchNode, swapped) = self.swapInorder(searchNode, 3)
					continue
					
		
			# key zit niet in de huidige node: check welke child de key wel kan bevatten
			
			if key < searchNode.k1:
				if searchNode.c1.size() == 1:
					self.Merge(searchNode, 1)
					continue
				else:
					searchNode = searchNode.c1
			elif searchNode.size() == 1 or key < searchNode.k2:
				if searchNode.c2.size() == 1:
					self.Merge(searchNode, 2)
					continue
				else:
					searchNode = searchNode.c2
			elif searchNode.size() == 2 or key < searchNode.k3:
				if searchNode.c3.size() == 1:
					self.Merge(searchNode, 3)
					continue
				else:
					searchNode = searchNode.c3
			else: #Searchnode bevat 3 elementen en key is groter dan de derde zoeksleutel
				if searchNode.c4.size() == 1:	
					self.Merge(searchNode, 4)
					continue
				else:
					searchNode = searchNode.c4
						
		
		# searchNode is een blad die mogelijk key bevat
		
		if key == searchNode.k1:
			searchNode.remove_item(1)
			return True
		elif key == searchNode.k2:
			searchNode.remove_item(2)
			return True
		elif searchNode.size() > 2 and key == searchNode.k3:
			searchNode.remove_item(3)
			return True
		else:
			return False
					
			
		
	def swapInorder(self, node, itemNum):
		""" Dit is een interne functie van het ADT en mag niet gebruikt worden van buitenaf.  
			 Verwisselt een item in een gegeven (niet-blad) node met zijn inorder successor. Na dit gedaan te hebben geeft het de parent van de node waarin het item zich nu bevindt terug. """
		
		if itemNum == 1:
			if node.c2.size() == 1:
				self.Merge(node, 2)
				return (node, False)
			searchNode = node.c2
		elif itemNum == 2:
			if node.c3.size() == 1:
				self.Merge(node, 3)
				return (node, False)
			searchNode = node.c3
		else: # itemNum == 3
			if node.c4.size() == 1:
				self.Merge(node, 4)
				return (node, False)
			searchNode = node.c4
		
		while not searchNode.is_leaf():
			if searchNode.c1.size() == 1:
				self.Merge(searchNode, 1)
			else:
				searchNode = searchNode.c1
		
		#searchNode is een blad, het eerste item in searchNode is de inorder successor
		if itemNum == 1:
			(node.k1, node.d1, searchNode.k1, searchNode.d1) = (searchNode.k1, searchNode.d1, node.k1, node.d1)
		elif itemNum == 2:
			(node.k2, node.d2, searchNode.k1, searchNode.d1) = (searchNode.k1, searchNode.d1, node.k2, node.d2)
		else: #itemNum == 3
			(node.k3, node.d3, searchNode.k1, searchNode.d1) = (searchNode.k1, searchNode.d1, node.k3, node.d3)

		return (searchNode, True)

		
		
	def Merge(self, parent, nodeNum):
		""" Dit is een interne functie van het ADT en mag niet gebruikt worden van buitenaf.
			 De aangewezen node van de gegeven parent wordt gemerged. Dit kan een vermindering in de hoeveelheid nodes/niveaus in de boom teweegbrengen. """
		
		sibR = None
		sibL = None
		
		if nodeNum == 1:
			node = parent.c1
			sibR = parent.c2
		if nodeNum == 2:
			sibL = parent.c1
			node = parent.c2
			if parent.size() > 1:
				sibR = parent.c3
		if nodeNum == 3:
			sibL = parent.c2
			node = parent.c3
			if parent.size() > 2:
				sibR = parent.c4
		if nodeNum == 4:
			sibL = parent.c3
			node = parent.c4
			
		if sibL != None and sibL.size() > 1:
			if sibL.size() == 2:
				if nodeNum == 2:
					node.add_item(parent.k1, parent.d1)
					(parent.k1, parent.d1) = (sibL.k2, sibL.d2)
				if nodeNum == 3:
					node.add_item(parent.k2, parent.d2)
					(parent.k2, parent.d2) = (sibL.k2, sibL.d2)
				if nodeNum == 4:
					node.add_item(parent.k3, parent.d3)
					(parent.k3, parent.d3) = (sibL.k2, sibL.d2)
				(node.c1, sibL.c3, sibL.k2, sibL.d2) = (sibL.c3, None, None, None)
				
			if sibL.size() == 3:
				if nodeNum == 2:
					node.add_item(parent.k1, parent.d1)
					(parent.k1, parent.d1) = (sibL.k3, sibL.d3)
				if nodeNum == 3:
					node.add_item(parent.k2, parent.d2)
					(parent.k2, parent.d2) = (sibL.k3, sibL.d3)
				if nodeNum == 4:
					node.add_item(parent.k3, parent.d3)
					(parent.k3, parent.d3) = (sibL.k3, sibL.d3)
				(node.c1, sibL.c4, sibL.k3, sibL.d3) = (sibL.c4, None, None, None)
		
		elif sibR != None and sibR.size() > 1:
			if nodeNum == 1:
				node.add_item(parent.k1, parent.d1)
				(parent.k1, parent.d1) = (sibR.k1, sibR.d1)
			if nodeNum == 2:
				node.add_item(parent.k2, parent.d2)
				(parent.k2, parent.d2) = (sibR.k1, sibR.d1)
			if nodeNum == 3:
				node.add_item(parent.k3, parent.d3)
				(parent.k3, parent.d3) = (sibR.k1, sibR.d1)
			(node.c3, sibR.c1, sibR.c2, sibR.c3, sibR.c4) = (sibR.c1, sibR.c2, sibR.c3, sibR.c4, None)
			
		# De node's siblings hebben geen overtollige items, er zal gemerged moeten worden met de parent.
		
		elif parent.size() == 1:		# Speciaal geval: Dit kan enkel gebeuren als de parent de root van de boom is
			leftNode = parent.c1	# Het maakt niet uit welke van deze 2 de te mergen node is, het resultaat is hoe dan ook hetzelfde
			rightNode = parent.c2
			
			(parent.k2, parent.d2) = (parent.k1, parent.d1) 
			(parent.k1, parent.d1, parent.c1, parent.c2) = (leftNode.k1, leftNode.d1, leftNode.c1, leftNode.c2)
			(parent.k3, parent.d3, parent.c3, parent.c4) = (rightNode.k1, rightNode.d1, rightNode.c1, rightNode.c2)
			del(leftNode)
			del(rightNode)
		
		elif parent.size() == 2:
			if nodeNum < 3:		# We mergen de eerste twee nodes zowel als de eerste of de tweede de "te mergen" node is.
				leftNode = parent.c1
				rightNode = parent.c2
				
				leftNode.add_item(parent.k1, parent.d1)							# De linkernode wordt de gemergede node
				leftNode.add_item(rightNode.k1, rightNode.d1)
				(leftNode.c3, leftNode.c4) = (rightNode.c1, rightNode.c2)
				
				parent.remove_item(1)													# De parent wordt aangepast
				(parent.c2, parent.c3) = (parent.c3, None)
				
				del(rightNode)
				
				
			if nodeNum == 3:
				leftNode = parent.c2
				rightNode = parent.c3
				
				leftNode.add_item(parent.k2, parent.d2)							# De linkernode wordt de gemergede node
				leftNode.add_item(rightNode.k1, rightNode.d1)
				(leftNode.c3, leftNode.c4) = (rightNode.c1, rightNode.c2)
				
				parent.remove_item(2)													# De parent wordt aangepast
				(parent.c3) = (None)
				
				del(rightNode)
		
		
		elif parent.size() == 3:
			if nodeNum < 3:		# We mergen de eerste twee nodes
				leftNode = parent.c1
				rightNode = parent.c2
				
				leftNode.add_item(parent.k1, parent.d1)							# De linkernode wordt de gemergede node
				leftNode.add_item(rightNode.k1, rightNode.d1)
				(leftNode.c3, leftNode.c4) = (rightNode.c1, rightNode.c2)
				
				parent.remove_item(1)													# De parent wordt aangepast
				(parent.c2, parent.c3, parent.c4) = (parent.c3, parent.c4, None)
				del(rightNode)
				
				
			if nodeNum > 2:		# We mergen de laatste twee nodes
				leftNode = parent.c3
				rightNode = parent.c4
				
				leftNode.add_item(parent.k3, parent.d3)							# De linkernode wordt de gemergede node
				leftNode.add_item(rightNode.k1, rightNode.d1)
				(leftNode.c3, leftNode.c4) = (rightNode.c1, rightNode.c2)
				
				parent.remove_item(3)													# De parent wordt aangepast
				(parent.c4) = (None)
				
				del(rightNode)
		
		
		
	def RetrieveItem(self, key):
		""" Vindt het item met gegeven 'key', als het dit vindt geeft het de data van dat item terug, als het dit niet vind geeft het de waarde None terug."""
		searchNode = self.root
		
		while True:
			if searchNode == None:
				return None

			if searchNode.k1 == key:
				return searchNode.d1
			elif searchNode.k2 == key:
				return searchNode.d2
			elif searchNode.k3 == key:
				return searchNode.d3
					
			else: # Het item is niet gevonden
				if searchNode.is_leaf():	# searchNode was het laatste item
					return None
				else:
					if key < searchNode.k1:	
						searchNode = searchNode.c1
						continue
					elif searchNode.size() > 1 and key < searchNode.k2:
						searchNode = searchNode.c2
						continue
					elif searchNode.size() > 2 and key < searchNode.k3:
						searchNode = searchNode.c3
						continue
					else: # size is 3 en key > de derde key van de node
						searchNode = searchNode.rightmost_child()
