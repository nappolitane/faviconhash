# Favicon Hash

Pyhton script to calculate the favicon hash of websites. This hash is useful for finding websites on the internet that use the same technologies. A tool like shodan.io could be used `http.favicon.hash:000`.
## Usage
```
python3 faviconhash.py -u https://domain.com/favicon.ico
```
When using the `-u` option the script is just requesting the .ico file contents and calculates its hash.
If the website is not providing the `/favicon.ico` URI, then search inside the index source page for the following:
`<link rel="shortcut icon" href="/favicon.ico" />`
`<link rel="icon" href="/favicon.png" />`
`<link rel="apple-touch-icon" href="images/touch.png" />`
`<link rel="apple-touch-icon-precomposed" href="images/touch.png" />`

```
python3 faviconhash.py -d domain.com
```
When using `-d` option the script is searching in the google database. You can change the script if you want it to search in the duckduckgo database. 

> **Tip:** Use this option **only if** you can't find the URL for the .ico file
