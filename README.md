#ZINCPY - A Python API for the ZINC database. 

The ZINC database (http://zinc.docking.org/) is a fantastic resource for chemists, containing over 35 million purchasable molecules, made by combining many popular (and niche!) chemical catalogs.

This is a python module which allows you to succinctly query the ZINC database, allowing you to specify:

* The SMILES string of the target
* The catalog to query
* The range of molecular weights
* The number of rotatable bonds

and to filter by:

* Molecular similarity
* Molecular indentity
* Substructure


More of the filters exposed in ZINC querying will be added in coming versions


##Example

1: Search for targets with a specific smiles as a substructure 

```python

import zincpy

zp = zincpy.ZincParser()
zp.set_search_parameters({'structure.smiles':'c1ccccc1', 'structure.similarity':'substructure'})
info = zp.search()
print info
```


2: Search for targets which have a structural similarity to either benzene or pyrrole of at least 0.9 

```python

import zincpy

zp = zincpy.ZincParser()
zp.set_search_parameters({'structure.similarity':0.9})
info = zp.search_smiles_list(['c1ccccc1', 'c1cc[nH]c1'])
print info
```


##Contact

This code is maintained by Ed Pyzer-Knapp, who can be reached at epyzerknapp(antispam)fas.harvard.edu