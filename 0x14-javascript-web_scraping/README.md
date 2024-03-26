# 0x14-javascript-web_scraping Project #

## What is JSON? ##
JSON is a text-based data format following JavaScript object syntax, which was popularized by Douglas Crockford, it is close to JS object literal syntax.
* Converting a string to a native object is called deserialization, while converting a native object to a string so it can be transmitted across the network is called serialization *
How to check the nodejs version you have? : type node -v in your terminal
Required to get installed in this project:
1. Install Node 14 ( I used a newer version it's okay)
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

2. semi-standard to fix your JS code accorsing to the standard:
Install semi-standard
$ sudo npm install semistandard --global

3. Install request module and use it:
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules

A JSON string can be stored in its own file, which is basically just a text file with an extension of .json. We can also convert arrays to/from JSON like the following format:
``` [
  {

    "name": "Molecule Man",
    "age": 29,
    "secretIdentity": "Dan Jukes",
    "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
  }
]

 ```
```

You'd just have to access array items (in its parsed version) by starting with an array index, for example [0]["powers"][0].
---

## You can validate JSON using an application like JSONLint ##
## More intersting things about JSON: ##
- JSON is purely a string with a specified data format — it contains only properties, no methods.
- JSON requires double quotes to be used around strings and property names. Single quotes are not valid other than surrounding the entire JSON string.
- Even a single misplaced comma or colon can cause a JSON file to go wrong, and not work. You should be careful to validate any data you are attempting to use (although computer-generated JSON is less likely to include errors, as long as the generator program is working correctly). You can validate JSON using an application like JSONLint.
- JSON can actually take the form of any data type that is valid for inclusion inside JSON, not just arrays or objects. So for example, a single string or number would be valid JSON.
- Unlike in JavaScript code in which object properties may be unquoted, in JSON only quoted strings may be used as properties.)


