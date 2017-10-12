#!/usr/bin/env python
import PhyloTree_lib 

def main():

	print("PhyloTree V16:")
	tree_16=PhyloTree_lib.PhyloTree("resources/PhyloTree_16.xlsx")
	print("The root of the tree:")
	print(tree_16.get_root())
	print("")
	print("From the Root to H1a1:")
	print(tree_16.get_all_haplogroups_leaf_to_root("H1a1"))
	print("")
	print("From H1a1 to the leaves:")
	print(tree_16.get_all_haplogroups_root_to_leaf("H1a1"))
	print("")
	print("From H1a1 to the leaves, only 1 level:")
	print(tree_16.get_all_haplogroups_root_to_leaf("H1a1",1))
	print("")
	print("SNPs for haplogroup H1a1:")
	print tree_16.get_snps_haplogroup("H1a1")
	print("")

	print("PhyloTree V17:")
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
	print("")
	
	
	#dic_nodes=PhyloTree_lib.get_dic_objects_from_excel("PhyloTree_17.xlsx")

	#print(dir(PhyloTree_lib))
	#print(PhyloTree_lib.get_root(dic_nodes))


##############

if __name__ == "__main__":
    main()	

