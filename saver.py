import json
import tool
from tool import depaginate
founded = depaginate()
data = tool.collect(founded)
output = data

with open('output.json', 'w', encoding='utf-8') as gain:
    json.dump(output, gain, indent=2, ensure_ascii=False)
