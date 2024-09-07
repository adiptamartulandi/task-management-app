

class TaskManagementApp:
    """
    This class is the main class of the application. It is responsible for managing tasks.
    This class have 4 functionalitis CRUD: Create, Read, Update, and Delete task.

    Each task has a title, description, and status.
    Currently, using in-mempory data storage, so the data will be lost when the application/server is closed.
    """

    def __init__(self):
        self.data = {}

    def create_task(self, title: str, description: str, status: str):
        """
        Create a new task with the given title and description.
        """

        self.data[title] = {
            "description": description,
            "status": status
        }

    def read_task(self, title: str):
        """
        Read the task with the given title.
        """

        task = self.data.get(title)
        if task:
            return task
        else:
            return "Task not found, please check the title."

    def update_task(self, title: str, type: str, value: str):
        """
        Update the task with the given title.
        User can update the task description or status.
        """

        task = self.data.get(title)
        if task:
            if type == "description":
                task["description"] = value
            elif type == "status":
                task["status"] = value
            else:
                return "Invalid type. Please use description or status."
        else:
            return "Task not found, please check the title."

    def delete_task(self, title: str):
        """
        Delete the task with the given title.
        """

        task = self.data.get(title)
        if task:
            del self.data[title]
        else:
            return "Task not found, please check the title."

    def show_all_tasks(self):
        """
        Show all the tasks.
        """

        return self.data
