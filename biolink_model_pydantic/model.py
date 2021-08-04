# Auto generated from biolink-model.yaml by pydanticgen.py version: 0.9.0
# Generation date: 2021-08-04 10:42
# Schema: Biolink-Model
#
# id: https://w3id.org/biolink/biolink-model
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import datetime
import inspect
import logging
import re
from collections import namedtuple
from dataclasses import field
from enum import Enum, unique
from typing import Any, ClassVar, List, Optional, Union

from pydantic import constr, validator
from pydantic.dataclasses import dataclass

LOG = logging.getLogger(__name__)

metamodel_version = "1.7.0"

curie_regexp = r'^[a-zA-Z_]?[a-zA-Z_0-9-]*:([A-Za-z0-9_][A-Za-z0-9_.-]*[A-Za-z0-9_]*)?$'
curie_pattern = re.compile(curie_regexp)

# Type Aliases
Unit = Union[int, float]
LabelType = str
IriType = constr(regex=r'^(http|ftp)')
Curie = constr(regex=curie_regexp)
URIorCURIE = Union[Curie, IriType]
NarrativeText = str
XSDDate = datetime.date
TimeType = datetime.time
SymbolType = str
FrequencyValue = str
PercentageFrequencyValue = float
BiologicalSequence = str
Quotient = float
Bool = bool

# Namespaces

valid_prefix = [
    "AAO",
    "ABS",
    "ACEVIEW_WORM",
    "ACLAME",
    "ADW",
    "AEO",
    "AERO",
    "AFFY_PROBESET",
    "AFTOL_TAXONOMY",
    "AGD",
    "AGRICOLA",
    "AGRO",
    "ALLERGOME",
    "AMOEBADB",
    "ANTIBODYREGISTRY",
    "ANTWEB",
    "AOP",
    "AOP_EVENTS",
    "AOP_RELATIONSHIPS",
    "AOP_STRESSOR",
    "APB",
    "APD",
    "APHIDBASE_TRANSCRIPT",
    "APID_INTERACTIONS",
    "APO",
    "AQTLPub",
    "AQTLTrait",
    "ARACHNOSERVER",
    "ARDB",
    "ARK",
    "ARO",
    "ARRAYEXPRESS",
    "ARRAYEXPRESS_PLATFORM",
    "ARRAYMAP",
    "ARXIV",
    "ASAP",
    "ASCL",
    "ASIN",
    "ASPGD_LOCUS",
    "ASPGD_PROTEIN",
    "ATC",
    "ATCC",
    "ATCVET",
    "ATFDB_FAMILY",
    "ATO",
    "AUTDB",
    "Aeolus",
    "BACMAP_BIOG",
    "BACMAP_MAP",
    "BAO",
    "BCGO",
    "BCO",
    "BDGP_EST",
    "BDGP_INSERTION",
    "BEETLEBASE",
    "BEGDB",
    "BFO",
    "BGEE_FAMILY",
    "BGEE_GENE",
    "BGEE_ORGAN",
    "BGEE_STAGE",
    "BIGG_COMPARTMENT",
    "BIGG_METABOLITE",
    "BIGG_MODEL",
    "BIGG_REACTION",
    "BILA",
    "BIND",
    "BINDINGDB",
    "BIOCARTA_PATHWAY",
    "BIOCATALOGUE_SERVICE",
    "BIOCYC",
    "BIOGRID",
    "BIOMINDER",
    "BIOMODELS_DB",
    "BIOMODELS_KISAO",
    "BIOMODELS_TEDDY",
    "BIOMODELS_VOCABULARY",
    "BIONUMBERS",
    "BIOPORTAL",
    "BIOPROJECT",
    "BIOSAMPLE",
    "BIOSYSTEMS",
    "BIOTOOLS",
    "BITTERDB_CPD",
    "BITTERDB_REC",
    "BNODE",
    "BOLD_TAXONOMY",
    "BOOTSTREP",
    "BRENDA",
    "BROAD",
    "BSPO",
    "BT",
    "BTO",
    "BUGBASE_EXPT",
    "BUGBASE_PROTOCOL",
    "BYKDB",
    "CABRI",
    "CAID",
    "CAMEO",
    "CAPS",
    "CARO",
    "CAS",
    "CATH",
    "CATH_DOMAIN",
    "CATH_SUPERFAMILY",
    "CATTLEQTLDB",
    "CAZY",
    "CCDS",
    "CCO",
    "CDAO",
    "CDD",
    "CDPD",
    "CELLIMAGE",
    "CELLOSAURUS",
    "CEPH",
    "CGD",
    "CGSC",
    "CHADO",
    "CHARPROT",
    "CHEBI",
    "CHEMBL_COMPOUND",
    "CHEMBL_MECHANISM",
    "CHEMBL_TARGET",
    "CHEMDB",
    "CHEMIDPLUS",
    "CHEMINF",
    "CHEMSPIDER",
    "CHICKENQTLDB",
    "CHMO",
    "CHR",
    "CID",
    "CIO",
    "CL",
    "CLDB",
    "CLINICALTRIALS",
    "CLINVAR",
    "CLINVAR_RECORD",
    "CLINVAR_SUBMISSION",
    "CLO",
    "CLUSTR",
    "CMF",
    "CMMR",
    "CMO",
    "CMR_GENE",
    "COAR_RESOURCE",
    "COGS",
    "COGS_FUNCTION",
    "COMBINE_SPECIFICATIONS",
    "COMPLEXPORTAL",
    "COMPTOX",
    "COMPULYEAST",
    "CONOSERVER",
    "CORIELL",
    "CORUM",
    "COSMIC",
    "CPC",
    "CPT",
    "CRISPRDB",
    "CRO",
    "CRYPTODB",
    "CSA",
    "CST",
    "CST_AB",
    "CTD",
    "CTD_CHEMICAL",
    "CTD_DISEASE",
    "CTD_GENE",
    "CTENO",
    "CUBEDB",
    "CVDO",
    "CYGD",
    "ChemBank",
    "ClinVarSubmitters",
    "ClinVarVariant",
    "CoriellCollection",
    "CoriellFamily",
    "CoriellIndividual",
    "D1ID",
    "DAILYMED",
    "DARC",
    "DASHR",
    "DASHR_EXPRESSION",
    "DATA",
    "DATF",
    "DBD",
    "DBEST",
    "DBG2INTRONS",
    "DBGAP",
    "DBPROBE",
    "DBSNP",
    "DC_CL",
    "DDANAT",
    "DDPHENO",
    "DECIPHER",
    "DEGRADOME",
    "DEPOD",
    "DEV_GA4GHDOS",
    "DGIdb",
    "DICTYBASE_EST",
    "DICTYBASE_GENE",
    "DIDEO",
    "DINTO",
    "DIP",
    "DISPROT",
    "DOID",
    "DOMMINO",
    "DOOR",
    "DOQCS_MODEL",
    "DOQCS_PATHWAY",
    "DPV",
    "DRAGONDB_ALLELE",
    "DRAGONDB_DNA",
    "DRAGONDB_LOCUS",
    "DRAGONDB_PROTEIN",
    "DRON",
    "DRSC",
    "DRUGBANK",
    "DRUGBANKV4_TARGET",
    "DRUGBANK_TARGET",
    "DUO",
    "DrugCentral",
    "EBIMETAGENOMICS_PROJ",
    "EBIMETAGENOMICS_SAMP",
    "EC",
    "EC-CODE",
    "ECHOBASE",
    "ECO",
    "ECOCORE",
    "ECOGENE",
    "ECOLIWIKI",
    "ECTO",
    "ECYANO_ENTITY",
    "ECYANO_MODEL",
    "ECYANO_RULE",
    "EDAM",
    "EDAM-DATA",
    "EDAM-FORMAT",
    "EDAM-OPERATION",
    "EDAM-TOPIC",
    "EFO",
    "EGA_DATASET",
    "EGA_STUDY",
    "EGGNOG",
    "EHDA",
    "EHDAA",
    "EHDAA2",
    "ELM",
    "EMAP",
    "EMAPA",
    "EMDB",
    "EMMA",
    "ENA_EMBL",
    "ENCODE",
    "ENSEMBL",
    "ENSEMBL_BACTERIA",
    "ENSEMBL_FUNGI",
    "ENSEMBL_METAZOA",
    "ENSEMBL_PLANT",
    "ENSEMBL_PROTIST",
    "ENVO",
    "EO",
    "EOM",
    "EPD",
    "EPO",
    "ERO",
    "ERV",
    "EU89H",
    "EUCLINICALTRIALS",
    "EUPATH",
    "EV",
    "EXAC_GENE",
    "EXAC_TRANSCRIPT",
    "EXAC_VARIANT",
    "ExO",
    "FACEBASE",
    "FAIRSHARING",
    "FAO",
    "FB",
    "FBOL",
    "FBSP",
    "FBbi",
    "FBbt",
    "FBcv",
    "FBdv",
    "FDADrug",
    "FIX",
    "FLOPO",
    "FLU",
    "FLYSTOCK",
    "FMA",
    "FOODON",
    "FPLX",
    "FSNP",
    "FUNCAT",
    "FUNCBASE_FLY",
    "FUNCBASE_HUMAN",
    "FUNCBASE_MOUSE",
    "FUNCBASE_YEAST",
    "FUNGIDB",
    "FYPO",
    "FlyBase",
    "GA4GHDOS",
    "GABI",
    "GAMMA",
    "GAZ",
    "GDC",
    "GENATLAS",
    "GENECARDS",
    "GENEDB",
    "GENEFARM",
    "GENEPIO",
    "GENETREE",
    "GENEWIKI",
    "GENO",
    "GENPEPT",
    "GENPROP",
    "GEO",
    "GIARDIADB",
    "GINAS",
    "GLIDA_GPCR",
    "GLIDA_LIGAND",
    "GLYCOEPITOPE",
    "GLYCOMEDB",
    "GLYTOUCAN",
    "GMD",
    "GMD_ANALYTE",
    "GMD_GCMS",
    "GMD_PROFILE",
    "GMD_REF",
    "GNPIS",
    "GO",
    "GOA",
    "GOLD_GENOME",
    "GOLD_META",
    "GOOGLE_PATENT",
    "GOP",
    "GOREL",
    "GO_REF",
    "GPCRDB",
    "GPMDB",
    "GRAMENE_GENE",
    "GRAMENE_GROWTHSTAGE",
    "GRAMENE_PROTEIN",
    "GRAMENE_QTL",
    "GRAMENE_TAXONOMY",
    "GREENGENES",
    "GRID",
    "GRIN_TAXONOMY",
    "GRO",
    "GRSDB",
    "GSID",
    "GTEx",
    "GTOPDB",
    "GUDMAP",
    "GWASCENTRAL_MARKER",
    "GWASCENTRAL_PHENOTYPE",
    "GWASCENTRAL_STUDY",
    "GXA_EXPT",
    "GXA_GENE",
    "GenBank",
    "GeneReviews",
    "HABRONATTUS",
    "HAMAP",
    "HANCESTRO",
    "HAO",
    "HCPCS",
    "HCVDB",
    "HDR",
    "HGMD",
    "HGNC",
    "HGNC_FAMILY",
    "HGNC_GENEFAMILY",
    "HGNC_SYMBOL",
    "HINV_LOCUS",
    "HINV_PROTEIN",
    "HINV_TRANSCRIPT",
    "HMDB",
    "HOGENOM",
    "HOM",
    "HOMD_SEQ",
    "HOMD_TAXON",
    "HOMOLOGENE",
    "HOVERGEN",
    "HP",
    "HPA",
    "HPM_PEPTIDE",
    "HPM_PROTEIN",
    "HPO",
    "HPRD",
    "HSSP",
    "HUGE",
    "HsapDv",
    "IAO",
    "ICD",
    "ICD0",
    "ICD10",
    "ICD9",
    "ICEBERG_ELEMENT",
    "ICEBERG_FAMILY",
    "ICO",
    "IDEAL",
    "IDO",
    "IDOMAL",
    "IEV",
    "IMEX",
    "IMGT_HLA",
    "IMGT_LIGM",
    "IMG_GENE",
    "IMG_TAXON",
    "IMPC",
    "IMPRESS-parameter",
    "IMPRESS-procedure",
    "IMPRESS-protocol",
    "IMR",
    "INCHI",
    "INCHIKEY",
    "INO",
    "INSDC",
    "INSDC_CDS",
    "INSDC_GCA",
    "INSDC_SRA",
    "INTACT",
    "INTACT_MOLECULE",
    "IPI",
    "IPR",
    "IRD_SEGMENT",
    "IREFWEB",
    "ISBN-10",
    "ISBN-13",
    "ISFINDER",
    "IUPHAR_FAMILY",
    "IUPHAR_LIGAND",
    "IUPHAR_RECEPTOR",
    "J",
    "JAX",
    "JAXMICE",
    "JCGGDB",
    "JCM",
    "JCSD",
    "JSTOR",
    "JWS",
    "KEGG",
    "KEGG-ds",
    "KEGG-hsa",
    "KEGG-ko",
    "KEGG-path",
    "KEGG_BRITE",
    "KEGG_COMPOUND",
    "KEGG_DGROUP",
    "KEGG_DISEASE",
    "KEGG_DRUG",
    "KEGG_ENVIRON",
    "KEGG_ENZYME",
    "KEGG_GENE",
    "KEGG_GENES",
    "KEGG_GENOME",
    "KEGG_GLYCAN",
    "KEGG_METAGENOME",
    "KEGG_MODULE",
    "KEGG_ORTHOLOGY",
    "KEGG_PATHWAY",
    "KEGG_RCLASS",
    "KEGG_REACTION",
    "KISAO",
    "KNAPSACK",
    "LGIC",
    "LICEBASE",
    "LIGANDBOX",
    "LIGANDEXPO",
    "LINCS_CELL",
    "LINCS_DATA",
    "LINCS_PROTEIN",
    "LINCS_SMALLMOLECULE",
    "LIPIDBANK",
    "LIPIDMAPS",
    "LIPRO",
    "LOGGERHEAD",
    "LOINC",
    "LPT",
    "LRG",
    "MA",
    "MACIE",
    "MAIZEGDB_LOCUS",
    "MAMO",
    "MAO",
    "MASSBANK",
    "MASSIVE",
    "MAT",
    "MATRIXDB_ASSOCIATION",
    "MDM",
    "MEDDRA",
    "MEDLINEPLUS",
    "MEROPS",
    "MEROPS_FAMILY",
    "MEROPS_INHIBITOR",
    "MESH",
    "MESH_2012",
    "MESH_2013",
    "METABOLIGHTS",
    "METACYC_COMPOUND",
    "METACYC_REACTION",
    "METANETX_CHEMICAL",
    "METANETX_COMPARTMENT",
    "METANETX_REACTION",
    "METLIN",
    "MEX",
    "MF",
    "MFMO",
    "MFO",
    "MFOEM",
    "MFOMD",
    "MGI",
    "MI",
    "MIAPA",
    "MICRO",
    "MICROSCOPE",
    "MICROSPORIDIA",
    "MIM",
    "MIMODB",
    "MINID",
    "MINT",
    "MIPMOD",
    "MIR",
    "MIRBASE",
    "MIRBASE_MATURE",
    "MIREX",
    "MIRIAM_COLLECTION",
    "MIRIAM_RESOURCE",
    "MIRNAO",
    "MIRNEST",
    "MIRO",
    "MIRTARBASE",
    "MMDB",
    "MMO",
    "MMP_CAT",
    "MMP_DB",
    "MMP_REF",
    "MMRRC",
    "MMUSDV",
    "MO",
    "MOBIDB",
    "MOD",
    "MODELDB",
    "MOLBASE",
    "MONARCH",
    "MONDO",
    "MOP",
    "MP",
    "MPATH",
    "MPD",
    "MPD-assay",
    "MPD-strain",
    "MPID",
    "MPIO",
    "MRO",
    "MS",
    "MSigDB",
    "MUGEN",
    "MULTICELLDS_CELL_LINE",
    "MULTICELLDS_COLLECTION",
    "MULTICELLDS_SNAPSHOT",
    "MW_PROJECT",
    "MW_STUDY",
    "MYCOBANK",
    "MYCO_LEPRA",
    "MYCO_MARINUM",
    "MYCO_SMEG",
    "MYCO_TUBER",
    "MZSPEC",
    "MetaCyc",
    "MonarchArchive",
    "MonarchData",
    "NAPDI",
    "NAPP",
    "NARCIS",
    "NASC",
    "NBN",
    "NBO",
    "NBRC",
    "NCBIAssembly",
    "NCBIGENE",
    "NCBIGI",
    "NCBIGene",
    "NCBIGenome",
    "NCBIPROTEIN",
    "NCBITaxon",
    "NCIM",
    "NCIMR",
    "NCIT",
    "NCRO",
    "NDC",
    "NDDF",
    "NEUROLEX",
    "NEUROMORPHO",
    "NEURONDB",
    "NEUROVAULT_COLLECTION",
    "NEUROVAULT_IMAGE",
    "NEXTDB",
    "NEXTPROT",
    "NGL",
    "NIAEST",
    "NIF_CELL",
    "NIF_DYSFUNCTION",
    "NIF_GROSSANATOMY",
    "NLMID",
    "NMR",
    "NONCODEV3",
    "NONCODEV4_GENE",
    "NONCODEV4_RNA",
    "NORINE",
    "NUCLEARBD",
    "OAE",
    "OARCS",
    "OBA",
    "OBAN",
    "OBCS",
    "OBI",
    "OBIB",
    "OBO",
    "OBOREL",
    "OBO_REL",
    "OCI",
    "OCLC",
    "ODOR",
    "OGG",
    "OGI",
    "OGMS",
    "OGSF",
    "OHD",
    "OHMI",
    "OIO",
    "OLATDV",
    "OMA_GRP",
    "OMA_PROTEIN",
    "OMIA",
    "OMIA-breed",
    "OMIABIS",
    "OMIM",
    "OMIT",
    "OMP",
    "OMRSE",
    "ONTONEO",
    "OOSTT",
    "OPB",
    "OPL",
    "OPM",
    "ORCID",
    "ORDB",
    "ORIDB_SACCH",
    "ORIDB_SCHIZO",
    "ORPHA",
    "ORPHANET",
    "ORPHANET_ORDO",
    "ORTHODB",
    "ORYZABASE_GENE",
    "ORYZABASE_MUTANT",
    "ORYZABASE_STAGE",
    "ORYZABASE_STRAIN",
    "OTL",
    "OVAE",
    "P3DB_PROTEIN",
    "P3DB_SITE",
    "PAINT_REF",
    "PALEODB",
    "PANTHER",
    "PANTHER_FAMILY",
    "PANTHER_NODE",
    "PANTHER_PATHWAY",
    "PANTHER_PTHCMP",
    "PAO",
    "PASS2",
    "PATHEMA",
    "PATHWAYCOMMONS",
    "PATO",
    "PATO-PROPERTY",
    "PAXDB_ORGANISM",
    "PAXDB_PROTEIN",
    "PAZAR",
    "PCO",
    "PDB",
    "PDB-CCD",
    "PDB_LIGAND",
    "PDQ",
    "PDRO",
    "PDUMDV",
    "PD_ST",
    "PECO",
    "PEPTIDEATLAS",
    "PEROXIBASE",
    "PFAM",
    "PGDSO",
    "PGN",
    "PGX",
    "PHARMGKB_DISEASE",
    "PHARMGKB_DRUG",
    "PHARMGKB_GENE",
    "PHARMGKB_PATHWAYS",
    "PHAROS",
    "PHENOLEXPLORER",
    "PHOSPHOPOINT_KINASE",
    "PHOSPHOPOINT_PROTEIN",
    "PHOSPHOSITE_PROTEIN",
    "PHOSPHOSITE_RESIDUE",
    "PHYLOMEDB",
    "PHYTOZOME_LOCUS",
    "PID_PATHWAY",
    "PIGQTLDB",
    "PINA",
    "PIROPLASMA",
    "PIRSF",
    "PLANA",
    "PLANTTFDB",
    "PLASMODB",
    "PLO",
    "PMAP_CUTDB",
    "PMAP_SUBSTRATEDB",
    "PMC",
    "PMCID",
    "PMDB",
    "PMID",
    "PMP",
    "PO",
    "POCKETOME",
    "POLBASE",
    "POMBASE",
    "PORO",
    "PPO",
    "PR",
    "PRIDE",
    "PRIDE_PROJECT",
    "PRINTS",
    "PROBONTO",
    "PRODOM",
    "PROGLYC",
    "PROPREO",
    "PROSITE",
    "PROTCLUSTDB",
    "PROTEOMICSDB_PEPTIDE",
    "PROTEOMICSDB_PROTEIN",
    "PROTONET_CLUSTER",
    "PROTONET_PROTEINCARD",
    "PSCDB",
    "PSEUDOMONAS",
    "PSIMI",
    "PSIPAR",
    "PUBCHEM_BIOASSAY",
    "PUBCHEM_COMPOUND",
    "PUBCHEM_SUBSTANCE",
    "PUBMED",
    "PW",
    "PX",
    "PathWhiz",
    "RBK",
    "RBRC",
    "REACT",
    "REACTOME",
    "REBASE",
    "REFSEQ",
    "REPODB",
    "RESID",
    "REX",
    "RFAM",
    "RGD",
    "RGDRef",
    "RGD_QTL",
    "RGD_STRAIN",
    "RHEA",
    "RICEGAP",
    "RICENETDB_COMPOUND",
    "RICENETDB_GENE",
    "RICENETDB_MIRNA",
    "RICENETDB_PROTEIN",
    "RICENETDB_REACTION",
    "RNACENTRAL",
    "RNAMODS",
    "RNAO",
    "RO",
    "ROUGE",
    "RRID",
    "RS",
    "RTXKG1",
    "RXCUI",
    "RXNO",
    "RXNORM",
    "ResearchID",
    "SABIORK_EC",
    "SABIORK_KINETICRECORD",
    "SABIORK_REACTION",
    "SAO",
    "SASBDB",
    "SBO",
    "SCIENCESIGNALING_PATH",
    "SCIENCESIGNALING_PDC",
    "SCIENCESIGNALING_PIC",
    "SCOP",
    "SCRETF",
    "SDBS",
    "SEED",
    "SEED_COMPOUND",
    "SEMMEDDB",
    "SEP",
    "SEPIO",
    "SGD",
    "SGD_PATHWAYS",
    "SGD_REF",
    "SGN",
    "SHEEPQTLDB",
    "SIBO",
    "SIDER_DRUG",
    "SIDER_EFFECT",
    "SIGNALING-GATEWAY",
    "SIO",
    "SISU",
    "SITEX",
    "SMART",
    "SMPDB",
    "SNOMED",
    "SNOMEDCT",
    "SNPEFF",
    "SO",
    "SOPHARM",
    "SOYBASE",
    "SPD",
    "SPIKE_MAP",
    "SPLASH",
    "STAP",
    "STATO",
    "STITCH",
    "STOREDB",
    "STRING",
    "SUBTILIST",
    "SUBTIWIKI",
    "SUGARBIND",
    "SUPFAM",
    "SWH",
    "SWISS-MODEL",
    "SWISSLIPID",
    "SWISSREGULON",
    "SWO",
    "SYMP",
    "ScopusID",
    "SwissProt",
    "T3DB",
    "TADS",
    "TAHE",
    "TAHH",
    "TAIR",
    "TAIR_GENE",
    "TAIR_LOCUS",
    "TAIR_PROTEIN",
    "TAO",
    "TARBASE",
    "TAXONOMY",
    "TAXRANK",
    "TCDB",
    "TGD",
    "TGMA",
    "TIGRFAM",
    "TISSUELIST",
    "TO",
    "TOL",
    "TOPDB",
    "TOPFIND",
    "TOXOPLASMA",
    "TRANS",
    "TREEBASE",
    "TREEFAM",
    "TRICHDB",
    "TRITRYPDB",
    "TTD_DRUG",
    "TTD_TARGET",
    "TTO",
    "TrEMBL",
    "UBERGRAPH",
    "UBERON",
    "UBERON_CORE",
    "UBIO_NAMEBANK",
    "UCSC",
    "UMBBD_COMPOUND",
    "UMBBD_ENZYME",
    "UMBBD_PATHWAY",
    "UMBBD_REACTION",
    "UMBBD_RULE",
    "UMLS",
    "UMLSSC",
    "UMLSSG",
    "UMLSST",
    "UNIGENE",
    "UNII",
    "UNIMOD",
    "UNIPARC",
    "UNIPATHWAY",
    "UNIPATHWAY_COMPOUND",
    "UNIPATHWAY_REACTION",
    "UNIPROT",
    "UNIPROT_ISOFORM",
    "UNISTS",
    "UNITE",
    "UO",
    "UPHENO",
    "USPTO",
    "UniProtKB",
    "VALIDATORDB",
    "VANDF",
    "VARIO",
    "VBASE2",
    "VBRC",
    "VECTORBASE",
    "VFDB_GENE",
    "VFDB_GENUS",
    "VHOG",
    "VIPR",
    "VIRALZONE",
    "VIRSIRNA",
    "VIVO",
    "VMC",
    "VMHMETABOLITE",
    "VMHREACTION",
    "VO",
    "VSAO",
    "VT",
    "VTO",
    "WB",
    "WBBT",
    "WBLS",
    "WBPhenotype",
    "WBVocab",
    "WB_RNAI",
    "WD_Entity",
    "WD_Prop",
    "WIKIDATA",
    "WIKIDATA_PROPERTY",
    "WIKIGENES",
    "WIKIPATHWAYS",
    "WIKIPEDIA_EN",
    "WORFDB",
    "WORMPEP",
    "WORMS",
    "WormBase",
    "XAO",
    "XCO",
    "XENBASE",
    "XL",
    "XPO",
    "Xenbase",
    "YDPM",
    "YEASTINTRON",
    "YETFASCO",
    "YID",
    "YPO",
    "YRCPDR",
    "ZEA",
    "ZECO",
    "ZFA",
    "ZFIN",
    "ZFIN_EXPRESSION",
    "ZFIN_PHENOTYPE",
    "ZFS",
    "ZINC",
    "ZP",
    "alliancegenome",
    "apollo",
    "biolink",
    "catfishQTL",
    "cattleQTL",
    "chembio",
    "chickenQTL",
    "dbSNPIndividual",
    "dbVar",
    "dc",
    "dcat",
    "dct",
    "dcterms",
    "dctypes",
    "dictyBase",
    "doi",
    "fabio",
    "faldo",
    "foaf",
    "foodb_compound",
    "gff3",
    "gpi",
    "gtpo",
    "hetio",
    "horseQTL",
    "idot",
    "interpro",
    "isbn",
    "isni",
    "issn",
    "linkml",
    "medgen",
    "oa",
    "oboInOwl",
    "oboformat",
    "os",
    "owl",
    "pav",
    "pigQTL",
    "prov",
    "qud",
    "rainbow_troutQTL",
    "rdf",
    "rdfs",
    "schema",
    "sheepQTL",
    "shex",
    "skos",
    "uuid",
    "void",
    "wgs",
    "xml",
    "xsd",
]


