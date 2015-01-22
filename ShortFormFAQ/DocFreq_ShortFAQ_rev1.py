import random
import math
import datetime
from string import Template
import xlrd

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer 
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch 

# Misc setup routines

def labelsList():
    return """
		data116
		data117
		clk001
		data118
		clk002
		data119
		data119a
		data120
		clk003
		data121
		data121a
		clk004
		data122
		clk005
		data123
		data123a
		data123b
	""".split()
        
def myPages(canvas, doc): 
    canvas.saveState() 
    canvas.setFillColor('#a0a0a0')
    canvas.setFont('Helvetica-Oblique',10) 
    canvas.drawString(1.0*inch, 0.65*inch, "%s" % pageinfo) 
    canvas.drawCentredString(pageWidth/2.0, 0.65*inch, "%s" % dateNow)
    canvas.setFont('Helvetica',10) 
    canvas.drawString(pageWidth-1.0*inch, 0.65*inch, "%d" % doc.page) 

    # Color scale boxes
    canvas.setFillColor(shortColor1) 
    canvas.rect(pageWidth-0.7*inch, 0.65*inch, 0.1*inch, 0.04*inch, fill=1, stroke=0) 
    canvas.setFillColor(shortColor2) 
    canvas.rect(pageWidth-0.7*inch, 0.75*inch, 0.1*inch, 0.04*inch, fill=1, stroke=0) 
    canvas.setFillColor(shortColor3) 
    canvas.rect(pageWidth-0.7*inch, 0.85*inch, 0.1*inch, 0.04*inch, fill=1, stroke=0) 

    # Color scale text labels
    canvas.setFillColor('#000000') 
    canvas.setFont('Helvetica',6) 
    canvas.drawString(pageWidth-0.55*inch, 0.6*inch, "%d" % int(100*short_max*0.00)) 
    canvas.drawString(pageWidth-0.55*inch, 0.7*inch, "%d" % int(100*short_max*0.33)) 
    canvas.drawString(pageWidth-0.55*inch, 0.8*inch, "%d" % int(100*short_max*0.66)) 
    canvas.drawString(pageWidth-0.55*inch, 0.9*inch, "%d" % int(100*short_max*1.00)) 
    canvas.drawString(pageWidth-0.715*inch, 1.01*inch, "%s" % ('Short %')) 

    # Color scale label ticks
    canvas.setLineWidth(0.35) 
    canvas.setStrokeColor('#000000') 
    # canvas.setDash(0.5, 0.5)
    canvas.line(pageWidth-0.7*inch, 0.62*inch, pageWidth-0.57*inch, 0.62*inch) 
    canvas.line(pageWidth-0.7*inch, 0.72*inch, pageWidth-0.57*inch, 0.72*inch) 
    canvas.line(pageWidth-0.7*inch, 0.82*inch, pageWidth-0.57*inch, 0.82*inch) 
    canvas.line(pageWidth-0.7*inch, 0.92*inch, pageWidth-0.57*inch, 0.92*inch) 

    # Text scale letters
    longStr = 'eE'
    scaleOffset = 1.25*inch	
    scaleUpset = 0.68*inch
    canvas.setFillColor('#000000') 
    canvas.setFont('Helvetica',8) 
    canvas.drawRightString(scaleOffset-0.6*inch, 1.32*inch-scaleUpset, "%s" % (longStr)) 
    canvas.setFont('Helvetica',10) 
    canvas.drawRightString(scaleOffset-0.6*inch, 1.45*inch-scaleUpset, "%s" % (longStr)) 
    canvas.setFont('Helvetica',12) 
    canvas.drawRightString(scaleOffset-0.6*inch, 1.60*inch-scaleUpset, "%s" % (longStr)) 
    canvas.setFont('Helvetica',14) 
    canvas.drawRightString(scaleOffset-0.6*inch, 1.770*inch-scaleUpset, "%s" % (longStr)) 
    canvas.setFont('Helvetica',6) 

    # Text scale text labels
    canvas.setFillColor('#000000') 
    canvas.drawString(scaleOffset-0.55*inch, 1.275*inch-scaleUpset, "%d" % (0)) 
    canvas.drawString(scaleOffset-0.55*inch, 1.405*inch-scaleUpset, "%d" % (25)) 
    canvas.drawString(scaleOffset-0.55*inch, 1.550*inch-scaleUpset, "%d" % (50)) 
    canvas.drawString(scaleOffset-0.55*inch, 1.715*inch-scaleUpset, "%d" % (75)) 
    canvas.drawString(scaleOffset-0.55*inch, 1.905*inch-scaleUpset, "%d" % (100)) 
    canvas.drawString(scaleOffset-0.715*inch, 2.02*inch-scaleUpset, "%s" % ('Long %')) 

    # Text scale label ticks
    canvas.setLineWidth(0.35) 
    canvas.setStrokeColor('#000000') 
    # canvas.setDash(0.5, 0.5)
    canvas.line(scaleOffset-0.665*inch, 1.30*inch-scaleUpset, scaleOffset-0.57*inch, 1.30*inch-scaleUpset) 
    canvas.line(scaleOffset-0.685*inch, 1.425*inch-scaleUpset, scaleOffset-0.57*inch, 1.425*inch-scaleUpset) 
    canvas.line(scaleOffset-0.7*inch, 1.575*inch-scaleUpset, scaleOffset-0.57*inch, 1.575*inch-scaleUpset) 
    canvas.line(scaleOffset-0.715*inch, 1.745*inch-scaleUpset, scaleOffset-0.57*inch, 1.745*inch-scaleUpset) 
    canvas.line(scaleOffset-0.715*inch, 1.935*inch-scaleUpset, scaleOffset-0.57*inch, 1.935*inch-scaleUpset) 

    canvas.restoreState()

