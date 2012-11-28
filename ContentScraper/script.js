try{
listPrice = document.getElementsByClassName("priceList")[1].innerHTML
}catch(err){
	console.log("Error is with listPrice")
	listPrice = "N/A"
}
//this puts back some HTML that need to be stripped
//final price is not applicable if it is a item not on sale
//"finalPrice"
try{
	finalPrice = document.getElementsByClassName("salePrice")[0].innerHTML
	//will not work if price is bigger than 4
	price = finalPrice.substring(finalPrice.search("</sup>")+6, finalPrice.search("</sup>")+14)
	price = price.substring(0, price.search("<"))
	decimalPrice = finalPrice.substring(finalPrice.search("</span>")+7)
	decimalPrice = decimalPrice.substring(0, decimalPrice.search("<"))
}catch(err){
	console.log("Error is with finalPrice")
	price = "N/A"
	decimalPrice = "N/A"
}
//has a lot to be stripped
//UPC No.
//also shipping weight
//and MFG Part No.
//Manufactured by:
try{
pInfo = document.getElementsByClassName("pInfo")[0].innerHTML
UPC = pInfo.substring(pInfo.search("UPC"), pInfo.search("Box"))
UPC = UPC.substring(UPC.search("<strong>")+8, UPC.search("</strong>"))

//assumes weight will be in pounds
shipWGT = pInfo.substring(pInfo.search("Shipping Weight:"), pInfo.search("pound"))
shipWGT = shipWGT.substring(shipWGT.search("<strong>")+8)
shipWGT = shipWGT.trim()

MFG_No = pInfo.substring(pInfo.search("Mfg Part No:"), pInfo.search("UPC No"))
MFG_No = MFG_No.substring(MFG_No.search("<b>")+3, MFG_No.search("</b>"))

MFG = pInfo.substring(pInfo.search("<strong>")+8, pInfo.search("</strong>"))
}catch(err){
	console.log("error is with pInfo")
	pInfo = "N/A"
	UPC = "N/A"
	shipWGT = "N/A"
	MFG_No = "N/A"
	MFG = "N/A"
}


chrome.extension.sendMessage([price, decimalPrice, UPC, shipWGT, MFG_No, MFG, listPrice])