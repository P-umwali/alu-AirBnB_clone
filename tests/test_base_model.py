import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_save(self):
        self.model.save()
        self.assertIsInstance(self.model.updated_at, datetime)
        # Add more assertions to validate the behavior of the save() method

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        # Add more assertions to validate the content of the dictionary

    def test_id(self):
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)
        # Add more assertions to validate the ID generation and uniqueness

    def test_created_at(self):
        self.assertIsInstance(self.model.created_at, datetime)
        # Add more assertions to validate the behavior of the created_at attribute

    def test_str(self):
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)
        # Add more assertions to validate the string representation

if __name__ == '__main__':
    unittest.main()
