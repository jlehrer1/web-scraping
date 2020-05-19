**google_img.py**

For scraping 100 google images of the given search term. This is the limit for an individual search in Google. TODO: Grab images for related keywords

Usage: 
```
google_img.py <params file> <search term> <write location>
```

If the write location doesn't currently exist, the user will be prompted to create it.

The params file must be in the form
```
<KEY>
<CX>
```

**rand_img.py**

For scraping an arbitrary number of random images to a specified write location. 

Usage:
```
rand_img.py <num images> <write location>
```
If the write location doesn't currently exist, the user will be prompted to create it.
