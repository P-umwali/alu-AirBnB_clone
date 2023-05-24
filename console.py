import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Handle end-of-file input (Ctrl+D) to quit the program"""
        print()
        return True

    def do_help(self, arg):
        """Provide help information for commands"""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            instance = eval(arg)()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = class_name + "." + instance_id
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = class_name + "." + instance_id
            obj = storage.all().get(key)
            if obj:
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        try:
            if arg:
                class_name = arg
                if class_name not in storage.classes:
                    print("** class doesn't exist **")
                    return

                instances = [str(obj) for obj in storage.all().values()
                             if type(obj).__name__ == class_name]
            else:
                instances = [str(obj) for obj in storage.all().values()]

            print(instances)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = class_name + "." + instance_id
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            attr_name = args[2]
            if len(args)
