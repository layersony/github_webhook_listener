# Github Webhook Listener
### Version 1

A python Program that automatically updates your local or remote Repos

Set up the GitHub webhook:

* Go to the GitHub page for the repo you're interested in.
* Click on "Settings" in the rightmost list of options at the top of the page.
* Click on "Webhooks" in the left-hand menu.
* Click on "Add webhook" on the right.
* Enter your server's address in the "Payload URL" box, followed by /webhook.
* Choose application/json as the content type.
* Set "Just the push event." as the event type.
* Click "Add webhook".

### Payload URL
```bash
https://<live server url>/webhook/<name of repository>
```
## Contact Me
Email me on [Gmail](sammaingi5@gmail.com)
