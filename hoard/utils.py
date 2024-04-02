# Define the server address and port
SERVER_ADDRESS = ('localhost', 8000)

# Define the data store
data_store = {}

# Define the supported data types
SUPPORTED_TYPES = (str, bytes, int, float, type(None), list, dict)

MAX_KEY_LENGTH = 1024  # Maximum length of a key (in bytes)
MAX_VALUE_LENGTH_BYTES = 1048576  # Maximum length of a value (1 MB)
