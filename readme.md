# Web Applications with Django: Developing REST APIs

This repo is for the course followed at Percipio/Learning People entitled 'Web
Applications with Django: Developing REST APIs'.

The code covers a basic model for famous actors, with text, numerical and image
fields.

A full `dumpdata` has been made for the data used in the making of this app. The
model entries are at the end of `fixtures.json`.

The API can be viewed in the 'Browsable API' when the server is running. Also,
`curl` commands can be issued from the terminal.

Here is an example to add a new actor with `curl`:

```bash
curl -X POST localhost:8000 \
-H 'content-type: application/json' \
-d '{"name": "Whoever", "age": 99}' \
| python -m json.tool
```

This will send a `POST` request to the view at the root url. This corresponds to
the `ActorList` class-based view, which has handlers for `GET` and `POST` methods.

Backslashes '`\`' are used to allow for entry across multiple terminal lines.
Headers and data are specified with the `-H` and `-d` flags, respectively. The
output is 'piped' with '`|`' into a more readable, indented JSON format.

## General pattern

- Create a Django model as normal.
- Create a serializer to transform the model to JSON format.
- Subclass `APIView` from DRF to make list and detail views.
  - In general, models are created/deleted in the list and updated in the detail
    view endpoints.
- Create handler methods in the views for the HTTP verbs you want to use.
  - A detail view like `ActorByID` here has `get`, `put` and `delete` methods made.
- Define view urls like normal.
- Use the Browsable API or `curl` commands to perform CRUD functions.

In general, views return a DRF `Response` object with some filtered, serialized
data. Think in terms of querysets or valid form data.

## Notes

- `POST` requests need some data accompanying them - valid model entry data.
- Return status codes in views where data is edited, such as OK or Bad Request.
- `--head` and `OPTIONS` type requests can be made to access endpoint metadata.
- Editing views are validated with `is_valid()` just like a Django form.
- You can only perform the HTTP verbs on an endpoint when they have been specified
  in the view.
- When curling binary data such as an image, output it somewhere with `-O` or `--output`.
