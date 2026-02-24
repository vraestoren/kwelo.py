# kwelo.py
Web-API for [kwelo.com](https://www.kwelo.com) online tools focused on reliability and speed

## Example
```python
from kwelo import Kwelo

kwelo = Kwelo()
ip_location = kwelo.get_ip_location(ip_address="")
print(ip_location)
```
