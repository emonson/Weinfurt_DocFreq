# After changing data labels to include dataXXX and manually splitting off 200s, etc.
# Running this to create a new Data Values version rather than trying to separately modify
# old version

f = open('LongVer_newLabelsPrelim3_rev5.html','r')
whole = f.read()
f.close()
whole_fsp = whole.split('</font>')

labelList = []
for ii,xx in enumerate(whole_fsp[1:-1]):

	# Get the data label from each line
	dlStart = xx.find('${s_')
	dlEnd = xx.find('} color=${')
	labelList.append(xx[dlStart+4:dlEnd])
	
	
labelList.sort()
for yy in labelList:
	print yy