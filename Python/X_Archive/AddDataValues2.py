# After changing data labels to include dataXXX and manually splitting off 200s, etc.
# Running this to create a new Data Values version rather than trying to separately modify
# old version

f = open('LongVer_newLabelsPrelim3_rev5.html','r')
whole = f.read()
whole_fsp = whole.split('</font>')

for ii,xx in enumerate(whole_fsp[1:-1]):
	# Make sure there is a space at the end of the sentence
	if xx[-1] != ' ':
		whole_fsp[ii+1] += ' '
		
	# Get the data label from each line
	dlStart = xx.find('${s_')
	dlEnd = xx.find('} color=${')
	dLabel = xx[dlStart+4:dlEnd]
	
	# Add data values piece & re-add </font> since removed with .split()
	whole_fsp[ii+1] += '(${lo_' + dLabel + '}, ${sh_' + dLabel + '}) </font>'
	
whole2 = ''.join(whole_fsp)
fout = open('LongVer_newLabelsDataPrelim3_rev5.html','w')
fout.write(whole2)
fout.close()
f.close()