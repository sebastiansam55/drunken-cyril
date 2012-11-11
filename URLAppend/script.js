chrome.browserAction.onClicked.addListener(function(tab){
	URL = tab.url;
	$.post("http://u2xs.com/tmp/fiverr/URLappend.php", {taburl: URL});
	console.log("Saving "+URL);	
});