MySQL-bisect
============

This is a tool for searching for a change in a huge folder of SQL dumps
that is non-trivial to detect without full SQL functionality.

	Usage: mysqlbisect [OPTIONS] [FILENAME]...

	  Takes a number of SQL dumps, imports them into a temporary database and
	  runs a query on them. Then it performs a binary search on them to find the
	  EARLIEST dump where the query returns a result. The SQL dumps are
	  processed in alphabetical filename order. If a query returns a row
	  consisting only of 0 and NULL, it will be counted as "no result".

	Options:
	  -h, --host TEXT      MySQL host to use for temporary databases
	  -u, --user TEXT      MySQL user to use for temporary databases. Needs
						   permission to create and drop databases of the name
						   specified with --db.
	  -p, --password TEXT  MySQL user password
	  --db TEXT            MySQL database name scheme for temporary database.
						   Default: bisect_tmp
	  -q, --query TEXT     MySQL query to check in each file.  [required]
	  -v, --verbose        Verbose output.
	  --help               Show this message and exit.

License
-------

Copyright 2016 Raphael Michel

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
