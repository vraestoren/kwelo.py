from os import getcwd
from time import time
from pathlib import Path
from requests import Session

class Kwelo:
	def __init__(self) -> None:
		self.api = "https://api.kwelo.com/v1"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def save_file(
			self,
			content: bytes,
			location: str = getcwd()) -> bool:
		with open(
			Path(location).joinpath(f"{time() * 1000}.jpg"), mode="wb+") as file:
				file.write(content)
				file.close()
		return True

	def get_self_ip_address(self) -> dict:
		return self.session.get(
			f"{self.api}/network/ip-address/my?format=json").json()

	def get_ip_address_location(self, ip_address: str) -> dict:
		return self.session.get(
			f"{self.api}/network/ip-address/location/{ip_address}?format=json").json()

	def get_identicon(self, name: str) -> bool:
		return self.save_file(self.session.get(
			f"{self.api}/media/identicon/{name}").content)
