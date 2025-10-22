    # create_env.py
    import os

    # Define your environment variables
    env_variables = {
        "DATABASE_URL": "postgresql://user:password@host:port/database_name",
        "API_KEY": "your_secret_api_key_here",
        "DEBUG_MODE": "True"
    }

    # Specify the path for the .env file
    env_file_path = ".env"

    try:
        with open(env_file_path, "w") as f:
            for key, value in env_variables.items():
                f.write(f"{key}={value}\n")
        print(f".env file created successfully at: {os.path.abspath(env_file_path)}")
    except IOError as e:
        print(f"Error creating .env file: {e}")