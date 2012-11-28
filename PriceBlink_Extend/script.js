console.log("Script running")
console.log("iframes abound!")
str = document.getElementById("pb-iframe")
console.log(str)
chrome.extension.sendMessage(str)
document.write(str)
	