# Pydantic config and validators
class PydanticConfig:
    """
    Pydantic config
    https://pydantic-docs.helpmanual.io/usage/model_config/
    """

    validate_assignment = True
    validate_all = True
    underscore_attrs_are_private = True
    extra = 'forbid'
    arbitrary_types_allowed = True  # TODO re-evaluate this


def check_curie_prefix(cls, curie: Union[List, str, None]):
    if isinstance(curie, list):
        for cur in curie:
            prefix = cur.split(':')[0]
            if prefix not in valid_prefix:

                LOG.warning(f"{curie} prefix '{prefix}' not in curie map")
                if hasattr(cls, '_id_prefixes') and cls._id_prefixes:
                    LOG.warning(f"Consider one of {cls._id_prefixes}")
                else:
                    LOG.warning(
                        f"See https://biolink.github.io/biolink-model/context.jsonld "
                        f"for a list of valid curie prefixes"
                    )
    elif curie:
        prefix = curie.split(':')[0]
        if prefix not in valid_prefix:
            LOG.warning(f"{curie} prefix '{prefix}' not in curie map")
            if hasattr(cls, '_id_prefixes') and cls._id_prefixes:
                LOG.warning(f"Consider one of {cls._id_prefixes}")
            else:
                LOG.warning(
                    f"See https://biolink.github.io/biolink-model/context.jsonld "
                    f"for a list of valid curie prefixes"
                )


def convert_scalar_to_list_check_curies(cls, value: Any) -> List[str]:
    """
    Converts list fields that have been passed a scalar to a 1-sized list

    Also checks prefix checks curies.  Because curie regex constraints
    are applied prior to running this function, we can use this for both
    curie and non-curie fields by rechecking re.match(curie_pattern, some_string)
    """
    if not isinstance(value, list):
        value = [value]
    for val in value:
        if isinstance(val, str) and re.match(curie_pattern, val):
            check_curie_prefix(cls, val)
    return value


def check_value_is_not_none(slotname: str, value: Any):
    is_none = False
    if isinstance(value, list) or isinstance(value, dict):
        if not field:
            is_none = True
    else:
        if value is None:
            is_none = True

    if is_none:
        raise ValueError(f"{slotname} is required")


