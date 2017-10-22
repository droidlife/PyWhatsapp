# PyWhatsapp
> Python script to control whatsapp web using terminal

# Overview
PyWhatsapp contains python script that uses selenium to automate the use of whatsapp web.
The selenium is currently using chrome webdriver.

![Alt Text](https://res.cloudinary.com/ankurj/image/upload/v1508597411/Peek_2017-10-21_19-58_tfpr7i.gif)


# Requirements

1. Install chrome using 
   `sudo apt-get install google-chrome-stable`
   
2. Download chromeweb driver from <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads" target="_blank">here</a>.

3. Install selenium using `pip install selenium`

4. Add `export CHROME_DRIVER='\path\to\chrom\driver'` in bashrc file

# Usage

Just run the whats.py file by

`python whats.py`
<br>

Things you can do with the script:

1. Send a **scheduled** message.

2. **Broadcast** a message by specifying the user name by comma separated values. <br>
   Eg: `Ankur, Bhanu, Riyaz, Mayank`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
