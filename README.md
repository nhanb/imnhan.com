# My blog

This is the source code for http://www.nerdyweekly.com using
[Pelican](http://github.com/getpelican/pelican)

# Dev environment

This repo targets Pelican 3.7 on python3. Initial setup on Ubuntu with virtualenvwrapper looks
something like this:

```bash
mkvirtualenv -p `which python3` pelican
pip install --upgrade pip
pip install -r requirements.txt
```

Then use:

- `make devserver` / `make stopserver` for local dev at port 8000
- `make github` to publish to www.nerdyweekly.com

Alternatively, if you find the `make dev/stopserver` workflow clumsy, manually run `pelican -r` and
simple python http server to keep everything in the foreground:

```bash
pelican -r content  # in 1 terminal
cd output && python3 -m http.server 8000  # in another terminal
```


# License

All code and content within this repository is licensed under the terms of the MIT license:

```
The MIT License (MIT)

Copyright (c) 2013-2015 Bui Thanh Nhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
