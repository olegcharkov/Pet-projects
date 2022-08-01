import configparser

config = configparser.ConfigParser()

config.add_section("Token_name")

with open("token.ini", "w") as secure_files:
    config.write(secure_files)
    secure_files.close()

