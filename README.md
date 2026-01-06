How to start jenkin server?


How to start payload url for webhook?
	step1:
	=========================
	start terminal in windows.
	run npx localtunnel --port 8080
	keep the terminal open
	==========================

	If the tunnel is closed then follow step 1
	Take th new url and add as a new payload url in webhook on github reository setting.
	add a sufix at url as /github-webhooks/
	
	for example: if url is https://pretty-rules-stay.loca.lt
	https://pretty-rules-stay.loca.lt/github-webhook/
