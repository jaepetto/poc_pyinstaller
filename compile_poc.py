import click

@click.command()
@click.option('-st', '--status',type=click.Choice(['up', 'down']) , default='down', help='Status of the server to manage (up/down)')
@click.option('-b', '--backend', default='app_http', help='Name of the backend to manage')
@click.option('-se', '--server', default='localhost', help='Name of the server to manage')
def changeStatus(status, backend, server):
    command_switcher = {
        'up': 'up',
        'down': 'down'
    }
    command = command_switcher.get(status, 'unknown')
    if command == 'unknown':
        print 'unknown command'
    else:
        print '{}:{}:{}'.format(command, backend, server)

if __name__ == "__main__":
    changeStatus()