# Predicates
@unique
class PredicateType(str, Enum):
    """
    Enum for biolink predicates
    """

    abundance_affected_by = "biolink:abundance_affected_by"
    abundance_decreased_by = "biolink:abundance_decreased_by"
    abundance_increased_by = "biolink:abundance_increased_by"
    active_in = "biolink:active_in"
    actively_involved_in = "biolink:actively_involved_in"
    actively_involves = "biolink:actively_involves"
    activity_affected_by = "biolink:activity_affected_by"
    activity_affects = "biolink:activity_affects"
    activity_decreased_by = "biolink:activity_decreased_by"
    activity_increased_by = "biolink:activity_increased_by"
    acts_upstream_of = "biolink:acts_upstream_of"
    acts_upstream_of_negative_effect = "biolink:acts_upstream_of_negative_effect"
    acts_upstream_of_or_within = "biolink:acts_upstream_of_or_within"
    acts_upstream_of_or_within_negative_effect = (
        "biolink:acts_upstream_of_or_within_negative_effect"
    )
    acts_upstream_of_or_within_positive_effect = (
        "biolink:acts_upstream_of_or_within_positive_effect"
    )
    acts_upstream_of_positive_effect = "biolink:acts_upstream_of_positive_effect"
    adverse_event_caused_by = "biolink:adverse_event_caused_by"
    affected_by = "biolink:affected_by"
    affects = "biolink:affects"
    affects_abundance_of = "biolink:affects_abundance_of"
    affects_activity_of = "biolink:affects_activity_of"
    affects_degradation_of = "biolink:affects_degradation_of"
    affects_expression_in = "biolink:affects_expression_in"
    affects_expression_of = "biolink:affects_expression_of"
    affects_folding_of = "biolink:affects_folding_of"
    affects_localization_of = "biolink:affects_localization_of"
    affects_metabolic_processing_of = "biolink:affects_metabolic_processing_of"
    affects_molecular_modification_of = "biolink:affects_molecular_modification_of"
    affects_mutation_rate_of = "biolink:affects_mutation_rate_of"
    affects_response_to = "biolink:affects_response_to"
    affects_risk_for = "biolink:affects_risk_for"
    affects_secretion_of = "biolink:affects_secretion_of"
    affects_splicing_of = "biolink:affects_splicing_of"
    affects_stability_of = "biolink:affects_stability_of"
    affects_synthesis_of = "biolink:affects_synthesis_of"
    affects_transport_of = "biolink:affects_transport_of"
    affects_uptake_of = "biolink:affects_uptake_of"
    ameliorates = "biolink:ameliorates"
    approved_for_treatment_by = "biolink:approved_for_treatment_by"
    approved_to_treat = "biolink:approved_to_treat"
    author = "biolink:author"
    biomarker_for = "biolink:biomarker_for"
    broad_match = "biolink:broad_match"
    capable_of = "biolink:capable_of"
    catalyzes = "biolink:catalyzes"
    caused_by = "biolink:caused_by"
    causes = "biolink:causes"
    causes_adverse_event = "biolink:causes_adverse_event"
    chemically_interacts_with = "biolink:chemically_interacts_with"
    chemically_similar_to = "biolink:chemically_similar_to"
    close_match = "biolink:close_match"
    coexists_with = "biolink:coexists_with"
    coexpressed_with = "biolink:coexpressed_with"
    colocalizes_with = "biolink:colocalizes_with"
    condition_associated_with_gene = "biolink:condition_associated_with_gene"
    consumes = "biolink:consumes"
    contraindicated_for = "biolink:contraindicated_for"
    contributes_to = "biolink:contributes_to"
    contribution_from = "biolink:contribution_from"
    contributor = "biolink:contributor"
    correlated_with = "biolink:correlated_with"
    decreased_amount_in = "biolink:decreased_amount_in"
    decreases_abundance_of = "biolink:decreases_abundance_of"
    decreases_activity_of = "biolink:decreases_activity_of"
    decreases_degradation_of = "biolink:decreases_degradation_of"
    decreases_expression_of = "biolink:decreases_expression_of"
    decreases_folding_of = "biolink:decreases_folding_of"
    decreases_localization_of = "biolink:decreases_localization_of"
    decreases_metabolic_processing_of = "biolink:decreases_metabolic_processing_of"
    decreases_molecular_interaction = "biolink:decreases_molecular_interaction"
    decreases_molecular_modification_of = "biolink:decreases_molecular_modification_of"
    decreases_mutation_rate_of = "biolink:decreases_mutation_rate_of"
    decreases_response_to = "biolink:decreases_response_to"
    decreases_secretion_of = "biolink:decreases_secretion_of"
    decreases_splicing_of = "biolink:decreases_splicing_of"
    decreases_stability_of = "biolink:decreases_stability_of"
    decreases_synthesis_of = "biolink:decreases_synthesis_of"
    decreases_transport_of = "biolink:decreases_transport_of"
    decreases_uptake_of = "biolink:decreases_uptake_of"
    degradation_affected_by = "biolink:degradation_affected_by"
    degradation_decreased_by = "biolink:degradation_decreased_by"
    degradation_increased_by = "biolink:degradation_increased_by"
    derives_from = "biolink:derives_from"
    derives_into = "biolink:derives_into"
    develops_from = "biolink:develops_from"
    develops_into = "biolink:develops_into"
    directly_interacts_with = "biolink:directly_interacts_with"
    disease_has_basis_in = "biolink:disease_has_basis_in"
    disrupted_by = "biolink:disrupted_by"
    disrupts = "biolink:disrupts"
    editor = "biolink:editor"
    enabled_by = "biolink:enabled_by"
    enables = "biolink:enables"
    entity_negatively_regulated_by_entity = "biolink:entity_negatively_regulated_by_entity"
    entity_negatively_regulates_entity = "biolink:entity_negatively_regulates_entity"
    entity_positively_regulated_by_entity = "biolink:entity_positively_regulated_by_entity"
    entity_positively_regulates_entity = "biolink:entity_positively_regulates_entity"
    entity_regulated_by_entity = "biolink:entity_regulated_by_entity"
    entity_regulates_entity = "biolink:entity_regulates_entity"
    exacerbates = "biolink:exacerbates"
    exact_match = "biolink:exact_match"
    expressed_in = "biolink:expressed_in"
    expresses = "biolink:expresses"
    expression_affected_by = "biolink:expression_affected_by"
    expression_decreased_by = "biolink:expression_decreased_by"
    expression_increased_by = "biolink:expression_increased_by"
    folding_affected_by = "biolink:folding_affected_by"
    folding_decreased_by = "biolink:folding_decreased_by"
    folding_increased_by = "biolink:folding_increased_by"
    food_component_of = "biolink:food_component_of"
    gene_associated_with_condition = "biolink:gene_associated_with_condition"
    gene_product_of = "biolink:gene_product_of"
    genetic_association = "biolink:genetic_association"
    genetically_interacts_with = "biolink:genetically_interacts_with"
    has_active_ingredient = "biolink:has_active_ingredient"
    has_biomarker = "biolink:has_biomarker"
    has_completed = "biolink:has_completed"
    has_contraindication = "biolink:has_contraindication"
    has_decreased_amount = "biolink:has_decreased_amount"
    has_excipient = "biolink:has_excipient"
    has_food_component = "biolink:has_food_component"
    has_frameshift_variant = "biolink:has_frameshift_variant"
    has_gene_product = "biolink:has_gene_product"
    has_increased_amount = "biolink:has_increased_amount"
    has_input = "biolink:has_input"
    has_manifestation = "biolink:has_manifestation"
    has_metabolite = "biolink:has_metabolite"
    has_missense_variant = "biolink:has_missense_variant"
    has_molecular_consequence = "biolink:has_molecular_consequence"
    has_nearby_variant = "biolink:has_nearby_variant"
    has_negative_upstream_actor = "biolink:has_negative_upstream_actor"
    has_negative_upstream_or_within_actor = "biolink:has_negative_upstream_or_within_actor"
    has_non_coding_variant = "biolink:has_non_coding_variant"
    has_nonsense_variant = "biolink:has_nonsense_variant"
    has_not_completed = "biolink:has_not_completed"
    has_nutrient = "biolink:has_nutrient"
    has_output = "biolink:has_output"
    has_part = "biolink:has_part"
    has_participant = "biolink:has_participant"
    has_phenotype = "biolink:has_phenotype"
    has_positive_upstream_actor = "biolink:has_positive_upstream_actor"
    has_positive_upstream_or_within_actor = "biolink:has_positive_upstream_or_within_actor"
    has_sequence_location = "biolink:has_sequence_location"
    has_sequence_variant = "biolink:has_sequence_variant"
    has_splice_site_variant = "biolink:has_splice_site_variant"
    has_substrate = "biolink:has_substrate"
    has_synonymous_variant = "biolink:has_synonymous_variant"
    has_upstream_actor = "biolink:has_upstream_actor"
    has_upstream_or_within_actor = "biolink:has_upstream_or_within_actor"
    has_variant_part = "biolink:has_variant_part"
    homologous_to = "biolink:homologous_to"
    in_cell_population_with = "biolink:in_cell_population_with"
    in_complex_with = "biolink:in_complex_with"
    in_linkage_disequilibrium_with = "biolink:in_linkage_disequilibrium_with"
    in_pathway_with = "biolink:in_pathway_with"
    in_taxon = "biolink:in_taxon"
    increased_amount_of = "biolink:increased_amount_of"
    increases_abundance_of = "biolink:increases_abundance_of"
    increases_activity_of = "biolink:increases_activity_of"
    increases_degradation_of = "biolink:increases_degradation_of"
    increases_expression_of = "biolink:increases_expression_of"
    increases_folding_of = "biolink:increases_folding_of"
    increases_localization_of = "biolink:increases_localization_of"
    increases_metabolic_processing_of = "biolink:increases_metabolic_processing_of"
    increases_molecular_interaction = "biolink:increases_molecular_interaction"
    increases_molecular_modification_of = "biolink:increases_molecular_modification_of"
    increases_mutation_rate_of = "biolink:increases_mutation_rate_of"
    increases_response_to = "biolink:increases_response_to"
    increases_secretion_of = "biolink:increases_secretion_of"
    increases_splicing_of = "biolink:increases_splicing_of"
    increases_stability_of = "biolink:increases_stability_of"
    increases_synthesis_of = "biolink:increases_synthesis_of"
    increases_transport_of = "biolink:increases_transport_of"
    increases_uptake_of = "biolink:increases_uptake_of"
    interacts_with = "biolink:interacts_with"
    is_active_ingredient_of = "biolink:is_active_ingredient_of"
    is_catalyst_of = "biolink:is_catalyst_of"
    is_excipient_of = "biolink:is_excipient_of"
    is_frameshift_variant_of = "biolink:is_frameshift_variant_of"
    is_input_of = "biolink:is_input_of"
    is_metabolite_of = "biolink:is_metabolite_of"
    is_missense_variant_of = "biolink:is_missense_variant_of"
    is_molecular_consequence_of = "biolink:is_molecular_consequence_of"
    is_nearby_variant_of = "biolink:is_nearby_variant_of"
    is_non_coding_variant_of = "biolink:is_non_coding_variant_of"
    is_nonsense_variant_of = "biolink:is_nonsense_variant_of"
    is_output_of = "biolink:is_output_of"
    is_sequence_variant_of = "biolink:is_sequence_variant_of"
    is_splice_site_variant_of = "biolink:is_splice_site_variant_of"
    is_substrate_of = "biolink:is_substrate_of"
    is_synonymous_variant_of = "biolink:is_synonymous_variant_of"
    lacks_part = "biolink:lacks_part"
    localization_affected_by = "biolink:localization_affected_by"
    localization_decreased_by = "biolink:localization_decreased_by"
    localization_increased_by = "biolink:localization_increased_by"
    located_in = "biolink:located_in"
    location_of = "biolink:location_of"
    manifestation_of = "biolink:manifestation_of"
    mentions = "biolink:mentions"
    metabolic_processing_affected_by = "biolink:metabolic_processing_affected_by"
    metabolic_processing_decreased_by = "biolink:metabolic_processing_decreased_by"
    metabolic_processing_increased_by = "biolink:metabolic_processing_increased_by"
    missing_from = "biolink:missing_from"
    model_of = "biolink:model_of"
    models = "biolink:models"
    molecular_activity_enabled_by = "biolink:molecular_activity_enabled_by"
    molecular_activity_has_input = "biolink:molecular_activity_has_input"
    molecular_activity_has_output = "biolink:molecular_activity_has_output"
    molecular_interaction_decreased_by = "biolink:molecular_interaction_decreased_by"
    molecular_interaction_increased_by = "biolink:molecular_interaction_increased_by"
    molecular_modification_affected_by = "biolink:molecular_modification_affected_by"
    molecular_modification_decreased_by = "biolink:molecular_modification_decreased_by"
    molecular_modification_increased_by = "biolink:molecular_modification_increased_by"
    molecularly_interacts_with = "biolink:molecularly_interacts_with"
    mutation_rate_affected_by = "biolink:mutation_rate_affected_by"
    mutation_rate_decreased_by = "biolink:mutation_rate_decreased_by"
    narrow_match = "biolink:narrow_match"
    negatively_correlated_with = "biolink:negatively_correlated_with"
    nutrient_of = "biolink:nutrient_of"
    occurs_in = "biolink:occurs_in"
    opposite_of = "biolink:opposite_of"
    organism_taxon_subclass_of = "biolink:organism_taxon_subclass_of"
    orthologous_to = "biolink:orthologous_to"
    overlaps = "biolink:overlaps"
    paralogous_to = "biolink:paralogous_to"
    part_of = "biolink:part_of"
    participates_in = "biolink:participates_in"
    phenotype_of = "biolink:phenotype_of"
    physically_interacts_with = "biolink:physically_interacts_with"
    positively_correlated_with = "biolink:positively_correlated_with"
    preceded_by = "biolink:preceded_by"
    precedes = "biolink:precedes"
    predisposes = "biolink:predisposes"
    prevented_by = "biolink:prevented_by"
    prevents = "biolink:prevents"
    process_negatively_regulated_by_process = "biolink:process_negatively_regulated_by_process"
    process_negatively_regulates_process = "biolink:process_negatively_regulates_process"
    process_positively_regulated_by_process = "biolink:process_positively_regulated_by_process"
    process_positively_regulates_process = "biolink:process_positively_regulates_process"
    process_regulated_by_process = "biolink:process_regulated_by_process"
    process_regulates_process = "biolink:process_regulates_process"
    produced_by = "biolink:produced_by"
    produces = "biolink:produces"
    provider = "biolink:provider"
    publisher = "biolink:publisher"
    related_condition = "biolink:related_condition"
    related_to = "biolink:related_to"
    response_affected_by = "biolink:response_affected_by"
    response_decreased_by = "biolink:response_decreased_by"
    response_increased_by = "biolink:response_increased_by"
    risk_affected_by = "biolink:risk_affected_by"
    same_as = "biolink:same_as"
    secretion_affected_by = "biolink:secretion_affected_by"
    secretion_decreased_by = "biolink:secretion_decreased_by"
    secretion_increased_by = "biolink:secretion_increased_by"
    sequence_location_of = "biolink:sequence_location_of"
    similar_to = "biolink:similar_to"
    splicing_affected_by = "biolink:splicing_affected_by"
    splicing_decreased_by = "biolink:splicing_decreased_by"
    splicing_increased_by = "biolink:splicing_increased_by"
    stability_affected_by = "biolink:stability_affected_by"
    stability_decreased_by = "biolink:stability_decreased_by"
    stability_increased_by = "biolink:stability_increased_by"
    subclass_of = "biolink:subclass_of"
    superclass_of = "biolink:superclass_of"
    synthesis_decreased_by = "biolink:synthesis_decreased_by"
    synthesis_increased_by = "biolink:synthesis_increased_by"
    sythesis_affected_by = "biolink:sythesis_affected_by"
    temporally_related_to = "biolink:temporally_related_to"
    transcribed_from = "biolink:transcribed_from"
    transcribed_to = "biolink:transcribed_to"
    translates_to = "biolink:translates_to"
    translation_of = "biolink:translation_of"
    transport_affected_by = "biolink:transport_affected_by"
    transport_decreased_by = "biolink:transport_decreased_by"
    transport_increased_by = "biolink:transport_increased_by"
    treated_by = "biolink:treated_by"
    treats = "biolink:treats"
    uptake_affected_by = "biolink:uptake_affected_by"
    uptake_decreased_by = "biolink:uptake_decreased_by"
    uptake_increased_by = "biolink:uptake_increased_by"
    variant_part_of = "biolink:variant_part_of"
    xenologous_to = "biolink:xenologous_to"


Predicate = namedtuple(
    'biolink_predicate', [pred.value.replace('biolink:', '') for pred in PredicateType]
)(*[pred.value for pred in PredicateType])


# Enumerations
@unique
class LogicalInterpretationEnum(str, Enum):

    SomeSome = "SomeSome"
    AllSome = "AllSome"
    InverseAllSome = "InverseAllSome"


@unique
class ReactionDirectionEnum(str, Enum):

    left_to_right = "left_to_right"
    right_to_left = "right_to_left"
    bidirectional = "bidirectional"
    neutral = "neutral"


@unique
class ReactionSideEnum(str, Enum):

    left = "left"
    right = "right"


@unique
class PhaseEnum(str, Enum):
    """
    phase
    """

    value_0 = "0"
    value_1 = "1"
    value_2 = "2"


@unique
class StrandEnum(str, Enum):
    """
    strand
    """

    value_0 = "+"
    value_1 = "-"
    value_2 = "."
    value_3 = "?"


@unique
class SequenceEnum(str, Enum):
    """
    type of sequence
    """

    NA = "NA"
    AA = "AA"


# Classes


@dataclass(config=PydanticConfig)
class OntologyClass:
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be
    considered both instances of biolink classes, and OWL classes in their own right. In general you should not need
    to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of
    endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
    """

    # Class Variables
    _id_prefixes: ClassVar[List[str]] = ["MESH", "UMLS", "KEGG.BRITE"]


@dataclass(config=PydanticConfig)
class Annotation:
    """
    Biolink Model root class for entity annotations.
    """


@dataclass(config=PydanticConfig)
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric
    value
    """

    # Class Variables
    _category: ClassVar[str] = "QuantityValue"

    has_unit: Optional[Union[str, Unit]] = None
    has_numeric_value: Optional[Union[float, float]] = None


@dataclass(config=PydanticConfig)
class Attribute(Annotation, OntologyClass):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """

    # Class Variables
    _category: ClassVar[str] = "Attribute"
    _id_prefixes: ClassVar[List[str]] = ["EDAM-DATA", "EDAM-FORMAT", "EDAM-OPERATION", "EDAM-TOPIC"]

    has_attribute_type: Union[str, OntologyClass] = None
    name: Optional[Union[str, LabelType]] = None
    has_quantitative_value: Optional[
        Union[List[Union[str, QuantityValue]], Union[str, QuantityValue]]
    ] = field(default_factory=list)
    has_qualitative_value: Optional[URIorCURIE] = None
    iri: Optional[IriType] = None
    source: Optional[Union[str, LabelType]] = None

    # Validators

    @validator('has_attribute_type')
    def validate_required_has_attribute_type(cls, value):
        check_value_is_not_none("has_attribute_type", value)
        return value

    @validator('has_quantitative_value')
    def convert_has_quantitative_value_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('has_qualitative_value')
    def check_has_qualitative_value_prefix(cls, value):
        check_curie_prefix(cls, value)
        return value


@dataclass(config=PydanticConfig)
class BiologicalSex(Attribute):

    # Class Variables
    _category: ClassVar[str] = "BiologicalSex"


@dataclass(config=PydanticConfig)
class PhenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
    """

    # Class Variables
    _category: ClassVar[str] = "PhenotypicSex"


@dataclass(config=PydanticConfig)
class GenotypicSex(BiologicalSex):
    """
    An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex
    chromosomes.
    """

    # Class Variables
    _category: ClassVar[str] = "GenotypicSex"


@dataclass(config=PydanticConfig)
class SeverityValue(Attribute):
    """
    describes the severity of a phenotypic feature or disease
    """

    # Class Variables
    _category: ClassVar[str] = "SeverityValue"


@dataclass(config=PydanticConfig)
class RelationshipQuantifier:

    pass


@dataclass(config=PydanticConfig)
class SensitivityQuantifier(RelationshipQuantifier):

    pass


@dataclass(config=PydanticConfig)
class SpecificityQuantifier(RelationshipQuantifier):

    pass


@dataclass(config=PydanticConfig)
class PathognomonicityQuantifier(SpecificityQuantifier):
    """
    A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the
    feature implies the existence of the disease
    """


@dataclass(config=PydanticConfig)
class FrequencyQuantifier(RelationshipQuantifier):
    has_count: Optional[Union[int, int]] = None
    has_total: Optional[Union[int, int]] = None
    has_quotient: Optional[Union[float, float]] = None
    has_percentage: Optional[Union[float, float]] = None


@dataclass(config=PydanticConfig)
class ChemicalOrDrugOrTreatment:

    pass


@dataclass(config=PydanticConfig)
class Entity:
    """
    Root Biolink Model class for all things and informational relationships, real or imagined.
    """

    id: URIorCURIE = None
    iri: Optional[IriType] = None
    category: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)
    type: Optional[Union[str, str]] = None
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    source: Optional[Union[str, LabelType]] = None
    provided_by: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)
    has_attribute: Optional[Union[List[Union[str, Attribute]], Union[str, Attribute]]] = field(
        default_factory=list
    )

    # Validators

    @validator('id')
    def validate_required_id(cls, value):
        check_value_is_not_none("id", value)
        check_curie_prefix(cls, value)
        return value

    @validator('category')
    def convert_category_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('provided_by')
    def convert_provided_by_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('has_attribute')
    def convert_has_attribute_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    def __post_init__(self):
        # Initialize default categories if not set
        # by traversing the MRO chain
        if not self.category:
            self.category = list(
                {
                    f'biolink:{super_class._category}'
                    for super_class in inspect.getmro(type(self))
                    if hasattr(super_class, '_category')
                }
            )


