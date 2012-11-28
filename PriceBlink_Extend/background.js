URL = "http://192.168.1.105/test.php"

chrome.tabs.onUpdated.addListener(function(tabid, changeinfo, tab){
	chrome.tabs.executeScript(tabid, {"file": "script.js"})
	
});

chrome.extension.onMessage.addListener(function(message, sender, sendResponse){
	console.log("Message Recieved")
	console.log(message)
	console.log(sender)
	//$.post(URL, {info: info});
});