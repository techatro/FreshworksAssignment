<h1 align="center">Freshworks Assignment</h1>

<h5 align="center">
  <br>
  <br>
  Freshworks Assignment
  <br>
</h5>

### About

# About
This Project was one of the Interview Round by [Freshworks](https://www.freshworks.com/).
 
## Problem Statement
Build a file-based key-value data store that supports the basic CRD (create, read, and delete) operations. This data store is meant to be used as local storage for one single process on one laptop. The datastore must be exposed as a library to clients that can instantiate a class and work with the data store.

### Requirements

- Python 3

### How to use

<pre>

from crud import CRUD # import the crud.py as Library

x = CRUD() # Instantiate the CRUD class

print(x.read()) # Access the class functions 

print(x.create("college","Mahendra College of Engineering"))

print(x.read())

print(x.update("college","Mahendra Engineering College"))

print(x.delete("college"))

</pre>

## Operation Supported:

 - Create
 - Read
 - Update
 - Delete

 ## Functionalities Supported:

 - [x] It can be initialized using an optional file path. If one is
       not provided, it will reliably create itself in a reasonable
       location on the laptop.
 - [x] A new key-value pair can be added to the data store using the
       Create operation. The key is always a string - capped at 32chars.
       The value is always a JSON object - capped at 16KB.
 - [x] If Create is invoked for an existing key, an appropriate error
       must be returned
 - [x] A Read operation on a key can be performed by providing the key,
       and receive the value in the response, as a JSON object.
 - [x] A Delete operation can be performed by providing the key.
 - [x] Appropriate error responses must always be returned to a client
       if it uses the data store in unexpected ways or breaches any
       limits.
 - [x] The size of the file storing data must never exceed 1GB.


