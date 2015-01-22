# After changing data labels to new dataXXX scheme, automating
# some of the sentence splits based on the Datamap...xls sheet

import xlrd

book = xlrd.open_workbook('Datamap with Sentence IDs.xls')
sh = book.sheet_by_index(0)

ids = sh.col_values(0,12)
sentences = sh.col_values(1,12)

f = open('LongVer_newLabelsPrelim_rev5.html','r')
# File has some non-ascii characters in it
whole = f.read().decode('latin_1')

for ii, id in enumerate(ids):
	id = str(id)
	if id.endswith(('a', 'b', 'c', 'd')):
		oldStr = sentences[ii].strip()
		newStr = '</font>\n<font size=${s_%s} color=${c_%s}>%s' % (id, id, oldStr)
		whole = whole.replace(oldStr, newStr)
		
# Have to manually fix 92a and 95a since the text is identical
oldStr = 'We will keep health information and research data on secure computers. </font>\n<font size=${s_data092a} color=${c_data092a}></font>\n<font size=${s_data095a} color=${c_data095a}>'
newStr = 'We will keep health information and research data on secure computers. </font>\n<font size=${s_data092a} color=${c_data092a}>'
whole = whole.replace(oldStr, newStr)

oldStr = 'We will store this list on secure computers. </font>\n<font size=${s_data092a} color=${c_data092a}></font>\n<font size=${s_data095a} color=${c_data095a}>'
newStr = 'We will store this list on secure computers. </font>\n<font size=${s_data095a} color=${c_data095a}>'
whole = whole.replace(oldStr, newStr)

fout = open('LongVer_newLabelsPrelim2_rev5.html','w')
# for some reason must re-encode before writing
fout.write(whole.encode('latin_1'))
fout.close()
f.close()

# data179a didn't split properly for some reason
# data138b is a duplicate, so it overwrote data138
# split the 200s manually for now
# manually changed (their) mistake of data138b -> 138b 

		
