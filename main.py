#alt- files
import AASCII
import user
import hub

#stat menu
print("Welcome to:")
print(AASCII.logo())

# robot selection
hub.main()

#game start
print(AASCII.board())
print("Welcome to the map - you are currently at: ", user.pos())

print("Testing")
