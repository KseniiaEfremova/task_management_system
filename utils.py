import json
import logging


def get_host_user_and_passwd_from_file(file_name: str) -> tuple:
    """
    Retrieves user and password information from a JSON configuration file.
    Args:
        file_name (str): The name of the JSON configuration file.
    Returns:
        tuple: A tuple containing host (str), user (str) and password (str) extracted from the file.
    Raises:
        ValueError: If the retrieved credentials (user or password) are empty or None.
        FileNotFoundError: If the specified file does not exist.
        KeyError: If the "user" or "passwd" keys are missing in the JSON data.
        json.JSONDecodeError: If the file content is not a valid JSON.
    """
    try:
        with open(file_name, 'r') as config_file:
            data = json.load(config_file)
            host = data["host"]
            user = data["user"]
            passwd = data["passwd"]
        if not host or not user or not passwd:
            # Print an error message and raise a ValueError if user or password or host is empty or None
            print("Invalid user or password or host in JSON configuration.")
            raise ValueError("Invalid user or password or host in JSON configuration.")
        return host, user, passwd
    except FileNotFoundError as e:
        print(f"The file '{file_name}' does not exist.")
        raise e
    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error reading JSON data from '{file_name}': {e}")
        raise e
    except Exception as e:
        # Catch unexpected exceptions, log them, and raise to crash the program
        logging.exception(f"Unexpected error occurred: {e}")
        raise e
