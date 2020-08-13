django_website
==============
Task was to develop a basic web application for an online newspaper using the Django framework.


## Deployment


### Production


## Development


### Setup

- Create a [virtualenv](https://github.com/partiban21/wiki_docs/blob/master/pyenv_wiki.md#pyenv-wiki).

- Install the local package:

  ```bash
  pip install -r requirements.txt
  ```

### Running

Start the Django local server

1. Move into the django_website directory using the Terminal (should be able to see manage.py)  
2. Run the command "python manage.py migrate" (optional)  
2. Run the command "python manage.py runserver"  
3. Copy and past the link into web browser.  

    ```bash
    cd django_website
    python manage.py runserver 8081
    Performing system checks...

    System check identified no issues (0 silenced).
    
    August 13, 2020 - 13:31:44
    Django version 1.11.29, using settings 'groupCW.settings'
    Starting development server at http://127.0.0.1:8081/
    Quit the server with CONTROL-C.
    ```


### Testing

Bots can be tested using (something like) `curl`, with each bot residing under
it's own URL path (see the `bot` file for confirmation)
Arguments can passed to the bot under the `text` form parameter.

```
curl -X POST -d 'command=&text=???' http://localhost:5000/BOTNAME
```

