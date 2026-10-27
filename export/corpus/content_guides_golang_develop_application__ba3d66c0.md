---
title: Connect the Go application to CockroachDB
description: Connect the Go application to CockroachDB.
---

## Prerequisites

Start with [Set up CockroachDB for Go development](develop-database.md). See [Go guide prerequisites](prerequisites.md).

For container operations, see [Container lifecycle and published ports](/guides/container-lifecycle.md).

## Meet the example application

Now that you have started and configured the database engine, you can switch your attention to the application.

The example application for this module is an extended version of `docker-gs-ping` application you've used in the previous modules. You have two options:

- You can update your local copy of `docker-gs-ping` to match the new extended version presented in this chapter; or
- You can clone the [docker/docker-gs-ping-dev](https://github.com/docker/docker-gs-ping-dev) repository. This latter approach is recommended.

To checkout the example application, run:

```console
$ git clone https://github.com/docker/docker-gs-ping-dev.git
# ... output omitted ...
```

The application's `main.go` now includes database initialization code, as well as the code to implement a new business requirement:

- An HTTP `POST` request to `/send` containing a `{ "value" : string }` JSON must save the value to the database.

You also have an update for another business requirement. The requirement was:

- The application responds with a text message containing a heart symbol ("`<3`") on requests to `/`.

And now it's going to be:

- The application responds with the string containing the count of messages stored in the database, enclosed in the parentheses.

  Example output: `Hello, Docker! (7)`

The full source code listing of `main.go` follows.

```go
package main

import (
	"context"
	"database/sql"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/cenkalti/backoff/v4"
	"github.com/cockroachdb/cockroach-go/v2/crdb"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {

	e := echo.New()

	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	db, err := initStore()
	if err != nil {
		log.Fatalf("failed to initialize the store: %s", err)
	}
	defer db.Close()

	e.GET("/", func(c echo.Context) error {
		return rootHandler(db, c)
	})

	e.GET("/ping", func(c echo.Context) error {
		return c.JSON(http.StatusOK, struct{ Status string }{Status: "OK"})
	})

	e.POST("/send", func(c echo.Context) error {
		return sendHandler(db, c)
	})

	httpPort := os.Getenv("HTTP_PORT")
	if httpPort == "" {
		httpPort = "8080"
	}

	e.Logger.Fatal(e.Start(":" + httpPort))
}

type Message struct {
	Value string `json:"value"`
}

func initStore() (*sql.DB, error) {

	pgConnString := fmt.Sprintf("host=%s port=%s dbname=%s user=%s password=%s sslmode=disable",
		os.Getenv("PGHOST"),
		os.Getenv("PGPORT"),
		os.Getenv("PGDATABASE"),
		os.Getenv("PGUSER"),
		os.Getenv("PGPASSWORD"),
	)

	var (
		db  *sql.DB
		err error
	)
	openDB := func() error {
		db, err = sql.Open("postgres", pgConnString)
		return err
	}

	err = backoff.Retry(openDB, backoff.NewExponentialBackOff())
	if err != nil {
		return nil, err
	}

	if _, err := db.Exec(
		"CREATE TABLE IF NOT EXISTS message (value TEXT PRIMARY KEY)"); err != nil {
		return nil, err
	}

	return db, nil
}

func rootHandler(db *sql.DB, c echo.Context) error {
	r, err := countRecords(db)
	if err != nil {
		return c.HTML(http.StatusInternalServerError, err.Error())
	}
	return c.HTML(http.StatusOK, fmt.Sprintf("Hello, Docker! (%d)\n", r))
}

func sendHandler(db *sql.DB, c echo.Context) error {

	m := &Message{}

	if err := c.Bind(m); err != nil {
		return c.JSON(http.StatusInternalServerError, err)
	}

	err := crdb.ExecuteTx(context.Background(), db, nil,
		func(tx *sql.Tx) error {
			_, err := tx.Exec(
				"INSERT INTO message (value) VALUES ($1) ON CONFLICT (value) DO UPDATE SET value = excluded.value",
				m.Value,
			)
			if err != nil {
				return c.JSON(http.StatusInternalServerError, err)
			}
			return nil
		})

	if err != nil {
		return c.JSON(http.StatusInternalServerError, err)
	}

	return c.JSON(http.StatusOK, m)
}

func countRecords(db *sql.DB) (int, error) {

	rows, err := db.Query("SELECT COUNT(*) FROM message")
	if err != nil {
		return 0, err
	}
	defer rows.Close()

	count := 0
	for rows.Next() {
		if err := rows.Scan(&count); err != nil {
			return 0, err
		}
		rows.Close()
	}

	return count, nil
}
```

The repository also includes the `Dockerfile`, which is almost exactly the same as the multi-stage `Dockerfile` introduced in the previous modules. It uses the official Docker Go image to build the application and then builds the final image by placing the compiled binary into the much slimmer, distroless image.

Regardless of whether you had updated the old example application, or checked out the new one, this new Docker image has to be built to reflect the changes to the application source code.

## Build the application

You can build the image with the familiar `build` command:

```console
$ docker build --tag docker-gs-ping-roach .
```

## Run the application

Now, run your container. This time you'll need to set some environment variables so that your application knows how to access the database. For now, you’ll do this right in the `docker run` command. Later you'll see a more convenient method with Docker Compose.

> [!NOTE]
>
> Since you're running your CockroachDB cluster in insecure mode, the value for the password can be anything.
>
> In production, don't run in insecure mode.

```console
$ docker run -it --rm -d \
  --network mynet \
  --name rest-server \
  -p 80:8080 \
  -e PGUSER=totoro \
  -e PGPASSWORD=myfriend \
  -e PGHOST=db \
  -e PGPORT=26257 \
  -e PGDATABASE=mydb \
  docker-gs-ping-roach
```

There are a few points to note about this command.

- You map container port `8080` to host port `80` this time. Thus, for `GET` requests you can get away with literally `curl localhost`:

  ```console
  $ curl localhost
  Hello, Docker! (0)
  ```

  Or, if you prefer, a proper URL would work just as well:

  ```console
  $ curl http://localhost/
  Hello, Docker! (0)
  ```

- The total number of stored messages is `0` for now. This is fine, because you haven't posted anything to your application yet.
- You refer to the database container by its hostname, which is `db`. This is why you had `--hostname db` when you started the database container.

- The actual password doesn't matter, but it must be set to something to avoid confusing the example application.
- The container you've just run is named `rest-server`. These names are useful for managing the container lifecycle:

  ```console
  # Don't do this just yet, it's only an example:
  $ docker container rm --force rest-server
  ```

## Test the application

In the previous section, you've already tested querying your application with `GET` and it returned zero for the stored message counter. Now, post some messages to it:

```console
$ curl --request POST \
  --url http://localhost/send \
  --header 'content-type: application/json' \
  --data '{"value": "Hello, Docker!"}'
```

The application responds with the contents of the message, which means it has been saved in the database:

```json
{ "value": "Hello, Docker!" }
```

Send another message:

```console
$ curl --request POST \
  --url http://localhost/send \
  --header 'content-type: application/json' \
  --data '{"value": "Hello, Oliver!"}'
```

And again, you get the value of the message back:

```json
{ "value": "Hello, Oliver!" }
```

Run curl and see what the message counter says:

```console
$ curl localhost
Hello, Docker! (2)
```

In this example, you sent two messages and the database kept them. Or has it? Stop and remove all your containers, but not the volumes, and try again.

First, stop the containers:

```console
$ docker container stop rest-server roach
rest-server
roach
```

Then, remove them:

```console
$ docker container rm rest-server roach
rest-server
roach
```

Verify that they're gone:

```console
$ docker container list --all
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

And start them again, database first:

```console
$ docker run -d \
  --name roach \
  --hostname db \
  --network mynet \
  -p 26257:26257 \
  -p 8080:8080 \
  -v roach:/cockroach/cockroach-data \
  cockroachdb/cockroach:latest-v25.4 start-single-node \
  --insecure
```

And the service next:

```console
$ docker run -it --rm -d \
  --network mynet \
  --name rest-server \
  -p 80:8080 \
  -e PGUSER=totoro \
  -e PGPASSWORD=myfriend \
  -e PGHOST=db \
  -e PGPORT=26257 \
  -e PGDATABASE=mydb \
  docker-gs-ping-roach
```

Lastly, query your service:

```console
$ curl localhost
Hello, Docker! (2)
```

Great! The count of records from the database is correct although you haven't only stopped the containers, but you've also removed them before starting new instances. The difference is in the managed volume for CockroachDB, which you reused. The new CockroachDB container has read the database files from the disk, just as it normally would if it were running outside the container.

## Wind down everything

Remember, that you're running CockroachDB in insecure mode. Now that you've built and tested your application, it's time to wind everything down before moving on. You can list the containers that you are running with the `list` command:

```console
$ docker container list
```

Now that you know the container IDs, you can use `docker container stop` and `docker container rm`, as demonstrated in the previous modules.

Stop the CockroachDB and `docker-gs-ping-roach` containers before moving on.

