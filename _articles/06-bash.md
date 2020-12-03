---
layout: defaults/article
title: Is a Bash variable set?
tags:
  - bash
---

# Is a Bash variable set?

#### Preventing unbound variables is good, but we need a way to tell if a variable has no content or has never been initialized

A variable is often referred to as a box with a name and a content. A command like the following:
```
echo Hello $name
```

Will print _Hello_, and then… the content of the box named ‘name’.
If the box is empty Bash will print nothing, as expected.
Bash will print nothing also if the box was never created!

As beginners, we just care about variable containing _something_,
but soon or later we will need to distinguish among:

- **Defined variables** (variables properly created, or initialized, no matter if the content is a zero or an empty string!)
- **Undefined variables** (variable never created)

There are several good reasons: sometimes we can deal with empty strings as a valid
content of a variable, so checking if the string is empty is not a valid input
validation. Same when the user can supply a number, including zero.

But beyond specific examples, the distinction between defined and undefined
variables enables strict checking of unbound variables. If you, for example,
declare `$firstname` and then print `$first_name`…
you are not going to see the expected output. This typo can lead to severe
problems, but if we ban unbound variables from our life, we can play safer!

Checking a variable in Bash is not as easy as it should
(mainly because Bash was not born with this feature in mind), but it’s
[possible](https://stackoverflow.com/questions/3601515/how-to-check-if-a-variable-is-set-in-bash):

{% gist e321688e21311ac70ba0f5b1de06fd87 %}

If we run the script we get:
```
CHECK 1: variable ‘VAR’ is set, its content is ‘’
CHECK 2: variable ‘Var’ is unset
```

This means we have a way to tell the difference among initialized variables, even if with the empty string or zero value, and not initialized ones.

When writing a script is always a good idea to initialize variables with a
reasonable value (e.g. 0 for counters), but this method is useful to check
for variables we have little control for like
[user-supplied parameters](https://medium.com/ngs-sh/bash-script-getting-parameters-from-the-users-part-5-104fca1c2937) as `$1`.

_Norwich, Sep 27, 2018. Originally [published here](https://medium.com/ngs-sh/is-a-bash-variable-set-79bfd735512e)_
