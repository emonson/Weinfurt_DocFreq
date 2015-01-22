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
doc = SimpleDocTemplate('DocFreq_rev4data.pdf', pagesize = letter)
# Story = [Spacer(1,1*inch)] 
Story = [] 

style = styles["Normal"]
# style.fontName = "Times-Roman"
style.fontName = "Helvetica"
style.bulletFontName = "Helvetica"
style.fontSize = 11
style.allowWidows = 0
style.allowOrphans = 0

def MapDataToFontSize(dataVal):
	# Map combined (normalized to 1) data measure onto desired range and resolution 
	# 	to return a font size
	# Here want sizes to range from 8 to 16 by two...
	szMin = 8
	szMax = 14
	szInc = 1
	return int(szMin + szInc*math.floor(float(dataVal)*((szMax-szMin)/szInc)))

def MapDataToColor(longVal, shortVal):
	# Map normalized data values into integers which can index color lookup matrix
	# Here calculating whether short data values are statistically same, greater or less than long
	if abs(shortVal - longVal) <= 0.2:
		return '#000000'	# black
	elif (shortVal - longVal) > 0.2:
		return '#8f0000'	# red
	else:
		return '#00008f'	# blue

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
	# Font size is based on "long form" data
	fontSize = MapDataToFontSize(dataLong[ii])
	dict['s_' + str(ii)] = fontSize
	if fontSize > fmax: fmax = fontSize
	if fontSize < fmin: fmin = fontSize
	# Statistically compare long and short data to generate a color
	dict['c_' + str(ii)] = MapDataToColor(float(dataLong[ii]),float(dataShort[ii]))
	# Adding raw data for display
	dict['lo_' + str(ii)] = '%3.2f' % (float(dataLong[ii]))
	dict['sh_' + str(ii)] = '%3.2f' % (float(dataShort[ii]))
	
# Set paragraph leading based on font size bounds
style.spaceAfter = 7
style.leading = fmax*1.0
doc.bottomMargin = 1.25*inch

# Read in template document
f = open('LongVersion_dataVals_rev4.html','r')
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

