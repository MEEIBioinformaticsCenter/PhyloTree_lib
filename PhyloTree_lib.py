#!/usr/bin/env python

import xlrd
import copy

#### CLASSES 

class Node(object):
	haplogroup = ""
	level = -1
	parent = ""
	childs = []
	is_haplogroup = True
	snps = ""
	publications = ""

	# The class "constructor" - It's actually an initializer 
	def __init__(self, haplogroup, level, snps, publications, parent="", childs=[]):
		self.haplogroup = haplogroup
		self.level = level
		self.parent = parent
		self.snps = snps
		self.publications = publications
		self.childs = childs
	def __repr__(self):
		return "Node()"
	def __str__(self):
		return self.haplogroup+" (Level: "+str(self.level)+", Snps: "+self.snps+", Publications: "+self.publications+", Parent: "+self.parent+", # of Childs: "+str(len(self.childs))+")"

	def __del__(self):
		self.haplogroup = ""
		self.level = -1
		self.parent = ""
		del self.childs[:]
		self.snps = ""
		self.publications = ""



class PhyloTree:
	haplogroup_dic={}
	__DEFAULT_CHANGE_TABLE={'A':'G','G':'A','C':'T','T':'C'}

	def __init__(self, excel_file):
		self.haplogroup_dic=self.__get_dic_objects_from_excel(excel_file)

	def __remove_leters(self, snp):
		to_return=""
		letters=[]
		#admirations=0
		numbers=["0","1","2","3","4","5","6","7","8","9"]
		for letter in snp:
			if letter in numbers:
				to_return+=letter
			elif letter == " ":
				if to_return[-1]!="-":
					to_return+="-"
					#if admirations==2:
					#	to_return="@"+to_return
					#admirations=0
			#elif letter == "!":
			#	admirations+=1
			else:
				letters.append(letter)

		#if admirations==2:
		#	print("--------")
		#	print("@"+to_return)
		#	print("--------")
		#	return("@"+to_return)
			
		#elif "@" not in to_return:
		return(to_return)
			
		#else:
		#	print("I DON'T KNOW WHAT TO DO!")
		#	print(snp)
		#	print(to_return)
		#	exit(1) 
			


	
	# Excel file from PhyloTree as input and the dictionary of objects as output
	def __get_dic_objects_from_excel(self,excel_file):
		book = xlrd.open_workbook(excel_file)
		sheet = book.sheet_by_index(0)
	
		count_columns=len(sheet.row_values(0))
		count_rows=len(sheet.col_values(0))
		
		
		nodes={}
		last_Node_name=""
		
		row_num=0

		while row_num<count_rows:
			if sheet.cell(row_num,0).value!='':
				break
			row_num+=1

		while row_num<count_rows:
			col_num=0
			while col_num<count_columns:
				if sheet.cell(row_num,col_num).value!='':
					name=sheet.cell(row_num,col_num).value.strip()
					snps=sheet.cell(row_num,col_num+1).value.strip()
					level=col_num+1
					publications=sheet.cell(row_num,count_columns-2).value+" "+sheet.cell(row_num,count_columns-1).value.strip()
					aux_node=Node(name,level,snps,publications)
					
					if aux_node.snps=='':
						aux_node.level-=1	
	
					if last_Node_name!="":
						if nodes[last_Node_name].level<aux_node.level: #Previous is closer to the root, so is the father
							if aux_node.snps=='':
								aux_node.snps=aux_node.haplogroup
								aux_node.haplogroup=last_Node_name+"-"+self.__remove_leters(aux_node.snps.strip())
							
							aux_node.parent=last_Node_name
							nodes[last_Node_name].childs.append(aux_node.haplogroup)
						elif nodes[last_Node_name].level==aux_node.level: #Same level than previous, so brothers
							if aux_node.snps=='':
								aux_node.snps=aux_node.haplogroup
								aux_node.haplogroup=nodes[last_Node_name].parent+"-"+self.__remove_leters(aux_node.snps.strip())
							aux_node.parent=nodes[last_Node_name].parent
							nodes[nodes[last_Node_name].parent].childs.append(aux_node.haplogroup)
						else: #current closer to the root, so find a brother
							aux=last_Node_name
							while nodes[aux].level>aux_node.level:
								aux=nodes[aux].parent
							if aux_node.snps=='':
								aux_node.snps=aux_node.haplogroup
								aux_node.haplogroup=nodes[aux].parent+"-"+self.__remove_leters(aux_node.snps.strip())
							aux_node.parent=nodes[aux].parent
							nodes[nodes[aux].parent].childs.append(aux_node.haplogroup)
					else:
						if aux_node.snps=='':
							#aux_node.snps=aux_node.haplogroup
							aux_node.level-=1 ## Adjusting the leven when is not a haplogroup
						
					last_Node_name=aux_node.haplogroup
					nodes[aux_node.haplogroup]=copy.deepcopy(aux_node)
					del aux_node
					break #after finding the first cell with info, I don't continue on the row
				
				col_num+=1
			row_num+=1
	
		return nodes


	# Input is an array of haplogroups, returns the closest to the root, if same level, father of the first one
	def get_highest_leaf(self,array_haplogroups):
		array_haplogroups=list(set(array_haplogroups))

		if len(array_haplogroups)==1:
			return(array_haplogroups[0])
		
		dic_levels={}
		for haplogroup in array_haplogroups:
			try:
				dic_levels[self.haplogroup_dic[haplogroup].level].append(haplogroup)
			except KeyError:
				dic_levels[self.haplogroup_dic[haplogroup].level]=[haplogroup]
				pass
		if len(dic_levels[min(dic_levels.keys())])==1:

			return(dic_levels[min(dic_levels.keys())][0])
		else:
			return(str(self.haplogroup_dic[dic_levels[min(dic_levels.keys())][0]].parent))
			
	
	# Input is a haplogroup and it returns an array of haplogroups that are closer to the root
	def get_all_haplogroups_leaf_to_root(self,target_haplogroup):
		
		dic_nodes=self.haplogroup_dic
		list_root_haplogroups=[]
		cur_hap=target_haplogroup
		while cur_hap!='':
			if dic_nodes[cur_hap].is_haplogroup:
				list_root_haplogroups.append(dic_nodes[cur_hap].haplogroup)
			cur_hap=dic_nodes[cur_hap].parent
		return list(reversed(list_root_haplogroups))
			
	
	def get_all_haplogroups_root_to_leaf(self,target_haplogroup,depth=-1):
		
		dic_nodes=self.haplogroup_dic
		to_return=[]
		if len(dic_nodes[target_haplogroup].childs)==0 or depth==0: ###Base case
			to_return.append(target_haplogroup)
		else:
			to_return.append(target_haplogroup)
			for child in dic_nodes[target_haplogroup].childs:
				to_return+=self.get_all_haplogroups_root_to_leaf(child,depth-1)
		return(to_return)
		
	def get_snps_haplogroup(self,target_haplogroup):
		to_return=[]
		for haplo in self.get_all_haplogroups_leaf_to_root(target_haplogroup):
				for snp in self.haplogroup_dic[haplo].snps.split(" "):
					if snp!='':
						to_return.append(snp)
		return(to_return)
	
	def get_root(self):
		dic_nodes=self.haplogroup_dic
		for haplogroup in dic_nodes.keys():
			if dic_nodes[haplogroup].parent=='':
				break
		return(haplogroup)
	
	





