# greed

A customizable Telegram shop bot that accepts bitcoin payments. Demo at https://t.me/TgShopDemoBot

![](https://img.shields.io/badge/version-beta-blue.svg)

## Requirements, Installation & Usage

Please refer to the [main greed project fork](https://github.com/Steffo99/greed) for requirements, installation guide, and usage instructions before proceeding with the bitcoin setup below

## Integrating Bitcoin

1. You will require a Blockonomics API Key - Complete merchant setup wizard by clicking on Get Started for Free on [Blockonomics Merchants Page](https://www.blockonomics.co/merchants#/).

2. Edit the `config/config.toml` file to set your Blockonomics *api_key* from [Blockonomics Merchant Page](https://www.blockonomics.co/merchants#/stores), and a *secret* of your choosing, you'll use this secret while setting up the Callback URL below.

3. Set the HTTP Callback URL on the Blockonomics Merchants Page

	Below are instructions on how to deploy your bot to obtain a Callback URL using Ngrok or Heroku.

	### Deploy using [Ngrok](https://ngrok.com/download)
	* In a new terminal/cmd prompt, start the bitcoin callback listener on port 5000 `python3 -OO callback.py`
	* In another terminal/cmd prompt, start ngrok on port 5000 `./ngrok http 5000` or `~/ngrok http 5000`
	* Copy the Forwarding URL from ngrok.
	![](assets/images/ngrok.png) 
	* Set the HTTP Callback URL for your store on the [Blockonomics Merchants Page](https://www.blockonomics.co/merchants#/stores). Combine the Forwarding URL with `/callback?secret=YOUR_SECRET`, substituting in your chosen secret from step 2 in place of `YOUR_SECRET`
	   eg.  http://c7f7ecb92ht5.ngrok.io/callback?secret=aN32nFjf4

	### Deploy using [Heroku](https://www.heroku.com/)
	* Test using heroku cli command: `heroku local`
	* You will also be able to login to heroku and push your bot to heroku master to launch it into production using the following commands:
	```
	git init .
	git add .
	git commit -m "Deploy to Heroku"
	heroku login -i
	heroku git:remote -a {your-heroku-project-name}
	git push heroku master
	```
	* You can now start the greed bot and blockonomics callback from the Heroku Dashboard > Resources.
	![](assets/images/heroku.png) 
	* Set the HTTP Callback URL for your store on the [Blockonomics Merchants Page](https://www.blockonomics.co/merchants#/stores), combine the Heroku App URL with `/callback?secret=YOUR_SECRET`, substituting in your chosen secret from step 2 in place of `YOUR_SECRET`
		eg. https://greed.herokuapp.com/callback?secret=aN32nFjf4

That's it! Restart your bot and start accepting bitcoing payments with your bot!

## Credits
This project is a fork of [greed project](https://github.com/Steffo99/greed) by @Steffo99. We would like to thank @Steffo99 for putting this in public domain. 
