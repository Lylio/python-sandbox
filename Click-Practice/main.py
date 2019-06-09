import settings
import click

test1 = settings.MAVEN_GROUP_ID
test2 = settings.CLUSTER

settings.POD_SCALE = 14

test3 = settings.POD_SCALE


if __name__ == '__main__':

 print(test1)
 print(test2)
 print(test3)

 name = ctx.obj.prompt("Enter your name", "user-name")