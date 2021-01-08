## 🐱 Nekobin API Wrapper

### ⬇️ Installing nekobin via 🐍 pip:

```
pip install nekobin
```

### 🆕 Upgrading nekobin via 🐍 pip:

```
pip install -U nekobin
```

### ⬇️ Installing nekobin via 🌐 source:

```
git clone https://github.com/OpenRestfulAPI/nekobinpy
cd nekobinpy
make install
```


### 📖 Example Usage:

```
from nekobin import NekoBin, errors
import asyncio

nekobin = NekoBin()


async def main():
    try:
        neko = await nekobin.nekofy(
            content="Hello World",
            title="example",  # Optional
            author="pokurt"  # Optional
        )
    except errors.HostDownError:
        return print("Host is down at the moment")
    output = "Nekofy Content:\n-----------\n"
    output += "Key: " + neko.key + "\n"
    output += "URL: " + neko.url + "\n"
    output += "Raw URL: " + neko.raw + "\n"
    if neko.title:
        output += "Title: " + neko.title + "\n"
    if neko.author:
        output += "Author: " + neko.author + "\n"
    output += "Date: " + str(neko.date) + "\n"
    output += "Views: " + str(neko.views) + "\n"
    output += "Length: " + str(neko.length) + "\n"
    output += "Content: " + neko.content + "\n"
    print(output)


if __name__ == "__main__":
    asyncio.run(main())
```

### ©️ Copyrights

This Project was made by an indivial on [Telegram](https://t.me/DeprecatedUser). The person who made this API wrapper has nothing to do with [Nekobin](https://nekobin.com) or the base source of the paste service. Therefore All rights reserved to [Nekobin](https://nekobin.com) Paste Service's Rightful Owner [Dan](https://github.com/delivrance) Himself.