#
# Set whether data values are printed and output file name
#
WRITE_DATA_VALUES = True
outfileName = 'DocFreq_ShortFAQ_rev1.pdf'

shortColorGiven = '#000000'
shortColorProblem = '#ff0000'
# Brown to yellow-orange
# shortColor1 = '#eac79d'		# low freq
# shortColor2 = '#b86944'		# med freq
# shortColor3 = '#741e14'		# high freq
# CB 3-class seq PuRd
# shortColor1 = '#e7e1df'		# low freq
# shortColor2 = '#c994c7'		# med freq
# shortColor3 = '#dd1c77'		# high freq
# from CB 4-class seq PuRd
# shortColor1 = '#d7b5d8'		# low freq
# shortColor2 = '#df65b0'		# med freq
# shortColor3 = '#ce1256'		# high freq
# from CB 3-class seq RdPu
# shortColor1 = '#fde0dd'		# low freq
# shortColor2 = '#fa9fb5'		# med freq
# shortColor3 = '#c51b8a'		# high freq
# from CB 4-class seq OrRd == GOOD
# shortColor1 = '#fdcc8a'		# low freq
# shortColor2 = '#fc8d59'		# med freq
# shortColor3 = '#d7301f'		# high freq
# from CB 4-class seq OrRd
shortColor1 = '#f2c384'		# low freq
shortColor2 = '#de703e'		# med freq
shortColor3 = '#9e1506'		# high freq

if WRITE_DATA_VALUES:
    outfileName = outfileName.replace('FAQ','FAQ_Data')

pageinfo = "Size/Color v1 (Short FAQ Data)" 
dateNow = datetime.datetime.now().strftime("%d %b %Y")
styles = getSampleStyleSheet()
pageWidth, pageHeight = letter
doc = SimpleDocTemplate(outfileName, pagesize = letter)
# Story = [Spacer(1,1*inch)] 
Story = [] 

style = styles["Normal"]
# style.fontName = "Times-Roman"
style.fontName = "Helvetica"
style.bulletFontName = "Helvetica"
style.fontSize = 11
style.allowWidows = 0
style.allowOrphans = 0

def MapDataToFontSize(val):
    # Map combined (normalized to 1) data measure onto desired range and resolution 
    #   to return a font size
    # Here want sizes to range from 8 to 16 by two...
    if (val >= 0) & (val < 0.245):
        return 8
    elif (val >= 0.245) & (val < 0.495):
        return 10
    elif (val >= 0.495) & (val < 0.745):
        return 12
    elif (val >= 0.745) & (val <= 1.00):
        return 14
    else:
        return -1            # problem

def MapDataToColor(longVal, shortVal):
    # Map normalized data values into integers which can index color lookup matrix
    # Here calculating whether short data values are statistically same, greater or less than long
    if abs(shortVal - longVal) <= 0.2:
        return '#000000'    # black
    elif (shortVal - longVal) > 0.2:
        return '#8f0000'    # red
    else:
        return '#00008f'    # blue

