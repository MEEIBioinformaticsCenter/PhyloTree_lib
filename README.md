# PhyloTree_lib
Phython library to manipulate excel files from [PhyloTree.org](http://www.phylotree.org/)

## How to use it
This library allows you to open an excel file containning the whole PhyloTree and ask questions:

```python
import PhyloTree_lib

tree_17=PhyloTree_lib.PhyloTree("resources/PhyloTree_17.xlsx")
print("The root of the tree:")
print(tree_17.get_root())
print("")
print("From the Root to H1a1:")
print(tree_17.get_all_haplogroups_leaf_to_root("H1a1"))
print("")
print("From H1a1 to the leaves:")
print(tree_17.get_all_haplogroups_root_to_leaf("H1a1"))
print("")
print("From H1a1 to the leaves, only 1 level:")
print(tree_17.get_all_haplogroups_root_to_leaf("H1a1",1))
print("")
print("SNPs for haplogroup H1a1:")
print tree_17.get_snps_haplogroup("H1a1")
```
Output:
```
The root of the tree:
mt-MRCA (RSRS)

From the Root to H1a1:
[u'mt-MRCA (RSRS)', u"L1'2'3'4'5'6", u"L2'3'4'5'6", u"L2'3'4'6", u"L3'4'6", u"L3'4", u'L3', u'N', u'R', u'R0', u'HV', u'HV1', u'HV5', u'H', u'H1', u'H1a', u'H1a1']

From H1a1 to the leaves:
['H1a1', u'H1a1a', u'H1a1a1', u'H1a1b', u'H1a1c']

From H1a1 to the leaves, only 1 level:
['H1a1', u'H1a1a', u'H1a1b', u'H1a1c']

SNPs for haplogroup H1a1:
[u'C146T', u'C182T', u'T4312C', u'T10664C', u'C10915T', u'A11914G', u'G13276A', u'G16230A', u'C152T', u'A2758G', u'C2885T', u'G7146A', u'T8468C', u'C195T', u'A247G', u'A825t', u'T8655C', u'A10688G', u'C10810T', u'G13105A', u'T13506C', u'G15301A', u'A16129G', u'T16187C', u'C16189T', u'G4104A', u'A7521G', u'T182C!', u'T3594C', u'T7256C', u'T13650C', u'T16278C', u'A769G', u'A1018G', u'C16311T', u'G8701A', u'C9540T', u'G10398A', u'C10873T', u'A15301G!', u'T12705C', u'T16223C', u'G73A', u'A11719G', u'T14766C', u'A8014t', u'C16067T', u'A13105G!', u'G2706A', u'T7028C', u'G3010A', u'A73G!', u'A16162G', u'T6365C', u'T16209C']
```

## How to get the excel file
In the resources folder there are two excel files corresponging to PhyloTree V16 and V17. To generate one of these files, just download the PhyloTree in html format from [http://www.phylotree.org/builds/mtDNA_tree_Build_17.zip](http://www.phylotree.org/builds/mtDNA_tree_Build_17.zip), and open it with excel, then just save it with xlsx format.

