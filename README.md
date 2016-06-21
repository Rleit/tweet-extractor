# Tweet extractor

Extract tweets with the [Twitter Streaming API](https://dev.twitter.com/streaming) and store them in [MongoDB](https://www.mongodb.com).

## Installation

Create a virtual environment with Python 3.4

	virtualenv -p /usr/bin/python3.4 venv

Enter the virtual environment

	source venv/bin/activate

Install dependencies

	pip install --upgrade pip
	pip install -r requirements.txt

To install MongoDB on Ubuntu, follow this [link](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu).


## Usage

To run the program

	python main.py

To exit the virtual environment

	deactivate


## Contributors

[Jacky Casas](https://github.com/acknowledge)