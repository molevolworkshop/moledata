datafilename = "canids.nex"
treefilename = "canids_genetrees.tre"
locuslist = [
	"APOBS1",
	"APOBS2",
	"BDNF",
	"BRCA1S1",
	"BRCA1S2",
	"Ch14",
	"Ch21",
	"Ch24",
	"CHST12",
	"CMKOR1",
	"FGFR3",
	"GHRex09",
	"RAG1",
	"TMEM20",
	"VANGL2",
	"VWF"
	]

print("rm '%s';\n" % treefilename)		# start fresh each time script is run

print("#NEXUS\n")
print("begin paup;")
print("\texecute %s;\n" % datafilename)
for locusname in locuslist:
	print("\tinclude %s/only;" % locusname)
	print("\traxml exec=raxmlHPC;")
	print("\tsavetree file=canids_genetrees.tre format=newick append;")
	print()

print("\tinclude all;")
print("end;")
