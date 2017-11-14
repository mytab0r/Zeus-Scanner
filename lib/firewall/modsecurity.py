import re


__item__ = "ModSecurity: Open Source Web Application Firewall"


def detect(content, **kwargs):
    content = str(content)
    detection_schema = (
        re.compile(r"ModSecurity|NYOB", re.I),
        re.compile(r"Mod Security", re.I),
        re.compile(r"mod_security", re.I),
        re.compile(r"This error was generated by Mod_Security", re.I),
        re.compile(r"Web Server at", re.I),
        re.compile(r"page you are (accessing|trying)? (to|is)? (access)? (is|to)? (restricted)?", re.I)
    )
    for detection in detection_schema:
        if detection.search(content) is not None:
            return True