def MapShortDataToFontSize(shortVal, shortMax):
    # Map combined (normalized to 1) data measure onto desired range and resolution 
    #   to return a font size
    # Here want sizes to range from 8 to 16 by two...
    val = shortVal/shortMax

    if (val >= 0) & (val < 0.245):
        return 8
    elif (val >= 0.245) & (val < 0.495):
        return 10
    elif (val >= 0.495) & (val < 0.745):
        return 12
    elif (val >= 0.745) & (val <= 1.00):
        return 14
    else:
        return -1            # problem

def MapShortDataToColor(shortVal, shortMax):
    # Map normalized data values into colors
    # Here calculating based on short data fraction of max value (renormalizing)
    val = shortVal/shortMax
    
    if (val < 0):
        return shortColorGiven            # given
    elif (val >= 0) & (val < 0.33):
        return shortColor1
    elif (val >= 0.33) & (val < 0.66):
        return shortColor2
    elif (val >= 0.66) & (val <= 1.0):
        return shortColor3
    else:
        return shortColorProblem            # problem

def LabelConvert(label, type):
    if type == 1:           # Text
        return str(label)
    elif type == 2:         # Integer
        return str(int(label))
    

# Read in short version data
short_book = xlrd.open_workbook('WillFindTestData_rev1.xls')
short_sheet = short_book.sheet_by_index(0)
short_ids = short_sheet.col_values(1,1)
short_id_types = short_sheet.col_types(1,1)
short_selected = short_sheet.col_values(2,1)
short_given = short_sheet.col_values(3,1)
short_ntotal = short_sheet.col_values(4,1)

# Some data labels are formatted as integers in Excel, so convert these to strings w/o decimals
short_labels = map(LabelConvert, short_ids, short_id_types)

labels_list = labelsList()
short_data = {}
for ii, id in enumerate(short_labels):
    short_data[id] = float(short_selected[ii])/float(short_ntotal[ii])
    # Option to choose all "Given" sentences as selected
    if short_given[ii] == 'Yes':
        short_data[id] = -1.0
    labels_list.remove(id)

# Check that all labels assigned
if len(labels_list) > 0:
    print "ERROR: Not all labels use for short form data! \n"


# Build up dictionary of font sizes and colors from the data
dict = {}
dict['spAftSec'] = 18
dict['spAftHdr'] = 8

fmax = -1
fmin = 10000

labels_list = labelsList()
short_max = max(short_data.values())
# Build up dictionaries for later use in Template(w)
for id in labels_list:
    
    # Font size is based on "long form" data
    fontSize = MapShortDataToFontSize(short_data[id], short_max)
    dict['s_' + id] = fontSize
    if fontSize > fmax: fmax = fontSize
    if fontSize < fmin: fmin = fontSize
    
    # Statistically compare long and short data to generate a color
    dict['c_' + id] = MapShortDataToColor(short_data[id], short_max)
    
    # if doing data labels
    if WRITE_DATA_VALUES:
		# if doing data labels
		if (short_data[id] >= 0):
			dict['sh_' + id] = '%d' % (int(100*short_data[id]))
		else:
			dict['sh_' + id] = '-'
    
# Set paragraph leading based on font size bounds
style.spaceAfter = 7
style.leading = fmax*1.1
doc.bottomMargin = 1.25*inch

# Read in template document
f = open('WillFindResults_rev1.html','r')
# If doing data labels
# f = open('LongVer_newLabelsDataPrelim3_rev5.html','r')

w = f.read()
f.close()

if WRITE_DATA_VALUES:
	whole_fsp = w.split('</font>')
	
	for ii,xx in enumerate(whole_fsp[1:-1]):
		# Make sure there is a space at the end of the sentence
		if xx[-1] != ' ':
			whole_fsp[ii+1] += ' '
			
		# Get the data label from each line
		dlStart = xx.find('${s_')
		dlEnd = xx.find('} color=${')
		dLabel = xx[dlStart+4:dlEnd]
		
		# Add data values piece & re-add </font> since removed with .split()
		whole_fsp[ii+1] += '(${sh_' + dLabel + '}) </font>'
		
	w = ''.join(whole_fsp)


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



