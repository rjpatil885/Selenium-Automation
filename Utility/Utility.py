import json

class Utility_QA:

  dic_list = []
  dic_list_iframe = []
  dic_list_handle = []

  def set_data(self,data):

    self.dic_list.append(data)

    Json_To_Dums().data_json_dums_test(self.dic_list)
    
  def set_data_iframe(self,data):

      self.dic_list_iframe.append(data)

      Json_To_Dums().data_json_dums_test_iframe(self.dic_list_iframe)
      

  def set_data_handle(self,data):

        self.dic_list_handle.append(data)

        Json_To_Dums().data_json_dums_test_handle(self.dic_list_handle)
        
  def data_json_load(self):

    with open('Data/test_data/test.json') as json_file: 
          
      data = json.load(json_file)

    return data

  def data_json_load_iframe(self):

    with open('Data/test_data/iframe.json') as json_file: 
          
      data = json.load(json_file)

    return data

  def data_json_load_handle(self):

    with open('Data/test_data/handle.json') as json_file: 
          
      data = json.load(json_file)

    return data

class Json_To_Dums:

  def data_json_dums_test(self,data):

    with open('Data/test_data/test.json' , 'w' ) as f : 

      json.dump(data, f, indent=2, ensure_ascii=False)

  def data_json_dums_test_iframe(self,data):

    with open('Data/test_data/iframe.json' , 'w' ) as f : 

      json.dump(data, f, indent=2, ensure_ascii=False)

      
  def data_json_dums_test_handle(self,data):

    with open('Data/test_data/handle.json' , 'w' ) as f : 

      json.dump(data, f, indent=2, ensure_ascii=False)
