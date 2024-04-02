import pickle
from socketserver import ThreadingTCPServer, BaseRequestHandler
from .utils import MAX_VALUE_LENGTH_BYTES, MAX_KEY_LENGTH, SUPPORTED_TYPES, SERVER_ADDRESS


class HoardRequestHandler(BaseRequestHandler):
    """
    Request handler for the Hoard server.
    """

    def handle(self):
        """
        Handle a new client connection.
        """
        data = self.receive_data()
        response = self.process_request(data)
        self.send_response(response)

    def receive_data(self):
        """
        Receive data from the client.
        """
        return self.request.recv(MAX_VALUE_LENGTH_BYTES)

    def send_response(self, response):
        """
        Send the response back to the client.
        """
        self.request.sendall(response)

    def process_request(self, data):
        """
        Process the client request and return the appropriate response.
        """

        # Parse the commands and arguments
        command_name, args = self.parse_command(data.decode('utf-8'))

        # Handle the command
        if command_name == 'GET':
            return self.handle_get(args)
        elif command_name == 'SET':
            return self.handle_set(args)
        elif command_name == 'DELETE':
            return self.handle_delete(args)
        elif command_name == 'FLUSH':
            return self.handle_flush(args)
        elif command_name == 'MGET':
            return self.handle_mget(args)
        elif command_name == 'MSET':
            return self.handle_mset(args)
        else:
            return b'ERROR: Unknown command'

    def parse_command(self, command):
        """
        Parse the command and return the command name and arguments.
        """
        parts = command.split()
        if not parts:
            return None, None
        command_name = parts[0].upper()
        args = parts[1:]
        return command_name, args

    def handle_get(self, args):
        """
        Handle the GET command.
        """
        if len(args) != 1:
            return b'Error: Invalid number of arguments'
        key = args[0].encode('utf-8')
        if len(key) > MAX_KEY_LENGTH:
            return b'Error: Key too long'
        value = data_store.get(key)
        if value is None:
            return b'NIL'
        else:
            return pickle.dumps(value)

    def handle_set(self, args):
        """
        Handle the SET command.
        """
        if len(args) != 2:
            return b'Error: Invalid number of arguments'
        key, value = args
        if len(key) > MAX_KEY_LENGTH:
            return b'Error: Key too long'
        try:
            value = pickle.loads(value)
            if not isinstance(value, SUPPORTED_TYPES):
                return b'Error: Unsupported data type'
            if len(pickle.dumps(value)) > MAX_VALUE_LENGTH_BYTES:
                return b'Error: Value too large'
            data_store[key] = value
            return b'Ok!'
        except pickle.UnpicklingError:
            return b'Error: Invalid data format'

    def handle_delete(self, args):
        """
        Handle the DELETE command.
        """
        if len(args) != 1:
            return b'Error: Invalid number of arguments'
        key = args[0]
        if len(key) > MAX_KEY_LENGTH:
            return b'Error: Key too long'
        if key in data_store:
            del data_store[key]
            return b'Ok!'
        else:
            return b'NIL'

    def handle_flush(self, args):
        """
        Handle the FLUSH command.
        """
        data_store.clear()
        return b'OK'

    def handle_mget(self, args):
        """
        Handle the MGET command.
        """
        if not args:
            return b'Error: Invalid number of arguments'
        values = []
        for key in args:
            if len(key) > MAX_KEY_LENGTH:
                values.append(b'Error: Key too long')
            else:
                value = data_store.get(key)
                if value is None:
                    values.append(b'NIL')
                else:
                    values.append(pickle.dumps(value))
        return b' '.join(values)

    def handle_mset(self, args):
        """
        Handle the MSET command.
        """
        if len(args) % 2 != 0:
            return b'Error: Invalid number of arguments'
        for i in range(0, len(args), 2):
            key, value = args[i:i + 2]
            if len(key) > MAX_KEY_LENGTH:
                return b'Error: Key too long'
            try:
                value = pickle.loads(value)
                if not isinstance(value, SUPPORTED_TYPES):
                    return b'Error: Unsupported data type'
                if len(pickle.dumps(value)) > MAX_VALUE_LENGTH_BYTES:
                    return b'Error: Value too large'
            except pickle.UnpicklingError:
                return b'Error: Invalid data format'
            data_store[key] = value
        return b'Ok'


def main():
    """
    The main function that starts the server.
    """
    try:
        server = ThreadingTCPServer(SERVER_ADDRESS, HoardRequestHandler)
        print(f'Listening on {SERVER_ADDRESS}')
        server.serve_forever()
    except Exception as e:
        print(f'Error: {e}')
        return


if __name__ == "__main__":
    main()
