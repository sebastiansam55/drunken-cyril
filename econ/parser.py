#tax processor
import csv

cat = ['Property Taxes', 'General Sales and Gross Receipts Taxes', 'Alcoholic Beverages Sales Tax', 'Amusements Sales Tax', 'Insurance Premiums Sales Tax', 'Motor Fuels Sales Tax', 'Pari-mutuels Sales Tax', 'Public Utilities Sales Tax', 'Tobacco Products Sales Tax', 'Other Selective Sales and Gross Receipts Taxes', 'Alcoholic Beverages License', 'Amusements License', 'Corporations in General License', 'Hunting and Fishing License', 'Motor Vehicles License', 'Motor Vehicle Operators License', 'Public Utilities License', 'Occupation and Businesses License, NEC', 'Other License Taxes', 'Individual Income Taxes', 'Corporation Net Income Taxes', 'Death and Gift Taxes', 'Documentary and Stock Transfer Taxes', 'Severance Taxes', 'Taxes, NEC']

abbr = ['ST', 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


states ={'ST':{}, 'AL':{}, 'AK':{}, 'AZ':{}, 'AR':{}, 'CA':{}, 'CO':{}, 'CT':{}, 'DE':{}, 'FL':{}, 'GA':{}, 'HI':{}, 'ID':{}, 'IL':{}, 'IN':{}, 'IA':{}, 'KS':{}, 'KY':{}, 'LA':{}, 'ME':{}, 'MD':{}, 'MA':{}, 'MI':{}, 'MN':{}, 'MS':{}, 'MO':{}, 'MT':{}, 'NE':{}, 'NV':{}, 'NH':{}, 'NJ':{}, 'NM':{}, 'NY':{}, 'NC':{}, 'ND':{}, 'OH':{}, 'OK':{}, 'OR':{}, 'PA':{}, 'RI':{}, 'SC':{}, 'SD':{}, 'TN':{}, 'TX':{}, 'UT':{}, 'VT':{}, 'VA':{}, 'WA':{}, 'WV':{}, 'WI':{}, 'WY':{}}
print(len(states))

reader = csv.reader(open("12staxcd.txt", "r"))	
reader.next()
reader.next()

linecount = 0
for line in reader:
	count = -1;
	for item in line:	
		count+=1
		states[abbr[count]][cat[linecount]] = item
		if count>=50:
			break
		
	linecount+=1
	
#print states	

html= "<html><head><title> Taxes </title></head><body>"

html += "<table border=\"1\">"
html += "<tr>"
html += "<td></td>"
for taxname in cat:
	html+="<th>"+taxname+"</th>"
html+="</tr>"

for state in states:
	html+="<tr>"
	html+="<th>"+state+"</th>"	
	print state
	print states[state]
	print "\n"
	for tax in states[state]:
		if state=="ST":
			break
		html+="<td>"+str(int(states[state][tax]))+"</td>"
		print tax
		print states[state][tax]
	html+="</tr>"
		
		
html+="</table></body></html>"
print html
f = open("html.html", "w")
f.write(html)
f.close()
		
	