@dataclass(config=PydanticConfig)
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """

    # Class Variables
    _category: ClassVar[str] = "NamedThing"

    category: Union[List[URIorCURIE], URIorCURIE] = None

    # Validators

    @validator('category')
    def validate_required_category(cls, value):
        check_value_is_not_none("category", value)
        convert_scalar_to_list_check_curies(cls, value)
        return value


@dataclass(config=PydanticConfig)
class RelationshipType(OntologyClass):
    """
    An OWL property used as an edge label
    """

    # Class Variables
    _category: ClassVar[str] = "RelationshipType"


@dataclass(config=PydanticConfig)
class GeneOntologyClass(OntologyClass):
    """
    an ontology class that describes a functional aspect of a gene, gene prodoct or complex
    """


@dataclass(config=PydanticConfig)
class UnclassifiedOntologyClass(OntologyClass):
    """
    this is used for nodes that are taken from an ontology but are not typed using an existing biolink class
    """


@dataclass(config=PydanticConfig)
class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """

    # Class Variables
    _category: ClassVar[str] = "TaxonomicRank"
    _id_prefixes: ClassVar[List[str]] = ["TAXRANK"]


@dataclass(config=PydanticConfig)
class OrganismTaxon(NamedThing):
    """
    A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria).
    Can also be used to represent strains or subspecies.
    """

    # Class Variables
    _category: ClassVar[str] = "OrganismTaxon"
    _id_prefixes: ClassVar[List[str]] = ["NCBITaxon", "MESH"]

    has_taxonomic_rank: Optional[Union[str, TaxonomicRank]] = None
    subclass_of: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)

    # Validators

    @validator('subclass_of')
    def convert_subclass_of_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)


@dataclass(config=PydanticConfig)
class AdministrativeEntity(NamedThing):

    pass


@dataclass(config=PydanticConfig)
class Agent(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """

    # Class Variables
    _category: ClassVar[str] = "Agent"
    _id_prefixes: ClassVar[List[str]] = ["isbn", "ORCID", "ScopusID", "ResearchID", "GSID", "isni"]

    id: URIorCURIE = None
    affiliation: Optional[Union[List[Union[str, URIorCURIE]], Union[str, URIorCURIE]]] = field(
        default_factory=list
    )
    address: Optional[Union[str, str]] = None
    name: Optional[Union[str, LabelType]] = None

    # Validators

    @validator('affiliation')
    def convert_affiliation_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('id')
    def validate_required_id(cls, value):
        check_value_is_not_none("id", value)
        check_curie_prefix(cls, value)
        return value


@dataclass(config=PydanticConfig)
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """

    # Class Variables
    _id_prefixes: ClassVar[List[str]] = ["doi"]

    license: Optional[Union[str, str]] = None
    rights: Optional[Union[str, str]] = None
    format: Optional[Union[str, str]] = None
    creation_date: Optional[Union[str, XSDDate]] = None


@dataclass(config=PydanticConfig)
class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """

    # Class Variables
    _category: ClassVar[str] = "Dataset"


@dataclass(config=PydanticConfig)
class DatasetDistribution(InformationContentEntity):
    """
    an item that holds distribution level information about a dataset.
    """

    # Class Variables
    _category: ClassVar[str] = "DatasetDistribution"

    distribution_download_url: Optional[Union[str, str]] = None


@dataclass(config=PydanticConfig)
class DatasetVersion(InformationContentEntity):
    """
    an item that holds version level information about a dataset.
    """

    # Class Variables
    _category: ClassVar[str] = "DatasetVersion"

    has_dataset: Optional[Union[URIorCURIE, Dataset]] = None
    ingest_date: Optional[Union[str, str]] = None
    has_distribution: Optional[Union[URIorCURIE, DatasetDistribution]] = None

    # Validators

    @validator('has_dataset')
    def check_has_dataset_prefix(cls, value):
        check_curie_prefix(Dataset, value)
        return value

    @validator('has_distribution')
    def check_has_distribution_prefix(cls, value):
        check_curie_prefix(DatasetDistribution, value)
        return value


@dataclass(config=PydanticConfig)
class DatasetSummary(InformationContentEntity):
    """
    an item that holds summary level information about a dataset.
    """

    # Class Variables
    _category: ClassVar[str] = "DatasetSummary"

    source_web_page: Optional[Union[str, str]] = None
    source_logo: Optional[Union[str, str]] = None


@dataclass(config=PydanticConfig)
class ConfidenceLevel(InformationContentEntity):
    """
    Level of confidence in a statement
    """

    # Class Variables
    _category: ClassVar[str] = "ConfidenceLevel"


@dataclass(config=PydanticConfig)
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """

    # Class Variables
    _category: ClassVar[str] = "EvidenceType"


@dataclass(config=PydanticConfig)
class InformationResource(InformationContentEntity):
    """
    A database or knowledgebase and its supporting ecosystem of interfaces and services that deliver content to
    consumers (e.g. web portals, APIs, query endpoints, streaming services, data downloads, etc.). A single
    Information Resource by this definition may span many different datasets or databases, and include many access
    endpoints and user interfaces. Information Resources include project-specific resources such as a Translator
    Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb.
    """

    # Class Variables
    _category: ClassVar[str] = "InformationResource"


@dataclass(config=PydanticConfig)
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal
    or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or
    section highlighted by NLP). The scope is intended to be general and include information published on the web, as
    well as printed materials, either directly or in one of the Publication Biolink category subclasses.
    """

    # Class Variables
    _category: ClassVar[str] = "Publication"
    _id_prefixes: ClassVar[List[str]] = ["NLMID"]

    id: URIorCURIE = None
    type: Union[str, str] = None
    authors: Optional[Union[List[Union[str, str]], Union[str, str]]] = field(default_factory=list)
    pages: Optional[Union[List[Union[str, str]], Union[str, str]]] = field(default_factory=list)
    summary: Optional[Union[str, str]] = None
    keywords: Optional[Union[List[Union[str, str]], Union[str, str]]] = field(default_factory=list)
    mesh_terms: Optional[Union[List[Union[str, URIorCURIE]], Union[str, URIorCURIE]]] = field(
        default_factory=list
    )
    xref: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)
    name: Optional[Union[str, LabelType]] = None

    # Validators

    @validator('authors')
    def convert_authors_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('pages')
    def convert_pages_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('keywords')
    def convert_keywords_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('mesh_terms')
    def convert_mesh_terms_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('xref')
    def convert_xref_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('id')
    def validate_required_id(cls, value):
        check_value_is_not_none("id", value)
        check_curie_prefix(cls, value)
        return value

    @validator('type')
    def validate_required_type(cls, value):
        check_value_is_not_none("type", value)
        return value


@dataclass(config=PydanticConfig)
class Book(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """

    # Class Variables
    _category: ClassVar[str] = "Book"
    _id_prefixes: ClassVar[List[str]] = ["isbn", "NLMID"]

    id: URIorCURIE = None
    type: Union[str, str] = None

    # Validators

    @validator('id')
    def validate_required_id(cls, value):
        check_value_is_not_none("id", value)
        check_curie_prefix(cls, value)
        return value

    @validator('type')
    def validate_required_type(cls, value):
        check_value_is_not_none("type", value)
        return value


@dataclass(config=PydanticConfig)
class BookChapter(Publication):

    # Class Variables
    _category: ClassVar[str] = "BookChapter"

    published_in: Union[str, URIorCURIE] = None
    volume: Optional[Union[str, str]] = None
    chapter: Optional[Union[str, str]] = None

    # Validators

    @validator('published_in')
    def validate_required_published_in(cls, value):
        check_value_is_not_none("published_in", value)
        check_curie_prefix(cls, value)
        return value


