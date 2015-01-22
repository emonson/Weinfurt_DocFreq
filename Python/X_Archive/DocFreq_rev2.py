import random
import math
from string import Template

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer 
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.rl_config import defaultPageSize 
from reportlab.lib.units import inch 

def myPages(canvas, doc): 
    canvas.saveState() 
    canvas.setFont('Helvetica',9) 
    canvas.drawString(inch, 0.75 * inch, "Page %d -- %s" % (doc.page, pageinfo)) 
    canvas.restoreState()
    
Title = "HELLO WORLD" 
pageinfo = "LONG/SHORT Coded Version (Random data)" 
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0] 
styles = getSampleStyleSheet()
doc = SimpleDocTemplate("DocFreq_rev2.pdf") 
Story = [Spacer(1,1*inch)] 

style = styles["Normal"] 
style.fontName = "Helvetica"
style.fontSize = 11
style.spaceAfter = 12
style.leading = 18

def ComboFunc(dataLong, dataShort):
	# Combine two data numbers into single measure for font size (still normalized to 1)
	# return float(dataLong)+float(dataShort)/2.0
	return float(dataLong)*float(dataShort)

def MapDataToFontSize(dataVal):
	# Map combined (normalized to 1) data measure onto desired range and resolution 
	# 	to return a font size
	# Here want sizes to range from 8 to 18 by two...
	return int(8 + 2*math.floor(float(dataVal)*5))

def MapDataToColorIdx(dataVal):
	# Map normalized data values into integers which can index color lookup matrix
	# Here using a 4 x 4 colormap
	return int(math.floor(float(dataVal)*4))

	# Original map 4x4
# 	colorTable = [['#b4a2ba', '#8173b9', '#4c44b9', '#1916b8']]
# 	colorTable.append(['#ac7384', '#7b5283', '#493183', '#181083'])
# 	colorTable.append(['#a4444f', '#75314f', '#45104f', '#17094e'])
# 	colorTable.append(['#9c1619', '#6f1019', '#420919', '#160319'])
	# Pure RB 3x3
# 	colorTable = [['#cccccc', '#7070cc', '#0000cc']]
# 	colorTable.append(['#cc7070', '#707070', '#000070'])
# 	colorTable.append(['#cc0000', '#700000', '#000000'])
# Pure RB 4x4
colorTable = [['#cccccc', '#8f8fcc', '#5252cc', '#0000cc']]
colorTable.append(['#cc8f8f', '#8f8f8f', '#52528f', '#00008f'])
colorTable.append(['#cc5252', '#8f5252', '#525252', '#000052'])
colorTable.append(['#cc0000', '#8f0000', '#520000', '#000000'])

# Read in long version data
fdataLong = open('dataLong.txt','r')
dataLong = fdataLong.readlines()
fdataLong.close()

# Read in short version data
fdataShort = open('dataShort.txt','r')
dataShort = fdataShort.readlines()
fdataShort.close()

# Check to make sure data is right length (146)
dict = {}
for ii in range(len(dataLong)):
	comboVal = ComboFunc(dataLong[ii], dataShort[ii])
	dict['s_' + str(ii)] = MapDataToFontSize(comboVal)
	idxLong = MapDataToColorIdx(dataLong[ii])
	idxShort = MapDataToColorIdx(dataShort[ii])
	dict['c_' + str(ii)] = colorTable[idxLong][idxShort]
	
# Read in template document
f = open('LongVersion_noCTabs_rev3.html','r')
w = f.read()
f.close()

t = Template(w)
wsub = t.substitute(dict)
wlines = wsub.splitlines()

# Now, iterate through lines, detecting whether starts with '<para' or ends with '</para>'
# and construct paragraphs, appending them to the story, then build the PDF doc.
textList = []
for line in wlines:
	textList.append(line)
	if line.endswith('</para>'):
		p = Paragraph(''.join(textList), style)
		# print ''.join(textList)
		Story.append(p) 
		del textList[:] 
	
doc.build(Story, onFirstPage=myPages, onLaterPages=myPages)

