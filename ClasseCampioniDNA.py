class CampioneDNA:
    
    """classe che rappresenta un campione di dna"""

    def __init__(self, __codice_campione, __sequenza, laboratorio, __geni_mappati = None, __mutazioni_rilevate= None):
        
        """crea un campione di DNA.

        :param __codice_campione: il codice del campione
        :type __codice_campione: str
        :param __sequenza: la sequenza di DNA del campione
        :type __sequenza: str
        :param laboratorio: il laboratorio che ha analizzato il campione
        :type laboratorio: str
        :param __geni_mappati: lista dei geni già identificati
        :type __geni_mappati: list
        :param __mutazioni_rilevate: dizionario delle mutazioni già rilevate
        :type __mutazioni_rilevate: dict
        """
        
        self.__codice_campione = __codice_campione
        self.__sequenza = __sequenza.upper()
        
        if __geni_mappati is None:
            self.__geni_mappati = []
        else:
            self.__geni_mappati = __geni_mappati
        
        if __mutazioni_rilevate is None:
            self.__mutazioni_rilevate = {}
        else:
            self.__mutazioni_rilevate = __mutazioni_rilevate
        
        self.laboratorio = laboratorio
    
    def aggiungi_gene(self, gene):
        
        """Aggiunge un gene alla lista dei geni 

        Il gene viene aggiunto solo se non è già presente

        :param gene: nome del gene da aggiungere
        :type gene: str
        """
        
        if gene not in self.__geni_mappati:
            self.__geni_mappati.append(gene)
    
    
    def registra_mutazione(self, posizione, tipo):
        
        """Registra una mutazione nel campione

        Se la posizione è già presente la mutazione viene aggiornata
        :param posizione: posizione della mutazione nella sequenza
        :type posizione: int
        :param tipo: tipo di mutazione rilevata
        :type tipo: str
        """
        
        self.__mutazioni_rilevate[posizione] = tipo
        
   
    def calcola_percentuale_gc(self):
               
        """calcola la percentuale di basi G e C nella sequenza

        :return: percentuale di basi G e C presenti nella sequenza
        :rtype: float
        """
               
        gc = 0
        
        for base in self.__sequenza:
            if base == "G" or base == "C":
                gc = gc + 1
        
        if len(self.__sequenza) == 0:
            return 0.0
        
        percentuale = (gc / len(self.__sequenza)) * 100
        
        return percentuale
    
   
    def stampa_report(self):
       
        """stampa un report con le informazioni del campione.

        nel report vengono mostrati il codice, il laboratorio,
        la sequenza, i geni, le mutazioni e la percentuale GC.
        Se la sequenza è troppo lunga (oltre 20 caratteri) viene mostrata solo una parte
        """
       
        if len(self.__sequenza) > 20:
            sequenza = self.__sequenza[:20] + "..."
        else:
            sequenza = self.__sequenza
       
        print("nreport campione:")
        print("Codice:", self.__codice_campione)
        print("Laboratorio:", self.laboratorio)
        print("Sequenza:", sequenza)
        print("Geni:", self.__geni_mappati)
        print("Mutazioni:", self.__mutazioni_rilevate)
        print("Percentuale gc:", self.calcola_percentuale_gc())
        
campione = CampioneDNA("DNA-4029", "ATGCGCTA", "LabGen")
campione.aggiungi_gene("ampR")
campione.aggiungi_gene("lacZ")
campione.aggiungi_gene("geneA")
campione.registra_mutazione(45, "sostituzione")
campione.registra_mutazione(120, "delezione")
percentuale = campione.calcola_percentuale_gc()
print("Percentuale gc:", percentuale)
campione.stampa_report()