@dataclass(config=PydanticConfig)
class Serial(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """

    # Class Variables
    _category: ClassVar[str] = "Serial"
    _id_prefixes: ClassVar[List[str]] = ["issn", "NLMID"]

    id: URIorCURIE = None
    type: Union[str, str] = None
    iso_abbreviation: Optional[Union[str, str]] = None
    volume: Optional[Union[str, str]] = None
    issue: Optional[Union[str, str]] = None

    # Validators

    @validator('id')
    def validate_required_id(cls, value):
        check_value_is_not_none("id", value)
        check_curie_prefix(cls, value)
        return value

    @validator('type')
    def validate_required_type(cls, value):
        check_value_is_not_none("type", value)
        return value


@dataclass(config=PydanticConfig)
class Article(Publication):

    # Class Variables
    _category: ClassVar[str] = "Article"
    _id_prefixes: ClassVar[List[str]] = ["PMID"]

    published_in: Union[str, URIorCURIE] = None
    iso_abbreviation: Optional[Union[str, str]] = None
    volume: Optional[Union[str, str]] = None
    issue: Optional[Union[str, str]] = None

    # Validators

    @validator('published_in')
    def validate_required_published_in(cls, value):
        check_value_is_not_none("published_in", value)
        check_curie_prefix(cls, value)
        return value


@dataclass(config=PydanticConfig)
class PhysicalEssenceOrOccurrent:
    """
    Either a physical or processual entity.
    """


@dataclass(config=PydanticConfig)
class PhysicalEssence(PhysicalEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
    """


@dataclass(config=PydanticConfig)
class PhysicalEntity(NamedThing, PhysicalEssence):
    """
    An entity that has material reality (a.k.a. physical essence).
    """

    # Class Variables
    _category: ClassVar[str] = "PhysicalEntity"


@dataclass(config=PydanticConfig)
class Occurrent(PhysicalEssenceOrOccurrent):
    """
    A processual entity.
    """


@dataclass(config=PydanticConfig)
class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """


@dataclass(config=PydanticConfig)
class Activity(NamedThing, ActivityAndBehavior):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include
    consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """

    # Class Variables
    _category: ClassVar[str] = "Activity"


@dataclass(config=PydanticConfig)
class Procedure(NamedThing, ActivityAndBehavior):
    """
    A series of actions conducted in a certain order or manner
    """

    # Class Variables
    _category: ClassVar[str] = "Procedure"


@dataclass(config=PydanticConfig)
class Phenomenon(NamedThing, Occurrent):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """

    # Class Variables
    _category: ClassVar[str] = "Phenomenon"


@dataclass(config=PydanticConfig)
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """

    # Class Variables
    _category: ClassVar[str] = "Device"


@dataclass(config=PydanticConfig)
class SubjectOfInvestigation:
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """


@dataclass(config=PydanticConfig)
class MaterialSample(PhysicalEntity, SubjectOfInvestigation):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    [SIO]
    """

    # Class Variables
    _category: ClassVar[str] = "MaterialSample"
    _id_prefixes: ClassVar[List[str]] = ["BIOSAMPLE", "GOLD.META"]


@dataclass(config=PydanticConfig)
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """

    # Class Variables
    _category: ClassVar[str] = "PlanetaryEntity"


@dataclass(config=PydanticConfig)
class EnvironmentalProcess(PlanetaryEntity, Occurrent):

    # Class Variables
    _category: ClassVar[str] = "EnvironmentalProcess"


@dataclass(config=PydanticConfig)
class EnvironmentalFeature(PlanetaryEntity):

    # Class Variables
    _category: ClassVar[str] = "EnvironmentalFeature"


@dataclass(config=PydanticConfig)
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """

    # Class Variables
    _category: ClassVar[str] = "GeographicLocation"

    latitude: Optional[Union[float, float]] = None
    longitude: Optional[Union[float, float]] = None


@dataclass(config=PydanticConfig)
class GeographicLocationAtTime(GeographicLocation):
    """
    a location that can be described in lat/long coordinates, for a particular time
    """

    # Class Variables
    _category: ClassVar[str] = "GeographicLocationAtTime"

    timepoint: Optional[Union[str, TimeType]] = None


@dataclass(config=PydanticConfig)
class BiologicalEntity(NamedThing):

    pass


@dataclass(config=PydanticConfig)
class ThingWithTaxon:
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms;
    genes, their products and other molecular entities; body parts; biological processes
    """

    in_taxon: Optional[
        Union[List[Union[URIorCURIE, OrganismTaxon]], Union[URIorCURIE, OrganismTaxon]]
    ] = field(default_factory=list)

    # Validators

    @validator('in_taxon')
    def convert_in_taxon_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(OrganismTaxon, value)


@dataclass(config=PydanticConfig)
class GenomicEntity(ThingWithTaxon):

    pass


@dataclass(config=PydanticConfig)
class ChemicalEntity(NamedThing, PhysicalEssence, ChemicalOrDrugOrTreatment):
    """
    A chemical entity is a physical entity that pertains to chemistry or biochemistry.
    """


@dataclass(config=PydanticConfig)
class MolecularEntity(ChemicalEntity):
    """
    A molecular entity is a chemical entity composed of individual or covalently bonded atoms.
    """

    # Class Variables
    _category: ClassVar[str] = "MolecularEntity"

    is_metabolite: Optional[Union[bool, Bool]] = None


@dataclass(config=PydanticConfig)
class ChemicalSubstance:

    # Class Variables
    _category: ClassVar[str] = "ChemicalSubstance"


@dataclass(config=PydanticConfig)
class SmallMolecule(MolecularEntity):
    """
    A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES,
    InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of
    representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium
    ion).
    """

    # Class Variables
    _category: ClassVar[str] = "SmallMolecule"
    _id_prefixes: ClassVar[List[str]] = [
        "PUBCHEM.COMPOUND",
        "CHEMBL.COMPOUND",
        "UNII",
        "CHEBI",
        "DRUGBANK",
        "MESH",
        "CAS",
        "DrugCentral",
        "GTOPDB",
        "HMDB",
        "KEGG.COMPOUND",
        "ChemBank",
        "Aeolus",
        "PUBCHEM.SUBSTANCE",
        "SIDER.DRUG",
        "INCHI",
        "INCHIKEY",
        "KEGG.GLYCAN",
        "KEGG.DRUG",
        "KEGG.DGROUP",
        "KEGG.ENVIRON",
    ]

    id: URIorCURIE = None

    # Validators

    @validator('id')
    def validate_required_id(cls, value):
        check_value_is_not_none("id", value)
        check_curie_prefix(cls, value)
        return value


@dataclass(config=PydanticConfig)
class ChemicalMixture(ChemicalEntity):
    """
    A chemical mixture is a chemical entity composed of two or more molecular entities.
    """

    # Class Variables
    _category: ClassVar[str] = "ChemicalMixture"


@dataclass(config=PydanticConfig)
class NucleicAcidEntity(MolecularEntity, GenomicEntity):
    """
    A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based
    sequence representations of its precise sequence; for convenience of representation, partial sequences of various
    kinds are included, even if they do not represent a physical molecule.
    """

    # Class Variables
    _category: ClassVar[str] = "NucleicAcidEntity"

    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None


@dataclass(config=PydanticConfig)
class MolecularMixture(ChemicalMixture):
    """
    A molecular mixture is a chemical mixture composed of two or more molecular entities with known concentration and
    stoichiometry.
    """

    # Class Variables
    _category: ClassVar[str] = "MolecularMixture"


@dataclass(config=PydanticConfig)
class ComplexMolecularMixture(ChemicalMixture):
    """
    A complex molecular mixture is a chemical mixture composed of two or more molecular entities with unknown
    concentration and stoichiometry.
    """

    # Class Variables
    _category: ClassVar[str] = "ComplexMolecularMixture"


@dataclass(config=PydanticConfig)
class BiologicalProcessOrActivity(BiologicalEntity, Occurrent, OntologyClass):
    """
    Either an individual molecular activity, or a collection of causally connected molecular activities in a
    biological system.
    """

    # Class Variables
    _category: ClassVar[str] = "BiologicalProcessOrActivity"
    _id_prefixes: ClassVar[List[str]] = ["GO", "REACT"]

    has_input: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)
    has_output: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)
    enabled_by: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)

    # Validators

    @validator('has_input')
    def convert_has_input_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('has_output')
    def convert_has_output_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('enabled_by')
    def convert_enabled_by_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)


@dataclass(config=PydanticConfig)
class MolecularActivity(BiologicalProcessOrActivity, Occurrent, OntologyClass):
    """
    An execution of a molecular function carried out by a gene product or macromolecular complex.
    """

    # Class Variables
    _category: ClassVar[str] = "MolecularActivity"
    _id_prefixes: ClassVar[List[str]] = [
        "GO",
        "REACT",
        "RHEA",
        "MetaCyc",
        "EC",
        "TCDB",
        "KEGG.REACTION",
        "KEGG.RCLASS",
        "KEGG.ENZYME",
    ]

    has_input: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)
    has_output: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)
    enabled_by: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)

    # Validators

    @validator('has_input')
    def convert_has_input_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('has_output')
    def convert_has_output_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('enabled_by')
    def convert_enabled_by_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)


@dataclass(config=PydanticConfig)
class BiologicalProcess(BiologicalProcessOrActivity, Occurrent, OntologyClass):
    """
    One or more causally connected executions of molecular functions
    """

    # Class Variables
    _category: ClassVar[str] = "BiologicalProcess"
    _id_prefixes: ClassVar[List[str]] = ["GO", "REACT", "MetaCyc", "KEGG.MODULE"]


@dataclass(config=PydanticConfig)
class Pathway(BiologicalProcess, OntologyClass):

    # Class Variables
    _category: ClassVar[str] = "Pathway"
    _id_prefixes: ClassVar[List[str]] = [
        "GO",
        "REACT",
        "KEGG",
        "SMPDB",
        "MSigDB",
        "PHARMGKB.PATHWAYS",
        "WIKIPATHWAYS",
        "FB",
        "PANTHER.PATHWAY",
    ]


@dataclass(config=PydanticConfig)
class PhysiologicalProcess(BiologicalProcess, OntologyClass):

    # Class Variables
    _category: ClassVar[str] = "PhysiologicalProcess"
    _id_prefixes: ClassVar[List[str]] = ["GO", "REACT"]


@dataclass(config=PydanticConfig)
class Behavior(BiologicalProcess, OntologyClass):

    # Class Variables
    _category: ClassVar[str] = "Behavior"


@dataclass(config=PydanticConfig)
class Death(BiologicalProcess):

    # Class Variables
    _category: ClassVar[str] = "Death"


@dataclass(config=PydanticConfig)
class ProcessedMaterial(ChemicalMixture):
    """
    A chemical entity (often a mixture) processed for consumption for nutritional, medical or technical use. Is a
    material entity that is created or changed during material processing.
    """

    # Class Variables
    _category: ClassVar[str] = "ProcessedMaterial"


@dataclass(config=PydanticConfig)
class Drug(MolecularMixture, ChemicalOrDrugOrTreatment, OntologyClass):
    """
    A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
    """

    # Class Variables
    _category: ClassVar[str] = "Drug"
    _id_prefixes: ClassVar[List[str]] = ["RXCUI", "NDC", "PHARMGKB.DRUG"]


@dataclass(config=PydanticConfig)
class EnvironmentalFoodContaminant(ChemicalEntity):

    # Class Variables
    _category: ClassVar[str] = "EnvironmentalFoodContaminant"


@dataclass(config=PydanticConfig)
class FoodAdditive(ChemicalEntity):

    # Class Variables
    _category: ClassVar[str] = "FoodAdditive"


@dataclass(config=PydanticConfig)
class Nutrient(ChemicalEntity):

    # Class Variables
    _category: ClassVar[str] = "Nutrient"


@dataclass(config=PydanticConfig)
class Macronutrient(Nutrient):

    # Class Variables
    _category: ClassVar[str] = "Macronutrient"


@dataclass(config=PydanticConfig)
class Micronutrient(Nutrient):

    # Class Variables
    _category: ClassVar[str] = "Micronutrient"


@dataclass(config=PydanticConfig)
class Vitamin(Micronutrient):

    # Class Variables
    _category: ClassVar[str] = "Vitamin"


@dataclass(config=PydanticConfig)
class Food(ChemicalMixture):
    """
    A substance consumed by a living organism as a source of nutrition
    """

    # Class Variables
    _category: ClassVar[str] = "Food"
    _id_prefixes: ClassVar[List[str]] = ["foodb.compound"]


@dataclass(config=PydanticConfig)
class OrganismAttribute(Attribute):
    """
    describes a characteristic of an organismal entity.
    """

    # Class Variables
    _category: ClassVar[str] = "OrganismAttribute"


@dataclass(config=PydanticConfig)
class PhenotypicQuality(OrganismAttribute):
    """
    A property of a phenotype
    """

    # Class Variables
    _category: ClassVar[str] = "PhenotypicQuality"


@dataclass(config=PydanticConfig)
class Inheritance(OrganismAttribute):
    """
    The pattern or 'mode' in which a particular genetic trait or disorder is passed from one generation to the next,
    e.g. autosomal dominant, autosomal recessive, etc.
    """

    # Class Variables
    _category: ClassVar[str] = "Inheritance"


@dataclass(config=PydanticConfig)
class OrganismalEntity(BiologicalEntity):
    """
    A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding
    chemical entities
    """

    has_attribute: Optional[Union[List[Union[str, Attribute]], Union[str, Attribute]]] = field(
        default_factory=list
    )

    # Validators

    @validator('has_attribute')
    def convert_has_attribute_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)


@dataclass(config=PydanticConfig)
class LifeStage(OrganismalEntity, ThingWithTaxon):
    """
    A stage of development or growth of an organism, including post-natal adult stages
    """

    # Class Variables
    _category: ClassVar[str] = "LifeStage"


@dataclass(config=PydanticConfig)
class IndividualOrganism(OrganismalEntity, ThingWithTaxon):
    """
    An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID:
    ORCID:0000-0002-5355-2576
    """

    # Class Variables
    _category: ClassVar[str] = "IndividualOrganism"
    _id_prefixes: ClassVar[List[str]] = ["ORCID"]


@dataclass(config=PydanticConfig)
class PopulationOfIndividualOrganisms(OrganismalEntity, ThingWithTaxon):
    """
    A collection of individuals from the same taxonomic class distinguished by one or more characteristics.
    Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance
    for Genome Resources]
    """

    # Class Variables
    _category: ClassVar[str] = "PopulationOfIndividualOrganisms"
    _id_prefixes: ClassVar[List[str]] = ["HANCESTRO"]


@dataclass(config=PydanticConfig)
class StudyPopulation(PopulationOfIndividualOrganisms):
    """
    A group of people banded together or treated as a group as participants in a research study.
    """

    # Class Variables
    _category: ClassVar[str] = "StudyPopulation"


@dataclass(config=PydanticConfig)
class DiseaseOrPhenotypicFeature(BiologicalEntity, ThingWithTaxon):
    """
    Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these
    as distinct, others such as MESH conflate.
    """

    # Class Variables
    _category: ClassVar[str] = "DiseaseOrPhenotypicFeature"


@dataclass(config=PydanticConfig)
class Disease(DiseaseOrPhenotypicFeature):

    # Class Variables
    _category: ClassVar[str] = "Disease"
    _id_prefixes: ClassVar[List[str]] = [
        "MONDO",
        "DOID",
        "OMIM",
        "ORPHANET",
        "EFO",
        "UMLS",
        "MESH",
        "MEDDRA",
        "NCIT",
        "SNOMEDCT",
        "medgen",
        "ICD10",
        "ICD9",
        "ICD0",
        "KEGG.DISEASE",
        "HP",
        "MP",
    ]


@dataclass(config=PydanticConfig)
class PhenotypicFeature(DiseaseOrPhenotypicFeature):

    # Class Variables
    _category: ClassVar[str] = "PhenotypicFeature"
    _id_prefixes: ClassVar[List[str]] = [
        "HP",
        "EFO",
        "NCIT",
        "UMLS",
        "MEDDRA",
        "MP",
        "ZP",
        "UPHENO",
        "APO",
        "FBcv",
        "WBPhenotype",
        "SNOMEDCT",
        "MESH",
        "XPO",
    ]


@dataclass(config=PydanticConfig)
class BehavioralFeature(PhenotypicFeature):
    """
    A phenotypic feature which is behavioral in nature.
    """

    # Class Variables
    _category: ClassVar[str] = "BehavioralFeature"


@dataclass(config=PydanticConfig)
class AnatomicalEntity(OrganismalEntity, ThingWithTaxon, PhysicalEssence):
    """
    A subcellular location, cell type or gross anatomical part
    """

    # Class Variables
    _category: ClassVar[str] = "AnatomicalEntity"
    _id_prefixes: ClassVar[List[str]] = ["UBERON", "GO", "CL", "UMLS", "MESH", "NCIT"]


@dataclass(config=PydanticConfig)
class CellularComponent(AnatomicalEntity):
    """
    A location in or around a cell
    """

    # Class Variables
    _category: ClassVar[str] = "CellularComponent"
    _id_prefixes: ClassVar[List[str]] = ["GO", "MESH", "UMLS", "NCIT", "SNOMEDCT", "CL", "UBERON"]


@dataclass(config=PydanticConfig)
class Cell(AnatomicalEntity):

    # Class Variables
    _category: ClassVar[str] = "Cell"
    _id_prefixes: ClassVar[List[str]] = ["CL", "PO", "UMLS", "NCIT", "MESH", "UBERON", "SNOMEDCT"]


@dataclass(config=PydanticConfig)
class CellLine(OrganismalEntity):

    # Class Variables
    _category: ClassVar[str] = "CellLine"
    _id_prefixes: ClassVar[List[str]] = ["CLO"]


@dataclass(config=PydanticConfig)
class GrossAnatomicalStructure(AnatomicalEntity):

    # Class Variables
    _category: ClassVar[str] = "GrossAnatomicalStructure"
    _id_prefixes: ClassVar[List[str]] = ["UBERON", "UMLS", "MESH", "NCIT", "PO", "FAO"]


@dataclass(config=PydanticConfig)
class MacromolecularMachineMixin:
    """
    A union of gene locus, gene product, and macromolecular complex mixin. These are the basic units of function in a
    cell. They either carry out individual biological activities, or they encode molecules which do this.
    """

    name: Optional[Union[str, SymbolType]] = None


@dataclass(config=PydanticConfig)
class GeneOrGeneProduct(MacromolecularMachineMixin):
    """
    A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another
    """

    # Class Variables
    _id_prefixes: ClassVar[List[str]] = ["CHEMBL.TARGET", "IUPHAR.FAMILY"]


@dataclass(config=PydanticConfig)
class Gene(NucleicAcidEntity, GeneOrGeneProduct, ThingWithTaxon):
    """
    A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A
    gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
    """

    # Class Variables
    _category: ClassVar[str] = "Gene"
    _id_prefixes: ClassVar[List[str]] = [
        "NCBIGene",
        "ENSEMBL",
        "HGNC",
        "MGI",
        "ZFIN",
        "dictyBase",
        "WB",
        "WormBase",
        "FB",
        "RGD",
        "SGD",
        "POMBASE",
        "OMIM",
        "KEGG.GENE",
        "UMLS",
        "Xenbase",
    ]

    symbol: Optional[Union[str, str]] = None
    synonym: Optional[Union[List[Union[str, LabelType]], Union[str, LabelType]]] = field(
        default_factory=list
    )
    xref: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)

    # Validators

    @validator('synonym')
    def convert_synonym_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('xref')
    def convert_xref_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)


@dataclass(config=PydanticConfig)
class GeneProductMixin(GeneOrGeneProduct):
    """
    The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA
    molecules.
    """

    # Class Variables
    _id_prefixes: ClassVar[List[str]] = ["UniProtKB", "gtpo", "PR"]

    synonym: Optional[Union[List[Union[str, LabelType]], Union[str, LabelType]]] = field(
        default_factory=list
    )
    xref: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)

    # Validators

    @validator('synonym')
    def convert_synonym_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('xref')
    def convert_xref_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)


@dataclass(config=PydanticConfig)
class GeneProductIsoformMixin(GeneProductMixin):
    """
    This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene
    product is intended to represent a specific isoform rather than a canonical or reference or generic product. The
    designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
    """


@dataclass(config=PydanticConfig)
class MacromolecularComplexMixin(MacromolecularMachineMixin):
    """
    A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which
    at least one component is a protein and the constituent parts function together.
    """

    # Class Variables
    _id_prefixes: ClassVar[List[str]] = ["INTACT", "GO", "PR", "REACT"]


@dataclass(config=PydanticConfig)
class Genome(BiologicalEntity, GenomicEntity):
    """
    A genome is the sum of genetic material within a cell or virion.
    """

    # Class Variables
    _category: ClassVar[str] = "Genome"


@dataclass(config=PydanticConfig)
class Exon(NucleicAcidEntity):
    """
    A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA
    splicing.
    """

    # Class Variables
    _category: ClassVar[str] = "Exon"


@dataclass(config=PydanticConfig)
class Transcript(NucleicAcidEntity):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase.
    """

    # Class Variables
    _category: ClassVar[str] = "Transcript"
    _id_prefixes: ClassVar[List[str]] = ["ENSEMBL", "FB"]


@dataclass(config=PydanticConfig)
class CodingSequence(NucleicAcidEntity):

    # Class Variables
    _category: ClassVar[str] = "CodingSequence"


@dataclass(config=PydanticConfig)
class Polypeptide(MolecularEntity):
    """
    A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based
    sequence representations of its precise primary structure; for convenience of representation, partial sequences of
    various kinds are included, even if they do not represent a physical molecule.
    """

    # Class Variables
    _category: ClassVar[str] = "Polypeptide"
    _id_prefixes: ClassVar[List[str]] = ["UniProtKB", "PR", "ENSEMBL", "FB", "UMLS"]


@dataclass(config=PydanticConfig)
class Protein(Polypeptide, GeneProductMixin):
    """
    A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated
    translation of mRNA
    """

    # Class Variables
    _category: ClassVar[str] = "Protein"


@dataclass(config=PydanticConfig)
class ProteinIsoform(Protein, GeneProductIsoformMixin):
    """
    Represents a protein that is a specific isoform of the canonical or reference protein. See
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
    """

    # Class Variables
    _category: ClassVar[str] = "ProteinIsoform"
    _id_prefixes: ClassVar[List[str]] = ["UniProtKB", "UNIPROT.ISOFORM", "PR", "ENSEMBL"]


@dataclass(config=PydanticConfig)
class RNAProduct(Transcript, GeneProductMixin):

    # Class Variables
    _category: ClassVar[str] = "RNAProduct"
    _id_prefixes: ClassVar[List[str]] = ["RNACENTRAL"]


@dataclass(config=PydanticConfig)
class RNAProductIsoform(RNAProduct, GeneProductIsoformMixin):
    """
    Represents a protein that is a specific isoform of the canonical or reference RNA
    """

    # Class Variables
    _category: ClassVar[str] = "RNAProductIsoform"
    _id_prefixes: ClassVar[List[str]] = ["RNACENTRAL"]


@dataclass(config=PydanticConfig)
class NoncodingRNAProduct(RNAProduct):

    # Class Variables
    _category: ClassVar[str] = "NoncodingRNAProduct"
    _id_prefixes: ClassVar[List[str]] = ["RNACENTRAL", "NCBIGene", "ENSEMBL"]


@dataclass(config=PydanticConfig)
class MicroRNA(NoncodingRNAProduct):

    # Class Variables
    _category: ClassVar[str] = "MicroRNA"
    _id_prefixes: ClassVar[List[str]] = ["MIR", "HGNC", "WormBase"]


@dataclass(config=PydanticConfig)
class SiRNA(NoncodingRNAProduct):
    """
    A small RNA molecule that is the product of a longer exogenous or endogenous dsRNA, which is either a bimolecular
    duplex or very long hairpin, processed (via the Dicer pathway) such that numerous siRNAs accumulate from both
    strands of the dsRNA. SRNAs trigger the cleavage of their target molecules.
    """

    # Class Variables
    _category: ClassVar[str] = "SiRNA"
    _id_prefixes: ClassVar[List[str]] = ["MIR", "HGNC", "WormBase"]


@dataclass(config=PydanticConfig)
class GeneGroupingMixin:
    """
    any grouping of multiple genes or gene products
    """

    has_gene_or_gene_product: Optional[
        Union[List[Union[URIorCURIE, Gene]], Union[URIorCURIE, Gene]]
    ] = field(default_factory=list)

    # Validators

    @validator('has_gene_or_gene_product')
    def convert_has_gene_or_gene_product_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(Gene, value)


@dataclass(config=PydanticConfig)
class GeneFamily(NucleicAcidEntity, GeneGroupingMixin):
    """
    any grouping of multiple genes or gene products related by common descent
    """

    # Class Variables
    _category: ClassVar[str] = "GeneFamily"
    _id_prefixes: ClassVar[List[str]] = [
        "PANTHER.FAMILY",
        "HGNC.FAMILY",
        "FB",
        "interpro",
        "CATH",
        "CDD",
        "HAMAP",
        "PFAM",
        "PIRSF",
        "PRINTS",
        "PRODOM",
        "PROSITE",
        "SMART",
        "SUPFAM",
        "TIGRFAM",
        "CATH.SUPERFAMILY",
        "RFAM",
        "KEGG.ORTHOLOGY",
        "EGGNOG",
    ]


@dataclass(config=PydanticConfig)
class Zygosity(Attribute):

    # Class Variables
    _category: ClassVar[str] = "Zygosity"


@dataclass(config=PydanticConfig)
class Genotype(BiologicalEntity, PhysicalEssence, GenomicEntity):
    """
    An information content entity that describes a genome by specifying the total variation in genomic sequence and/or
    gene expression, relative to some established background
    """

    # Class Variables
    _category: ClassVar[str] = "Genotype"
    _id_prefixes: ClassVar[List[str]] = ["ZFIN", "FB"]

    has_zygosity: Optional[Union[str, Zygosity]] = None


@dataclass(config=PydanticConfig)
class Haplotype(BiologicalEntity, GenomicEntity, PhysicalEssence):
    """
    A set of zero or more Alleles on a single instance of a Sequence[VMC]
    """

    # Class Variables
    _category: ClassVar[str] = "Haplotype"


@dataclass(config=PydanticConfig)
class SequenceVariant(NucleicAcidEntity):
    """
    An allele that varies in its sequence from what is considered the reference allele at that locus.
    """

    # Class Variables
    _category: ClassVar[str] = "SequenceVariant"
    _id_prefixes: ClassVar[List[str]] = [
        "CAID",
        "CLINVAR",
        "ClinVarVariant",
        "WIKIDATA",
        "DBSNP",
        "DBSNP",
        "MGI",
        "ZFIN",
        "FB",
        "WB",
        "WormBase",
    ]

    id: URIorCURIE = None
    has_gene: Optional[Union[List[Union[URIorCURIE, Gene]], Union[URIorCURIE, Gene]]] = field(
        default_factory=list
    )
    has_biological_sequence: Optional[Union[str, BiologicalSequence]] = None

    # Validators

    @validator('has_gene')
    def convert_has_gene_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(Gene, value)

    @validator('id')
    def validate_required_id(cls, value):
        check_value_is_not_none("id", value)
        check_curie_prefix(cls, value)
        return value


@dataclass(config=PydanticConfig)
class Snv(SequenceVariant):
    """
    SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist
    """

    # Class Variables
    _category: ClassVar[str] = "Snv"


