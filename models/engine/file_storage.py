import json
from models.base_model import BaseModel  # Add this import statement

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    if class_name == "BaseModel":
                        from models.base_model import BaseModel
                        cls = BaseModel
                    else:
                        cls = globals()[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
                    
