# Python-GetKeys
Micro-package to get a config variable or secrutiy key from a list of possible
locations.

I personally tend to keep all my API keys in a few different locations
depending on the security needed. This package will simply check that list of
locations for the first place the key is found and return it. If the specified
key is not found, you have the option to raise an exception or prompt for
the user to input the value on the command line.

## Configuration
By default the this script will check the following locations. It can be changed
by create a new config file at `~/.config/getkeys.json` containing a list of 
key.json files to check.

```json
{
  "paths": [
    "~/.config/keys.json",
    "~/Private/keys/keys.json"
  ]
}
```

## Usage Example
```python
from getkey import getkey

# This example will check the above two files for a value set at
# the json path jira.apikey. If the key is not found in any of the
# files, it will prompt the user for input on the command line.
apikey = getkey('jira.apikey')  

# This does the same as above, but will raise an Exception rather
# than prompting the user for input.
apikey = getkey('jira.apikey', prompt=False)
```