@dataclass(config=PydanticConfig)
class ReagentTargetedGene(NucleicAcidEntity):
    """
    A gene altered in its expression level in the context of some experiment as a result of being targeted by
    gene-knockdown reagent(s) such as a morpholino or RNAi.
    """

    # Class Variables
    _category: ClassVar[str] = "ReagentTargetedGene"


@dataclass(config=PydanticConfig)
class ClinicalAttribute(Attribute):
    """
    Attributes relating to a clinical manifestation
    """

    # Class Variables
    _category: ClassVar[str] = "ClinicalAttribute"


@dataclass(config=PydanticConfig)
class ClinicalMeasurement(ClinicalAttribute):
    """
    A clinical measurement is a special kind of attribute which results from a laboratory observation from a subject
    individual or sample. Measurements can be connected to their subject by the 'has attribute' slot.
    """

    # Class Variables
    _category: ClassVar[str] = "ClinicalMeasurement"

    has_attribute_type: Union[str, OntologyClass] = None

    # Validators

    @validator('has_attribute_type')
    def validate_required_has_attribute_type(cls, value):
        check_value_is_not_none("has_attribute_type", value)
        return value


@dataclass(config=PydanticConfig)
class ClinicalModifier(ClinicalAttribute):
    """
    Used to characterize and specify the phenotypic abnormalities defined in the phenotypic abnormality sub-ontology,
    with respect to severity, laterality, and other aspects
    """

    # Class Variables
    _category: ClassVar[str] = "ClinicalModifier"


@dataclass(config=PydanticConfig)
class ClinicalCourse(ClinicalAttribute):
    """
    The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the
    affected individual
    """

    # Class Variables
    _category: ClassVar[str] = "ClinicalCourse"


@dataclass(config=PydanticConfig)
class Onset(ClinicalCourse):
    """
    The age group in which (disease) symptom manifestations appear
    """

    # Class Variables
    _category: ClassVar[str] = "Onset"


@dataclass(config=PydanticConfig)
class ClinicalEntity(NamedThing):
    """
    Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed
    under biological entities
    """

    # Class Variables
    _category: ClassVar[str] = "ClinicalEntity"


@dataclass(config=PydanticConfig)
class ClinicalTrial(ClinicalEntity):

    # Class Variables
    _category: ClassVar[str] = "ClinicalTrial"


@dataclass(config=PydanticConfig)
class ClinicalIntervention(ClinicalEntity):

    # Class Variables
    _category: ClassVar[str] = "ClinicalIntervention"


@dataclass(config=PydanticConfig)
class ClinicalFinding(PhenotypicFeature):
    """
    this category is currently considered broad enough to tag clinical lab measurements and other biological
    attributes taken as 'clinical traits' with some statistical score, for example, a p value in genetic associations.
    """

    # Class Variables
    _category: ClassVar[str] = "ClinicalFinding"
    _id_prefixes: ClassVar[List[str]] = ["LOINC", "NCIT", "EFO"]

    has_attribute: Optional[
        Union[List[Union[str, ClinicalAttribute]], Union[str, ClinicalAttribute]]
    ] = field(default_factory=list)

    # Validators

    @validator('has_attribute')
    def convert_has_attribute_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)


@dataclass(config=PydanticConfig)
class Hospitalization(ClinicalIntervention):

    # Class Variables
    _category: ClassVar[str] = "Hospitalization"


@dataclass(config=PydanticConfig)
class SocioeconomicAttribute(Attribute):
    """
    Attributes relating to a socioeconomic manifestation
    """

    # Class Variables
    _category: ClassVar[str] = "SocioeconomicAttribute"


@dataclass(config=PydanticConfig)
class Case(IndividualOrganism):
    """
    An individual (human) organism that has a patient role in some clinical context.
    """

    # Class Variables
    _category: ClassVar[str] = "Case"


@dataclass(config=PydanticConfig)
class Cohort(StudyPopulation):
    """
    A group of people banded together or treated as a group who share common characteristics. A cohort 'study' is a
    particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time.
    """

    # Class Variables
    _category: ClassVar[str] = "Cohort"


@dataclass(config=PydanticConfig)
class ExposureEvent:
    """
    A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more
    phenotypic features of that organism, potentially mediated by genes
    """

    timepoint: Optional[Union[str, TimeType]] = None


@dataclass(config=PydanticConfig)
class GenomicBackgroundExposure(
    BiologicalEntity, ExposureEvent, GeneGroupingMixin, PhysicalEssence, GenomicEntity
):
    """
    A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or
    other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing
    an outcome.
    """

    # Class Variables
    _category: ClassVar[str] = "GenomicBackgroundExposure"


@dataclass(config=PydanticConfig)
class PathologicalEntityMixin:
    """
    A pathological (abnormal) structure or process.
    """


@dataclass(config=PydanticConfig)
class PathologicalProcess(BiologicalProcess, PathologicalEntityMixin):
    """
    A biologic function or a process having an abnormal or deleterious effect at the subcellular, cellular,
    multicellular, or organismal level.
    """

    # Class Variables
    _category: ClassVar[str] = "PathologicalProcess"


@dataclass(config=PydanticConfig)
class PathologicalProcessExposure(PathologicalProcess, ExposureEvent):
    """
    A pathological process, when viewed as an exposure, representing an precondition, leading to or influencing an
    outcome, e.g. autoimmunity leading to disease.
    """

    # Class Variables
    _category: ClassVar[str] = "PathologicalProcessExposure"


@dataclass(config=PydanticConfig)
class PathologicalAnatomicalStructure(AnatomicalEntity, PathologicalEntityMixin):
    """
    An anatomical structure with the potential of have an abnormal or deleterious effect at the subcellular, cellular,
    multicellular, or organismal level.
    """

    # Class Variables
    _category: ClassVar[str] = "PathologicalAnatomicalStructure"


@dataclass(config=PydanticConfig)
class PathologicalAnatomicalExposure(PathologicalAnatomicalStructure, ExposureEvent):
    """
    An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or
    influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome.
    """

    # Class Variables
    _category: ClassVar[str] = "PathologicalAnatomicalExposure"


@dataclass(config=PydanticConfig)
class DiseaseOrPhenotypicFeatureExposure(
    DiseaseOrPhenotypicFeature, ExposureEvent, PathologicalEntityMixin
):
    """
    A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or
    influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin
    pigmentation predisposing an individual to skin cancer.
    """

    # Class Variables
    _category: ClassVar[str] = "DiseaseOrPhenotypicFeatureExposure"


@dataclass(config=PydanticConfig)
class ChemicalExposure(ChemicalEntity, ExposureEvent):
    """
    A chemical exposure is an intake of a particular chemical entity, other than a drug.
    """

    # Class Variables
    _category: ClassVar[str] = "ChemicalExposure"


@dataclass(config=PydanticConfig)
class ComplexChemicalExposure(ChemicalExposure):
    """
    A complex chemical exposure is an intake of a chemical mixture (e.g. gasoline), other than a drug.
    """

    # Class Variables
    _category: ClassVar[str] = "ComplexChemicalExposure"


@dataclass(config=PydanticConfig)
class DrugExposure(Drug, ExposureEvent):
    """
    A drug exposure is an intake of a particular drug.
    """

    # Class Variables
    _category: ClassVar[str] = "DrugExposure"


@dataclass(config=PydanticConfig)
class DrugToGeneInteractionExposure(DrugExposure, GeneGroupingMixin):
    """
    drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are
    known to constitute an 'exposure' to the organism, leading to or influencing an outcome.
    """

    # Class Variables
    _category: ClassVar[str] = "DrugToGeneInteractionExposure"


@dataclass(config=PydanticConfig)
class Treatment(NamedThing, ExposureEvent, ChemicalOrDrugOrTreatment):
    """
    A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices
    and/or procedures
    """

    # Class Variables
    _category: ClassVar[str] = "Treatment"

    has_drug: Optional[Union[List[Union[URIorCURIE, Drug]], Union[URIorCURIE, Drug]]] = field(
        default_factory=list
    )
    has_device: Optional[Union[List[Union[URIorCURIE, Device]], Union[URIorCURIE, Device]]] = field(
        default_factory=list
    )
    has_procedure: Optional[
        Union[List[Union[URIorCURIE, Procedure]], Union[URIorCURIE, Procedure]]
    ] = field(default_factory=list)

    # Validators

    @validator('has_drug')
    def convert_has_drug_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(Drug, value)

    @validator('has_device')
    def convert_has_device_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(Device, value)

    @validator('has_procedure')
    def convert_has_procedure_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(Procedure, value)


@dataclass(config=PydanticConfig)
class BioticExposure(OrganismTaxon, ExposureEvent):
    """
    An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses).
    """

    # Class Variables
    _category: ClassVar[str] = "BioticExposure"


@dataclass(config=PydanticConfig)
class GeographicExposure(GeographicLocation, ExposureEvent):
    """
    A geographic exposure is a factor relating to geographic proximity to some impactful entity.
    """

    # Class Variables
    _category: ClassVar[str] = "GeographicExposure"


@dataclass(config=PydanticConfig)
class EnvironmentalExposure(EnvironmentalProcess, ExposureEvent):
    """
    A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B),
    atmospheric (heat, cold, general pollution) and water-born contaminants.
    """

    # Class Variables
    _category: ClassVar[str] = "EnvironmentalExposure"


@dataclass(config=PydanticConfig)
class BehavioralExposure(Behavior, ExposureEvent):
    """
    A behavioral exposure is a factor relating to behavior impacting an individual.
    """

    # Class Variables
    _category: ClassVar[str] = "BehavioralExposure"


@dataclass(config=PydanticConfig)
class SocioeconomicExposure(Behavior, ExposureEvent):
    """
    A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g.
    poverty).
    """

    # Class Variables
    _category: ClassVar[str] = "SocioeconomicExposure"

    has_attribute: Union[
        List[Union[str, SocioeconomicAttribute]], Union[str, SocioeconomicAttribute]
    ] = None

    # Validators

    @validator('has_attribute')
    def validate_required_has_attribute(cls, value):
        check_value_is_not_none("has_attribute", value)
        convert_scalar_to_list_check_curies(cls, value)
        return value


@dataclass(config=PydanticConfig)
class Outcome:
    """
    An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of
    various categories of possible biological or non-biological (e.g. clinical) outcomes.
    """


@dataclass(config=PydanticConfig)
class PathologicalProcessOutcome(PathologicalProcess, Outcome):
    """
    An outcome resulting from an exposure event which is the manifestation of a pathological process.
    """

    # Class Variables
    _category: ClassVar[str] = "PathologicalProcessOutcome"


@dataclass(config=PydanticConfig)
class PathologicalAnatomicalOutcome(PathologicalAnatomicalStructure, Outcome):
    """
    An outcome resulting from an exposure event which is the manifestation of an abnormal anatomical structure.
    """

    # Class Variables
    _category: ClassVar[str] = "PathologicalAnatomicalOutcome"


@dataclass(config=PydanticConfig)
class DiseaseOrPhenotypicFeatureOutcome(DiseaseOrPhenotypicFeature, Outcome):
    """
    Physiological outcomes resulting from an exposure event which is the manifestation of a disease or other
    characteristic phenotype.
    """

    # Class Variables
    _category: ClassVar[str] = "DiseaseOrPhenotypicFeatureOutcome"


@dataclass(config=PydanticConfig)
class BehavioralOutcome(Behavior, Outcome):
    """
    An outcome resulting from an exposure event which is the manifestation of human behavior.
    """

    # Class Variables
    _category: ClassVar[str] = "BehavioralOutcome"


@dataclass(config=PydanticConfig)
class HospitalizationOutcome(Hospitalization, Outcome):
    """
    An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room
    visit) or chronic (inpatient) hospitalization.
    """

    # Class Variables
    _category: ClassVar[str] = "HospitalizationOutcome"


@dataclass(config=PydanticConfig)
class MortalityOutcome(Death, Outcome):
    """
    An outcome of death from resulting from an exposure event.
    """

    # Class Variables
    _category: ClassVar[str] = "MortalityOutcome"


@dataclass(config=PydanticConfig)
class EpidemiologicalOutcome(BiologicalEntity, Outcome):
    """
    An epidemiological outcome, such as societal disease burden, resulting from an exposure event.
    """

    # Class Variables
    _category: ClassVar[str] = "EpidemiologicalOutcome"


@dataclass(config=PydanticConfig)
class SocioeconomicOutcome(Behavior, Outcome):
    """
    An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure
    event
    """

    # Class Variables
    _category: ClassVar[str] = "SocioeconomicOutcome"


