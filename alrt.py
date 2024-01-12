#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description='Description of your alrt application.')
    # Add your custom command-line arguments here, if any
    # parser.add_argument('--example', help='Example argument')

    args = parser.parse_args()

    # Your application logic goes here
    print("Hello from alrt!")

if __name__ == "__main__":
    main()

