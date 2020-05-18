# Remote Ops: A server ML pipeline

## What?
A framework boilerplate to use when requiring a server to perform remote ML tasks. Add the required the files in `src/components` and create the pipeline workflow in `src/tasks.py` .

## Setting Up
By default, the server is set up to receive images. The type can be changed from inside `src/main.py`.\
The server also has ID as parameter if the data being received is to be personalised or have operations upon it which require specific identity. \
Just send the ID as a parameter and modify the `imgName()` path to accomodate image changes.

## Running
The program uses to threads to perform multiple tasks concurrently on the data. If an order has to be followed, simply remove the thread function and call the functions in the order required in `src/tasks.py`.
To create a list of tasks to be done on received data, update the task queue in `src/tasks.py` with a parameter for thread-safe or not.

## Client
`client.py` is a template file which can be used in the program calling the remote-ops server.

### To Do:
- [ ] Make task queue distributed
