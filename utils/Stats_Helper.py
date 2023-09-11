class Stats_Helper(dict):
    def __init__(self, data:dict):
        self.data = data
        if "success" in data:
            self.success = data["success"]
        else:
            self.success = False
    
    def __str__(self):
        return f"Json object: {self.success}"
    
    def __eq__(self, __value: object) -> bool:
        return self.success == __value
    
    def __missing__(self):
        return Stats_Helper({})
    
    def __getitem__(self, item):
        if item in self.data:
            if type(self.data[item]) == dict:
                return Stats_Helper(self.data[item])
            else:
                return self.data[item]
        else:
            return Stats_Helper({})

            