@dataclass(config=PydanticConfig)
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """

    # Class Variables
    _category: ClassVar[str] = "Association"

    subject: Union[URIorCURIE, NamedThing] = None
    predicate: Union[str, PredicateType] = None
    object: Union[URIorCURIE, NamedThing] = None
    relation: Union[str, URIorCURIE] = None
    negated: Optional[Union[bool, Bool]] = None
    qualifiers: Optional[Union[List[Union[str, OntologyClass]], Union[str, OntologyClass]]] = field(
        default_factory=list
    )
    publications: Optional[
        Union[List[Union[URIorCURIE, Publication]], Union[URIorCURIE, Publication]]
    ] = field(default_factory=list)
    type: Optional[Union[str, str]] = None
    category: Optional[Union[List[URIorCURIE], URIorCURIE]] = field(default_factory=list)

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(NamedThing, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(NamedThing, value)
        return value

    @validator('relation')
    def validate_required_relation(cls, value):
        check_value_is_not_none("relation", value)
        check_curie_prefix(cls, value)
        return value

    @validator('qualifiers')
    def convert_qualifiers_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('publications')
    def convert_publications_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(Publication, value)

    @validator('category')
    def convert_category_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)


@dataclass(config=PydanticConfig)
class ContributorAssociation(Association):
    """
    Any association between an entity (such as a publication) and various agents that contribute to its realisation
    """

    # Class Variables
    _category: ClassVar[str] = "ContributorAssociation"

    subject: Union[URIorCURIE, InformationContentEntity] = None
    predicate: Union[str, PredicateType] = None
    object: Union[URIorCURIE, Agent] = None
    qualifiers: Optional[Union[List[Union[str, OntologyClass]], Union[str, OntologyClass]]] = field(
        default_factory=list
    )

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(InformationContentEntity, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(Agent, value)
        return value

    @validator('qualifiers')
    def convert_qualifiers_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)


@dataclass(config=PydanticConfig)
class GenotypeToGenotypePartAssociation(Association):
    """
    Any association between one genotype and a genotypic entity that is a sub-component of it
    """

    # Class Variables
    _category: ClassVar[str] = "GenotypeToGenotypePartAssociation"

    predicate: Union[str, PredicateType] = None
    subject: Union[URIorCURIE, Genotype] = None
    object: Union[URIorCURIE, Genotype] = None

    # Validators

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Genotype, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(Genotype, value)
        return value


@dataclass(config=PydanticConfig)
class GenotypeToGeneAssociation(Association):
    """
    Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single
    one. There is no assumption of cardinality
    """

    # Class Variables
    _category: ClassVar[str] = "GenotypeToGeneAssociation"

    predicate: Union[str, PredicateType] = None
    subject: Union[URIorCURIE, Genotype] = None
    object: Union[URIorCURIE, Gene] = None

    # Validators

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Genotype, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(Gene, value)
        return value


@dataclass(config=PydanticConfig)
class GenotypeToVariantAssociation(Association):
    """
    Any association between a genotype and a sequence variant.
    """

    # Class Variables
    _category: ClassVar[str] = "GenotypeToVariantAssociation"

    predicate: Union[str, PredicateType] = None
    subject: Union[URIorCURIE, Genotype] = None
    object: Union[URIorCURIE, SequenceVariant] = None

    # Validators

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Genotype, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(SequenceVariant, value)
        return value


@dataclass(config=PydanticConfig)
class GeneToGeneAssociation(Association):
    """
    abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes
    homology and interaction.
    """

    subject: Union[str, GeneOrGeneProduct] = None
    object: Union[str, GeneOrGeneProduct] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        return value


@dataclass(config=PydanticConfig)
class GeneToGeneHomologyAssociation(GeneToGeneAssociation):
    """
    A homology association between two genes. May be orthology (in which case the species of subject and object should
    differ) or paralogy (in which case the species may be the same)
    """

    # Class Variables
    _category: ClassVar[str] = "GeneToGeneHomologyAssociation"

    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class GeneExpressionMixin:
    """
    Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the
    expression occurs.
    """

    quantifier_qualifier: Optional[Union[str, OntologyClass]] = None
    expression_site: Optional[Union[URIorCURIE, AnatomicalEntity]] = None
    stage_qualifier: Optional[Union[URIorCURIE, LifeStage]] = None
    phenotypic_state: Optional[Union[URIorCURIE, DiseaseOrPhenotypicFeature]] = None

    # Validators

    @validator('expression_site')
    def check_expression_site_prefix(cls, value):
        check_curie_prefix(AnatomicalEntity, value)
        return value

    @validator('stage_qualifier')
    def check_stage_qualifier_prefix(cls, value):
        check_curie_prefix(LifeStage, value)
        return value

    @validator('phenotypic_state')
    def check_phenotypic_state_prefix(cls, value):
        check_curie_prefix(DiseaseOrPhenotypicFeature, value)
        return value


@dataclass(config=PydanticConfig)
class GeneToGeneCoexpressionAssociation(GeneToGeneAssociation, GeneExpressionMixin):
    """
    Indicates that two genes are co-expressed, generally under the same conditions.
    """

    # Class Variables
    _category: ClassVar[str] = "GeneToGeneCoexpressionAssociation"

    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class PairwiseGeneToGeneInteraction(GeneToGeneAssociation):
    """
    An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between
    genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
    """

    # Class Variables
    _category: ClassVar[str] = "PairwiseGeneToGeneInteraction"

    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None

    # Validators

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('relation')
    def validate_required_relation(cls, value):
        check_value_is_not_none("relation", value)
        check_curie_prefix(cls, value)
        return value


@dataclass(config=PydanticConfig)
class PairwiseMolecularInteraction(PairwiseGeneToGeneInteraction):
    """
    An interaction at the molecular level between two physical entities
    """

    # Class Variables
    _category: ClassVar[str] = "PairwiseMolecularInteraction"

    subject: Union[URIorCURIE, MolecularEntity] = None
    id: URIorCURIE = None
    predicate: Union[str, PredicateType] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[URIorCURIE, MolecularEntity] = None
    interacting_molecules_category: Optional[Union[str, OntologyClass]] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(MolecularEntity, value)
        return value

    @validator('id')
    def validate_required_id(cls, value):
        check_value_is_not_none("id", value)
        check_curie_prefix(cls, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('relation')
    def validate_required_relation(cls, value):
        check_value_is_not_none("relation", value)
        check_curie_prefix(cls, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(MolecularEntity, value)
        return value


@dataclass(config=PydanticConfig)
class CellLineToEntityAssociationMixin:
    """
    An relationship between a cell line and another entity
    """

    subject: Union[URIorCURIE, CellLine] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(CellLine, value)
        return value


@dataclass(config=PydanticConfig)
class ChemicalEntityToEntityAssociationMixin:
    """
    An interaction between a chemical entity and another entity
    """

    subject: Union[URIorCURIE, ChemicalEntity] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(ChemicalEntity, value)
        return value


@dataclass(config=PydanticConfig)
class DrugToEntityAssociationMixin(ChemicalEntityToEntityAssociationMixin):
    """
    An interaction between a drug and another entity
    """

    subject: Union[URIorCURIE, Drug] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Drug, value)
        return value


@dataclass(config=PydanticConfig)
class ChemicalToEntityAssociationMixin(ChemicalEntityToEntityAssociationMixin):
    """
    An interaction between a chemical entity and another entity
    """

    subject: Union[URIorCURIE, ChemicalEntity] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(ChemicalEntity, value)
        return value


@dataclass(config=PydanticConfig)
class CaseToEntityAssociationMixin:
    """
    An abstract association for use where the case is the subject
    """

    subject: Union[URIorCURIE, Case] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Case, value)
        return value


@dataclass(config=PydanticConfig)
class ChemicalToChemicalAssociation(Association, ChemicalToEntityAssociationMixin):
    """
    A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal
    edges, e.g. one chemical converted to another.
    """

    # Class Variables
    _category: ClassVar[str] = "ChemicalToChemicalAssociation"

    object: Union[URIorCURIE, ChemicalEntity] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(ChemicalEntity, value)
        return value


@dataclass(config=PydanticConfig)
class ReactionToParticipantAssociation(ChemicalToChemicalAssociation):

    # Class Variables
    _category: ClassVar[str] = "ReactionToParticipantAssociation"

    subject: Union[URIorCURIE, MolecularEntity] = None
    stoichiometry: Optional[Union[int, int]] = None
    reaction_direction: Optional[Union[str, ReactionDirectionEnum]] = None
    reaction_side: Optional[Union[str, ReactionSideEnum]] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(MolecularEntity, value)
        return value


@dataclass(config=PydanticConfig)
class ReactionToCatalystAssociation(ReactionToParticipantAssociation):

    # Class Variables
    _category: ClassVar[str] = "ReactionToCatalystAssociation"

    object: Union[str, GeneOrGeneProduct] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        return value


@dataclass(config=PydanticConfig)
class ChemicalToChemicalDerivationAssociation(ChemicalToChemicalAssociation):
    """
    A causal relationship between two chemical entities, where the subject represents the upstream entity and the
    object represents the downstream. For any such association there is an implicit reaction:
    IF
    R has-input C1 AND
    R has-output C2 AND
    R enabled-by P AND
    R type Reaction
    THEN
    C1 derives-into C2 <<catalyst qualifier P>>
    """

    # Class Variables
    _category: ClassVar[str] = "ChemicalToChemicalDerivationAssociation"

    subject: Union[URIorCURIE, ChemicalEntity] = None
    object: Union[URIorCURIE, ChemicalEntity] = None
    predicate: Union[str, PredicateType] = None
    catalyst_qualifier: Optional[
        Union[List[Union[str, MacromolecularMachineMixin]], Union[str, MacromolecularMachineMixin]]
    ] = field(default_factory=list)

    # Validators

    @validator('catalyst_qualifier')
    def convert_catalyst_qualifier_to_list_check_curies(cls, value):
        return convert_scalar_to_list_check_curies(cls, value)

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(ChemicalEntity, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(ChemicalEntity, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class ChemicalToPathwayAssociation(Association, ChemicalToEntityAssociationMixin):
    """
    An interaction between a chemical entity and a biological process or pathway.
    """

    # Class Variables
    _category: ClassVar[str] = "ChemicalToPathwayAssociation"

    object: Union[URIorCURIE, Pathway] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(Pathway, value)
        return value


@dataclass(config=PydanticConfig)
class ChemicalToGeneAssociation(Association, ChemicalToEntityAssociationMixin):
    """
    An interaction between a chemical entity and a gene or gene product.
    """

    # Class Variables
    _category: ClassVar[str] = "ChemicalToGeneAssociation"

    object: Union[str, GeneOrGeneProduct] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        return value


@dataclass(config=PydanticConfig)
class DrugToGeneAssociation(Association, DrugToEntityAssociationMixin):
    """
    An interaction between a drug and a gene or gene product.
    """

    # Class Variables
    _category: ClassVar[str] = "DrugToGeneAssociation"

    object: Union[str, GeneOrGeneProduct] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        return value


@dataclass(config=PydanticConfig)
class MaterialSampleToEntityAssociationMixin:
    """
    An association between a material sample and something.
    """

    subject: Union[URIorCURIE, MaterialSample] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(MaterialSample, value)
        return value


@dataclass(config=PydanticConfig)
class MaterialSampleDerivationAssociation(Association):
    """
    An association between a material sample and the material entity from which it is derived.
    """

    # Class Variables
    _category: ClassVar[str] = "MaterialSampleDerivationAssociation"

    subject: Union[URIorCURIE, MaterialSample] = None
    object: Union[URIorCURIE, NamedThing] = None
    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(MaterialSample, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(NamedThing, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class DiseaseToEntityAssociationMixin:
    subject: Union[URIorCURIE, Disease] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Disease, value)
        return value


@dataclass(config=PydanticConfig)
class EntityToExposureEventAssociationMixin:
    """
    An association between some entity and an exposure event.
    """

    object: Union[str, ExposureEvent] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        return value


@dataclass(config=PydanticConfig)
class DiseaseToExposureEventAssociation(
    Association, DiseaseToEntityAssociationMixin, EntityToExposureEventAssociationMixin
):
    """
    An association between an exposure event and a disease.
    """

    # Class Variables
    _category: ClassVar[str] = "DiseaseToExposureEventAssociation"


@dataclass(config=PydanticConfig)
class ExposureEventToEntityAssociationMixin:
    """
    An association between some exposure event and some entity.
    """

    subject: Union[str, ExposureEvent] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value


@dataclass(config=PydanticConfig)
class EntityToOutcomeAssociationMixin:
    """
    An association between some entity and an outcome
    """

    object: Union[str, Outcome] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        return value


@dataclass(config=PydanticConfig)
class ExposureEventToOutcomeAssociation(
    Association, ExposureEventToEntityAssociationMixin, EntityToOutcomeAssociationMixin
):
    """
    An association between an exposure event and an outcome.
    """

    # Class Variables
    _category: ClassVar[str] = "ExposureEventToOutcomeAssociation"

    has_population_context: Optional[Union[URIorCURIE, PopulationOfIndividualOrganisms]] = None
    has_temporal_context: Optional[Union[str, TimeType]] = None

    # Validators

    @validator('has_population_context')
    def check_has_population_context_prefix(cls, value):
        check_curie_prefix(PopulationOfIndividualOrganisms, value)
        return value


@dataclass(config=PydanticConfig)
class FrequencyQualifierMixin:
    """
    Qualifier for frequency type associations
    """

    frequency_qualifier: Optional[Union[str, FrequencyValue]] = None


@dataclass(config=PydanticConfig)
class EntityToFeatureOrDiseaseQualifiersMixin(FrequencyQualifierMixin):
    """
    Qualifiers for entity to disease or phenotype associations.
    """

    severity_qualifier: Optional[Union[str, SeverityValue]] = None
    onset_qualifier: Optional[Union[str, Onset]] = None


@dataclass(config=PydanticConfig)
class EntityToPhenotypicFeatureAssociationMixin(EntityToFeatureOrDiseaseQualifiersMixin):
    object: Union[URIorCURIE, PhenotypicFeature] = None
    sex_qualifier: Optional[Union[str, BiologicalSex]] = None
    description: Optional[Union[str, NarrativeText]] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(PhenotypicFeature, value)
        return value


@dataclass(config=PydanticConfig)
class NamedThingToInformationContentEntityAssociation(Association):
    """
    association between a named thing and a information content entity where the specific context of the relationship
    between that named thing and the publication is unknown. For example, model organisms databases often capture the
    knowledge that a gene is found in a journal article, but not specifically the context in which that gene was
    documented in the article. In these cases, this association with the accompanying predicate 'mentions' could be
    used. Conversely, for more specific associations (like 'gene to disease association', the publication should be
    captured as an edge property).
    """

    # Class Variables
    _category: ClassVar[str] = "NamedThingToInformationContentEntityAssociation"

    subject: Union[URIorCURIE, NamedThing] = None
    object: Union[URIorCURIE, Publication] = None
    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(NamedThing, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(Publication, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class EntityToDiseaseAssociationMixin(EntityToFeatureOrDiseaseQualifiersMixin):
    """
    mixin class for any association whose object (target node) is a disease
    """

    object: Union[URIorCURIE, Disease] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(Disease, value)
        return value


@dataclass(config=PydanticConfig)
class DiseaseOrPhenotypicFeatureToEntityAssociationMixin:
    subject: Union[URIorCURIE, DiseaseOrPhenotypicFeature] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(DiseaseOrPhenotypicFeature, value)
        return value


@dataclass(config=PydanticConfig)
class DiseaseOrPhenotypicFeatureToLocationAssociation(
    Association, DiseaseOrPhenotypicFeatureToEntityAssociationMixin
):
    """
    An association between either a disease or a phenotypic feature and an anatomical entity, where the
    disease/feature manifests in that site.
    """

    # Class Variables
    _category: ClassVar[str] = "DiseaseOrPhenotypicFeatureToLocationAssociation"

    object: Union[URIorCURIE, AnatomicalEntity] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(AnatomicalEntity, value)
        return value


@dataclass(config=PydanticConfig)
class EntityToDiseaseOrPhenotypicFeatureAssociationMixin:
    object: Union[URIorCURIE, DiseaseOrPhenotypicFeature] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(DiseaseOrPhenotypicFeature, value)
        return value


@dataclass(config=PydanticConfig)
class CellLineToDiseaseOrPhenotypicFeatureAssociation(
    Association,
    CellLineToEntityAssociationMixin,
    EntityToDiseaseOrPhenotypicFeatureAssociationMixin,
):
    """
    An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an
    individual with that disease or phenotype.
    """

    # Class Variables
    _category: ClassVar[str] = "CellLineToDiseaseOrPhenotypicFeatureAssociation"

    subject: Union[URIorCURIE, DiseaseOrPhenotypicFeature] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(DiseaseOrPhenotypicFeature, value)
        return value


@dataclass(config=PydanticConfig)
class ChemicalToDiseaseOrPhenotypicFeatureAssociation(
    Association,
    ChemicalToEntityAssociationMixin,
    EntityToDiseaseOrPhenotypicFeatureAssociationMixin,
):
    """
    An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise
    to or exacerbates the phenotype.
    """

    # Class Variables
    _category: ClassVar[str] = "ChemicalToDiseaseOrPhenotypicFeatureAssociation"

    object: Union[URIorCURIE, DiseaseOrPhenotypicFeature] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(DiseaseOrPhenotypicFeature, value)
        return value


@dataclass(config=PydanticConfig)
class MaterialSampleToDiseaseOrPhenotypicFeatureAssociation(
    Association,
    MaterialSampleToEntityAssociationMixin,
    EntityToDiseaseOrPhenotypicFeatureAssociationMixin,
):
    """
    An association between a material sample and a disease or phenotype.
    """

    # Class Variables
    _category: ClassVar[str] = "MaterialSampleToDiseaseOrPhenotypicFeatureAssociation"


@dataclass(config=PydanticConfig)
class GenotypeToEntityAssociationMixin:
    subject: Union[URIorCURIE, Genotype] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Genotype, value)
        return value


@dataclass(config=PydanticConfig)
class GenotypeToPhenotypicFeatureAssociation(
    Association, EntityToPhenotypicFeatureAssociationMixin, GenotypeToEntityAssociationMixin
):
    """
    Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype,
    either in isolation or through environment
    """

    # Class Variables
    _category: ClassVar[str] = "GenotypeToPhenotypicFeatureAssociation"

    predicate: Union[str, PredicateType] = None
    subject: Union[URIorCURIE, Genotype] = None

    # Validators

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Genotype, value)
        return value


@dataclass(config=PydanticConfig)
class ExposureEventToPhenotypicFeatureAssociation(
    Association, EntityToPhenotypicFeatureAssociationMixin
):
    """
    Any association between an environment and a phenotypic feature, where being in the environment influences the
    phenotype.
    """

    # Class Variables
    _category: ClassVar[str] = "ExposureEventToPhenotypicFeatureAssociation"

    subject: Union[str, ExposureEvent] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value


@dataclass(config=PydanticConfig)
class DiseaseToPhenotypicFeatureAssociation(
    Association, EntityToPhenotypicFeatureAssociationMixin, DiseaseToEntityAssociationMixin
):
    """
    An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the
    disease in some way.
    """

    # Class Variables
    _category: ClassVar[str] = "DiseaseToPhenotypicFeatureAssociation"


@dataclass(config=PydanticConfig)
class CaseToPhenotypicFeatureAssociation(
    Association, EntityToPhenotypicFeatureAssociationMixin, CaseToEntityAssociationMixin
):
    """
    An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or
    has had the phenotype.
    """

    # Class Variables
    _category: ClassVar[str] = "CaseToPhenotypicFeatureAssociation"


@dataclass(config=PydanticConfig)
class BehaviorToBehavioralFeatureAssociation(
    Association, EntityToPhenotypicFeatureAssociationMixin
):
    """
    An association between an mixture behavior and a behavioral feature manifested by the individual exhibited or has
    exhibited the behavior.
    """

    # Class Variables
    _category: ClassVar[str] = "BehaviorToBehavioralFeatureAssociation"

    subject: Union[URIorCURIE, Behavior] = None
    object: Union[URIorCURIE, BehavioralFeature] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Behavior, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(BehavioralFeature, value)
        return value


@dataclass(config=PydanticConfig)
class GeneToEntityAssociationMixin:
    subject: Union[str, GeneOrGeneProduct] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value


@dataclass(config=PydanticConfig)
class VariantToEntityAssociationMixin:
    subject: Union[URIorCURIE, SequenceVariant] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(SequenceVariant, value)
        return value


@dataclass(config=PydanticConfig)
class GeneToPhenotypicFeatureAssociation(
    Association, EntityToPhenotypicFeatureAssociationMixin, GeneToEntityAssociationMixin
):

    # Class Variables
    _category: ClassVar[str] = "GeneToPhenotypicFeatureAssociation"

    subject: Union[str, GeneOrGeneProduct] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value


@dataclass(config=PydanticConfig)
class GeneToDiseaseAssociation(
    Association, EntityToDiseaseAssociationMixin, GeneToEntityAssociationMixin
):

    # Class Variables
    _category: ClassVar[str] = "GeneToDiseaseAssociation"

    subject: Union[str, GeneOrGeneProduct] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value


@dataclass(config=PydanticConfig)
class VariantToGeneAssociation(Association, VariantToEntityAssociationMixin):
    """
    An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in
    linkage disequilibrium)
    """

    # Class Variables
    _category: ClassVar[str] = "VariantToGeneAssociation"

    object: Union[URIorCURIE, Gene] = None
    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(Gene, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class VariantToGeneExpressionAssociation(VariantToGeneAssociation, GeneExpressionMixin):
    """
    An association between a variant and expression of a gene (i.e. e-QTL)
    """

    # Class Variables
    _category: ClassVar[str] = "VariantToGeneExpressionAssociation"

    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class VariantToPopulationAssociation(
    Association, VariantToEntityAssociationMixin, FrequencyQuantifier, FrequencyQualifierMixin
):
    """
    An association between a variant and a population, where the variant has particular frequency in the population
    """

    # Class Variables
    _category: ClassVar[str] = "VariantToPopulationAssociation"

    subject: Union[URIorCURIE, SequenceVariant] = None
    object: Union[URIorCURIE, PopulationOfIndividualOrganisms] = None
    has_quotient: Optional[Union[float, float]] = None
    has_count: Optional[Union[int, int]] = None
    has_total: Optional[Union[int, int]] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(SequenceVariant, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(PopulationOfIndividualOrganisms, value)
        return value


@dataclass(config=PydanticConfig)
class PopulationToPopulationAssociation(Association):
    """
    An association between a two populations
    """

    # Class Variables
    _category: ClassVar[str] = "PopulationToPopulationAssociation"

    subject: Union[URIorCURIE, PopulationOfIndividualOrganisms] = None
    object: Union[URIorCURIE, PopulationOfIndividualOrganisms] = None
    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(PopulationOfIndividualOrganisms, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(PopulationOfIndividualOrganisms, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class VariantToPhenotypicFeatureAssociation(
    Association, VariantToEntityAssociationMixin, EntityToPhenotypicFeatureAssociationMixin
):

    # Class Variables
    _category: ClassVar[str] = "VariantToPhenotypicFeatureAssociation"

    subject: Union[URIorCURIE, SequenceVariant] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(SequenceVariant, value)
        return value


@dataclass(config=PydanticConfig)
class VariantToDiseaseAssociation(
    Association, VariantToEntityAssociationMixin, EntityToDiseaseAssociationMixin
):

    # Class Variables
    _category: ClassVar[str] = "VariantToDiseaseAssociation"

    subject: Union[URIorCURIE, NamedThing] = None
    predicate: Union[str, PredicateType] = None
    object: Union[URIorCURIE, NamedThing] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(NamedThing, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(NamedThing, value)
        return value


@dataclass(config=PydanticConfig)
class GenotypeToDiseaseAssociation(
    Association, GenotypeToEntityAssociationMixin, EntityToDiseaseAssociationMixin
):

    # Class Variables
    _category: ClassVar[str] = "GenotypeToDiseaseAssociation"

    subject: Union[URIorCURIE, NamedThing] = None
    predicate: Union[str, PredicateType] = None
    object: Union[URIorCURIE, NamedThing] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(NamedThing, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(NamedThing, value)
        return value


@dataclass(config=PydanticConfig)
class ModelToDiseaseAssociationMixin:
    """
    This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in
    that it recapitulates some features of the disease in a way that is useful for studying the disease outside a
    patient carrying the disease
    """

    subject: Union[URIorCURIE, NamedThing] = None
    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(NamedThing, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class GeneAsAModelOfDiseaseAssociation(
    GeneToDiseaseAssociation, ModelToDiseaseAssociationMixin, EntityToDiseaseAssociationMixin
):

    # Class Variables
    _category: ClassVar[str] = "GeneAsAModelOfDiseaseAssociation"

    subject: Union[str, GeneOrGeneProduct] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value


@dataclass(config=PydanticConfig)
class VariantAsAModelOfDiseaseAssociation(
    VariantToDiseaseAssociation, ModelToDiseaseAssociationMixin, EntityToDiseaseAssociationMixin
):

    # Class Variables
    _category: ClassVar[str] = "VariantAsAModelOfDiseaseAssociation"

    subject: Union[URIorCURIE, SequenceVariant] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(SequenceVariant, value)
        return value


@dataclass(config=PydanticConfig)
class GenotypeAsAModelOfDiseaseAssociation(
    GenotypeToDiseaseAssociation, ModelToDiseaseAssociationMixin, EntityToDiseaseAssociationMixin
):

    # Class Variables
    _category: ClassVar[str] = "GenotypeAsAModelOfDiseaseAssociation"

    subject: Union[URIorCURIE, Genotype] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Genotype, value)
        return value


@dataclass(config=PydanticConfig)
class CellLineAsAModelOfDiseaseAssociation(
    CellLineToDiseaseOrPhenotypicFeatureAssociation,
    ModelToDiseaseAssociationMixin,
    EntityToDiseaseAssociationMixin,
):

    # Class Variables
    _category: ClassVar[str] = "CellLineAsAModelOfDiseaseAssociation"

    subject: Union[URIorCURIE, CellLine] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(CellLine, value)
        return value


@dataclass(config=PydanticConfig)
class OrganismalEntityAsAModelOfDiseaseAssociation(
    Association, ModelToDiseaseAssociationMixin, EntityToDiseaseAssociationMixin
):

    # Class Variables
    _category: ClassVar[str] = "OrganismalEntityAsAModelOfDiseaseAssociation"

    subject: Union[URIorCURIE, OrganismalEntity] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(OrganismalEntity, value)
        return value


@dataclass(config=PydanticConfig)
class OrganismToOrganismAssociation(Association):

    # Class Variables
    _category: ClassVar[str] = "OrganismToOrganismAssociation"

    subject: Union[URIorCURIE, IndividualOrganism] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[URIorCURIE, IndividualOrganism] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(IndividualOrganism, value)
        return value

    @validator('relation')
    def validate_required_relation(cls, value):
        check_value_is_not_none("relation", value)
        check_curie_prefix(cls, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(IndividualOrganism, value)
        return value


@dataclass(config=PydanticConfig)
class TaxonToTaxonAssociation(Association):

    # Class Variables
    _category: ClassVar[str] = "TaxonToTaxonAssociation"

    subject: Union[URIorCURIE, OrganismTaxon] = None
    relation: Union[str, URIorCURIE] = None
    object: Union[URIorCURIE, OrganismTaxon] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(OrganismTaxon, value)
        return value

    @validator('relation')
    def validate_required_relation(cls, value):
        check_value_is_not_none("relation", value)
        check_curie_prefix(cls, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(OrganismTaxon, value)
        return value


@dataclass(config=PydanticConfig)
class GeneHasVariantThatContributesToDiseaseAssociation(GeneToDiseaseAssociation):

    # Class Variables
    _category: ClassVar[str] = "GeneHasVariantThatContributesToDiseaseAssociation"

    subject: Union[str, GeneOrGeneProduct] = None
    sequence_variant_qualifier: Optional[Union[URIorCURIE, SequenceVariant]] = None

    # Validators

    @validator('sequence_variant_qualifier')
    def check_sequence_variant_qualifier_prefix(cls, value):
        check_curie_prefix(SequenceVariant, value)
        return value

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value


@dataclass(config=PydanticConfig)
class GeneToExpressionSiteAssociation(Association):
    """
    An association between a gene and an expression site, possibly qualified by stage/timing info.
    """

    # Class Variables
    _category: ClassVar[str] = "GeneToExpressionSiteAssociation"

    subject: Union[str, GeneOrGeneProduct] = None
    object: Union[URIorCURIE, AnatomicalEntity] = None
    predicate: Union[str, PredicateType] = None
    stage_qualifier: Optional[Union[URIorCURIE, LifeStage]] = None
    quantifier_qualifier: Optional[Union[str, OntologyClass]] = None

    # Validators

    @validator('stage_qualifier')
    def check_stage_qualifier_prefix(cls, value):
        check_curie_prefix(LifeStage, value)
        return value

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(AnatomicalEntity, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class SequenceVariantModulatesTreatmentAssociation(Association):
    """
    An association between a sequence variant and a treatment or health intervention. The treatment object itself
    encompasses both the disease and the drug used.
    """

    subject: Union[URIorCURIE, SequenceVariant] = None
    object: Union[URIorCURIE, Treatment] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(SequenceVariant, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(Treatment, value)
        return value


@dataclass(config=PydanticConfig)
class FunctionalAssociation(Association):
    """
    An association between a macromolecular machine mixin (gene, gene product or complex of gene products) and either
    a molecular activity, a biological process or a cellular location in which a function is executed.
    """

    # Class Variables
    _category: ClassVar[str] = "FunctionalAssociation"

    subject: Union[str, MacromolecularMachineMixin] = None
    object: Union[str, GeneOntologyClass] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        return value


@dataclass(config=PydanticConfig)
class MacromolecularMachineToEntityAssociationMixin:
    """
    an association which has a macromolecular machine mixin as a subject
    """

    subject: Union[URIorCURIE, NamedThing] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(NamedThing, value)
        return value


@dataclass(config=PydanticConfig)
class MacromolecularMachineToMolecularActivityAssociation(
    FunctionalAssociation, MacromolecularMachineToEntityAssociationMixin
):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity
    (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to
    its execution.
    """

    # Class Variables
    _category: ClassVar[str] = "MacromolecularMachineToMolecularActivityAssociation"

    object: Union[URIorCURIE, MolecularActivity] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(MolecularActivity, value)
        return value


