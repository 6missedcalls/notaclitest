from asyncio import subprocess
import os
from re import sub
import subprocess
import random

# Random Alias Generator
def random_alias():
  # create a random alias using all letters and numbers
  letters = "abcdefghijklmnopqrstuvwxyz0123456789"
  # create an 8 character alias with the letters and numbers
  alias = ""
  for i in range(8):
    alias += random.choice(letters)
  return alias

# Start of testing

def startDaemon():
  process = subprocess.Popen("speedway daemon start", shell=True)
  return process

def createAccount(password):
  subprocess.call("speedway account create", shell=True)
  # enter the password in the shell
  subprocess.call(password, shell=True)

def loginAccount():
  subprocess.call("speedway account login", shell=True)

def buyAlias():
  alias = random_alias()
  subprocess.call("speedway account buy-alias " + alias, shell=True)

def createSchema():
  subprocess.call("speedway schema create --file ~/speedway_testing/schema_test.json --label notaclitool", shell=True)

def getSchema():
  subprocess.call("speedway schema get all", shell=True)

def documentBuild():
  schemaDid = input("Enter the schema DID: ")
  subprocess.call("speedway document build " + schemaDid + " --label notaclitool --file ~/speedway_testing/document_test.json", shell=True)

def documentGet():
  documentCid = input("Enter the document CID: ")
  subprocess.call("speedway document get " + documentCid + " --output ~/speedway_testing/output.json", shell=True)

def createBucket():
  subprocess.call("speedway bucket create", shell=True)

def main():
  i = input("Would you like to login or create an account (login/create)? ")
  if i == "login":
    process = startDaemon()
    lcheck = loginAccount()
  elif i == "create":
    process = startDaemon()
    ccheck = createAccount()
  else:
    print("Invalid input")
    exit()
  # buyAlias()
  createSchema()
  getSchema()
  documentBuild()
  documentGet()
  createBucket()
  process.kill()

if __name__ == "__main__":
  main()