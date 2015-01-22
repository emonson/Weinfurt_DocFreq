import random
import math

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer 
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.rl_config import defaultPageSize 
from reportlab.lib.units import inch 
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0] 
styles = getSampleStyleSheet()

# class ParagraphStyle(PropertySet): 
#     defaults = { 
#         'fontName':'Times-Roman', 
#         'fontSize':10, 
#         'leading':12, 
#         'leftIndent':0, 
#         'rightIndent':0, 
#         'firstLineIndent':0, 
#         'alignment':TA_LEFT, 	# TA_LEFT = 0, TA_CENTER = 1
#         'spaceBefore':0, 
#         'spaceAfter':0, 
#         'bulletFontName':'Times-Roman', 
#         'bulletFontSize':10, 
#         'bulletIndent':0, 
#         'textColor': black, 
#         'backColor':None, 
#         'wordWrap':None, 
#         'borderWidth': 0, 
#         'borderPadding': 0, 
#         'borderColor': None, 
#         'borderRadius': None, 
#         'allowWidows': 1, 
#         'allowOrphans': 0, 
#         } 

Title = "HELLO WORLD" 
pageinfo = "platypus example" 
def myFirstPage(canvas, doc): 
    canvas.saveState() 
    canvas.setFont('Helvetica-Bold',12) 
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title) 
    canvas.setFont('Helvetica',9) 
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo) 
    canvas.restoreState()
    
def myLaterPages(canvas, doc): 
    canvas.saveState() 
    canvas.setFont('Helvetica',9) 
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo)) 
    canvas.restoreState()
    
def go(): 
	doc = SimpleDocTemplate("phello.pdf") 
	Story = [Spacer(1,1*inch)] 
	style = styles["Normal"] 
	style.fontName = "Helvetica"
	style.fontSize = 11
	style.spaceAfter = 12
	style.leading = 18
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
	for i in range(100): 
		bogustextList = ["<para>"]
		for j in range(20):
			fontSize = random.uniform(8,18)
			scaledValue = 4.0*(fontSize-8.0)/10.0
			theta = (math.pi/2.0)*random.random()
			colorX = int(math.floor(scaledValue*math.cos(theta)))
			colorY = int(math.floor(scaledValue*math.sin(theta)))
			# print scaledValue, theta, colorX, colorY
			bogustextList.append('<font size=' + str(fontSize) + \
				' color="' + colorTable[colorX][colorY] + \
				('">This is Paragraph number %s. </font>' % i))
		# print ''.join(bogustextList) 
		bogustextList.append("</para>")
		p = Paragraph(''.join(bogustextList), style) 
		Story.append(p) 
		# Story.append(Spacer(1,0.2*inch)) 
	doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

go()

# In the real version
# from string import Template
# 
# def ComboFunc(dataLong, dataShort):
# 	# Combine two data numbers into single measure for font size (still normalized to 1)
# 	pass
#
# def MapDataToFontSize(dataVal):
# 	# Map combined data measure onto desired range and resolution to return a font size
# 	pass
# 
# def MapDataToColorIdx(dataNum):
# 	# Map normalized data values into integers which can index color lookup matrix
# 	pass
# 
# fdataLong = open('dataLong.txt','r')
# dataLong = fdataLong.readlines()
# fdataShort = open('dataShort.txt','r')
# dataShort = fdataShort.readlines()
# # Check to make sure data is right length (146)
# dict = {}
# for ii in range(len(dataLong)):
# 	dict['s_' + str(ii)] = MapDataToFontSize(ComboFunc(dataLong, dataShort))
# 	dict['c_' + str(ii)] = colorTable[MapDataToColorIdx(dataLong[ii])][MapDataToColorIdx(dataShort[ii])]
# 	
# f = open('file.html','r')
# w = f.read()
# t = template(w)
# wsub = t.substitute(dict)
# 
# wlines = wsub.splitlines()
# Now, iterate through lines, detecting whether starts with '<para' or ends with '</para>'
# and construct paragraphs, appending them to the story, then build the PDF doc.
# for line in wlines:
# 	textList = []


