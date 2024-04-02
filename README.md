# Hoard Server

Hoard Server is a Python implementation of a simple key-value data store server. It supports various commands such as GET, SET, DELETE, FLUSH, MGET, and MSET for managing key-value pairs. The server is built on top of the `socketserver` module and uses `pickle` for data serialization.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
 - [Prerequisites](#prerequisites)
 - [Installation](#installation)
 - [Configuration](#configuration)
- [Usage](#usage)
 - [Starting the Server](#starting-the-server)
 - [Supported Commands](#supported-commands)
   - [GET](#get)
   - [SET](#set)
   - [DELETE](#delete)
   - [FLUSH](#flush)
   - [MGET](#mget)
   - [MSET](#mset)
- [Code Structure](#code-structure)
 - [hoard.py](#mainpy)
 - [server.py](#serverpy)
 - [utils.py](#utilspy)
- [Contributing](#contributing)
- [License](#license)

## Features

- Lightweight and easy-to-use key-value data store server
- Supports various data types for values (strings, bytes, integers, floats, None, lists, and dictionaries)
- Configurable maximum key and value lengths
- Threaded server for handling multiple client connections concurrently
- Simple text-based protocol for client communication

## Getting Started

### Prerequisites

- Python 3.6 or later

### Installation

1. Clone the repository:

        $ git clone https://github.com/TheTiredOne22/Hoard.git

2. Navigate to the project directory:

        $ cd hoard


### Configuration

The server can be configured using environment variables. The following variables are available:

- `SERVER_ADDRESS` (default: `'localhost:8000'`): The address and port on which the server should listen, in the format `host:port`.
- `MAX_KEY_LENGTH` (default: `1024`): The maximum length of a key in bytes.
- `MAX_VALUE_LENGTH` (default: `1048576`): The maximum length of a value in bytes.

You can set these variables in your environment or create a `.env` file in the project directory with the desired values:

 ## Usage

### Starting the Server

To start the server, run the following command:

      $ python manage.py hoard.py

This will start the server listening on the configured address and port.

