chrome.tabs.onUpdated.addListener(function(tabid, changeInfo, tab){
	if(tab.url.search("www.amazon.com/gp/product/handle-buy-box") >= 0){
		chrome.tabs.executeScript(tab.id, {"file":"script.js"})
	}
});
