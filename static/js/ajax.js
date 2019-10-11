function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
					}
			}
	}
	return cookieValue;
}

function doajax(url1,argv,fun,doalert){
	if(doalert == "undefined") doalert = true;
	http_request = false;     
	if (window.XMLHttpRequest) { // Mozilla, Safari,...
		http_request = new XMLHttpRequest();
		if (http_request.overrideMimeType) {
			http_request.overrideMimeType('text/xml');
		}
	} 
	else if (window.ActiveXObject) { // IE
		try {
			http_request = new ActiveXObject("Msxml2.XMLHTTP");
		} 
		catch (e) {
			alert("[Msxml2.XMLHTTP]I can't send the message!"+e.message);
		try {
			http_request = new ActiveXObject("Microsoft.XMLHTTP");
		} 
		catch (e) {
			alert("[Microsoft.XMLHTTP]I can't send the message!"+e.message);
		}
		}
	}

	if (!http_request) {
		alert('Giving up :( Cannot create an XMLHTTP instance');
		return false;
	}
	http_request.onreadystatechange =  function(){
		if(http_request.readyState == 4)
			if(http_request.status == 200){
				if(fun != null)
					fun(http_request.responseText);
				else
					if(doalert) alert(http_request.responseText);
			}
			//else alert(http_request.status + ": " + http_request.statusText);
	};
	//alert(url1 + "?" + argv);
	http_request.open('GET', url1+"?"+argv, false);
	http_request.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	http_request.setRequestHeader("Charset", "utf-8");
	http_request.send(null);
}

function doajax_post(url1,argv,fun){
	http_request = false;     
	if (window.XMLHttpRequest) { // Mozilla, Safari,...
		http_request = new XMLHttpRequest();
		if (http_request.overrideMimeType) {
			http_request.overrideMimeType('text/xml');
		}
	} 
	else if (window.ActiveXObject) { // IE
		try {
			http_request = new ActiveXObject("Msxml2.XMLHTTP");
		} 
		catch (e) {
			alert("[Msxml2.XMLHTTP]I can't send the message!"+e.message);
		try {
			http_request = new ActiveXObject("Microsoft.XMLHTTP");
		} 
		catch (e) {
			alert("[Microsoft.XMLHTTP]I can't send the message!"+e.message);
		}
		}
	}

	if (!http_request) {
		alert('Giving up :( Cannot create an XMLHTTP instance');
		return false;
	}
	http_request.onreadystatechange =  function(){
		if(http_request.readyState == 4)
			if(http_request.status == 200) {
				if(fun != null)
					fun(http_request.responseText);
				else
					alert(http_request.responseText);
			}
			//else alert(http_request.status + ": " + http_request.statusText);
	};
	//alert(url1 + "?" + argv);
	http_request.open('POST', url1, false);
	http_request.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	http_request.setRequestHeader("Charset", "utf-8");
	http_request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));  
	http_request.send(argv);
}