

from django.db import models 
from uthdemo.models import ( 
    Photo, 
    Reference, 
    Work_order, 
) 
# from uthdemo.utils.choices import ( 
#     DOCUMENT_TYPE
# ) 
import uuid 


class Document(models.Model): 
    """ References Reference table. """ 
    class DocumentType(models.TextChoices): 
        ORDRE_DE_TRAVAUX = "ORDRE DE TRAVAUX", ("ORDRE DE TRAVAUX"), 
        COMPTE_RENDU_D_INTERVENTION = "COMPTE-RENDU D'INTERVENTIONu", ("COMPTE-RENDU D'INTERVENTION"), 
        DOSSIER_D_INGENIERIE = "DOSSIER D INGENIERIE : REGLES D INGENIERIE UTILISEES", ("DOSSIER D INGENIERIE : REGLES D INGENIERIE UTILISEES"), 
        RAPPORT_D_ETUDE = "RAPPORT D ETUDE", ("RAPPORT D ETUDE"), 
        PLAN_DE_SITUATION_OU_SYNOPTIQUE_GEOGRAPHIQUE = "PLAN DE SITUATION, SYNOPTIQUE GEOGRAPHIQUE", ("PLAN DE SITUATION, SYNOPTIQUE GEOGRAPHIQUE"), 
        PLAN_DE_PHASAGE = "PLAN DE PHASAGE", ("PLAN DE PHASAGE"), 
        PLAN_DE_CABLAGE = "PLAN DE CABLAGE", ("PLAN DE CABLAGE"), 
        PLAN_DE_MASQUE_OU_FICHE_FOA = "PLAN DE MASQUE OU FICHE FOA", ("PLAN DE MASQUE OU FICHE FOA"), 
        DOSSIER_APPUIS_AERIENS = "DOSSIER APPUIS AERIENS", ("DOSSIER APPUIS AERIENS"), 
        PHOTO = "PHOTO", ("PHOTO"), 
        PLAN_DE_GENIE_CIVIL = "PLAN DE GENIE CIVIL", ("PLAN DE GENIE CIVIL"), 
        DOSSIER_DE_LEVE_OU_D_INVESTIGATIONS_COMPLEMENTAIRES = "DOSSIER DE LEVE OU D INVESTIGATIONS COMPLEMENTAIRES", ("DOSSIER DE LEVE OU D INVESTIGATIONS COMPLEMENTAIRES"), 
        DETAIL_OU_SCHEMA_DE_GENIE_CIVIL = "DETAIL OU SCHEMA DE GENIE CIVIL", ("DETAIL OU SCHEMA DE GENIE CIVIL"), 
        DOSSIER_DE_PIQUETAGE = "DOSSIER DE PIQUETAGE", ("DOSSIER DE PIQUETAGE"), 
        DOSSIER_DE_RELEVE_BOITES_AUX_LETTRES = "DOSSIER DE RELEVE BOITES AUX LETTRES", ("DOSSIER DE RELEVE BOITES AUX LETTRES"), 
        REGLEMENT_DE_VOIRIE = "REGLEMENT DE VOIRIE", ("REGLEMENT DE VOIRIE"), 
        PERMISSION_OU_AUTORISATION_DE_VOIRIE = "PERMISSION OU AUTORISATION DE VOIRIE", ("PERMISSION OU AUTORISATION DE VOIRIE"), 
        DT_EMISES_DANS_LE_CADRE_DU_PROJET_DE_DEPLOIEMENT = "DT EMISES DANS LE CADRE DU PROJET DE DEPLOIEMENT", ("DT EMISES DANS LE CADRE DU PROJET DE DEPLOIEMENT"), 
        DICT_EMISES_DANS_LE_CADRE_DU_PROJET_DE_DEPLOIEMENT = "DICT EMISES DANS LE CADRE DU PROJET DE DEPLOIEMENT", ("DICT EMISES DANS LE CADRE DU PROJET DE DEPLOIEMENT"), 
        DIAGNOSTIC_AMIANTE_ENROBE = "DIAGNOSTIC AMIANTE ENROBE", ("DIAGNOSTIC AMIANTE ENROBE"), 
        CONTRAT_OU_CONVENTION_DE_LOCATION_CESSION_ACHAT_OCCUPATION_D_INFRASTRUCTURE = "CONTRAT OU CONVENTION DE LOCATION/CESSION/ACHAT/OCCUPATION D INFRASTRUCTURE", ("CONTRAT OU CONVENTION DE LOCATION/CESSION/ACHAT/OCCUPATION D INFRASTRUCTURE"), 
        CONTRAT_OU_CONVENTION_DE_CO_CONSTRUCTION_OU_MUTUALISATION_DE_TRAVAUX = "CONTRAT OU CONVENTION DE CO-CONSTRUCTION OU MUTUALISATION DE TRAVAUX", ("CONTRAT OU CONVENTION DE CO-CONSTRUCTION OU MUTUALISATION DE TRAVAUX"), 
        DOSSIER_D_IMPLANTATION = "DOSSIER D IMPLANTATION (SRO, NRO, BPI…)", ("DOSSIER D IMPLANTATION (SRO, NRO, BPI…)"), 
        SYNOPTIQUE_OPTIQUE = "SYNOPTIQUE OPTIQUE", ("SYNOPTIQUE OPTIQUE"), 
        PLAN_DE_BOITE_OU_AUTRE_ELEMENT_DE_BRANCHEMENT_PASSIF = "PLAN DE BOITE, OU AUTRE ELEMENT DE BRANCHEMENT PASSIF", ("PLAN DE BOITE, OU AUTRE ELEMENT DE BRANCHEMENT PASSIF"), 
        SCHEMA_DE_RACCORDEMENT = "SCHEMA DE RACCORDEMENT (BAIE, ARMOIRE, REPARTITEUR…)", ("SCHEMA DE RACCORDEMENT (BAIE, ARMOIRE, REPARTITEUR…)"), 
        DOCUMENTATION_TECHNIQUE_D_EQUIPEMENT = "DOCUMENTATION TECHNIQUE D EQUIPEMENT", ("DOCUMENTATION TECHNIQUE D EQUIPEMENT"), 
        CONVENTION_THD_IMMEUBLE = "CONVENTION THD IMMEUBLE", ("CONVENTION THD IMMEUBLE"), 
        CONVENTION_CADRE_BAILLEUR_SOCIAL = "CONVENTION CADRE BAILLEUR SOCIALCIS", ("CONVENTION CADRE BAILLEUR SOCIAL"), 
        REGLEMENT_DE_SERVICE = "REGLEMENT DE SERVICE", ("REGLEMENT DE SERVICE"), 
        AUTRE_CONVENTION_D_OCCUPATION_EMPRISE_PRIVEE = "AUTRE CONVENTION D OCCUPATION EMPRISE PRIVEE", ("AUTRE CONVENTION D OCCUPATION EMPRISE PRIVEE"), 
        MESURE_DE_REFLECTOMETRIE = "MESURE DE REFLECTOMETRIE", ("MESURE DE REFLECTOMETRIE"), 
        TEST_D_ETANCHEITE_DE_FOURREAUX_ET_OU_TESTS_DE_MANDRINAGE_AIGUILLAGE = "TEST D ETANCHEITE DE FOURREAUX ET/OU TESTS DE MANDRINAGE, AIGUILLAGEMFX", ("TEST D ETANCHEITE DE FOURREAUX ET/OU TESTS DE MANDRINAGE, AIGUILLAGE"), 
        PV_DE_RECEPTION_GENIE_CIVIL = "PV DE RECEPTION GENIE CIVIL", ("PV DE RECEPTION GENIE CIVIL"), 
        DOSSIER_INFRASTRUCTURE_D_ACCUEIL = "DDOSSIER INFRASTRUCTURE D ACCUEIL", ("DOSSIER INFRASTRUCTURE D ACCUEIL"), 
        DOSSIER_DE_CABLAGE = "DOSSIER DE CABLAGE", ("DOSSIER DE CABLAGE"), 
        DOSSIER_OPTIQUE = "DOSSIER OPTIQUE", ("DOSSIER OPTIQUE"), 
        DOSSIER_DE_PROJET = "DOSSIER DE PROJET", ("DOSSIER DE PROJET"), 
        DOSSIER_DE_LIVRABLES_GRACETHD = "DOSSIER DE LIVRABLES GRACETHD", ("DOSSIER DE LIVRABLES GRACETHD"), 
        DOSSIER_DE_COMMANDE_POUR_LOCATION_OCCUPATION_D_INFRASTRUCTURE = "DOSSIER DE COMMANDE POUR LOCATION/OCCUPATION D INFRASTRUCTURE", ("DOSSIER DE COMMANDE POUR LOCATION/OCCUPATION D INFRASTRUCTURE"), 
        DOSSIER_DE_CREATION_DE_SITE = "DOSSIER DE CREATION DE SITE", ("DOSSIER DE CREATION DE SITE"), 
        DOSSIER_DE_RACCORDEMENT_DE_SITE = "DOSSIER DE RACCORDEMENT DE SITE", ("DOSSIER DE RACCORDEMENT DE SITE"), 
        PLAN_LOCAL_D_URBANISME = "PLAN LOCAL D URBANISME", ("PLAN LOCAL D URBANISME"), 
        FICHE_DE_RECETTE = "FICHE DE RECETTE", ("FICHE DE RECETTE"), 
        PV_DE_RECEPTION_DE_VOIRIE = "PV DE RECEPTION DE VOIRIE", ("PV DE RECEPTION DE VOIRIE"), 
        DIAGNOSTIC_TECHNIQUE_AMIANTE_POUR_UN_IMMEUBLE = "DIAGNOSTIC TECHNIQUE AMIANTE POUR UN IMMEUBLE", ("DIAGNOSTIC TECHNIQUE AMIANTE POUR UN IMMEUBLE") 

    uuid = models.UUIDField( 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False 
    ) 
    racine = models.CharField( 
        max_length=2, 
        db_index=True, 
        blank=True, 
        null=True 
    ) 
    id = models.CharField( 
        max_length=11, 
        db_index=True, 
        blank=True, 
        null=True 
    ) 
    # code = models.CharField( 
    #     max_length=254, 
    #     null=True, 
    #     blank=True,  
    # ) 
    # reftier 
    ext_code = models.CharField( 
        max_length=254, 
        null=True, 
        blank=True, 
    ) 
    name = models.CharField( 
        max_length=254, 
        null=True, 
        blank=True, 
    ) 
    # Ref de l'objet 
    reference = models.ForeignKey( 
        Reference, 
        on_delete=models.CASCADE, 
        related_name='document_reference', 
        null=True, 
        blank=True, 
    ) 
    work_order = models.ForeignKey( 
        Work_order, 
        on_delete=models.CASCADE, 
        related_name='document_work_order', 
        blank=True, 
        null=True, 
    ) 
    photo = models.ForeignKey( 
        Photo, 
        on_delete=models.CASCADE, 
        related_name='document_photo', 
        blank=True, 
        null=True,  
    ) 
    type = models.CharField( 
        max_length=254, 
        # max_length=3, 
        # choices=DOCUMENT_TYPE, 
        choices=DocumentType.choices,
        null=True, 
        blank=True, 
    ) 
    indice = models.CharField( 
        max_length=3, 
        null=True, 
        blank=True, 
    ) 
    indice_date = models.DateField( 
        null=True, 
        blank=True, 
    ) 
    # Classe de précision cartographique (pour les documents cartographiques soumis au décret DT-DICT). 
    cartographic_class = models.CharField( 
        max_length=2, 
        null=True, 
        blank=True, 
    ) 
    # url1 : URL du fichier éditable 
    # url2 : URL du fichier publiable (PDF, etc.) 			
    document_url = models.CharField( 
        max_length=254, 
        null=True, 
        blank=True, 
    ) 
    comment = models.TextField( 
        null=True, 
        blank=True, 
    ) 
    created_at = models.DateField( 
        auto_now_add=True, 
        null=True, 
        blank=True, 
    ) 
    updated_at = models.DateField( 
        null=True, 
        blank=True, 
    ) 
    archived_at = models.DateField( 
        null=True, 
        blank=True, 
    ) 
    archive_reason = models.CharField( 
        max_length=254, 
        null=True, 
        blank=True, 
    ) 

    def __str__(self) -> str: 
        if not self.racine: 
            racine = '' 
        else: 
            racine = self.racine 
        if not self.id: 
            id = '' 
        else: 
            id = self.id 
        return f'''{racine}{id}, {self.name}, 
            {self.type}. '''  # , 

    # Metadata
    class Meta:
        ordering = ['-created_at'] 
