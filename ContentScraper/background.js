chrome.tabs.onUpdated.addListener(function(tabid, changeInfo, tab){
	if(tab.url.search("tigerdirect.com/applications/SearchTools/") >= 0){
		chrome.pageAction.show(tabid);
		chrome.pageAction.setIcon({"path": "icon_19.png", "tabId": tabid})
		chrome.tabs.executeScript(tab.id, {"file": "script.js"})		
	}
});
chrome.extension.onMessage.addListener(function(message, sender, sendResponse){
	tab = sender['tab']
	tabTitle = tab.title
	console.log(message)
	$.post("http://192.168.1.105/contentscraper.php", {price: message[0], decimalPrice: message[1], UPC: message[2], weight: message[3], MFG_No: message[4], MFG: message[5], listPrice: message[6], title: tabTitle});
	console.log("Sent!")
});