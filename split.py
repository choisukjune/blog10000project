import json

a = "저렴한 상해보험 추천 비교 정리 뜻 포함, 현대해상 마음플러스 상해종합보험 등-----https://blog.naver.com/PostView.naver?blogId=1004goods&logNo=223417275649&categoryNo=35&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=&from="
b = a.split("-----")[1].split("?")[1].split("&")

d = {}
for c in b:
    e = c.split("=")
    d[ e[0] ] = e[1]
with open("test.json", 'w') as outfile:
    json.dump(d, outfile, indent=4)


f = open("test.json","r")
testJson = f.read()
result = json.loads(testJson)
print(result['blogId'])

f.close()


json_data = '{ "p1": { "name": "chulsu", "age": 20 }, "p2": { "name": "younghee", "age": 22 } }'
dict_data = { "p1": { "name": "chulsu", "age": 20 }, "p2": { "name": "younghee", "age": 22 } }

# Convert json to dict
result = json.loads(json_data)
print("parse_json result: %s" % type(result))

# Convert dict to json
result = json.dumps(dict_data)
print("convert_json result: %s" % type(result))
