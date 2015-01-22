# First pass at changing to new data label scheme 
# After this will have to hand split new lines and change strange
# labels 
# -- EMonson 24 Nov 2008

f = open('LongVersion_noCTabs_rev4.html','r')
whole4 = f.read()

# e.g. All ${s_0} add one and put in data -> ${s_data001}
for ii in range(146):
	for ss in ['s', 'c']:
		oldStr = '${' + ss + '_' + str(ii) + '}'
		newStr = '${' + ss + '_data' + str(ii+1).zfill(3) + '}'
		whole4 = whole4.replace(oldStr, newStr)
	
fout = open('LongVer_newLabelsPrelim_rev5.html','w')
fout.write(whole4)
fout.close()
f.close()

# Data labels version

f = open('LongVersion_dataVals_rev4.html','r')
whole4 = f.read()

# e.g. All ${s_0} add one and put in data -> ${s_data001}
for ii in range(146):
	for ss in ['s', 'c', 'lo', 'sh']:
		oldStr = '${' + ss + '_' + str(ii) + '}'
		newStr = '${' + ss + '_data' + str(ii+1).zfill(3) + '}'
		whole4 = whole4.replace(oldStr, newStr)
	
fout = open('LongVer_newLabelsDataPrelim_rev5.html','w')
fout.write(whole4)
fout.close()
f.close()