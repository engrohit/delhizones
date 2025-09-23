import json
from bs4 import BeautifulSoup

input_file = "D:/GIT demo/Delhizones/sdbdata_files/sheet001.html"
output_file = "D:/GIT demo/Delhizones/sdbdata_files/sdb.json"

# List of field names in order (as per your format)
fields = [
    "New IP ID", "Category", "BA", "District", "SDCA", "Site Name Master DPR", "ON Aired Date", "Exist Site ID",
    "4G Site ID_Band1", "4G Site ID__Band28", "4G Site ID_Band41", "New IP ID", "Enb_B1", "Enb_B28", "Enb_B41",
    "Media Type", "Maan Media Connectivity", "OAM CEF IP pool", "OAM CEF HW GW", "OAM CEF HW IP", "OAM HW VLAN",
    "OAM RAC IP Pool", "OAM RAC GW", "OAM RAC B1(L2100)", "OAM RAC B28(L700)", "OAM RAC B41(L2500)", "OAM RAC VLAN",
    "S1C RAC IP Pool", "S1C GW", "S1C B1(L2100)", "S1C B28(L700)", "S1C  B41(L2500)", "S1C VLAN", "S1U RAC IP Pool",
    "S1U GW", "S1U B1(L2100)", "S1U B28(L700)", "S1U  B41(L2500)", "S1U VLAN", "MME", "MME IP", "TAC ID", "Router",
    "ID", "Subnet ID", "Final Router Series", "Latitude", "Longitude"
]

with open(input_file, encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]  # Skip header

data = []
for row in rows:
    cells = row.find_all("td")
    if len(cells) < len(fields):
        continue  # skip incomplete rows
    entry = {fields[i]: cells[i].get_text(strip=True) for i in range(len(fields))}
    data.append(entry)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(data)} rows to {output_file}")