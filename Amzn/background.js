chrome.tabs.onUpdated.addListener(function(tabid, changeInfo, tab){
	if(tab.url.search("amazon.com") >= 0){
		chrome.pageAction.show(tabid);
		chrome.pageAction.setIcon({"path": "icon_19.png", "tabId": tabid})	
	}
});
chrome.pageAction.onClicked.addListener(function(tab){
	chrome.tabs.executeScript(tab.id, {"file":"script.js"})
});
chrome.extension.onMessage.addListener(function(message, sender, sendResponse){
	console.log(message)
	console.log(sender['tab'].url)
	URLToPost = "http://www.amazon.com/gp/item-dispatch/ref=wl_mb_bmvd_1_awl"
	//$.post(URLToPost, message)
	console.log($.post(URLToPost, {"session-id": message['sessionid'], "ASIN": message['asin'], "isMerchantExclusive": message['merchantExclusive'], "merchantID": message['merch'], "nodeID": message['nodeID'], "offerListingID": message['offerListingID'],	"sellingCustomerID": message['sellingCustomerID'], "sourceCustomerOrgListID": message['srcCustOrgListID'], "sourceCustomerOrgListItemID": message['srcCustOrgListItemID'], "qid": message['qid'], "sr": message['sr'], "storeID":message['storeID'], "tagActionCode": message['tagActionCode'], "viewID": message['viewID'], "isAddon": message['isAddon']}))
	//$.post(
});