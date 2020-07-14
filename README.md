Django-example
==============
Task was to develop a basic web application for an online newspaper using the Django framework.


## Deployment


### Production


## Development


### Setup

- Create a [virtualenv](https://github.com/partiban21/wiki_docs/blob/master/pyenv_wiki.md#pyenv-wiki).

- Install the local package:

  ```bash
  pip install -e .
  ```

### Running

Start the Django local server

```bash
cd Django-example
python manage.py runserver
```


### Testing

Bots can be tested using (something like) `curl`, with each bot residing under
it's own URL path (see the `bot` file for confirmation)
Arguments can passed to the bot under the `text` form parameter.

```
curl -X POST -d 'command=&text=???' http://localhost:5000/BOTNAME
```

