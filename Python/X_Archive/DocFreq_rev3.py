import random
import math
import datetime
from string import Template

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer 
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch 

def myPages(canvas, doc): 
    canvas.saveState() 
    canvas.setFillColorRGB(0.5, 0.5, 0.5)
    canvas.setFont('Helvetica-Oblique',10) 
    canvas.drawString(1.0*inch, 0.65*inch, "%s" % pageinfo) 
    canvas.drawCentredString(pageWidth/2.0, 0.65*inch, "%s" % dateNow)
    canvas.setFont('Helvetica',10) 
    canvas.drawString(pageWidth-1.0*inch, 0.65*inch, "%d" % doc.page) 
    canvas.restoreState()
    
pageinfo = "Size/Color v3 (Random data)" 
dateNow = datetime.datetime.now().strftime("%d %b %Y")
styles = getSampleStyleSheet()
pageWidth, pageHeight = letter
doc = SimpleDocTemplate('DocFreq_rev3.pdf', pagesize = letter)
# Story = [Spacer(1,1*inch)] 
Story = [] 

style = styles["Normal"]
# style.fontName = "Times-Roman"
style.fontName = "Helvetica"
style.bulletFontName = "Helvetica"
style.fontSize = 11
style.allowWidows = 0
style.allowOrphans = 0

def ComboFunc(dataLong, dataShort):
	# Combine two data numbers into single measure for font size (still normalized to 1)
	return (float(dataLong)+float(dataShort))/2.0
	# return float(dataLong)*float(dataShort)

def MapDataToFontSize(dataVal):
	# Map combined (normalized to 1) data measure onto desired range and resolution 
	# 	to return a font size
	# Here want sizes to range from 8 to 16 by two...
	szMin = 8
	szMax = 14
	szInc = 1
	return int(szMin + szInc*math.floor(float(dataVal)*((szMax-szMin)/szInc)))

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

# TODO: Check to make sure data is right length (146)j

# Build up dictionary of font sizes and colors from the data
dict = {}
dict['spAfTitle'] = 24
dict['spBefSeq'] = 18
dict['spBefHds'] = 28
dict['seqLftInd'] = 16
dict['bulInd'] = 16
dict['bulTxtInd'] = 32

fmax = -1
fmin = 10000
for ii in range(len(dataLong)):
	comboVal = ComboFunc(dataLong[ii], dataShort[ii])
	fontSize = MapDataToFontSize(comboVal)
	dict['s_' + str(ii)] = fontSize
	if fontSize > fmax: fmax = fontSize
	if fontSize < fmin: fmin = fontSize
	idxLong = MapDataToColorIdx(dataLong[ii])
	idxShort = MapDataToColorIdx(dataShort[ii])
	dict['c_' + str(ii)] = colorTable[idxLong][idxShort]
	
# Set paragraph leading based on font size bounds
style.spaceAfter = 7
style.leading = fmax*1.0
doc.bottomMargin = 1.25*inch

# Read in template document
f = open('LongVersion_noCTabs_rev4.html','r')
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

