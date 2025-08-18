import json
data={"name":"john","age":30}
with open("data.json","w") as f:
    json.dump(data,f)