@dataclass(config=PydanticConfig)
class MacromolecularMachineToBiologicalProcessAssociation(
    FunctionalAssociation, MacromolecularMachineToEntityAssociationMixin
):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a biological process
    or pathway (as represented in the GO biological process branch), where the entity carries out some part of the
    process, regulates it, or acts upstream of it.
    """

    # Class Variables
    _category: ClassVar[str] = "MacromolecularMachineToBiologicalProcessAssociation"

    object: Union[URIorCURIE, BiologicalProcess] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(BiologicalProcess, value)
        return value


@dataclass(config=PydanticConfig)
class MacromolecularMachineToCellularComponentAssociation(
    FunctionalAssociation, MacromolecularMachineToEntityAssociationMixin
):
    """
    A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component
    (as represented in the GO cellular component branch), where the entity carries out its function in the cellular
    component.
    """

    # Class Variables
    _category: ClassVar[str] = "MacromolecularMachineToCellularComponentAssociation"

    object: Union[URIorCURIE, CellularComponent] = None

    # Validators

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(CellularComponent, value)
        return value


@dataclass(config=PydanticConfig)
class GeneToGoTermAssociation(FunctionalAssociation):

    # Class Variables
    _category: ClassVar[str] = "GeneToGoTermAssociation"

    subject: Union[URIorCURIE, Gene] = None
    object: Union[str, GeneOntologyClass] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Gene, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        return value


@dataclass(config=PydanticConfig)
class SequenceAssociation(Association):
    """
    An association between a sequence feature and a nucleic acid entity it is localized to.
    """

    # Class Variables
    _category: ClassVar[str] = "SequenceAssociation"


@dataclass(config=PydanticConfig)
class GenomicSequenceLocalization(SequenceAssociation):
    """
    A relationship between a sequence feature and a nucleic acid entity it is localized to. The reference entity may
    be a chromosome, chromosome region or information entity such as a contig.
    """

    # Class Variables
    _category: ClassVar[str] = "GenomicSequenceLocalization"

    subject: Union[URIorCURIE, NucleicAcidEntity] = None
    object: Union[URIorCURIE, NucleicAcidEntity] = None
    predicate: Union[str, PredicateType] = None
    start_interbase_coordinate: Optional[Union[int, int]] = None
    end_interbase_coordinate: Optional[Union[int, int]] = None
    genome_build: Optional[Union[str, StrandEnum]] = None
    strand: Optional[Union[str, StrandEnum]] = None
    phase: Optional[Union[str, PhaseEnum]] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(NucleicAcidEntity, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(NucleicAcidEntity, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class SequenceFeatureRelationship(Association):
    """
    For example, a particular exon is part of a particular transcript or gene
    """

    # Class Variables
    _category: ClassVar[str] = "SequenceFeatureRelationship"

    subject: Union[URIorCURIE, NucleicAcidEntity] = None
    object: Union[URIorCURIE, NucleicAcidEntity] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(NucleicAcidEntity, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(NucleicAcidEntity, value)
        return value


@dataclass(config=PydanticConfig)
class TranscriptToGeneRelationship(SequenceFeatureRelationship):
    """
    A gene is a collection of transcripts
    """

    # Class Variables
    _category: ClassVar[str] = "TranscriptToGeneRelationship"

    subject: Union[URIorCURIE, Transcript] = None
    object: Union[URIorCURIE, Gene] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Transcript, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(Gene, value)
        return value


@dataclass(config=PydanticConfig)
class GeneToGeneProductRelationship(SequenceFeatureRelationship):
    """
    A gene is transcribed and potentially translated to a gene product
    """

    # Class Variables
    _category: ClassVar[str] = "GeneToGeneProductRelationship"

    subject: Union[URIorCURIE, Gene] = None
    object: Union[str, GeneProductMixin] = None
    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Gene, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class ExonToTranscriptRelationship(SequenceFeatureRelationship):
    """
    A transcript is formed from multiple exons
    """

    # Class Variables
    _category: ClassVar[str] = "ExonToTranscriptRelationship"

    subject: Union[URIorCURIE, Exon] = None
    object: Union[URIorCURIE, Transcript] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(Exon, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(Transcript, value)
        return value


@dataclass(config=PydanticConfig)
class GeneRegulatoryRelationship(Association):
    """
    A regulatory relationship between two genes
    """

    # Class Variables
    _category: ClassVar[str] = "GeneRegulatoryRelationship"

    predicate: Union[str, PredicateType] = None
    subject: Union[str, GeneOrGeneProduct] = None
    object: Union[str, GeneOrGeneProduct] = None

    # Validators

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        return value


@dataclass(config=PydanticConfig)
class AnatomicalEntityToAnatomicalEntityAssociation(Association):
    subject: Union[URIorCURIE, AnatomicalEntity] = None
    object: Union[URIorCURIE, AnatomicalEntity] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(AnatomicalEntity, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(AnatomicalEntity, value)
        return value


@dataclass(config=PydanticConfig)
class AnatomicalEntityToAnatomicalEntityPartOfAssociation(
    AnatomicalEntityToAnatomicalEntityAssociation
):
    """
    A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are
    related by parthood. This includes relationships between cellular components and cells, between cells and tissues,
    tissues and whole organisms
    """

    # Class Variables
    _category: ClassVar[str] = "AnatomicalEntityToAnatomicalEntityPartOfAssociation"

    subject: Union[URIorCURIE, AnatomicalEntity] = None
    object: Union[URIorCURIE, AnatomicalEntity] = None
    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(AnatomicalEntity, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(AnatomicalEntity, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class AnatomicalEntityToAnatomicalEntityOntogenicAssociation(
    AnatomicalEntityToAnatomicalEntityAssociation
):
    """
    A relationship between two anatomical entities where the relationship is ontogenic, i.e. the two entities are
    related by development. A number of different relationship types can be used to specify the precise nature of the
    relationship.
    """

    # Class Variables
    _category: ClassVar[str] = "AnatomicalEntityToAnatomicalEntityOntogenicAssociation"

    subject: Union[URIorCURIE, AnatomicalEntity] = None
    object: Union[URIorCURIE, AnatomicalEntity] = None
    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(AnatomicalEntity, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(AnatomicalEntity, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class OrganismTaxonToEntityAssociation:
    """
    An association between an organism taxon and another entity
    """

    subject: Union[URIorCURIE, OrganismTaxon] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(OrganismTaxon, value)
        return value


@dataclass(config=PydanticConfig)
class OrganismTaxonToOrganismTaxonAssociation(Association, OrganismTaxonToEntityAssociation):
    """
    A relationship between two organism taxon nodes
    """

    subject: Union[URIorCURIE, OrganismTaxon] = None
    object: Union[URIorCURIE, OrganismTaxon] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(OrganismTaxon, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(OrganismTaxon, value)
        return value


@dataclass(config=PydanticConfig)
class OrganismTaxonToOrganismTaxonSpecialization(OrganismTaxonToOrganismTaxonAssociation):
    """
    A child-parent relationship between two taxa. For example: Homo sapiens subclass_of Homo
    """

    # Class Variables
    _category: ClassVar[str] = "OrganismTaxonToOrganismTaxonSpecialization"

    subject: Union[URIorCURIE, OrganismTaxon] = None
    object: Union[URIorCURIE, OrganismTaxon] = None
    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(OrganismTaxon, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(OrganismTaxon, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class OrganismTaxonToOrganismTaxonInteraction(OrganismTaxonToOrganismTaxonAssociation):
    """
    An interaction relationship between two taxa. This may be a symbiotic relationship (encompassing mutualism and
    parasitism), or it may be non-symbiotic. Example: plague transmitted_by flea; cattle domesticated_by Homo sapiens;
    plague infects Homo sapiens
    """

    # Class Variables
    _category: ClassVar[str] = "OrganismTaxonToOrganismTaxonInteraction"

    subject: Union[URIorCURIE, OrganismTaxon] = None
    object: Union[URIorCURIE, OrganismTaxon] = None
    predicate: Union[str, PredicateType] = None
    associated_environmental_context: Optional[Union[str, str]] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(OrganismTaxon, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(OrganismTaxon, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value


@dataclass(config=PydanticConfig)
class OrganismTaxonToEnvironmentAssociation(Association, OrganismTaxonToEntityAssociation):
    subject: Union[URIorCURIE, OrganismTaxon] = None
    object: Union[URIorCURIE, NamedThing] = None
    predicate: Union[str, PredicateType] = None

    # Validators

    @validator('subject')
    def validate_required_subject(cls, value):
        check_value_is_not_none("subject", value)
        check_curie_prefix(OrganismTaxon, value)
        return value

    @validator('object')
    def validate_required_object(cls, value):
        check_value_is_not_none("object", value)
        check_curie_prefix(NamedThing, value)
        return value

    @validator('predicate')
    def validate_required_predicate(cls, value):
        check_value_is_not_none("predicate", value)
        return value
