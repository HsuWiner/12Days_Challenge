# -*- coding: utf-8 -*-
import  urllib.request as Url_Req
import  os , csv



res = "https://data.nhi.gov.tw/resource/mask/maskdata.csv"

# print(os.getcwd())
path = './github/12Week_Challenge/DownLoad/'
os.chdir(path)
# print(os.getcwd())
filename = 'maskdata_auto.csv'

Url_Req.urlretrieve(res , filename)

with open(filename , 'r' , newline='') as file_data:
      csvconver = csv.reader(file_data)
      mask_data = list(csvconver)
      # print(mask_data)


# for (kye_index , key_list) in enumerate(mask_data[0]):
#       print(kye_index , key_list)
#
# for value_list in mask_data[1:]:
#       print (value_list[0])


# dict_from_list = {}
dict_city_sum = {}
# list_cisty = []
child = []
aldult = []
for (kye_index , key_list) in enumerate(mask_data[0]):
      # print(kye_index , key_list)
      # list_data = []
      for value_list in mask_data[1:]:
            # print(value_list)
            # list_data.append(value_list[kye_index])
            if kye_index == 2:
                  # list_cisty.append(value_list[kye_index][0:3])

                  if value_list[kye_index][0:3] in dict_city_sum:
                        # print('OK')
                        search_index = list(dict_city_sum.keys()).index(value_list[kye_index][0:3])
                        # print('增加前',child[search_index],value_list[5] )
                        child[search_index] += int(value_list[5])
                        # print('增加後',child[search_index])
                        #
                        # print('增加前',aldult[search_index],value_list[4])
                        aldult[search_index] += int(value_list[4])
                        # print('增加後',aldult[search_index])
                  else:
                        dict_city_sum[value_list[kye_index][0:3]] = value_list[kye_index][0:3]
                        child.append(int(value_list[5]))
                        aldult.append(int(value_list[4]))
                        # dict_city_sum['child'] = value_list[5]
                        # dict_city_sum['aldult'] = value_list[4]
                  pass
            pass
      # print(list_data)
      # dict_from_list[key_list] = list_data
      pass
            # print(value_list[kye_index])
# dict_from_list["城市"] = list_cisty

# dict_city_sum['child'] = child
# dict_city_sum['aldult'] = child

# print(dict_city_sum.items())

for key in dict_city_sum:
      search_index = list(dict_city_sum.keys()).index(key)
      print('城市名：',key,'--->成人口罩剩餘數：',aldult[search_index],';','兒童口罩剩餘數：',child[search_index] )
      pass

# print(dict_from_list.keys())
#
# print(dict_from_list["城市"][0])
# print(dict_from_list["成人口罩剩餘數"][0])
# print(dict_from_list["兒童口罩剩餘數"][0])

# dict_city_sum = {}
# city = []
# child = []
# aldult = []
#
# for (key,value) in dict_from_list.items():
#       if key == "城市":
#             city = value
#       if key == "成人口罩剩餘數":
#             aldult = value
#       if key == "兒童口罩剩餘數":
#             child = value
#       pass
#
# print(city)
# print(aldult)
# print(child)
