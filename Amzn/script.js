console.log("AmazonWishList Running!")
baseURL = document.getElementById("handleBuy").action
sessionid = document.getElementById("session-id").value
asin = document.getElementById("ASIN").value
merchantExclusive = document.getElementById("isMerchantExclusive").value
merch = document.getElementById("merchantID").value
nodeID = document.getElementById("nodeID").value
offerListingID = document.getElementById("offerListingID").value
sellingCustomerID = document.getElementById("sellingCustomerID").value
srcCustOrgListID = document.getElementById("sourceCustomerOrgListID").value
srcCustOrgListItemID = document.getElementById("sourceCustomerOrgListItemID").value
qid = document.getElementById("qid").value
sr = document.getElementById("sr").value
storeID = document.getElementById("storeID").value
tagActionCode = document.getElementById("tagActionCode").value
viewID = document.getElementById("viewID").value
isAddon = document.getElementById("isAddon").value

dataToPost = {"session-id": sessionid, "ASIN": asin, "isMerchantExclusive": merchantExclusive, "merchantID": merch, "nodeID": nodeID, "offerListingID": offerListingID,	"sellingCustomerID": sellingCustomerID, "sourceCustomerOrgListID": srcCustOrgListID, "sourceCustomerOrgListItemID": srcCustOrgListItemID,"qid": qid, "sr": sr, "storeID":storeID, "tagActionCode": tagActionCode, "viewID":viewID, "isAddon":isAddon}
	
chrome.extension.sendMessage(dataToPost)