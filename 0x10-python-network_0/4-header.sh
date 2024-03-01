<<<<<<< HEAD
#!/usr/bin/python3
# using delete to pass the url as a first argument
curl -s "$1" -X DELETE

=======
#!/bin/bash
# Sams as task 3 except the header variable
curl -sH "X-School-User-Id: 98" -X GET "$1"
>>>>>>> f029d22dabb64dee8c310d4b90e288949e88758c
