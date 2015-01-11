# Implementatie van de 2-3-4 Boom
# Door:			Sibert Aerts
# Tests door:	Othman Nahhas
# Revisie en verdere debugging door: Jonathan Van der Cruysse


class TwoThreeFourNode:
    """ Een Node van een 2-3-4 Boom. """

    def __init__(self, key=None, data=None):

        self.data = [data, None, None] # De data items: 1, 2 en 3
        self.keys = [key, None, None] # De sleutels: 1, 2 en 3
        self.children = [None] * 4 # De children: 1, 2, 3 en 4

    @property
    def d1(self):
        """ Geeft het eerste data-element terug. """
        return self.data[0]
    
    @d1.setter
    def d1(self, value):
        """ Geeft de waarde 'value' aan het eerste data-element. """
        self.data[0] = value

    @property
    def d2(self):
        """ Geeft het tweede data-element terug. """
        return self.data[1]
    
    @d2.setter
    def d2(self, value):
        """ Geeft de waarde 'value' aan het tweede data-element. """
        self.data[1] = value

    @property
    def d3(self):
        """ Geeft het derde data-element terug. """
        return self.data[2]
    
    @d3.setter
    def d3(self, value):
        """ Geeft de waarde 'value' aan het derde data-element. """
        self.data[2] = value

    @property
    def k1(self):
        """ Geeft de eerste key terug. """
        return self.keys[0]
    
    @k1.setter
    def k1(self, value):
        """ Geeft de waarde 'value' aan de eerste key. """
        self.keys[0] = value

    @property
    def k2(self):
        """ Geeft de tweede key terug. """
        return self.keys[1]
    
    @k2.setter
    def k2(self, value):
        """ Geeft de waarde 'value' aan de tweede key. """
        self.keys[1] = value

    @property
    def k3(self):
        """ Geeft de derde key terug. """
        return self.keys[2]
    
    @k3.setter
    def k3(self, value):
        """ Geeft de waarde 'value' aan de derde key. """
        self.keys[2] = value

    @property
    def c1(self):
        """ Geeft het eerste kind terug. """
        return self.children[0]
    
    @c1.setter
    def c1(self, value):
        """ Geeft de waarde 'value' aan het eerste kind. """
        self.children[0] = value

    @property
    def c2(self):
        """ Geeft het tweede kind terug. """
        return self.children[1]
    
    @c2.setter
    def c2(self, value):
        """ Geeft de waarde 'value' aan het tweede kind. """
        self.children[1] = value

    @property
    def c3(self):
        """ Geeft het derde kind terug. """
        return self.children[2]
    
    @c3.setter
    def c3(self, value):
        """ Geeft de waarde 'value' aan het derde kind. """
        self.children[2] = value

    @property
    def c4(self):
        """ Geeft het vierde kind terug. """
        return self.children[3]
    
    @c4.setter
    def c4(self, value):
        """ Geeft de waarde 'value' aan het vierde kind. """
        self.children[3] = value
        
    def size(self):
        """ Geeft terug hoeveel items de node bevat. """
        # Het aantal elementen in de knop komt overeen met het maximaal aantal keys min het aantal keys die niet ingevuld zijn.
        # int(k is None) geeft 1 als k None is, en 0 als k niet None is.
        return 3 - sum([int(k is None) for k in self.keys])

    def get_key_index(self, key, comparer = lambda x, y: x == y):
        """ Gets the index of the leftmost key in this node that matches the given key. 
            Said match is provided by a comparison function, which defaults to equality.
            If no key matches the given key, -1 is returned. """
        for i in range(0, len(self.keys)):
            if self.keys[i] is not None and comparer(key, self.keys[i]):
                return i + 1 # Indices beginnen hier vanaf 1
        return -1

    def get_key(self, i):
        """ Geeft de i-de key van deze knoop, indien die bestaat. Anders, None. """
        return self.keys[i - 1]

    def get_child(self, i):
        """ Geeft het i-de kind van deze knop, indien dat bestaat. Anders, None. """
        if i - 1 not in range(0, len(self.children)):
            return None
        return self.children[i - 1]

    def get_children(self, i, count):
        """ Geeft 'count' kinderen, beginnende met het i-de kind van deze knop. """
        return self.children[i - 1 : i - 1 + count]

    def set_child(self, i, child):
        """ Zet het gegeven kind in 'child' als i-de kind in deze knoop. """
        self.children[i - 1] = child

    def set_children(self, i, children):
        """ Wijst de gegeven kinderen in 'children' toe aan deze knop, te beginnen bij het i-de kind.
            Zo voert tree.set_children(3, [node1, node2]) de volgende actie uit: tree.c3 <- node1, tree.c4 <- node2 """
        for j in range(len(children)):
            self.set_child(i + j, children[j])

    def shift_children_left(self, index):
        """ Shifts alle kinderen van de knop een plaats naar links, vanaf 'index + 1'. """
        for i in range(index, len(self.children) + 1): # Kind op 'index' wordt gewoon overschreven. Dit zou altijd None moeten zijn.
            self.set_child(i, self.get_child(i + 1))
        self.children[len(self.children) - 1] = None # Laatste kind wordt 'None' om te vermijden dat kinderen gedupliceerd worden

    def shift_children_right(self, index):
        """ Shifts alle kinderen van de knop een plaats naar rechts, vanaf 'index'. """
        for i in reversed(range(index, len(self.children))): # Meest rechtse kind wordt gewoon overschreven. Dit zou altijd None moeten zijn.
            self.set_child(i + 1, self.get_child(i))
        self.set_child(index, None)

    def remove_child(self, i):
        """ Verwijdert het i-de kind uit de knop. """
        self.shift_children_left(i)

    def get_containing_child_index(self, key):
        """ Zoekt de index van het kind dat de gegeven key zou kunnen bevatten, in de assumptie dat deze node dat niet doet. """
        key_index = self.get_key_index(key, lambda x, y: x < y)
        if key_index == -1:
            return self.rightmost_child_index()
        else: # Een key is gevonden. Deze komt overeen met de meest rechtse key die groter dan of gelijk aan 'key' is
            return key_index

    def get_containing_child(self, key):
        """ Zoekt het kind dat de gegeven key zou kunnen bevatten, in de assumptie dat deze node dat niet doet. """
        return self.get_child(self.get_containing_child_index(key))

    def count(self):
        """ Geeft het totale aantal elementen in de boom. """
        
        result = self.size()
        for item in [self.c1, self.c2, self.c3, self.c4]:
            if item != None:
                result += item.count()
        return result

    def rightmost_child(self):
        """ Zoekt het meest rechtse kind van de knop en geeft dat terug. """
        return self.get_child(self.rightmost_child_index())

    def rightmost_child_index(self):
        """ Zoekt de index van het meest rechtse kind van de knop. """
        return self.size() + 1

    def get_halves(self):
        """ Verdeelt de boom in twee helften: het linker field met de linker kinderen en het rechter field met de rechter kinderen. 
            Deze worden vervolgens teruggegeven als een tupel.
            Deze methode kan enkel succesvol opgeroepen worden bij een 3-knop. """
        
        newN1 = TwoThreeFourNode(self.k1, self.d1)
        (newN1.c1, newN1.c2) = (self.c1, self.c2)

        newN2 = TwoThreeFourNode(self.k3, self.d3)
        (newN2.c1, newN2.c2) = (self.c3, self.c4)
        
        return (newN1, newN2)
        
    def is_leaf(self):
        """ Geeft een boolean terug die aangeeft of de node een blad is. """
        
        if self.c1 == None:
            return True
        return False

    def get_item(self, i):
        """ Geeft een tupel die de key en data van het i-de data field van deze node bevat. """
        return (self.keys[i - 1], self.data[i - 1])

    def set_item(self, i, item):
        """ Associeert 'key' en 'data' met het i-de data field van deze node. """
        (key, data) = item
        self.keys[i - 1] = key
        self.data[i - 1] = data

    def copy_item(self, i, target):
        """ Kopieert het item met index 'i' naar node 'target'. """
        (k, d) = self.get_item(i)
        target.add_item(k, d)

    def move_item(self, sourceIndex, targetIndex, target):
        """ Verplaatst het item met index 'sourceIndex' vanuit deze knop naar het data field met index 'targetIndex' van 'target' """
        target.set_item(targetIndex, self.get_item(sourceIndex))
        self.remove_item(sourceIndex)
    
    def add_item(self, newKey, newData=None):
        """ Dit is een interne functie van het ADT en mag niet gebruikt worden van buitenaf. 
             Voegt een item toe aan de hand van een sleutel 'newKey', de andere items en children in de node worden gepast opgeschoven. """
        
        if self.size() == 0:
            (self.k1, self.d1) = (newKey, newData)
        elif newKey < self.k1:
            (self.k1, self.k2, self.k3) = (newKey, self.k1, self.k2)
            (self.d1, self.d2, self.d3) = (newData, self.d1, self.d2)
            # Kinderen een plaats naar rechts opschuiven
            (self.c2, self.c3, self.c4) = (self.c1, self.c2, self.c3)
        elif self.size() == 1 or newKey < self.k2:
            (self.k2, self.k3) = (newKey, self.k2)
            (self.d2, self.d3) = (newData, self.d2)
            # Kinderen een plaats naar rechts opschuiven, vanaf key #2
            (self.c3, self.c4) = (self.c2, self.c3)
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

        i = 0
        isParent = not self.is_leaf()
        if isParent:
            yield from self.children[0].IterateInorder()
        while i < len(self.data) and self.data[i] is not None:
            yield self.data[i]
            if isParent:
                yield from self.children[i + 1].IterateInorder()
            i += 1
            
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
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        """ Geeft een visuele representatie van de keys in de hoogste twee niveaus van de boom, voor debug doeleinden."""
        s = ""
        s += " " * 10 + str(self.root) + "\n"
        
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
            newroot = TwoThreeFourNode()		# Speciaal geval
            newroot.c1 = self.root
            self.root = newroot
            self.Split(newroot, 1)
        
        newSpot = self.root
        
        while not newSpot.is_leaf():
            nextIndex = newSpot.get_containing_child_index(key)
            nextChild = newSpot.get_child(nextIndex)
            if nextChild.size() == 3:
                self.Split(newSpot, nextIndex)
            else:
                newSpot = nextChild
        
        # Uit de while loop: newSpot is het blad met minder dan 3 items waarin
        # het item moet worden toegevoegd
        newSpot.add_item(key, data)
            
    def Split(self, parent, childIndex):
        """ Interne operatie van het ADT 2-3-4 Boom, mag niet gebruikt worden van buitenaf. 
            Het aangewezen kind van de gegeven parent wordt gepast gesplitst in 2 2-Nodes, terwijl de parent een 2- of 3-Node wordt.
            Dit kind moet een 3-node zijn. """

        # Kind zoeken
        splitNode = parent.get_child(childIndex)

        # Kind verdelen in twee helften
        splitHalves = splitNode.get_halves()

        # Middelste item in het kind naar de ouder verplaatsen.
        parent.add_item(splitNode.k2, splitNode.d2)
        #parent.shift_children_right(childIndex + 1)
        # Helften toevoegen aan het kind
        parent.set_children(childIndex, splitHalves)    
    
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
                keyIndex = searchNode.get_key_index(key)
                if keyIndex != -1: # Key is gevonden. Swap inorder.
                    (searchNode, swapped) = self.swapInorder(searchNode, keyIndex)
                    continue
        
            # key zit niet in de huidige node: check welke child de key wel kan
            # bevatten
            
            childIndex = searchNode.get_containing_child_index(key)
            child = searchNode.get_child(childIndex)
            if child.size() == 1: 
                # Onderweg nodes mergen indien nodig
                self.Merge(searchNode, childIndex)
            else:
                searchNode = child
        
        # searchNode is een blad dat mogelijk de key bevat

        keyIndex = searchNode.get_key_index(key) # Key zoeken
        if keyIndex != -1:
            searchNode.remove_item(keyIndex) # Key gevonden -> Item verwijderen
            return True
        else:
            return False # Key niet gevonden
        
    def swapInorder(self, node, itemNum):
        """ Dit is een interne functie van het ADT en mag niet gebruikt worden van buitenaf.  
            Verwisselt een item in een gegeven (niet-blad) node met zijn inorder successor. 
            Na dit gedaan te hebben geeft het de parent van de node waarin het item zich nu bevindt terug. """
        
        searchNode = node.get_child(itemNum + 1) # Zoekactie begint bij kind i + 1 (waar 'i' de index van het data-element in de 2-3-4 boom-knop is)
        if searchNode.size() == 1: # Als dit kind slechts 1 item bevat, mergen we dit kind
            self.Merge(node, itemNum + 1)
            return (node, False)
            
        while not searchNode.is_leaf(): # Naar 'links', i.e. het eerste kind, blijven gaan tot een blad bereikt is
            if searchNode.c1.size() == 1:
                self.Merge(searchNode, 1) # Als het kind van grootte 1 is, merge
            else:
                searchNode = searchNode.c1
        
        # searchNode is een blad, het eerste item in searchNode is de inorder successor
        # Wisselen van key en data item met meest linkse key en data in node
        (node.keys[itemNum - 1], node.data[itemNum - 1], searchNode.k1, searchNode.d1) = (searchNode.k1, searchNode.d1, node.keys[itemNum - 1], node.data[itemNum - 1])

        return (searchNode, True)

    def Merge(self, parent, nodeNum):
        """ Dit is een interne functie van het ADT en mag niet gebruikt worden van buitenaf.
            De aangewezen node van de gegeven parent wordt gemerged. Dit kan een vermindering in de hoeveelheid nodes/niveaus in de boom teweegbrengen. 
            Merge dient alleen maar uitgevoerd te worden als 'parent.get_child(nodeNum)' een kind oplevert met 1 item. """

        sibL = parent.get_child(nodeNum - 1)
        node = parent.get_child(nodeNum)
        sibR = parent.get_child(nodeNum + 1)
            
        # Indien de linker sibling meer dan 2 kinderen heeft, worden die aangetast om te 'mergen'
        if sibL != None and sibL.size() > 1:
            # Index van linker sibling's meest rechts kind nu al berekenen voor de keys worden veranderd (die beinvloeden immers de grootte)
            # Idem voor grootte van de linker sibling
            sibLRightIndex = sibL.rightmost_child_index()
            sibLSize = sibL.size()
            # Het item links in de parent ten opzichte van de node wordt naar de node verplaatst
            parent.copy_item(nodeNum - 1, node)
            # Meest rechtse item wordt overgedragen van de sibling naar de parent
            # (overschrijft het item links in de parent ten opzichte van de node)
            sibL.move_item(sibLSize, nodeNum - 1, parent)
            # Linker sibling's meest rechtse kind wordt verplaatst naar node:
            # Meest linkse kind van node wordt overschreven door sibling's meest rechtse kind
            node.set_child(1, sibL.get_child(sibLRightIndex))
            # Verplaatste kind wordt uit linker sibling verwijderd
            sibL.remove_child(sibLRightIndex)
        # Als er geen linker sibling is, maar wel een rechter sibling, die aan die voorwaarde voldoet, wordt de rechter sibling gebruikt
        elif sibR != None and sibR.size() > 1:
            # Het item rechts in de parent ten opzichte van de node wordt naar de node verplaatst
            parent.copy_item(nodeNum, node)
            # Meest linkse item wordt overgedragen van de sibling naar de parent
            # (overschrijft het item rechts in de parent ten opzichte van de node)
            sibR.move_item(1, nodeNum, parent)
            # Rechter sibling's meest linkse kind wordt verplaatst naar node
            # Meest rechtse kind van node wordt overschreven door sibling's meest linkse kind
            node.c3 = sibR.c1
            # Kinderen van rechter sibling worden naar rechts opgeschoven, meest linkse kind wordt verwijderd
            sibR.remove_child(1)
            
        # De node's siblings hebben precies 1 item, er zal gemerged
        # moeten worden met de parent.
        elif parent.size() == 1:		# Speciaal geval: Dit kan enkel gebeuren als de parent de root van de boom is
            leftNode = parent.c1	    # Het maakt niet uit welke van deze 2 de te mergen node is, het resultaat is
                                        # hoe dan ook hetzelfde
            rightNode = parent.c2
            
            (parent.k2, parent.d2) = (parent.k1, parent.d1) 
            (parent.k1, parent.d1, parent.c1, parent.c2) = (leftNode.k1, leftNode.d1, leftNode.c1, leftNode.c2)
            (parent.k3, parent.d3, parent.c3, parent.c4) = (rightNode.k1, rightNode.d1, rightNode.c1, rightNode.c2)
        
        else:
            # De parent is van grootte 2 of 3.
            # Een node zal verwijderd worden, de inhoud ervan gemerged richting de linker sibling.
            # Die linker sibling zal dan van grootte 3 zijn, terwijl de parent een kind, en dus een item, verliest.

            # We mergen de eerste twee nodes zowel als de eerste of de tweede de 
            # "te mergen" node is. Deze stap gebeurt om zeker twee werkbare nodes te hebben om te mergen.
            rightNodeNum = 2 if nodeNum == 1 else nodeNum      

            # Twee siblings mergen, een linkse en een rechtse
            # Omdat de eerste if en elif cases niet bereikt zijn, 
            # en door de preconditie in de beschrijving van deze methode,
            # weten we dat deze allebei 1 item bevatten.
            leftNode = parent.get_child(rightNodeNum - 1)
            rightNode = parent.get_child(rightNodeNum)

            # Linkernode wordt de gemergede node
            # Item in de ouder tussen de linker en rechter node kopieren naar linker node
            parent.copy_item(rightNodeNum - 1, leftNode)
            # Meest linkse item in rechter node naar linker node kopieren
            leftNode.add_item(rightNode.k1, rightNode.d1)
            # Kinderen van rechtse node naar linkse node kopieren
            (leftNode.c3, leftNode.c4) = (rightNode.c1, rightNode.c2)

            # Gekopieerd item uit parent verwijderen
            parent.remove_item(rightNodeNum - 1)
            # Rechter node verwijderen 
            parent.remove_child(rightNodeNum)
        
    def RetrieveItem(self, key):
        """ Vindt het item met gegeven 'key', als het dit vindt geeft het de data van dat item terug, als het dit niet vind geeft het de waarde None terug."""
        searchNode = self.root
        
        while True:
            if searchNode is None:
                return None

            keyIndex = searchNode.get_key_index(key)
            if keyIndex != -1:
                return searchNode.data[keyIndex - 1]
            else: # Het item is niet gevonden
                if searchNode.is_leaf():	
                    # searchNode was een leaf, dus kunnen we niet verder zoeken
                    return None
                else:
                    # searchNode wordt 
                    searchNode = searchNode.get_containing_child(key)