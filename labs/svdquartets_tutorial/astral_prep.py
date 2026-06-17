datafilename = "anomaly_zone.nex"
treefilename = "az_tree.tre"
nloci = 10000

print("#NEXUS\n")
print("begin paup;")
print("\texecute %s;" % datafilename)
print("end;", end="")

print("begin sets;")
print("\tcharpartition genes = "),
for i in range(nloci):
	print("locus_%d:%d-%d" % (i+1, i*500 + 1, i*500+500), end="")
	if i < nloci - 1:
		print(",", end="")
	else:
		print(";")
print("end;\n")

print("begin paup;")
print("\t!rm -f %s;" % treefilename)
for i in range(nloci):
	print()
	print("\tinclude genes.locus_%d/only;" % (i+1))
	print("\traxml exec=raxmlHPC;")
	print("\tsavetree file=az_tree.tre format=newick append;")

print("\tinclude all;")
print("end;")
