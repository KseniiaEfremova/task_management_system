import json


def get_user_and_passwd_from_file(file_name: str) -> tuple:
    """
    Retrieves user and password information from a JSON configuration file.
    Args:
        file_name (str): The name of the JSON configuration file.
    Returns:
        tuple: A tuple containing user (str) and password (str) extracted from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        KeyError: If the "user" or "passwd" keys are missing in the JSON data.
        json.JSONDecodeError: If the file content is not a valid JSON.
    """
    try:
        with open(file_name, 'r') as config_file:
            data = json.load(config_file)
            user = data["user"]
            passwd = data["passwd"]
        return user, passwd
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_name}' does not exist.")
    except (KeyError, json.JSONDecodeError) as e:
        raise KeyError(f"Error reading JSON data from '{file_name}': {e}")
