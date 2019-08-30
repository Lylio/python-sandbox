import settings
import click

test1 = settings.MAVEN_GROUP_ID
test2 = settings.CLUSTER


#name = click.obj.prompt('Please enter name', ['user-name'])



if __name__ == '__main__':

    name = click.prompt('Please enter name')