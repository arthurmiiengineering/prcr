import os
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    '-n',
    '--name',
    help='Determines the name of the project folder.'
)
parser.add_argument(
    '-t',
    '--template',
    help='This is the template the project will be constructed from.',
    default='_default',
    nargs='?'
)
args = parser.parse_args()


with open('config.json', 'r') as f:
    config = json.load(f)


def create_item(item, path=''):
    if item['type'] == 'file':
        with open(f'{args.name}/{path}{item["name"]}', 'w') as f:
            f.write(item['contents'])
    else:
        os.mkdir(f'{args.name}/{path}{item["name"]}')
        for new_item in item['contents']:
            create_item(new_item, f'{path}{item["name"]}/')


def main():
    os.mkdir(args.name)
    with open(f'templates/{args.template}.json', 'r') as f:
        template = json.load(f)
        for item in template:
            create_item(item)


if __name__ == '__main__':
    main()